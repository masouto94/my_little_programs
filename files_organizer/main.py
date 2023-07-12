from files_organizer.files_organizer import *
from files_organizer.data_abm import *
from files_organizer.arg_parser import get_parser
from interface.custom_interface import InterfaceParser

con = DatabaseConnector('./database/pairing.db')
args = get_parser().parse_args()
if args.customize:
    collector = InterfaceParser(con)
    collector.launch()

if args.filesDir:
    data = parse_data(con.select("Select folder, extension from pairings"))
    pair_files_by_type(args.filesDir,data)

