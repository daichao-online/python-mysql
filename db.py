from flask import Flask
import mysql.connector

app = Flask(__name__)

# MySQL config
DB_CONFIG = {
    "host": "192.168.18.15",
    "user": "siouch",
    "password": "ouch16091997",
    "database": "guesthouse"
}

@app.route('/')
def insert_user():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        val = ("John Doe", "john@example.com")
        cursor.execute(sql, val)
        conn.commit()
        cursor.close()
        conn.close()
        return f"{cursor.rowcount} record inserted!"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="192.168.18.15", port=8080, debug=True)
