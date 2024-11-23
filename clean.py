import sqlite3 as sql
import json

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

for i, title in enumerate(titles):
    print(f"Title {i+1}: {title}")

for i, desc in enumerate(description):
    print(f"Description {i+1}: {desc}")
    
for i, snip in enumerate(snippet):
    print(f"Snippet {i+1}: {snip}")

for i, url in enumerate(url):
    print(f"URL {i+1}: {url}")


conn.close()