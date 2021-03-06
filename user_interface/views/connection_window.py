# imports
from PyQt5 import QtCore, QtGui, QtWidgets
from user_interface.helpers import csv_handling
from user_interface.helpers import connection
from PyQt5.QtWidgets import QMessageBox


class Ui_connection_window(object):
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

