import sqlite3 as sql
import json

"""
Cleans the result of requestStore.py in which 
title, description, snippet, and url
"""

conn = sql.connect("stockNews.db")
cursor = conn.cursor()

cursor.execute("""
SELECT * 
FROM stockNews
ORDER BY date DESC
LIMIT 1
""")

latest_entry = cursor.fetchone()
print(latest_entry)
entry_id, entry_date, stockNews = latest_entry
data = json.loads(stockNews)

titles = [article["title"] for article in data["data"]]
description = [article["description"] for article in data["data"]]
snippet = [article["snippet"] for article in data["data"]]
url = [article["url"] for article in data["data"]]

conn.close()