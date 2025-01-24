from clean import *
from email_func import e_alert

def returnArticle():
    titles_list = []
    description_list = []
    snippet_list = []
    url_list = []

    for i, title in enumerate(titles):
        titles_list.append(title)

    for i, desc in enumerate(description):
        description_list.append(desc)

    for i, snip in enumerate(snippet):
        snippet_list.append(snip)

    for i, link in enumerate(url):
        url_list.append(link)

    print("Success")
    return titles_list, description_list, snippet_list, url_list

titles_list, description_list, snippet_list, url_list = returnArticle()

title_content = "<br><br>".join(titles_list)
description_content = "<br><br>".join(description_list)


with open("email.html", "r", encoding="utf-8") as file:
    html_content = file.read()


placeholders = {
    "{body}": description_content,
    "{titles}": title_content,
}

for placeholder, value in placeholders.items():
    html_content = html_content.replace(placeholder, value)

e_alert(
    subject="Daily Newsletter",
    html_content=html_content,
    to="siva.dasaka75@gmail.com"
)
