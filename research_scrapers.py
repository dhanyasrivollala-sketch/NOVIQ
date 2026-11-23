import requests
import xml.etree.ElementTree as ET
from database.db import create_table, save_data


def get_research_papers():

    url = "https://export.arxiv.org/api/query"

    params = {
        "search_query": "all:artificial intelligence",
        "start": 0,
        "max_results": 10
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    root = ET.fromstring(response.content)

    namespace = {
        "atom": "http://www.w3.org/2005/Atom"
    }

    papers = []

    for entry in root.findall("atom:entry", namespace):

        papers.append({
            "title": entry.findtext(
                "atom:title", default="", namespaces=namespace
            ).strip(),

            "description": entry.findtext(
                "atom:summary", default="", namespaces=namespace
            ).strip(),

            "published": entry.findtext(
                "atom:published", default="", namespaces=namespace
            ),

            "url": entry.findtext(
                "atom:id", default="", namespaces=namespace
            ),

            "source": "arXiv"
        })

    return papers


if __name__ == "__main__":

    create_table()

    results = get_research_papers()

    if results:
        save_data("research", results)
        print("Research papers saved successfully!")
    else:
        print("No research papers found.")