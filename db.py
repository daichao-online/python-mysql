import mysql.connector #pip install mysql-connector-python

# Connect to MySQL
conn = mysql.connector.connect(
    host="192.168.18.15",
    user="siouch",
    password="ouch16091997",
    database="guesthouse"
)

# Create a cursor
cursor = conn.cursor()

# Example: Insert one record
sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
val = ("John Doe", "john@example.com")
cursor.execute(sql, val)

# Commit the transaction
conn.commit()

print(cursor.rowcount, "record inserted.")

# Close connection
cursor.close()
conn.close()
