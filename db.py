import sqlite3
import json
from pathlib import Path

DB_PATH = Path(__file__).parent / "noviq.db"


def connect_db():
    return sqlite3.connect(DB_PATH)


def create_table():

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS noviq_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            title TEXT,
            description TEXT,
            source TEXT,
            url TEXT,
            published TEXT,
            extra_data TEXT,
            UNIQUE(category, url)
        )
    """)

    connection.commit()
    connection.close()

    print("NOVIQ database created successfully!")


def save_data(category, items):

    connection = connect_db()
    cursor = connection.cursor()

    for item in items:

        title = item.get("title") or item.get("name") or "Untitled"

        description = (
            item.get("description")
            or item.get("abstract")
            or ""
        )

        source = (
            item.get("source")
            or item.get("company")
            or item.get("domain")
            or ""
        )

        url = item.get("url") or item.get("link") or ""

        published = item.get("published") or item.get("date") or ""

        cursor.execute("""
            INSERT OR IGNORE INTO noviq_data
            (category, title, description, source, url, published, extra_data)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            category,
            title,
            description,
            source,
            url,
            published,
            json.dumps(item)
        ))

    connection.commit()
    connection.close()

    print(f"{len(items)} {category} records processed.")


if __name__ == "__main__":
    create_table()