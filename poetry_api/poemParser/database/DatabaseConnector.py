import sqlite3

class DatabaseConnector():
    def __init__(self, database) -> None:
        self.connection = sqlite3.connect(database)
        self.connection.set_trace_callback(print)
        self.cursor = self.connection.cursor()
        self.initial_setup()
   
    def initial_setup(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS poems(id INTEGER PRIMARY KEY, title VARCHAR, author VARCHAR, object VARCHAR);")
        self.connection.commit()
        return
    
    def select(self, query: str):
       return self.cursor.execute(query).fetchall()
    
    def show_tables(self):
        return self.cursor.execute("SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%'").fetchall()

db = DatabaseConnector('poemParser/database/poems.db')

print(db.show_tables())