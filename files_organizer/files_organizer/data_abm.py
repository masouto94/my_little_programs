import sqlite3
from typing import List

class DatabaseConnector():
    def __init__(self, db: str) -> None:
        self.connection = sqlite3.connect(db)
        self.connection.set_trace_callback(print)

        self.cursor = self.connection.cursor()
        self.setup()

    def _commit_if_success(func):
        def container(*args):
            try:
                self = args[0]
                rows = func(*args)
                self.connection.commit()
                print(f"{rows} rows affected")
                return rows
            except sqlite3.Error as e:
                print(f"{e}")
        return container

    def _replace_placeholders(self, values:List[str]):
        return ', '.join(map(lambda x: x.replace(x,'?'),values))
    
    def setup(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS pairings(id INTEGER PRIMARY KEY, folder VARCHAR, extension VARCHAR UNIQUE)")
        self.connection.commit()

    def select(self, query: str):
       return self.cursor.execute(query).fetchall()

    @_commit_if_success
    def new_pairing(self, name: str, value: str):
        print(f"Saving new pairing {name} - {value}")
        return self.cursor.execute(f"INSERT INTO pairings(folder,extension) VALUES(?,?)", (name,value)).rowcount

    @_commit_if_success
    def new_pairing_batch(self, name: str, values: List[str]):
        data = [(name, value) for value in values]
        print(f"Saving new pairings for {name} with {len(data)} elements")
        return self.cursor.executemany(f"INSERT INTO pairings(folder,extension) VALUES(?,?)", data).rowcount
    
    @_commit_if_success
    def delete_pairing(self, name: str, value: str):
        print(f"Deleting pairing {name} - {value}")
        return self.cursor.execute(f"DELETE FROM pairings WHERE folder=? AND extension=?", (name,value)).rowcount

    @_commit_if_success
    def delete_pairing_batch(self, name: str, values: List[str]):
        print(f"Deleting pairings for {name} with {len(values)} elements")
        return self.cursor.execute(f"DELETE FROM pairings WHERE folder=? AND extension in ({self._replace_placeholders(values)})", (name, *values)).rowcount

    @_commit_if_success
    def delete_key(self, name: str):
        print(f"Deleting key {name}")
        return self.cursor.execute(f"DELETE FROM pairings WHERE folder=?", (name,)).rowcount
    
    @_commit_if_success
    def modify_key(self, name: str, new_name: str):
        print(f"Modifying key {name} to {new_name}")
        return self.cursor.execute(f"UPDATE pairings SET folder = ? WHERE folder = ?;", (new_name,name)).rowcount