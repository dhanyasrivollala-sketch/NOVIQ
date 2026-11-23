import requests
from database.db import create_table, save_data

def get_ai_internships():

    url = "https://www.arbeitnow.com/api/job-board-api"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()
        internships = []

        keywords = [
            "intern",
            "internship",
            "trainee"
        ]

        ai_keywords = [
            "artificial intelligence",
            "machine learning",
            "deep learning",
            "data science",
            "AI"
        ]

        for item in data.get("data", []):

            title = str(item.get("title", "")).lower()
            description = str(item.get("description", "")).lower()

            text = title + " " + description

            if (any(word in title for word in keywords)
                and any(word.lower() in text for word in ai_keywords)):

                internships.append({
                    "title": item.get("title"),
                    "company": item.get("company_name"),
                    "location": item.get("location"),
                    "url": item.get("url")
                })

        return internships

    except requests.RequestException as error:
        print("Error fetching internships:", error)
        return []

if __name__ == "__main__":

    create_table()

    results = get_ai_internships()

    print("\nNOVIQ - AI Internships\n")

    if results:
        save_data("internships", results)

        for internship in results:
            print("--------------------------")
            print("Title:", internship.get("title"))
            print("Company:", internship.get("company"))
            print("URL:", internship.get("url"))
    else:
        print("No internships found.")