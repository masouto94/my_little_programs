import sqlite3
from typing import List

class DatabaseConnector():
    def __init__(self, db: str) -> None:
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.setup()

    def _commit_if_success(self,func):
        count = func.rowcount
        def container():
            try:
                func()
            except sqlite3.Error as e:
                print(f"{e}")
                return
        self.connection.commit()
        print(f"{count} rows affected")
        return container

    def _replace_placeholders(self, values:List[str]):
        return ', '.join(map(lambda x: x.replace(x,'?'),values))
    
    def setup(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS pairings(id INTEGER PRIMARY KEY, folder VARCHAR, extension VARCHAR UNIQUE)")
        self.connection.commit()

    def select(self, query: str):
       return self.cursor.execute(query).fetchall()

    def new_pairing(self, name: str, value: str):
        print(f"Saving new pairing {name} - {value}")
        self._commit_if_success(
                self.cursor.execute(f"INSERT INTO pairings(folder,extension) VALUES(?,?)", (name,value))
                )

    def new_pairing_batch(self, name: str, values: List[str]):
        data = [(name, value) for value in values]
        print(f"Saving new pairings for {name} with {len(data)} elements")
        self._commit_if_success(
            self.cursor.executemany(f"INSERT INTO pairings(folder,extension) VALUES(?,?)", data)
            )

    def delete_pairing(self, name: str, value: str):
        print(f"Deleting pairing {name} - {value}")
        self._commit_if_success(
                self.cursor.execute(f"DELETE FROM pairings WHERE folder=? AND extension=?", (name,value))
                )

    def delete_pairing_batch(self, name: str, values: List[str]):
        print(f"Deleting pairings for {name} with {len(values)} elements")
        self._commit_if_success(
            self.cursor.execute(f"DELETE FROM pairings WHERE folder=? AND extension in ({self._replace_placeholders(values)})", (name, *values))
        )
