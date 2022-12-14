# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '窗口2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(1100, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.frame_sub = QtWidgets.QFrame(self.centralwidget)
        self.frame_sub.setGeometry(QtCore.QRect(0, 0, 1100, 900))
        self.frame_sub.setStyleSheet("QFrame {\n"
                                     "  background-color:rgb(242, 249, 255);\n"
                                     "}")
        self.frame_sub.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sub.setFrameShadow(QtWidgets.QFrame.Raised)

        self.label = QtWidgets.QLabel(self.frame_sub)
        self.label.setGeometry(QtCore.QRect(10, 20, 150, 40))
        self.label.setStyleSheet('font:14pt')

        self.discriminationDifficultyComboBox = QtWidgets.QComboBox(self.frame_sub)  # 辨别难度
        self.discriminationDifficultyComboBox.setGeometry(QtCore.QRect(140, 20, 150, 40))
        self.discriminationDifficultyComboBox.addItems(['', '低难度', '中难度',  '高难度'])
        self.discriminationDifficultyComboBox.setStyleSheet("font:12pt")

        self.label_2 = QtWidgets.QLabel(self.frame_sub)
        self.label_2.setGeometry(QtCore.QRect(300, 20, 130, 40))
        self.label_2.setStyleSheet('font:14pt')

        self.pictureTypeComboBox = QtWidgets.QComboBox(self.frame_sub)
        self.pictureTypeComboBox.setGeometry(QtCore.QRect(440, 20, 150, 40))
        self.pictureTypeComboBox.addItems(['', '左', '右'])
        self.pictureTypeComboBox.setStyleSheet("font:12pt")

        self.saveButton = QtWidgets.QPushButton(self.frame_sub)
        self.saveButton.setGeometry(QtCore.QRect(600, 20, 120, 40))
        self.saveButton.setStyleSheet("background-color:rgb(1, 144, 202);border:none;font:12pt;color:white")

        self.deleteButton = QtWidgets.QPushButton(self.frame_sub)
        self.deleteButton.setGeometry(QtCore.QRect(750, 20, 120, 40))
        self.deleteButton.setStyleSheet("background-color:rgb(1, 144, 202);border:none;font:12pt;color:white")

        self.showPictureLabel = QtWidgets.QLabel(self.frame_sub)
        self.showPictureLabel.setGeometry(QtCore.QRect(10, 70, 1080, 820))
        self.showPictureLabel.setStyleSheet("border-width: 1px;border-style: solid;border-color:black")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "辨别难度："))
        self.label_2.setText(_translate("MainWindow", "图片类型："))
        self.saveButton.setText(_translate("MainWindow", "保存"))
        self.deleteButton.setText(_translate("MainWindow", "删除"))


class setSystemSpaceImageEditDataInterface(QtWidgets.QMainWindow, Ui_MainWindow):  # 点击每条记录出现的界面，可以编辑和删除
    def __init__(self):
        super(setSystemSpaceImageEditDataInterface, self).__init__()
        self.setupUi(self)
        self.saveButton.clicked.connect(self.saveButtonClick)
        self.deleteButton.clicked.connect(self.deleteButtonClick)

    def saveButtonClick(self, *args):  # 系统设置-空间想象参数设置-保存编辑过的图片
        ...

    def deleteButtonClick(self, *args):  # 系统设置-空间想象参数设置-删除图片
        ...


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = setSystemSpaceImageEditDataInterface()
    gui.show()
    sys.exit(app.exec_())
