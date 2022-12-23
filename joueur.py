import cgi 
import sqlite3 
import json

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

dict_result = {}

connection = sqlite3.connect('Api.db')
cursor = connection.cursor()
cursor.execute("""SELECT * FROM players""")
users = cursor.fetchall()

for user in users:
    dict_result[user[0]] = (
        {
            "pseudo": user[1], 
            "lvl":user[2], 
            "maxHp":user[3],
            "maxMana": user[4], 
            "hp":user[5], 
            "mana":user[6],
            "xp":user[7], 
            "atq":user[8]
        }
    )
connection.close()

json_result = json.dumps(dict_result, indent = 4)
print(json_result)