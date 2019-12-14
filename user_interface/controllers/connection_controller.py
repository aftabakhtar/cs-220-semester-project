# logic for controllig connection window

# imports
import random
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from user_interface.helpers import csv_handling
from user_interface.helpers import connection
from PyQt5.QtWidgets import QMessageBox

from user_interface.views.connection_window import Ui_connection_window
from user_interface.views.customer_inquiry import Ui_customer_inquiry
from user_interface.views.airline_panel import Ui_airline_panel
from user_interface.views import airline_panel

class connection_controller(QMainWindow):

	def __init__(self, parent=None):
		super(connection_controller, self).__init__(parent)
		self.ui = Ui_connection_window()
		self.ui.setupUi(self)
		self.show()

		# connecting with login button
		self.ui.login_button.clicked.connect(lambda: self.login_clicked())

		# reading credentials from csv
		self.credentials = csv_handling.read_credentials()

	# handling login button clicked
	def login_clicked(self):
		conn = connection.connect(host=self.ui.host_field.text(), user=self.ui.username_field.text(), passwd=self.ui.password_field.text(), db=self.ui.database_field.text())

		# error handling
		if conn is 1:
			self.credentials = []
			self.credentials.append(self.ui.username_field.text())
			self.credentials.append(self.ui.password_field.text())
			self.credentials.append(self.ui.host_field.text())
			self.credentials.append(self.ui.database_field.text())
			csv_handling.write_credentials(self.credentials)
			self.show_popup("Success", "Connection was successfully established.", QMessageBox.Information)
			self.hide()

			# Here we will setup second window as well as hide this window
			# may be removed later
			self.window = QtWidgets.QMainWindow()
			self.ui = Ui_customer_inquiry()
			self.ui.setupUi(self.window)
			self.window.show()

			# the logic for the customer panel would be handled here
			# starting logic building for customer panel
			airport_codes = connection.exec_query("SELECT airport_code FROM location")
			codes = [item[0] for item in airport_codes.fetchall()]

			# populating combo boxes
			for code in codes:
				self.ui.arrival_box.addItem(code)
				self.ui.departure_box.addItem(code)
			self.ui.arrival_box.setCurrentIndex(1)

			self.ui.book_pushButton.clicked.connect(lambda: self.book_flight())
			date = self.ui.getPrice_button.clicked.connect(lambda: self.get_price())
			# look at the constructor of customer_inquiry.py view

		else:
			self.show_popup("Error", "Error in establishing connection. Please make sure you have entered the right credentials.", QMessageBox.Critical)

	# show_popup for displaying warnings and messages
	def show_popup(self, title, text, error_type):
		msg = QMessageBox()
		msg.setWindowTitle(title)
		msg.setText(text)
		msg.setIcon(error_type)
		msg.setStandardButtons(QMessageBox.Ok)

		display = msg.exec_()

	# method for filling in the credentials
	def set_credentials(self):
		# setting the text on the fields
		self.ui.username_field.setText(self.credentials[0])
		self.ui.password_field.setText(self.credentials[1])
		self.ui.host_field.setText(self.credentials[2])
		self.ui.database_field.setText(self.credentials[3])

	def book_flight(self):
		cur = connection.exec_query("SELECT plane_id from plane")
		planes = [item[0] for item in cur.fetchall()]
		cur = connection.exec_query("SELECT flight_id from flight")
		flights = [item[0] for item in cur.fetchall()]
		flight = max(flights) + 1
		plane = random.choice(planes)
		query = "INSERT INTO flight VALUES (" + str(flight) + ", " + str(plane) + ")"
		print(query)
		cur = connection.exec_query(query)
		connection.commit()

	def get_price(self):
		text = self.ui.calendar_widget.selectedDate()
		print(text.toString())

	# Method that may be used to pass the current window with ui
	def get_self(self):
		return self

def show_window():
	app = QtWidgets.QApplication(sys.argv)
	connection_window = QtWidgets.QMainWindow()
	ui = connection_controller()

	# custom method call to set the text according to csv
	ui.set_credentials()
	sys.exit(app.exec_())
