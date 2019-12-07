import MySQLdb


# method to create connection with database
def connect(host, user, passwd, db):
	conn  = MySQLdb.connect(host=host,user=root, passwd=passwd, db=db)
	conn.query("SELECT * FROM location")
	result = conn.store_result()
	print(result.fetch_row())

