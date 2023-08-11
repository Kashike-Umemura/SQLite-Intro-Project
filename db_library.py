import sqlite3
import os

def db_init():
	
	db_name = input("Name of database to initialize: ").strip()
	
	DB_PATH = '.\\DB\\' + db_name + '.db'
	
	if not os.path.exists('DB'):
		os.makedirs('DB')
	
	return db_connect(db_name)

	
def db_connect(db_name):
	
	print("Connecting to " + db_name)
	
	connection = sqlite3.connect('.\\DB\\' + db_name + '.db')
	
	print("Connection returned")
	
	return connection

def create_table(connection):
	
	cursor = connection.cursor()
	
	while True:
		table_name = input('Type table name')
		
		if table_name[0].isnumeric():
			
			print('Table name cannot start with a digit!')
			
			continue
		else:
		
			break
	
	table_name = table_name.split().join('_')
	
	table_attributes = input('Type the attributes of the table and the type (NULL, INTEGER, TEXT, NULL, BLOB), separated by a blank space, with the first one being it\'s primary key:')
	
	attribute_list = table_attributes.split()
	primary_key = attribute_list[0]
	other_attribute = attribute_list[1:]
	
	sql = 'CREATE TABLE ' + primary_key + ' INTEGER PRIMARY KEY AUTOINCREMENT' + 

if __name__ == '__main__':
	db_init()