from clean import *
from email_func import e_alert

def returnArticle():
    result = []

    for i, title in enumerate(titles):
        result.append(f"Title {i+1}: {title}")

    for i, desc in enumerate(description):
        result.append(f"Description {i+1}: {desc}")

    for i, snip in enumerate(snippet):
        result.append(f"Snippet {i+1}: {snip}")

    for i, link in enumerate(url):
        result.append(f"URL {i+1}: {link}")

    print("Success")
    return "<br><br>".join(result)


content = returnArticle()

with open("email.html", "r", encoding="utf-8") as file:
    html_template = file.read()

html_content = html_template.replace("{body}", content)


e_alert(
    subject="Daily Newsletter",
    html_content=html_content,
    to="siva.dasaka75@gmail.com"
)
