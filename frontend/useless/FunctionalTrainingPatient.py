# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(2200, 1280)
        self.leftPictureLabel = QtWidgets.QLabel(Form)
        self.leftPictureLabel.setGeometry(QtCore.QRect(40, 40, 1000, 1200))
        self.leftPictureLabel.setObjectName("leftPictureLabel")
        self.leftPictureLabel.setStyleSheet("background:rgb(255,255,255)")

        self.rightPictureLabel = QtWidgets.QLabel(Form)
        self.rightPictureLabel.setGeometry(QtCore.QRect(1150, 40, 1000, 1200))
        self.rightPictureLabel.setObjectName("rightPictureLabel")
        self.rightPictureLabel.setStyleSheet("background:rgb(255,255,255)")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


class FunctionalTrainingPatient(QtWidgets.QMainWindow, Ui_Form):  # 基本功能动作训练
    def __init__(self):
        super(FunctionalTrainingPatient, self).__init__()
        self.setupUi(self)

        self.desktop = QApplication.desktop()
        self.setGeometry(self.desktop.screenGeometry(1))

    def showLeftPictureByPicture(self, pic):
        self.leftPictureLabel.setPixmap(pic)
        ...

    def showRightPictureByPicture(self, pic):
        self.rightPictureLabel.setPixmap(pic)
        ...


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = FunctionalTrainingPatient()
    gui.show()
    sys.exit(app.exec_())
