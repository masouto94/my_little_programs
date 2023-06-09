import sqlite3
from typing import List

class DatabaseConnector():
    def __init__(self, db: str) -> None:
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.setup()

    def setup(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS pairings(id INTEGER PRIMARY KEY, folder VARCHAR, extension VARCHAR UNIQUE)")
        self.connection.commit()

    def select(self, query: str):
       return self.cursor.execute(query).fetchall()

    def new_pairing(self, name: str, values: List):
        data = [(name, value) for value in values]
        try:
            self.cursor.executemany(f"INSERT INTO pairings(folder,extension) VALUES(?,?)", data)
        except sqlite3.Error as e:
            print(f"Could not save {name} {data}. {e}")
            return
        self.connection.commit()
        print(f"Saved new pairing for {name}")
    



