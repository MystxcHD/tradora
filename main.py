from requestStore import *
from email.message import EmailMessage
import smtplib
from newsapi import NewsApiClient
import sqlite3 as sql
from datetime import datetime, timedelta

def e_alert(subject, html_content=None, html_file_path=None, to=None):
  if html_content is None and html_file_path is None:
        raise ValueError("No HTML content or file path provided.")
    
  if html_content is None:
      with open(html_file_path, 'r', encoding='utf-8') as file:
          html_content = file.read()
  msg = EmailMessage()
  msg.set_content("This email requires an HTML-compatible viewer.")
  msg.add_alternative(html_content, subtype="html")
  
  msg["subject"] = subject
  msg["to"] = to

  user = "tradora.newsletter@gmail.com"
  msg["from"] = user
  letters = "ggevkxouwqeylrte"

  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(user, letters)
  server.send_message(msg)
  server.quit()

def get_users():
    conn = sql.connect("users.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT email FROM users")
    subscribers = [row[0] for row in cursor.fetchall()]
    
    conn.close()
    return subscribers

def returnStockArticle():
    """
    Returns 4 lists containing the title, description,
    author, and url from the stock news API
    """
    titles_list = []
    description_list = []
    authors_list = []
    url_list = []

    for i, title in enumerate(stock_titles):
        titles_list.append(title)

    for i, desc in enumerate(stock_description):
        description_list.append(desc)

    for i, author in enumerate(stock_authors):
            authors_list.append(author)

    for i, link in enumerate(stock_urls):
        url_list.append(link)

    print("Success - Stocks")
    return titles_list, description_list,  authors_list, url_list

def returnCryptoArticle():
    """
    Returns 4 lists containing the title, description,
    author, and url from the crypto news API
    """
    titles_list = []
    description_list = []
    authors_list = []
    url_list = []

    for i, title in enumerate(crypto_titles):
        titles_list.append(title)

    for i, desc in enumerate(crypto_descriptions):
        description_list.append(desc)

    for i, author in enumerate(crypto_authors):
        authors_list.append(author)

    for i, link in enumerate(crypto_urls):
        url_list.append(link)

    print("Success - Crypto")
    return titles_list, description_list,  authors_list, url_list

# At a Glance News

s_titles_list, s_description_list,  s_authors_list, s_url_list = returnStockArticle()
c_titles_list, c_description_list,  c_authors_list, c_url_list = returnCryptoArticle()

market_news_blocks = ""
for title, description, author, url in zip(s_titles_list, s_description_list,  s_authors_list, s_url_list):
    market_news_blocks += f"""
    <div class="title-block">
        <h3>{title}</h3>
        <p class="description">{description}</p>
        <p class="author">{author}</p>
        <a href="{url}" class="link">Read more</a>
    </div>
    """

crypto_news_blocks = ""
for title, description, author, url in zip(c_titles_list, c_description_list,  c_authors_list, c_url_list):
    crypto_news_blocks += f"""
    <div class="title-block">
        <h3>{title}</h3>
        <p class="description">{description}</p>
        <p class="author">{author}</p>
        <a href="{url}" class="link">Read more</a>
    </div>
    """


def send_newsletter():
    with open("email.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    current_date = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    date_insertion = f"""<div style="text-align: center; font-size: 12px; color: #555; margin-top: 5px"><p>{current_date}</p></div>"""

    placeholders = {
        "{date_insertion}": date_insertion,
        "{market_news_blocks}": market_news_blocks,
        "{crypto_news_blocks}": crypto_news_blocks,
    }

    for placeholder, value in placeholders.items():
        html_content = html_content.replace(placeholder, value)

    subscribers = get_users()
    
    for email in subscribers:
        try:
            e_alert(subject="Daily Newsletter", html_content=html_content, to=email)
            print(f"Email sent to {email}")
        except Exception as e:
            print(f"Failed to send email to {email}: {e}")

send_newsletter()
