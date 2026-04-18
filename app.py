import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

user_input = input("Enter username: ")
query = "SELECT * FROM users WHERE username = '" + user_input + "'"

cursor.execute(query)

password = input("Enter password: ")
if password == "admin123":
    print("Login successful")

print("Connected to database")
conn.close()
