import sqlite3 as sql
import json

"""
Cleans the result of requestStore.py
"""

# Connect and init db

conn = sql.connect("stockNews.db")
cursor = conn.cursor()

cursor.execute("""
SELECT * 
FROM stockNews
ORDER BY date DESC
LIMIT 1
""")

latest_entry = cursor.fetchone()
entry_id, entry_date, stockNews_api_call, cryptoNews_api_call = latest_entry

# Clean Stock News API

stock_data = json.loads(stockNews_api_call)

stock_titles = [article["title"] for article in stock_data]
stock_description = [article["description"] for article in stock_data]
stock_authors = [article["author"] for article in stock_data]
stock_urls = [article["url"] for article in stock_data]

# Clean Crypto News

crypto_data = json.loads(cryptoNews_api_call)

crypto_titles = [article['title'] for article in crypto_data]
crypto_authors = [article['author'] for article in crypto_data]
crypto_descriptions = [article['description'] for article in crypto_data]
crypto_urls = [article['url'] for article in crypto_data]


conn.close()