# customer first window

from PyQt5 import QtCore, QtGui, QtWidgets
from user_interface.views.airline_panel import Ui_airline_panel
from user_interface.controllers import connection_controller
from user_interface.helpers import connection

class Ui_customer_inquiry(object):
    def __init__(self, parent=None):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_airline_panel()
        self.ui.setupUi(self.window)
        self.window.show()
        # All the logic related to airline_panel would be handled here
        connection.exec_query(connection.conn, "test")
        self.ui.add_employee_button.clicked.connect(lambda: print("Hello"))

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


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_customer_inquiry()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
