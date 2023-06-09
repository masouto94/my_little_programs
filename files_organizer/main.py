from files_organizer.files_organizer import *
from files_organizer.data_abm import *

con = DatabaseConnector('./database/pairing.db')

def parse_data(data):
    res = {}
    for tup in data:
        if tup[0] not in res.keys():
            res[tup[0]] = []
        res[tup[0]].append(tup[1])
    return res


data = parse_data(con.select("Select folder, extension from pairings "))

print(data)