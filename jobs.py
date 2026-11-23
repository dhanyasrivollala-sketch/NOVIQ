import requests
from database.db import create_table, save_data 


def get_ai_jobs():

    url = "https://www.arbeitnow.com/api/job-board-api"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()
        jobs = []

        keywords = [
            "artificial intelligence",
            "machine learning",
            "deep learning",
            "AI engineer",
            "data scientist"
        ]

        for item in data.get("data", []):

            text = (
                str(item.get("title", "")) + " " +
                str(item.get("description", ""))
            ).lower()

            if any(word in text for word in keywords):

                jobs.append({
                    "title": item.get("title"),
                    "company": item.get("company_name"),
                    "location": item.get("location"),
                    "remote": item.get("remote"),
                    "url": item.get("url")
                })

        return jobs

    except requests.RequestException as error:
        print("Error:", error)
        return []

if __name__ == "__main__":

    create_table()

    results = get_ai_jobs()

    print("\nNOVIQ - AI Jobs\n")

    if results:
        save_data("jobs", results)

        for job in results:
            print("--------------------------")
            print("Title:", job.get("title"))
            print("Company:", job.get("company"))
            print("URL:", job.get("url"))
    else:
        print("No jobs found.")