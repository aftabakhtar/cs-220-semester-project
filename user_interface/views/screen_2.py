# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen_2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_screen_2(object):
    def setupUi2(self, screen_2):
        screen_2.setObjectName("screen_2")
        screen_2.resize(584, 481)
        self.centralwidget = QtWidgets.QWidget(screen_2)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 150, 80, 25))
        self.pushButton.setObjectName("pushButton")
        screen_2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(screen_2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 584, 22))
        self.menubar.setObjectName("menubar")
        screen_2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(screen_2)
        self.statusbar.setObjectName("statusbar")
        screen_2.setStatusBar(self.statusbar)

        self.retranslateUi(screen_2)
        QtCore.QMetaObject.connectSlotsByName(screen_2)

    def retranslateUi(self, screen_2):
        _translate = QtCore.QCoreApplication.translate
        screen_2.setWindowTitle(_translate("screen_2", "MainWindow"))
        self.pushButton.setText(_translate("screen_2", "test"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    screen_2 = QtWidgets.QMainWindow()
    ui = Ui_screen_2()
    ui.setupUi2(screen_2)
    screen_2.show()
    sys.exit(app.exec_())

