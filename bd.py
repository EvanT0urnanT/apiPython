import sqlite3

connection = sqlite3.connect('ma_base.db')
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         firstname TEXT,
         lastname TEXT,
         age INTERGER
    )
""")
connection.commit()


cursor.execute("""
    INSERT INTO users (firstname, lastname, age) VALUES (?, ?, ?)
""", ("Lewis", "Hamilton", 37))
cursor.execute("""
    INSERT INTO users (firstname, lastname, age) VALUES (?, ?, ?)
""", ("Max", "Verstappen", 25))
cursor.execute("""
    INSERT INTO users (firstname, lastname, age) VALUES (?, ?, ?)
""", ("Pierre", "Gasly", 26))
cursor.execute("""
    INSERT INTO users (firstname, lastname, age) VALUES (?, ?, ?)
""", ("Charles", "Leclerc", 25))
cursor.execute("""
    INSERT INTO users (firstname, lastname, age) VALUES (?, ?, ?)
""", ("Sebastian", "Vettel", 35))
cursor.execute("""
    INSERT INTO users (firstname, lastname, age) VALUES (?, ?, ?)
""", ("Fernando", "Alonso", 41))
cursor.execute("""
    INSERT INTO users (firstname, lastname, age) VALUES (?, ?, ?)
""", ("Valtteri", "Bottas", 33))
connection.commit()
connection.close()