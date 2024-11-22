from email.message import EmailMessage
import smtplib

def e_alert(subject, body, to):
  msg = EmailMessage()
  msg.set_content(body)
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