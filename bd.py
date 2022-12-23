import sqlite3

connection = sqlite3.connect('Api.db')
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS players(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         pseudo TEXT,
         lvl interger,
         maxHp INTERGER,
         maxMana Interger,
         hp interger,
         mana interger,
         xp interger,
         atq interger
        
    )
""")
connection.commit()

connection.close()