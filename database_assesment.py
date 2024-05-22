'''
docstring
'''

import sqlite3

Database = "clashroyale_database.db"

with sqlite3.connect(Database) as db:
    cursor = db.cursor()
    sql = "SELECT * FROM card;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #prints nicely
    for card in results:
        print(f"ID: {card[0]} Name: {card[8]} Elixir: {card[4]}")

#closes the db
db.close()

