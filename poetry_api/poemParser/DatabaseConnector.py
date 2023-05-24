import sqlite3

class DatabaseConnector():
    def __init__(self, database) -> None:
        self.database = sqlite3.connect(database)
        self.connector = self.database.cursor()
       # self.initial_setup()
    # def initial_setup(self):
    #     self.connector.execute("CREATE TABLE IF NOT EXISTS rule(id INTEGER PRIMARY KEY, name TEXT, parameters TEXT)")
    #     return

db = DatabaseConnector('poems.db')
