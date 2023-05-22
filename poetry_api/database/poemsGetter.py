import sqlite3
import sys
# tell interpreter where to look
sys.path.insert(0,"/home/matias/Documents/misRepos/my_little_programs/poetry_api")
print(sys.path)
class DatabaseConnector():
    def __init__(self, database) -> None:
        self.database = sqlite3.connect(database)
        self.connector = self.database.cursor()
        self.initial_setup()
    def initial_setup(self):
        self.connector.execute("CREATE TABLE IF NOT EXISTS rule(id NUMERIC, name TEXT, parameters TEXT)")
        return

db = DatabaseConnector('poems.db')
