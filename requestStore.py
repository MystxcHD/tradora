import requests
import json
from newsapi import NewsApiClient
import sqlite3 as sql
from datetime import datetime, date, time, timedelta

"""
In requestStore.py, create an API call and store the API call
in the db for manipulation in clean.py
"""

# Create DB for all news and timestamps
conn = sql.connect("stockNews.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS stockNews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    stockNews_api_call TEXT NOT NULL,
    cryptoNews_api_call TEXT NOT NULL
)
""")
conn.commit()

# Time keeping

yesterday = datetime.now() - timedelta(days=1)
yesterday_date = yesterday.strftime("%Y-%m-%d")
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Call the Stock News API

newsapi = NewsApiClient(api_key="a14ac5366922446488cf43d42dd1e18b")
all_articles = newsapi.get_everything(q="stock market",
                                      from_param=yesterday_date,
                                      language="en",
                                      sort_by="relevancy")

if "articles" in all_articles:
    stock_data = json.dumps(all_articles["articles"][:3])
else:
    stock_data = json.dumps({"error": "Failed to fetch crypto articles"})
    
# Call the Crypto News API

newsapi = NewsApiClient(api_key="a14ac5366922446488cf43d42dd1e18b")
all_articles = newsapi.get_everything(q="cryptocurrency",
                                      from_param=yesterday_date,
                                      language="en",
                                      sort_by="relevancy")

if "articles" in all_articles:
    top_3_crypto = json.dumps(all_articles["articles"][:3])
else:
    top_3_crypto = json.dumps({"error": "Failed to fetch crypto articles"})

# Store the calls in the db

cursor.execute("""
INSERT INTO stockNews (date, stockNews_api_call, cryptoNews_api_call)
VALUES (?, ?, ?)
""", (current_date, stock_data, top_3_crypto))

conn.commit()

# Close the connection
conn.close()



