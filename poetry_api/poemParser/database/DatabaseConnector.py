import sqlite3

class DatabaseConnector():
    def __init__(self, database) -> None:
        self.connection = sqlite3.connect(database)
        self.connection.set_trace_callback(print)
        self.cursor = self.connection.cursor()
        self.initial_setup()
   
    def initial_setup(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS rule(id INTEGER PRIMARY KEY, name VARCHAR, parameters VARCHAR);")
        self.connection.commit()
        return
    
    def select(self, query: str):
       return self.cursor.execute(query).fetchall()

db = DatabaseConnector('poemParser/database/poems.db')
