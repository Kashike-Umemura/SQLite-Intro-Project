import sqlite3
import os


#	Input:	n/a
#	Return:	db_connect(db_name) (sqlite3.connect())
#	Desc:	Use to initiate a new SQLite3 database and returns a sqlite3.connect() 
#			object of the initialized database.
def db_init():
	
	db_name = input("Name of database to initialize: ").strip()
	
	DB_PATH = '.\\DB\\' + db_name + '.db'
	
	if not os.path.exists('DB'):
		os.makedirs('DB')
	
	return db_connect(db_name)
	

#	Input:	db_name (String)
#	Return:	connection (sqlite3.connect())
#	Desc:	Connects to the name of the database that you has been specified.
def db_connect(db_name):
	
	print("Connecting to " + db_name)
	
	connection = sqlite3.connect('.\\DB\\' + db_name + '.db')
	
	print("Connected")
	
	return connection


#	Input:	connection (sqlite3.connect())
#	Return:	n/a 
#	Desc:	Initializes a table with specified name and attributes, optional arguments such as keys and types are
#			available to be used as well.
def create_table(connection):
	
	cursor = connection.cursor()
	
	while True:
		table_name = input('Type table name:')
		
		if table_name[0].isnumeric():
			
			print('Table name cannot start with a digit!')
			
			continue
		else:
		
			break
	
	table_name = '_'.join(table_name.split())
	
	table_attributes = input('Type the attributes of the table, separated by a blank space, with the first one being '
							 'it\'s primary key:')
	
	attribute_list = table_attributes.split()
	
	for i in range(len(attribute_list)):
		
		option = input('Enter type and optional arguments for attribute: ' + attribute_list[i])
		
		attribute_list[i] = attribute_list[i] + ' ' + option
	
	sql = 'CREATE TABLE IF NOT EXISTS ' + table_name + '(' + ' ,'.join(attribute_list) + ')'

	cursor.execute(sql)
	
	connection.commit()
	

def add_data(connection, table_name):

	cursor = connection.execute("SELECT * FROM " + table_name)

	names = list(map(lambda x: x[0], cursor.description))

	print(names)


#def delete_row(connection):


#def search_table(connection):


def get_tables(connection):

	sql = "SELECT name FROM sqlite_master WHERE type='table';"

	cursor = connection.cursor()

	table_list = cursor.execute(sql).fetchall()

	return table_list


def get_cols(connection, table_name):

	cursor = connection.execute("SELECT * FROM " + table_name)

	names = list(map(lambda x: x[0], cursor.description))

	return names


if __name__ == '__main__':
	#connect = db_init()
	#create_table(connect)
	connect = db_connect('test')
	get_tables(connect)
