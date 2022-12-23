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

cursor.execute("""
    INSERT INTO players (pseudo, lvl, maxHp,maxMana,hp,mana,xp,atq) VALUES (?, ?, ?,?,?,?,?,?)
""", ("Evan", 1, 100,100,100,100,100,20))
connection.commit()

connection.close()