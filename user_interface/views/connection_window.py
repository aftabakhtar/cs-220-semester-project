# imports
from PyQt5 import QtCore, QtGui, QtWidgets
from user_interface.helpers import csv_handling
from user_interface.helpers import connection
from PyQt5.QtWidgets import QMessageBox

#maybe removed
from user_interface.views.screen_2 import Ui_screen_2

class Ui_connection_window(object):
    # constructor method to set the text in csv file
    def __init__(self):
        self.credentials = csv_handling.read_credentials()
        

    def setupUi(self, connection_window):
        connection_window.setObjectName("connection_window")
        connection_window.resize(290, 280)
        connection_window.setMinimumSize(QtCore.QSize(290, 280))
        connection_window.setMaximumSize(QtCore.QSize(290, 280))

        self.centralwidget = QtWidgets.QWidget(connection_window)
        self.centralwidget.setObjectName("centralwidget")

        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(180, 230, 80, 25))
        self.login_button.setObjectName("login_button")
        

        self.usernam_label = QtWidgets.QLabel(self.centralwidget)
        self.usernam_label.setGeometry(QtCore.QRect(30, 20, 61, 17))
        self.usernam_label.setObjectName("usernam_label")

        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(30, 70, 61, 17))
        self.password_label.setObjectName("password_label")

        self.username_field = QtWidgets.QLineEdit(self.centralwidget)
        self.username_field.setGeometry(QtCore.QRect(30, 40, 231, 25))
        self.username_field.setObjectName("username_field")

        self.password_field = QtWidgets.QLineEdit(self.centralwidget)
        self.password_field.setGeometry(QtCore.QRect(30, 90, 231, 25))
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_field.setObjectName("password_field")

        self.host_field = QtWidgets.QLineEdit(self.centralwidget)
        self.host_field.setGeometry(QtCore.QRect(30, 140, 231, 25))
        self.host_field.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.host_field.setObjectName("host_field")

        self.host_label = QtWidgets.QLabel(self.centralwidget)
        self.host_label.setGeometry(QtCore.QRect(30, 120, 55, 17))
        self.host_label.setObjectName("host_label")

        self.database_label = QtWidgets.QLabel(self.centralwidget)
        self.database_label.setGeometry(QtCore.QRect(30, 170, 61, 17))
        self.database_label.setObjectName("database_label")

        self.database_field = QtWidgets.QLineEdit(self.centralwidget)
        self.database_field.setGeometry(QtCore.QRect(30, 190, 231, 25))
        self.database_field.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.database_field.setObjectName("database_field")

        connection_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(connection_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 290, 22))
        self.menubar.setObjectName("menubar")

        connection_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(connection_window)
        self.statusbar.setObjectName("statusbar")
        connection_window.setStatusBar(self.statusbar)

        self.retranslateUi(connection_window)
        QtCore.QMetaObject.connectSlotsByName(connection_window)

        # attaching with button
        self.login_button.clicked.connect(lambda: self.login_clicked())

    def retranslateUi(self, connection_window):
        _translate = QtCore.QCoreApplication.translate
        connection_window.setWindowTitle(_translate("connection_window", "Connection"))
        self.login_button.setText(_translate("connection_window", "Login"))
        self.usernam_label.setText(_translate("connection_window", "Username"))
        self.password_label.setText(_translate("connection_window", "Password"))
        self.host_field.setText(_translate("connection_window", "localhost"))
        self.host_label.setText(_translate("connection_window", "Host"))
        self.database_label.setText(_translate("connection_window", "Database"))
        self.database_field.setText(_translate("connection_window", "flight_service"))

    # method for filling in the credentials
    def set_credentials(self):
        # setting the text on the fields
        self.username_field.setText(self.credentials[0])
        self.password_field.setText(self.credentials[1])
        self.host_field.setText(self.credentials[2])
        self.database_field.setText(self.credentials[3])

    # method for handling login button
    def login_clicked(self):
        conn = connection.connect(host=self.host_field.text(), user=self.username_field.text(), passwd=self.password_field.text(), db=self.database_field.text())
        
        # error handling
        if conn is 1:
            self.credentials = []
            self.credentials.append(self.username_field.text())
            self.credentials.append(self.password_field.text())
            self.credentials.append(self.host_field.text())
            self.credentials.append(self.database_field.text())
            csv_handling.write_credentials(self.credentials)
            self.show_popup("Success", "Connection was successfully established.", QMessageBox.Information)
            
            # Here we will setup second window as well as hide this window
            # may be removed later
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_screen_2()
            self.ui.setupUi2(self.window)
            self.window.show()
            


        else:
            self.show_popup("Error", "Error in establishing connection. Please make sure you have entered the right credentials.", QMessageBox.Critical)

    # method to show popups
    def show_popup(self, title, text, error_type):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(error_type)
        msg.setStandardButtons(QMessageBox.Ok)

        display = msg.exec_()


def show_window():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    connection_window = QtWidgets.QMainWindow()
    ui = Ui_connection_window()
    ui.setupUi(connection_window)

    # custom method call to set the text according to csv
    ui.set_credentials()
    
    connection_window.show()
    sys.exit(app.exec_())

    
