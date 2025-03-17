from flask import Flask, render_template, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
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
scheduler.add_job(run_scripts_in_order, 'cron', hour=12, minute=7)
scheduler.start()

@app.route('/')
def home():
    return render_template("landing.html")

@app.route('/subscribe', methods=['GET', 'POST'])
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

        cursor.execute("""
INSERT INTO users (name, email)
VALUES (?, ?)
""", (name, email))

        conn.commit()
        conn.close()

        print(f"Received name: {name}, email: {email}")
        return jsonify({'message': 'Thank you for subscribing!'})
    
    return render_template("subscribe.html")

if __name__ == '__main__':
    app.run(debug=True)