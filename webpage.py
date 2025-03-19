from flask import Flask, render_template, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from main import e_alert
import subprocess
import sqlite3 as sql

app = Flask(__name__)


def run_scripts_in_order():
    try:
        # Run requestStore.py
        print("Running requestStore.py...")
        subprocess.run(["python", "requestStore.py"], check=True)
        print("requestStore.py completed.")


        # Run main.py
        print("Running main.py...")
        subprocess.run(["python", "main.py"], check=True)
        print("main.py completed. Daily email sent.")
    
    except Exception as e:
        print(f"Error in running scripts: {e}")

scheduler = BackgroundScheduler()
scheduler.add_job(run_scripts_in_order, 'cron', hour=23, minute=35)
scheduler.start()

@app.route('/', methods=['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        name = request.json.get('name')
        email = request.json.get('email')
        
        conn = sql.connect("users.db")
        cursor = conn.cursor()

        cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
""")
        conn.commit()

        cursor.execute("SELECT 1 FROM users WHERE email = ?", (email,))
        exists = cursor.fetchone() is not None

        if exists:
            cursor.execute("DELETE FROM users WHERE email = ?", (email,))
            conn.commit()
            html_file = "bye.html"
            e_alert(subject="Unsubscribed from Tradora!", html_content="""<!DOCTYPE html>
<html>
    <head>
        <style>
            h1 {
                font-family: "Righteous", sans-serif;
                font-weight: 400;
                font-size: 32px;
                text-align: center;
            }
            h2 {
                font-family: Arial, sans-serif;
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 10px;
                color: #333;
            }
            h3 {
                font-family: Arial, sans-serif;
                font-size: 16px;
                font-weight: bold;
                margin-top: 10px;
            }
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                background-color: #f4f4f4;
                margin: 0;
                padding: 20px;
            }
            .email-container {
                max-width: 600px;
                margin: 0 auto;
                background: #ffffff;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                border: 1px solid #ddd;
            }
            .header {
                text-align: center;
                background: rgb(249, 249, 249);
                color: #000;
                padding: 10px 0;
                border: 4px solid #000;
                border-radius: 10px 10px 0 0;
            }
            .content {
                padding: 20px;
                font-size: 16px;
                color: #333;
            }
            .footer {
                text-align: center;
                font-size: 12px;
                color: #777;
                margin-top: 30px;
                border-top: 1px solid #eee;
                padding-top: 15px;
            }
            .title-block {
                background: #f9f9f9;
                padding: 15px;
                border-radius: 5px;
                margin-bottom: 15px;
                border-left: 4px solid rgb(249, 249, 249);
            }
            .description {
                font-size: 14px;
                color: #555;
            }
            .author {
                font-size: 12px;
                color: #888;
            }
            .button {
                display: inline-block;
                background: #0073e6;
                color: white;
                padding: 10px 15px;
                text-decoration: none;
                font-size: 14px;
                border-radius: 5px;
                text-align: center;
            }
            .button:hover {
                background: #005bb5;
            }
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                <img src="https://i.postimg.cc/QCrbX4SV/tradora-banner-transparent.png" alt="Tradora Logo" width="200">
            </div>
            <div class="content">
                <h1>Unsubscribed from Tradora</h1>
                <h3>We're sorry to see you go.</h3>
            </div>
            <div class="footer">
                <p><strong>Tradora provides market and cryptocurrency news for informational purposes only. This is not financial advice. Please do your own research before making any investment decisions.</strong></p>
            </div>
        </div>
    </body>
</html>
""", to=email)
            return jsonify({"message": "Successfully Unsubscribed!"})

        cursor.execute("""
INSERT INTO users (name, email)
VALUES (?, ?)
""", (name, email))

        conn.commit()
        conn.close()

        print(f"Received name: {name}, email: {email}")

        html_file_path = "hello.html"
        e_alert(subject="Welcome to Tradora!", html_content="""<!DOCTYPE html>
<html>
    <head>
        <style>
            h1 {
                font-family: "Righteous", sans-serif;
                font-weight: 400;
                font-size: 32px;
                text-align: center;
            }
            h2 {
                font-family: Arial, sans-serif;
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 10px;
                color: #333;
            }
            h3 {
                font-family: Arial, sans-serif;
                font-size: 16px;
                font-weight: bold;
                margin-top: 10px;
            }
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                background-color: #f4f4f4;
                margin: 0;
                padding: 20px;
            }
            .email-container {
                max-width: 600px;
                margin: 0 auto;
                background: #ffffff;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                border: 1px solid #ddd;
            }
            .header {
                text-align: center;
                background: rgb(249, 249, 249);
                color: #000;
                padding: 10px 0;
                border: 4px solid #000;
                border-radius: 10px 10px 0 0;
            }
            .content {
                padding: 20px;
                font-size: 16px;
                color: #333;
            }
            .footer {
                text-align: center;
                font-size: 12px;
                color: #777;
                margin-top: 30px;
                border-top: 1px solid #eee;
                padding-top: 15px;
            }
            .title-block {
                background: #f9f9f9;
                padding: 15px;
                border-radius: 5px;
                margin-bottom: 15px;
                border-left: 4px solid rgb(249, 249, 249);
            }
            .description {
                font-size: 14px;
                color: #555;
            }
            .author {
                font-size: 12px;
                color: #888;
            }
            .button {
                display: inline-block;
                background: #0073e6;
                color: white;
                padding: 10px 15px;
                text-decoration: none;
                font-size: 14px;
                border-radius: 5px;
                text-align: center;
            }
            .button:hover {
                background: #005bb5;
            }
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                <img src="https://i.postimg.cc/QCrbX4SV/tradora-banner-transparent.png" alt="Tradora Logo" width="200">
            </div>
            <div class="content">
                <h1>Welcome to Tradora!</h1>
                <h3>Actionable market news. Everyday. Straight to your inbox.</h3>
            </div>
            <div class="footer">
                <p><strong>Tradora provides market and cryptocurrency news for informational purposes only. This is not financial advice. Please do your own research before making any investment decisions.</strong></p>
            </div>
        </div>
    </body>
</html>
""", to=email)
        return jsonify({'message': 'Thank you for subscribing!'})
    
    return render_template("subscribe.html")

if __name__ == '__main__':
    app.run(debug=True)

# PROBLEM WITH hello.html AND bye.html