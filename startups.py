import requests

def get_startups():

    url = "https://api.github.com/search/repositories"

    params = {
        "q": "AI startups",
        "sort": "stars",
        "order": "desc",
        "per_page": 10
    }

    response = requests.get(url, params=params, timeout=15)

    if response.status_code == 200:
        data = response.json()

        startups = []

        for item in data["items"]:
            startups.append({
                "name": item["name"],
                "description": item["description"],
                "url": item["html_url"]
            })

        return startups

    else:
        print("Error fetching data:", response.status_code)
        return []


if __name__ == "__main__":
    results = get_startups()

    for startup in results:
        print(startup)