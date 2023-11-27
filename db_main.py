import db_library
import os

command_dict = {
	"create table" : db_library.create_table, 
	"add data" : db_library.add_data, 
	"delete row" : db_library.delete_row, 
	"search" : db_library.search_table, 
	"list tables" : db_library.get_tables, 
	"list cols" : db_library.get_cols, 
	"drop table" : db_library.drop, 
	"help" : "help", 
	"exit" : "exit"
}

# while True: 

	# command = input("Create or connect to a database, or exit?")
	
	# if command == "create":

		# connection = db_library.db_init()
		
		# break
		
	# elif command == "connect":

		# db_names = [f[0:-3] for f in os.listdir("./DB/") if ".db" in f]
		
		# print("\n".join(db_names))
		
		# db_name = input("Which database would you like to connect to?")
		
		# if db_name not in db_names:
			
			# print("Error: " + db_name + " is not a database available!")
		# else:
		
			#connection = db_library.db_connect(db_name)
			
			# break
			
	# elif command == "exit":

		# return "Closing program"
		
		# exit()
		
	# else:
		
		# print("Sorry I don't know what you mean, please try again")
			
			# exit()



db_names = [f[0:-3] for f in os.listdir("./DB/") if ".db" in f]
		
print("Database names: \n" + "\n".join(db_names))

db_name = input("Which database would you like to connect to? ")

connection = db_library.db_connect(db_name)

while True:
	
	command = input("Type in command: ")
	
	if command == "help":
		
		print("\n".join(list(command_dict.keys())))
		
	elif command in list(command_dict.keys()):
		
		command_dict[command]
	