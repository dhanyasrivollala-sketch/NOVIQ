import requests
import xml.etree.ElementTree as ET
from urllib.parse import quote
from database.db import create_table, save_data

def get_ai_news():

    query = quote("artificial intelligence OR ChatGPT OR OpenAI OR Gemini")

    url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        root = ET.fromstring(response.content)

        news = []

        for item in root.findall(".//item")[:10]:

            article = {
                "title": item.findtext("title"),
                "source": item.findtext("source"),
                "published": item.findtext("pubDate"),
                "url": item.findtext("link")
            }

            news.append(article)

        return news

    except requests.RequestException as error:
        print("News fetching error:", error)
        return []

    except ET.ParseError:
        print("Unable to read news feed.")
        return []

if __name__ == "__main__":

    create_table()

    results = get_ai_news()

    print("\nNOVIQ - Latest AI News\n")

    if results:
        save_data("news", results)

        for article in results:
            print("--------------------------")
            print("Title:", article["title"])
            print("Source:", article["source"])
            print("Published:", article["published"])
            print("URL:", article["url"])
    else:
        print("No news found.")

    