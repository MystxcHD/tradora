from clean import *
from email_func import e_alert

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

    print("Success")
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

    print("Success")
    return titles_list, description_list,  authors_list, url_list

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

with open("email.html", "r", encoding="utf-8") as file:
    html_content = file.read()

placeholders = {
    "{market_news_blocks}": market_news_blocks,
    "{crypto_news_blocks}": crypto_news_blocks,
}

for placeholder, value in placeholders.items():
    html_content = html_content.replace(placeholder, value)

e_alert(
    subject="Daily Newsletter",
    html_content=html_content,
    to="siva.dasaka75@gmail.com"
)

