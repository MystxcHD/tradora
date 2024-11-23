import requests
import sqlite3 as sql
from email_func import e_alert
from datetime import datetime, date, time, timedelta

"""
In main.py, create an API call and store the API call
in the db for manipulation in clean.py
"""

# Create DB for all news and timestamps
conn = sql.connect("stockNews.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS stockNews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    api_call TEXT NOT NULL
)
""")
conn.commit()

# Call the API and store it in the DB

yesterday = datetime.now() - timedelta(days=1)
yesterday_date = yesterday.strftime("%Y-%m-%d")

url = "https://api.stockdata.org/v1/news/all"

params = {
    "api_token": "THwsW9zE7G8lrV7Zg0SQXXBwZui2ywzsHYZMKWjk",
    "interval": "day",
    "published_on": yesterday_date,
    "sort": "total_documents",
    "sort_order": "desc",
}

response = requests.get(url, params=params)
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

cursor.execute("""
INSERT INTO stockNews (date, api_call)
VALUES (?, ?)
""", (current_date, response.text))

conn.commit()

# Close the connection
conn.close()



