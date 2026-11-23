import requests
from database.db import create_table, save_data


def get_github_projects():

    url = "https://api.github.com/search/repositories"

    params = {
        "q": "artificial intelligence",
        "sort": "stars",
        "order": "desc",
        "per_page": 10
    }

    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()

    data = response.json()

    projects = []

    for repo in data.get("items", []):
        projects.append({
            "name": repo.get("full_name"),
            "title": repo.get("name"),
            "description": repo.get("description") or "",
            "language": repo.get("language") or "",
            "stars": repo.get("stargazers_count", 0),
            "url": repo.get("html_url"),
            "source": "GitHub"
        })

    return projects


if __name__ == "__main__":

    create_table()

    results = get_github_projects()

    if results:
        save_data("github", results)
        print("GitHub projects saved successfully!")
    else:
        print("No GitHub projects found.")