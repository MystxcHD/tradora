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

    return "\n".join(result)

content = returnArticle()
e_alert("Daily Newsletter", content, "siva.dasaka75@gmail.com")