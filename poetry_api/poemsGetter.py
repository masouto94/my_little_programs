import sqlite3

db = sqlite3.connect("poems.db")
cursor = db.cursor()
cursor.execute
print(cursor.execute("SELECT name FROM sqlite_master").fetchall())