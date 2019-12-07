import MySQLdb


# method to create connection with database
def connect(host, user, passwd, db):
	try :
		connection  = MySQLdb.connect(host=host,user=user, passwd=passwd, db=db)
		# connection.query("SELECT * FROM location")
		# result = connection.store_result()
		return 1
	except MySQLdb.Error:
		return -1

