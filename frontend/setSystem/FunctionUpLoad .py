import sys

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(900, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet('background-color:rgb(242, 249, 255)')

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 150, 40))
        self.label.setStyleSheet("font:14pt")

        self.actionNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.actionNameLineEdit.setGeometry(QtCore.QRect(140, 20, 450, 40))
        self.actionNameLineEdit.setStyleSheet("font:14pt;background:white")

        self.actionAudioNameButton = QtWidgets.QPushButton(self.centralwidget)
        self.actionAudioNameButton.setGeometry(QtCore.QRect(600, 20, 250, 40))
        self.actionAudioNameButton.setStyleSheet("background-color:rgb(1, 144, 202);font:14pt;color:white")

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(10, 80, 150, 40))
        self.label_1.setStyleSheet("font:14pt")

        self.actionTypeComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.actionTypeComboBox.setGeometry(QtCore.QRect(140, 80, 250, 40))
        self.actionTypeComboBox.addItems(['', '精细动作', '复合旋转运动', '抓握运动', 'ADL活动', '双手联合运动'])
        self.actionTypeComboBox.setStyleSheet("font:14pt;background:white")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 150, 40))
        self.label_2.setStyleSheet("font:14pt")

        self.actionPartComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.actionPartComboBox.setGeometry(QtCore.QRect(140, 140, 250, 40))
        self.actionPartComboBox.addItems(['', '左', '右'])
        self.actionPartComboBox.setStyleSheet("font:14pt;background:white")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 210, 150, 40))
        self.label_3.setStyleSheet("font:14pt")

        self.actionNumberLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.actionNumberLineEdit.setGeometry(QtCore.QRect(140, 210, 450, 40))
        self.actionNumberLineEdit.setStyleSheet("font:14pt;background:white")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 280, 800, 80))
        self.label_4.setStyleSheet("font:14pt;color:red")
        self.label_4.setWordWrap(True)

        self.actionVedioButton = QtWidgets.QPushButton(self.centralwidget)
        self.actionVedioButton.setGeometry(QtCore.QRect(10, 370, 250, 50))
        self.actionVedioButton.setStyleSheet("background-color:rgb(1, 144, 202);font:14pt;color:white")

        self.actionAudioButton = QtWidgets.QPushButton(self.centralwidget)
        self.actionAudioButton.setGeometry(QtCore.QRect(280, 370, 250, 50))
        self.actionAudioButton.setStyleSheet("background-color:rgb(1, 144, 202);font:14pt;color:white")

        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(550, 370, 120, 50))
        self.saveButton.setStyleSheet("background-color:rgb(1, 144, 202);font:14pt;color:white")

        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(690, 370, 120, 50))
        self.deleteButton.setStyleSheet("background-color:rgb(1, 144, 202);font:14pt;color:white")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "功能动作训练上传页面"))
        self.label.setText(_translate("MainWindow", "动作名称:"))
        self.actionAudioNameButton.setText(_translate("MainWindow", "上传动作名称音频"))
        self.label_1.setText(_translate("MainWindow", "动作类型:"))
        self.label_2.setText(_translate("MainWindow", "动作部位:"))
        self.label_3.setText(_translate("MainWindow", "动作序号:"))
        self.label_4.setText(_translate("MainWindow", "备注:精细动作序号：1-10;复合旋转运动序号：1-6;抓握运动序号:1-4；ADL活动序号：1-5；双手联合运动：1-2"))
        self.actionVedioButton.setText(_translate("MainWindow", "上传动作视频"))
        self.actionAudioButton.setText(_translate("MainWindow", "上传动作音频"))
        self.saveButton.setText(_translate("MainWindow", "保存"))
        self.deleteButton.setText(_translate("MainWindow", "删除"))


class functionUpLoad(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(functionUpLoad, self).__init__()
        self.setupUi(self)
        self.saveButton.clicked.connect(self.saveButtonClick)
        self.deleteButton.clicked.connect(self.deleteButtonClick)
        self.actionAudioButton.clicked.connect(self.actionAudioButtonClick)
        self.actionVedioButton.clicked.connect(self.actionVedioButtonClick)
        self.actionAudioNameButton.clicked.connect(self.actionAudioNameButtonClick)
        #

    def saveButtonClick(self, *args):
        ...

    def deleteButtonClick(self, *args):
        ...

    def actionAudioButtonClick(self, *args):
        ...

    def actionVedioButtonClick(self, *args):
        ...

    def actionAudioNameButtonClick(self, *args):
        ...


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = functionUpLoad()
    gui.show()
    sys.exit(app.exec_())
