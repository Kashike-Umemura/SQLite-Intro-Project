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
	
#	Input: 	connection (sqlite3.connect()); table_name (string)
#	Return:	n/a
#	Desc:	Adds data to an table that exists, if table does not exist must be initialized first. Data must be inputted in the form of:
#				data1, data2, data3, ... , datan
#			Where n is the last attribute of the table. 
def add_data(connection, table_name):

	cursor = connection.cursor()
	
	col_names = get_cols(connection, table_name)
	
	number_of_col = len(col_names)
	
	var = '(?' + ', ?'*(number_of_col - 2) + ')'
	col_id = '(' + ' ,'.join(col_names[1:]) + ')'
	
	data = input('Please input data in the following order: ' + col_id + ' with no brackets')
	data = data.split(', ')
	for i in range(len(data)):
	
		if data[i].isnumeric():
		
			data[i] = int(data[i])
			
		elif ('.' in data[i]):
		
			data[i] = float(data[i])
			
			
	
	data = tuple(data)
	
	sql = "INSERT INTO " + table_name + " " + col_id + " VALUES " + var
	
	cursor.execute(sql, data)
	
	connection.commit()


def delete_row(connection):
	
	info = input("Please input table name, attribute name and deletion criteria.")
	info = info.split(", ")
	
	sql = "DELETE FROM " + info[0] + " WHERE " + info[1] + "=?"
	
	cursor = connection.cursor()
	
	cursor.execute(sql, (info[2],))
	
	cusor.commit()
	
	print("Rows with " + info[1] + " as " + info[2] + " has been deleted from table" + info[0] + ".")

def search_table(connection):
	
	param = input("Please type the table name and the parameters that you would like to search by:")
	
	sql = "SELECT * FROM " + param
	
	cusor = connection.cursor()
	
	rows = cursor.execute(sql).fetchall()
	
	for row in rows:
		print(row)

#	Input:	connection (sqlite3.connect())
#	Output:	table_list (list)
#	Desc:	Returns a list of all table names in the database that it you are currently connected to.
def get_tables(connection):

	sql = "SELECT name FROM sqlite_master WHERE type='table';"

	cursor = connection.cursor()

	table_list = cursor.execute(sql).fetchall()

	return table_list

#	Input:	connection (sqlite3.connect()); table_name (string)
#	Output:	names (list)
# 	Desc:	Returns a list of attribute (column) names in the table that table_name contains.
def get_cols(connection, table_name):

	cursor = connection.execute("SELECT * FROM " + table_name)

	names = list(map(lambda x: x[0], cursor.description))

	return names
