import sqlite3

connection = sqlite3.connect("users_data.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(name, password) ")
cursor.execute("INSERT INTO users VALUES ('rishab', '1234567890')")
cursor.execute("INSERT INTO users VALUES ('sajid', '9876543210')")
cursor.execute("INSERT INTO users VALUES ('yamaha', '1234512345')")

connection.commit()
