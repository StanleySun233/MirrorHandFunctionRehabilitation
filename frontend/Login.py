# 登录界面
import json
import sys

import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QGraphicsOpacityEffect, QMessageBox

import config
import frontend


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1600, 980)
        Form.setStyleSheet("background-image:url(./src/fig/login.png)")

        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.5)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(120, 140, 650, 700))
        self.label_3.setGraphicsEffect(self.opacity)

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(360, 400, 170, 60))
        self.label_4.setText('Welcome')
        self.label_4.setStyleSheet('''font:24pt;color:white;background-color:Transparent;''')

        # self.label_4.setGraphicsEffect(self.opacity.setOpacity(0))

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(250, 460, 440, 60))
        self.label_5.setText('多模态镜像管理系统')
        self.label_5.setStyleSheet('''font:24pt;color:white''')

        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(770, 140, 650, 700))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setStyleSheet('''QFrame{border:sold 10px rgba(0,0,0);background:white;}''')

        self.accountEntry = QtWidgets.QLineEdit(self.frame)
        self.accountEntry.setGeometry(QtCore.QRect(100, 120, 480, 50))
        self.accountEntry.setStyleSheet("background:white")
        # self.lineEdit.setStyleSheet('''QLineEdit{background-color:white;font-size:16px;font-style:MingLiU-ExtB;}''')

        self.passwordEntry = QtWidgets.QLineEdit(self.frame)
        self.passwordEntry.setGeometry(QtCore.QRect(100, 280, 480, 50))
        self.passwordEntry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEntry.setStyleSheet( "background:white")

        self.rememberCheckbox = QtWidgets.QCheckBox(self.frame)
        self.rememberCheckbox.setGeometry(QtCore.QRect(100, 360, 160, 30))
        self.rememberCheckbox.setStyleSheet(
            '''QCheckBox{background:rgba(85,170,255,0);color:black;font:14pt;font-style:MingLiU-ExtB;}''')

        self.forgetLabel = QtWidgets.QLabel(self.frame)
        self.forgetLabel.setGeometry(QtCore.QRect(240, 340, 120, 70))
        self.forgetLabel.setStyleSheet(
            '''QLabel{background-color:rgba(85,170,255,0);color:black;font-style:MingLiU-ExtB;font:14pt;}''')

        self.registerLabel = QtWidgets.QLabel(self.frame)
        self.registerLabel.setGeometry(QtCore.QRect(400, 340, 120, 70))
        self.registerLabel.setStyleSheet(
            '''QLabel{background-color:rgba(85,170,255,0);color:black;font-style:MingLiU-ExtB;font:14pt;}''')

        self.loginButton = QtWidgets.QPushButton(self.frame)
        self.loginButton.setGeometry(QtCore.QRect(100, 430, 480, 50))
        self.loginButton.setStyleSheet(
            '''QPushButton{background:#63B8FF;border-style:outset;border-radius:10px;font-style:MingLiU-ExtB;font:20pt;color:white;}''')

        self.exitButton = QtWidgets.QPushButton(self.frame)
        self.exitButton.setGeometry(QtCore.QRect(100, 530, 480, 50))
        self.exitButton.setStyleSheet(
            '''QPushButton{background:#63B8FF;border-style:outset;border-radius:10px;font-style:MingLiU-ExtB;font:20pt;color:white;}''')

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.accountEntry.setPlaceholderText(_translate("Form", "用户名"))
        self.passwordEntry.setPlaceholderText(_translate("Form", "密码"))
        self.rememberCheckbox.setText(_translate("Form", "记住"))
        self.forgetLabel.setText(_translate("Form", "忘记密码"))
        self.registerLabel.setText(_translate("Form", "注册账号"))
        self.loginButton.setText(_translate("Form", "登录"))
        self.exitButton.setText(_translate("Form", "退出"))


class login(QtWidgets.QMainWindow, Ui_Form):
    # singal = pyqtSignal(list)
    def __init__(self, accountId):
        super(login, self).__init__()
        self.forgetWindow = None
        self.registerWindow = None
        self.mainWindow = None
        self.setupUi(self)
        self.loginButton.mousePressEvent = self.loginButtonLeftClick
        self.forgetLabel.mousePressEvent = self.forgetButtonLeftClick
        self.exitButton.mousePressEvent = self.exitButtonClick
        self.accountId = accountId

    def loginButtonLeftClick(self, *args):
        account = self.accountEntry.text()
        password = self.passwordEntry.text()

        if account == '' or password == '':
            QMessageBox.warning(self, "登录", "账号或密码为空！", QMessageBox.Yes, QMessageBox.Yes)
            return

        data = {'account': account, 'password': password}
        resp = requests.post(config.userLogin, data=data)
        if resp.status_code != 200:
            QMessageBox.warning(self, "登录", "网络连接异常", QMessageBox.Yes, QMessageBox.Yes)
        res = json.loads(resp.content.decode('utf-8'))

        if res['code'] == 1:
            self.mainWindow = frontend.NewMainInterface.mainInterface(res['data'])
            self.mainWindow.show()
            self.close()
        else:
            # 登陆失败，密码错误or账号不存在，直接调用后端的提示信息
            QMessageBox.warning(self, "登录", res['msg'], QMessageBox.Yes, QMessageBox.Yes)

    def exitButtonClick(self, *args):
        self.close()

    def forgetButtonLeftClick(self, *args):
        self.forgetWindow = frontend.ForgetPassword.ForgetPassword(None)

        self.forgetWindow.show()


def run():
    app = QtWidgets.QApplication(sys.argv)
    gui = login(None)
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
