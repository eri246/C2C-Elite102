import mysql.connector
import tkinter

conn = mysql.connector.connect(
    user='root',
    host='localhost',
    password='Dog=cat6',
    database='c2cproject',
    
)

mycursor = conn.cursor()
# Create a new record
sql = """INSERT INTO client (email, password) VALUES ('john@example.com', 'mypassword')"""
try:
    mycursor.execute(sql)
    # Commit changes
    conn.commit()

