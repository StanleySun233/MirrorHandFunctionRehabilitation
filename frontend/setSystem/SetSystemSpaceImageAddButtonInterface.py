# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '窗口1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import sys

import cv2
import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import config
import tool.Tools


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(500, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.frame_sub = QtWidgets.QFrame(self.centralwidget)
        self.frame_sub.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.frame_sub.setStyleSheet("QFrame {background-color:rgb(242, 249, 255);}")
        self.frame_sub.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sub.setFrameShadow(QtWidgets.QFrame.Raised)

        self.label_3 = QtWidgets.QLabel(self.frame_sub)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 101, 40))
        self.label_3.setText('*')
        self.label_3.setStyleSheet("font:10pt;color:red")

        self.label = QtWidgets.QLabel(self.frame_sub)
        self.label.setGeometry(QtCore.QRect(30, 30, 101, 40))
        self.label.setStyleSheet("font:12pt")

        self.discriminationDifficultyComboBox = QtWidgets.QComboBox(self.frame_sub)
        self.discriminationDifficultyComboBox.setGeometry(QtCore.QRect(140, 30, 250, 40))
        self.discriminationDifficultyComboBox.addItems(['', '低难度', '中难度', '高难度'])
        self.discriminationDifficultyComboBox.setStyleSheet("font:12pt")

        self.label_4 = QtWidgets.QLabel(self.frame_sub)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 101, 40))
        self.label_4.setText('*')
        self.label_4.setStyleSheet("font:10pt;color:red")

        self.label_2 = QtWidgets.QLabel(self.frame_sub)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 101, 31))
        self.label_2.setStyleSheet("font:12pt")

        self.pictureTypeComboBox = QtWidgets.QComboBox(self.frame_sub)
        self.pictureTypeComboBox.setGeometry(QtCore.QRect(140, 100, 250, 40))
        self.pictureTypeComboBox.addItems(['', '左', '右'])
        self.pictureTypeComboBox.setStyleSheet("font:12pt")

        self.label_3 = QtWidgets.QLabel(self.frame_sub)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 101, 31))
        self.label_3.setStyleSheet("font:12pt")

        self.pictureNameTextbox = QtWidgets.QLineEdit(self.frame_sub)
        self.pictureNameTextbox.setGeometry(QtCore.QRect(140, 180, 250, 40))

        self.uploadPictureButton = QtWidgets.QPushButton(self.frame_sub)
        self.uploadPictureButton.setGeometry(QtCore.QRect(140, 300, 180, 50))
        self.uploadPictureButton.setStyleSheet("background-color:rgb(1, 144, 202);border:none;font:12pt;color:white")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "辨别难度："))
        self.label_2.setText(_translate("MainWindow", "图片类型："))
        self.label_3.setText(_translate("MainWindow", "图片名称："))
        self.uploadPictureButton.setText(_translate("MainWindow", "上传图片"))


class setSystemSpaceImageAddButtonInterface(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(setSystemSpaceImageAddButtonInterface, self).__init__()
        self.setupUi(self)
        self.uploadPictureButton.clicked.connect(self.uploadPictureButtonClick)

    def uploadPictureButtonClick(self, *args):  # 系统设置-空间想象参数设置-上传图片
        try:
            path = QtWidgets.QFileDialog.getOpenFileNames()[0]
            for i in path:
                if i == '':
                    return
                pic = cv2.imread(i)
                _id = tool.Tools.getTimeStamp()
                difficult = self.discriminationDifficultyComboBox.currentText()
                _type = self.pictureTypeComboBox.currentText()
                fileName = os.path.split(i)[1]
                trans = {"左": "left", "右": "right", "低难度": "easy", "中难度": "mid", "高难度": "hard"}
                cv2.imwrite(f"{config.GlobalPath}src/train/{trans[difficult]}/{trans[_type]}/{_id}.png",
                            cv2.resize(pic, (800, 740)))
                self.pictureNameTextbox.setText(i)
                data = {'id': _id, 'name': fileName, 'type': _type, 'difficult': difficult, 'pic_id': f"{_id}.png"}
                print(data)
                requests.post(config.spaceImageConfigInsert, data=data)
        except:
            QMessageBox.warning(self, "添加", "添加失败", QMessageBox.Yes, QMessageBox.Yes)
            return
        QMessageBox.warning(self, "添加", "添加成功", QMessageBox.Yes, QMessageBox.Yes)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = setSystemSpaceImageAddButtonInterface()
    gui.show()
    sys.exit(app.exec_())
