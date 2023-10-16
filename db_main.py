import db_library
import os

command_map = ["create table" : db_library.create_table, "add data" : db_library.add_data, "delete row" : db_library.delete_row, "search" : db_library.search_table,
	"help" : "help", "list tables" : db_library.get_tables, "list cols" : db_library.get_cols, "drop table" : db_library.drop]

command = input("Create or connect to a database?")

if command == "create":

	db_library.db_init()
	
elif command == "connect":

	db_names = [f[0:-3] for f in os.listdir("./DB/") if ".db" in f]
	
	print("\n".join(db_names))
	
	db_name = input("Which database would you like to connect to?")
	
	if db_name not in db_names:
		Print("Error: " + db_name + " is not a database available!")
		
	db_library.db_connect(db_name)

while command != "exit":
	
	command = input
	