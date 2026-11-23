from flask import Flask, jsonify, request
import sqlite3
from pathlib import Path

app = Flask(__name__)

DB_PATH = Path(__file__).parent / "database" / "noviq.db"

@app.route("/")
def home():
    return jsonify({"message": "NOVIQ API is running!"})

@app.route("/api/data")
def get_data():
    category = request.args.get("category")

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    if category:
        cursor.execute(
            "SELECT * FROM noviq_data WHERE category = ?",
            (category,)
        )
    else:
        cursor.execute("SELECT * FROM noviq_data")

    rows = [dict(row) for row in cursor.fetchall()]
    connection.close()

    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True)