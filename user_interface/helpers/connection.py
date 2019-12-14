import MySQLdb


# static variable for connection
conn = None

# method to create connection with database
def connect(host, user, passwd, db):
	try :
		global conn
		conn  = MySQLdb.connect(host=host,user=user, passwd=passwd, db=db)
		# connection.query("SELECT * FROM location")
		# result = connection.store_result()
		# print(result.fetch_row())
		return 1
	except MySQLdb.Error:
		return -1

# method to execute queries and return results
def exec_query(query):
	cur = conn.cursor()
	cur.execute(query)
	# result = conn.store_result()
	return cur

def commit():
	conn.commit()

def close_connection():
	global conn
	conn.close()
