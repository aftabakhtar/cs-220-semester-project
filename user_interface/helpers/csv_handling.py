import csv
import os

# method to read csv and convert it into list
def read_credentials():
	path = os.path.join(os.getcwd(), "user_interface", "helpers", "connection.csv")
	with open(path) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			# as there is only one row so returning it
			return row

def write_credentials(credentials):
	path = os.path.join(os.getcwd(), "user_interface", "helpers", "connection.csv")
	with open(path, "w") as csv_file:
		writer = csv.writer(csv_file, delimiter=',')
		writer.writerow(credentials)