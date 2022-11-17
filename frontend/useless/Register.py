# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import json
import sys

import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import config


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 500)
        self.setStyleSheet('QWidget{background-color:white}')
        self.userlineEdit = QtWidgets.QLineEdit(Form)
        self.userlineEdit.setGeometry(QtCore.QRect(220, 80, 260, 40))

        self.passwordlineEdit = QtWidgets.QLineEdit(Form)
        self.passwordlineEdit.setGeometry(QtCore.QRect(220, 160, 260, 40))
        self.passwordlineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.cpasswordlineEdit = QtWidgets.QLineEdit(Form)
        self.cpasswordlineEdit.setGeometry(QtCore.QRect(220, 240, 260, 40))
        self.cpasswordlineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.userNameLabel = QtWidgets.QLabel(Form)
        self.userNameLabel.setGeometry(QtCore.QRect(90, 80, 70, 40))
        self.userNameLabel.setStyleSheet('font:12pt')

        self.passwordLabel = QtWidgets.QLabel(Form)
        self.passwordLabel.setGeometry(QtCore.QRect(90, 160, 70, 40))
        self.passwordLabel.setStyleSheet('font:14pt')

        self.cpasswordLabel = QtWidgets.QLabel(Form)
        self.cpasswordLabel.setGeometry(QtCore.QRect(90, 240, 100, 40))
        self.cpasswordLabel.setStyleSheet('font:12pt')

        self.registerButton = QtWidgets.QPushButton(Form)
        self.registerButton.setGeometry(QtCore.QRect(220, 320, 160, 40))
        self.registerButton.setStyleSheet('font:16pt')

        self.registerLabel = QtWidgets.QLabel(Form)
        self.registerLabel.setGeometry(QtCore.QRect(250, 20, 60, 30))
        self.registerLabel.setStyleSheet('font:16pt')

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.userNameLabel.setText(_translate("Form", "用户名"))
        self.passwordLabel.setText(_translate("Form", "密 码"))
        self.cpasswordLabel.setText(_translate("Form", "确认密码"))
        self.registerButton.setText(_translate("Form", "注册"))
        self.registerLabel.setText(_translate("Form", "注册"))


class Register(QtWidgets.QMainWindow, Ui_Form):
    # singal = pyqtSignal(list)
    def __init__(self):
        super(Register, self).__init__()
        self.setupUi(self)
        self.registerButton.mousePressEvent = self.registerButtonClick

    def registerButtonClick(self, *args):  # 注册
        # 注册的账号存入数据库中
        user = self.userlineEdit.text()
        password = self.passwordlineEdit.text()
        cpassword = self.passwordlineEdit.text()  # 确认密码
        if cpassword != password:
            QMessageBox.Warning(self, '警告！', '两次输入密码不一致')
            return

        data = {'account': user, 'password': password}
        resp = requests.post(config.userRegister, data=data)
        if resp.status_code != 200:
            QMessageBox.warning(self, "注册", "网络连接异常", QMessageBox.Yes, QMessageBox.Yes)
        res = json.loads(resp.content.decode('utf-8'))
        if res['code'] == 1:
            QMessageBox.warning(self, "注册", res['msg'], QMessageBox.Yes, QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "注册", res['msg'], QMessageBox.Yes, QMessageBox.Yes)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Register()
    gui.show()
    sys.exit(app.exec_())
