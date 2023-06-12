import sqlite3
from typing import List

class DatabaseConnector():
    def __init__(self, db: str) -> None:
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.setup()

    def _commit_if_success(self,func):
        def container(*args):
            try:
                func(*args)
            except sqlite3.Error as e:
                print(f"{e}")
                return
        self.connection.commit()
        return container

    def setup(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS pairings(id INTEGER PRIMARY KEY, folder VARCHAR, extension VARCHAR UNIQUE)")
        self.connection.commit()

    def select(self, query: str):
       return self.cursor.execute(query).fetchall()

    # def new_pairing(self, name: str, value: str):
    #         try:
    #             self.cursor.execute(f"INSERT INTO pairings(folder,extension) VALUES(?,?)", (name,value))
    #         except sqlite3.Error as e:
    #             print(f"Could not save {name} {value}. {e}")
    #             return
    #         self.connection.commit()
    #         print(f"Saved new pairing for {name}")

    def new_pairing(self, name: str, value: str):
        self._commit_if_success(
                self.cursor.execute(f"INSERT INTO pairings(folder,extension) VALUES(?,?)", (name,value))
                )
        print(f"Saved new pairing for {name}")

    def new_pairing_batch(self, name: str, values: List[str]):
        try:
            data = [(name, value) for value in values]
            query = self.cursor.executemany(f"INSERT INTO pairings(folder,extension) VALUES(?,?)", data)
        except sqlite3.Error as e:
            print(f"Could not save {name} {data}. {e}")
            return
        self.connection.commit()
        print(f"Saved new pairings for {name} with {query.rowcount} elements")

    def delete_pairing(self, name: str, value: str):
        try:
            self.cursor.execute(f"DELETE FROM pairings WHERE folder=? AND extension=?", (name,value))
        except sqlite3.Error as e:
            print(f"Could not delete {name} {value}. {e}")
            return
        self.connection.commit()
        print(f"Deleted pairing {name} - {value}")

    def delete_pairing_batch(self, name: str, values: List[str]):
        try:
           query = self.cursor.execute(f"DELETE FROM pairings WHERE folder=? AND extension in ({self._replace_placeholders(values)})", (name, *values))
        except sqlite3.Error as e:
            print(f"Could not delete {name} {values}. {e}")
            return
        self.connection.commit()
        print(f"Deleted pairings for {name} with {query.rowcount} elements")

    def _replace_placeholders(self, values:List[str]):
        return ', '.join(map(lambda x: x.replace(x,'?'),values))