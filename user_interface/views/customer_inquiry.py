# customer first window

from PyQt5 import QtCore, QtGui, QtWidgets
from user_interface.views.airline_panel import Ui_airline_panel
from user_interface.controllers import connection_controller
from user_interface.helpers import connection
from PyQt5.QtWidgets import QMessageBox

class Ui_customer_inquiry(object):
    cell_loc = None
    def __init__(self, parent=None):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_airline_panel()
        self.ui.setupUi(self.window)
        self.window.show()
        # All the logic related to airline_panel would be handled here
        # connection.exec_query("test")
        # self.ui.tabWidget.currentChanged(0)
        self.setup_tables()

        self.ui.add_employee_button.clicked.connect(lambda: print("Hello"))
        self.ui.schedule_maint_button.clicked.connect(lambda: self.schedule_maintenance())

    def schedule_maintenance(self):
        selected_item = self.ui.fleet_table.currentItem()
        if selected_item is None:
            self.show_popup('Error', 'Please select a vehicle_id first', QMessageBox.Critical)
        else:
            print(selected_item.text())

    def setup_tables(self):
        cursor = connection.exec_query("SELECT * FROM flight JOIN plane USING (plane_id)")
        result = cursor.fetchall()

        self.ui.dash_flight_table.setRowCount(0)
        self.ui.dash_flight_table.setColumnCount(4)
        self.ui.dash_flight_table.setHorizontalHeaderLabels(['flight_id', 'plane_id', 'vehicle_id', 'model'])
        for row, row_data in enumerate(result):
            self.ui.dash_flight_table.insertRow(row)
            for col, col_data in enumerate(row_data):
                # print(row, col, col_data)
                self.ui.dash_flight_table.setItem(row, col, QtWidgets.QTableWidgetItem(str(col_data)))

        # populating fleet table
        cursor = connection.exec_query("(SELECT * FROM vehicle LEFT JOIN plane USING (vehicle_id) LEFT JOIN bus using (vehicle_id))")
        result = cursor.fetchall()
        self.ui.fleet_table.setRowCount(0)
        self.ui.fleet_table.setColumnCount(7)
        self.ui.fleet_table.setHorizontalHeaderLabels(['vehicle_id', 'location_id', 'bought', 'plane_id', 'model', 'bus_id', 'model'])
        for row, row_data in enumerate(result):
            self.ui.fleet_table.insertRow(row)
            for col, col_data in enumerate(row_data):
                # print(row, col, col_data)
                self.ui.fleet_table.setItem(row, col, QtWidgets.QTableWidgetItem(str(col_data)))

        # populating maintenance table
        cursor = connection.exec_query("SELECT * FROM maintenance")
        result = cursor.fetchall()
        self.ui.maintenance_table.setRowCount(0)
        self.ui.maintenance_table.setColumnCount(7)
        self.ui.maintenance_table.setHorizontalHeaderLabels(['maintenace_id', 'vehicle_id', 'cost', 'date', 'time', 'location', 'signed_of_by'])
        for row, row_data in enumerate(result):
            self.ui.maintenance_table.insertRow(row)
            for col, col_data in enumerate(row_data):
                # print(row, col, col_data)
                self.ui.maintenance_table.setItem(row, col, QtWidgets.QTableWidgetItem(str(col_data)))

        # populating employee table
        cursor = connection.exec_query("SELECT * FROM employee")
        result = cursor.fetchall()
        self.ui.employee_table.setRowCount(0)
        self.ui.employee_table.setColumnCount(7)
        self.ui.employee_table.setHorizontalHeaderLabels(['employee_id', 'location_id', 'f_name', 'm_init', 'l_name', 'age', 'salary'])
        for row, row_data in enumerate(result):
            self.ui.employee_table.insertRow(row)
            for col, col_data in enumerate(row_data):
                # print(row, col, col_data)
                self.ui.employee_table.setItem(row, col, QtWidgets.QTableWidgetItem(str(col_data)))


        # populating dashboard
        self.set_dash_status()

        # constantly looking for new addition to database
        # QtCore.QTimer.singleShot(5000, self.setup_tables)


    def set_dash_status(self):
        cursor = connection.exec_query("SELECT SUM(amount) FROM billing")
        finances = cursor.fetchone()[0]
        self.ui.dash_finances_label.setText("$" + str( finances))

        cursor = connection.exec_query("SELECT COUNT(*) FROM employee")
        employees = cursor.fetchone()[0]
        self.ui.dash_employee_label.setText(str(employees))

        cursor = connection.exec_query('SELECT count(*) FROM location')
        routes = cursor.fetchone()[0]
        self.ui.dash_activeR_label.setText(str(routes))

        cursor = connection.exec_query('SELECT count(*) FROM customer')
        passengers = cursor.fetchone()[0]
        self.ui.dash_passenger_label.setText(str(passengers))

        cursor = connection.exec_query('SELECT count(*) FROM vehicle')
        vehicles = cursor.fetchone()[0]
        self.ui.dash_fleet_label.setText(str(vehicles))

        cursor = connection.exec_query('SELECT count(*) FROM plane')
        planes = cursor.fetchone()[0]
        self.ui.dash_planes_label.setText(str(planes))

        cursor = connection.exec_query('SELECT count(*) FROM bus')
        busses = cursor.fetchone()[0]
        self.ui.dash_busses_label.setText(str(busses))

        cursor = connection.exec_query('SELECT count(*) FROM flight')
        flights = cursor.fetchone()[0]
        self.ui.dash_flights_label.setText(str(flights))





    def setupUi(self, MainWindow):
        MainWindow.setObjectName("customer_panel")
        MainWindow.resize(606, 360)
        MainWindow.setMinimumSize(QtCore.QSize(606, 360))
        MainWindow.setMaximumSize(QtCore.QSize(606, 360))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.departure_box = QtWidgets.QComboBox(self.centralwidget)
        self.departure_box.setGeometry(QtCore.QRect(40, 50, 171, 31))
        self.departure_box.setObjectName("departure_box")

        self.arrival_box = QtWidgets.QComboBox(self.centralwidget)
        self.arrival_box.setGeometry(QtCore.QRect(40, 120, 171, 31))
        self.arrival_box.setObjectName("arrival_box")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 101, 17))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 101, 17))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 30, 101, 17))
        self.label_3.setObjectName("label_3")

        self.calendar_widget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar_widget.setGeometry(QtCore.QRect(250, 50, 321, 191))
        self.calendar_widget.setObjectName("calendar_widget")

        self.passenger_box = QtWidgets.QComboBox(self.centralwidget)
        self.passenger_box.setGeometry(QtCore.QRect(40, 190, 171, 31))
        self.passenger_box.setObjectName("passenger_box")

        self.passenger_box.addItem("")
        self.passenger_box.addItem("")
        self.passenger_box.addItem("")
        self.passenger_box.addItem("")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 170, 111, 17))
        self.label_4.setObjectName("label_4")

        self.economyClass_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.economyClass_radioButton.setGeometry(QtCore.QRect(40, 240, 111, 23))
        self.economyClass_radioButton.setChecked(True)
        self.economyClass_radioButton.setObjectName("economyClass_radioButton")

        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.economyClass_radioButton)

        self.firstClass_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.firstClass_radioButton.setGeometry(QtCore.QRect(40, 270, 96, 23))
        self.firstClass_radioButton.setObjectName("firstClass_radioButton")

        self.buttonGroup.addButton(self.firstClass_radioButton)

        self.businessClass_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.businessClass_radioButton.setGeometry(QtCore.QRect(40, 300, 111, 23))
        self.businessClass_radioButton.setObjectName("businessClass_radioButton")

        self.buttonGroup.addButton(self.businessClass_radioButton)

        self.book_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.book_pushButton.setGeometry(QtCore.QRect(479, 280, 91, 31))
        self.book_pushButton.setObjectName("book_pushButton")

        self.getPrice_button = QtWidgets.QPushButton(self.centralwidget)
        self.getPrice_button.setGeometry(QtCore.QRect(370, 280, 91, 31))
        self.getPrice_button.setObjectName("getPrice_button")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 606, 22))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("customer_panel", "Customer Panel"))
        self.label.setText(_translate("MainWindow", "Departure Airport"))
        self.label_2.setText(_translate("MainWindow", "Arrival Airport"))
        self.label_3.setText(_translate("MainWindow", "Date"))
        self.passenger_box.setItemText(0, _translate("MainWindow", "1"))
        self.passenger_box.setItemText(1, _translate("MainWindow", "2"))
        self.passenger_box.setItemText(2, _translate("MainWindow", "3"))
        self.passenger_box.setItemText(3, _translate("MainWindow", "3+"))
        self.label_4.setText(_translate("MainWindow", "No. of Passengers"))
        self.economyClass_radioButton.setText(_translate("MainWindow", "Economy Class"))
        self.firstClass_radioButton.setText(_translate("MainWindow", "First Class"))
        self.businessClass_radioButton.setText(_translate("MainWindow", "Business Class"))
        self.book_pushButton.setText(_translate("MainWindow", "Book Flight"))
        self.getPrice_button.setText(_translate("MainWindow", "Get Price"))

    def show_popup(self, title, text, error_type):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(error_type)
        msg.setStandardButtons(QMessageBox.Ok)

        display = msg.exec_()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_customer_inquiry()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
