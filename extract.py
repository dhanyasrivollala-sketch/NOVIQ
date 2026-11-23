import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "database" / "noviq.db"

def extract_data():
    connection = sqlite3.connect(DB_PATH)

    query = """
    SELECT category, title, description, source, url, published
    FROM noviq_data
    """

    df = pd.read_sql_query(query, connection)
    connection.close()

    df.drop_duplicates(subset=["category", "url"], inplace=True)
    df.fillna("", inplace=True)

    output_folder = Path(__file__).parent.parent / "output"
    output_folder.mkdir(exist_ok=True)

    df.to_csv(output_folder / "noviq_data.csv", index=False)

    print("Data extracted and cleaned successfully!")
    print("Total records:", len(df))


if __name__ == "__main__":
    extract_data()