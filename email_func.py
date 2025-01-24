from email.message import EmailMessage
import smtplib

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

  user = "ta6750080@gmail.com"
  msg["from"] = user
  letters = "pmnqfjdajuajpunk"

  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(user, letters)
  server.send_message(msg)
  server.quit()