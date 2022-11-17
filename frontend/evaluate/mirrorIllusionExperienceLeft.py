# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '26.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import json
import sys

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QFileDialog

import config
import tool


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(1500, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet('background-color:rgb(242, 249, 255)')

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(500, 10, 400, 41))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet('font:16pt')

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 60, 200, 40))
        self.label.setStyleSheet('font:14pt')

        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(160, 60, 200, 40))
        self.name.setStyleSheet('font:14pt')

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 60, 200, 40))
        self.label_2.setStyleSheet('font:14pt')

        self.gender = QtWidgets.QLabel(self.centralwidget)
        self.gender.setGeometry(QtCore.QRect(360, 60, 200, 40))
        self.gender.setStyleSheet('font:14pt')

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 60, 200, 40))
        self.label_3.setStyleSheet('font:14pt')

        self.age = QtWidgets.QLabel(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(560, 60, 200, 40))
        self.age.setStyleSheet('font:14pt')

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(680, 60, 200, 40))
        self.label_4.setStyleSheet('font:14pt')

        self.hand = QtWidgets.QLabel(self.centralwidget)
        self.hand.setGeometry(QtCore.QRect(760, 60, 200, 40))
        self.hand.setStyleSheet('font:14pt')

        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(20, 140, 920, 40))
        self.label_23.setStyleSheet("font:14pt;font-weight:bold")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 200, 920, 40))
        self.label_5.setStyleSheet("font:14pt")

        self.oneScore = QtWidgets.QComboBox(self.centralwidget)
        self.oneScore.setGeometry(QtCore.QRect(955,200, 120, 40))
        self.oneScore.addItems(['','-5','-4','-3','-2','-1','0','1','2','3','4','5'])
        self.oneScore.setStyleSheet("font:14pt;background:white")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1075, 200, 100, 40))
        self.label_8.setStyleSheet("font:14pt")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 260, 920, 40))
        self.label_9.setStyleSheet("font:14pt")

        self.twoScore = QtWidgets.QComboBox(self.centralwidget)
        self.twoScore.setGeometry(QtCore.QRect(955, 260, 120, 40))
        self.twoScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.twoScore.setStyleSheet("font:14pt;background:white")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1075, 260, 100, 40))
        self.label_7.setStyleSheet("font:14pt")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 320, 760, 40))
        self.label_10.setStyleSheet("font:14pt")

        self.threeScore = QtWidgets.QComboBox(self.centralwidget)
        self.threeScore.setGeometry(QtCore.QRect(730, 320, 120, 40))
        self.threeScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.threeScore.setStyleSheet("font:14pt;background:white")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(855, 320, 760, 40))
        self.label_11.setStyleSheet("font:14pt")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 380, 800, 40))
        self.label_12.setStyleSheet("font:14pt")

        self.fourScore = QtWidgets.QComboBox(self.centralwidget)
        self.fourScore.setGeometry(QtCore.QRect(810, 380, 120, 40))
        self.fourScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.fourScore.setStyleSheet("font:14pt;background:white")

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(930, 380, 800, 40))
        self.label_13.setStyleSheet("font:14pt")

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 440, 870, 40))
        self.label_14.setStyleSheet("font:14pt")

        self.fiveScore = QtWidgets.QComboBox(self.centralwidget)
        self.fiveScore.setGeometry(QtCore.QRect(890, 440, 120, 40))
        self.fiveScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.fiveScore.setStyleSheet("font:14pt;background:white")

        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1018, 440, 870, 40))
        self.label_15.setStyleSheet("font:14pt")

        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(20, 500, 870, 40))
        self.label_16.setStyleSheet("font:14pt")

        self.sixScore = QtWidgets.QComboBox(self.centralwidget)
        self.sixScore.setGeometry(QtCore.QRect(670, 500, 120, 40))
        self.sixScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.sixScore.setStyleSheet("font:14pt;background:white")

        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(800, 500, 870, 40))
        self.label_17.setStyleSheet("font:14pt")

        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(20, 560, 870, 40))
        self.label_18.setStyleSheet("font:14pt")

        self.sevenScore = QtWidgets.QComboBox(self.centralwidget)
        self.sevenScore.setGeometry(QtCore.QRect(500, 560, 120, 40))
        self.sevenScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.sevenScore.setStyleSheet("font:14pt;background:white")

        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(630, 560, 870, 40))
        self.label_19.setStyleSheet("font:14pt")

        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(20, 620, 870, 40))
        self.label_20.setStyleSheet("font:14pt")

        self.eightScore = QtWidgets.QComboBox(self.centralwidget)
        self.eightScore.setGeometry(QtCore.QRect(525, 620, 120, 40))
        self.eightScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.eightScore.setStyleSheet("font:14pt;background:white")

        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(655, 620, 870, 40))
        self.label_21.setStyleSheet("font:14pt")

        self.PictureLabel = QtWidgets.QLabel(self.centralwidget)
        self.PictureLabel.setGeometry(QtCore.QRect(150, 710, 1000, 100))
        self.PictureLabel.setStyleSheet('background-image:url(./src/fig/mirrorLeft.jpg)')

        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(20, 850, 870, 40))
        self.label_22.setStyleSheet("font:16pt")

        self.totalScore = QtWidgets.QLineEdit(self.centralwidget)
        self.totalScore.setGeometry(QtCore.QRect(120, 850, 200, 40))
        self.totalScore.setStyleSheet("font:16pt;background:white")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 850, 260, 40))
        self.label_6.setStyleSheet("font:16pt")

        self.dateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(490, 850, 260, 40))
        self.dateEdit.setStyleSheet("font:16pt;background:white")
        self.dateEdit.setCalendarPopup(True)

        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(770, 850, 120, 40))
        self.saveButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.downLoadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downLoadButton.setGeometry(QtCore.QRect(910, 850, 120, 40))
        self.downLoadButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "视错觉评估"))
        self.title.setText(_translate("MainWindow", "镜像错觉体验"))
        self.label.setText(_translate("MainWindow", "姓名:"))
        self.name.setText(_translate("MainWindow", "--"))
        self.label_2.setText(_translate("MainWindow", "性别:"))
        self.gender.setText(_translate("MainWindow", "--"))
        self.label_3.setText(_translate("MainWindow", "年龄:"))
        self.age.setText(_translate("MainWindow", "--"))
        self.label_4.setText(_translate("MainWindow", "患手:"))
        self.hand.setText(_translate("MainWindow", "--"))
        self.label_23.setText(_translate("MainWindow", "注：以左侧肢体（患侧）为例，右侧为主动侧"))
        self.label_5.setText(_translate("MainWindow", "1.我觉得镜子里看到的自己左侧肢体（左手）很自然，不像是别人的(得分:"))
        self.label_6.setText(_translate("MainWindow", "评定日期:"))
        self.label_7.setText(_translate("MainWindow", ")"))
        self.label_8.setText(_translate("MainWindow", ")"))
        self.label_9.setText(_translate("MainWindow", "2.我觉得镜子里看到的左侧肢体（左手）和镜子后面的肢体是重合的(得分:"))
        self.label_10.setText(_translate("MainWindow", "3.我觉得镜子里看到的左侧肢体就是我的左侧肢体(得分:"))
        self.label_11.setText(_translate("MainWindow", ")"))
        self.label_12.setText(_translate("MainWindow", "4.我觉得镜子里的右侧肢体（左手）是自己身体的一部分(得分:"))
        self.label_13.setText(_translate("MainWindow", ")"))
        self.label_14.setText(_translate("MainWindow", "5.我觉得自己的左侧肢体（左手）也能跟着镜子里的左手动起来(得分:"))
        self.label_15.setText(_translate("MainWindow", ")"))
        self.label_16.setText(_translate("MainWindow", "6.我可以控制镜子里左侧肢体（左手）的运动(得分:"))
        self.label_17.setText(_translate("MainWindow", ")"))
        self.label_18.setText(_translate("MainWindow", "7.我无法分辨我的左手在哪里了(得分:"))
        self.label_19.setText(_translate("MainWindow", ")"))
        self.label_20.setText(_translate("MainWindow", "8.我感觉我的左侧肢体有些不寻常(得分:"))
        self.label_21.setText(_translate("MainWindow", ")"))
        self.label_22.setText(_translate("MainWindow", "总分:"))
        self.saveButton.setText(_translate("MainWindow", "保存"))
        self.downLoadButton.setText(_translate("MainWindow", "导出"))


class mirrorIllusionExperienceLeft(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,patient_id):
        super(mirrorIllusionExperienceLeft, self).__init__()
        self.setupUi(self)
        self.patient_id = patient_id

        self.patientInfo = \
            json.loads(requests.post(config.patientGetById, data={'id': self.patient_id}).content.decode('utf-8'))[
                'data']
        self.name = self.name.setText(self.patientInfo['name'])
        self.gender = self.gender.setText(self.patientInfo['gender'])
        self.age = self.age.setText(self.patientInfo['age'])
        self.hand = self.hand.setText(self.patientInfo['illness'])

        self.saveButton.clicked.connect(self.saveButtonClick)
        self.downLoadButton.clicked.connect(self.downLoadButtonClick)
    #
    def saveButtonClick(self, *args):
        code_1 = self.totalScore.text()
        code_2 = self.oneScore.currentText()
        code_3 = self.twoScore.currentText()
        code_4 = self.threeScore.currentText()
        code_5 = self.fourScore.currentText()
        code_6 = self.fiveScore.currentText()
        code_7 = self.sixScore.currentText()
        code_8 = self.sevenScore.currentText()
        code_9 = self.eightScore.currentText()
        test_date = self.dateEdit.text().replace('/', '-')
        sheet = {'id': tool.Tools.getTimeStamp(), 'patient_id': self.patient_id, 'code_1': code_1, 'code_2': code_2,
                 'code_3': code_3, 'code_4': code_4,'code_5': code_5, 'code_6': code_6,'code_7': code_7, 'code_8': code_8,
                 'code_9': code_9,'test_date': test_date}
        res = requests.post(config.ashworthInsert, data=sheet)
        QMessageBox.information(self, "保存", '保存成功', QMessageBox.Yes, QMessageBox.Yes)

        ...

    def downLoadButtonClick(self, *args):
        self.saveButton.hide()
        self.downLoadButton.hide()
        img = self.grab()
        self.saveButton.show()
        self.downLoadButton.show()
        path = QFileDialog.getExistingDirectory()
        img.save(f"{path}/{self.name.text()}_{self.dateEdit.text().replace('/', '-')}.png")
        ...


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = mirrorIllusionExperienceLeft()
    gui.show()
    sys.exit(app.exec_())