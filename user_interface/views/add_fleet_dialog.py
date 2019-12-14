# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_fleet_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_add_fleet(object):
    def setupUi(self, add_fleet):
        add_fleet.setObjectName("add_fleet")
        add_fleet.resize(369, 187)
        add_fleet.setMinimumSize(QtCore.QSize(369, 187))
        add_fleet.setMaximumSize(QtCore.QSize(369, 187))
        self.buttonBox = QtWidgets.QDialogButtonBox(add_fleet)
        self.buttonBox.setGeometry(QtCore.QRect(0, 130, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.plane_radio = QtWidgets.QRadioButton(add_fleet)
        self.plane_radio.setGeometry(QtCore.QRect(40, 20, 96, 23))
        self.plane_radio.setChecked(True)
        self.plane_radio.setObjectName("plane_radio")
        self.buttonGroup = QtWidgets.QButtonGroup(add_fleet)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.plane_radio)
        self.bus_radio = QtWidgets.QRadioButton(add_fleet)
        self.bus_radio.setGeometry(QtCore.QRect(40, 50, 96, 23))
        self.bus_radio.setObjectName("bus_radio")
        self.buttonGroup.addButton(self.bus_radio)
        self.input = QtWidgets.QLineEdit(add_fleet)
        self.input.setGeometry(QtCore.QRect(40, 90, 301, 25))
        self.input.setObjectName("input")

        self.retranslateUi(add_fleet)
        self.buttonBox.accepted.connect(add_fleet.accept)
        self.buttonBox.rejected.connect(add_fleet.reject)
        QtCore.QMetaObject.connectSlotsByName(add_fleet)

    def retranslateUi(self, add_fleet):
        _translate = QtCore.QCoreApplication.translate
        add_fleet.setWindowTitle(_translate("add_fleet", "Add to fleet"))
        self.plane_radio.setText(_translate("add_fleet", "Plane"))
        self.bus_radio.setText(_translate("add_fleet", "Bus"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     add_fleet = QtWidgets.QDialog()
#     ui = Ui_add_fleet()
#     ui.setupUi(add_fleet)
#     add_fleet.show()
#     sys.exit(app.exec_())
