import json
import sys

import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QSlider, QMessageBox, QFileDialog

import config
import tool


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(1600, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet('background-color:rgb(242, 249, 255)')

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(500, 10, 400, 41))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet('font:16pt')

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(50, 80, 1500, 1000))
        self.totalComBox = QtWidgets.QComboBox(self.centralwidget)
        self.totalComBox.setGeometry(QtCore.QRect(800, 10, 560, 40))
        self.totalComBox.addItems(['', '镜像错觉体验(左)', '镜像错觉体验(右)'])
        self.totalComBox.setStyleSheet("font:16pt;background:white")

        self.page = QtWidgets.QWidget()
        self.mirrorIllusionExperienceLeft_title = QtWidgets.QLabel(self.page)
        self.mirrorIllusionExperienceLeft_title.setGeometry(QtCore.QRect(500, 10, 400, 41))
        self.mirrorIllusionExperienceLeft_title.setAlignment(Qt.AlignCenter)
        self.mirrorIllusionExperienceLeft_title.setStyleSheet('font:16pt')

        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(80, 60, 200, 40))
        self.label.setStyleSheet('font:14pt')

        self.mirrorIllusionExperienceLeft_name = QtWidgets.QLabel(self.page)
        self.mirrorIllusionExperienceLeft_name.setGeometry(QtCore.QRect(160, 60, 200, 40))
        self.mirrorIllusionExperienceLeft_name.setStyleSheet('font:14pt')

        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(280, 60, 200, 40))
        self.label_2.setStyleSheet('font:14pt')

        self.mirrorIllusionExperienceLeft_gender = QtWidgets.QLabel(self.page)
        self.mirrorIllusionExperienceLeft_gender.setGeometry(QtCore.QRect(360, 60, 200, 40))
        self.mirrorIllusionExperienceLeft_gender.setStyleSheet('font:14pt')

        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(480, 60, 200, 40))
        self.label_3.setStyleSheet('font:14pt')

        self.mirrorIllusionExperienceLeft_age = QtWidgets.QLabel(self.page)
        self.mirrorIllusionExperienceLeft_age.setGeometry(QtCore.QRect(560, 60, 200, 40))
        self.mirrorIllusionExperienceLeft_age.setStyleSheet('font:14pt')

        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(680, 60, 200, 40))
        self.label_4.setStyleSheet('font:14pt')

        self.mirrorIllusionExperienceLeft_hand = QtWidgets.QLabel(self.page)
        self.mirrorIllusionExperienceLeft_hand.setGeometry(QtCore.QRect(760, 60, 200, 40))
        self.mirrorIllusionExperienceLeft_hand.setStyleSheet('font:14pt')

        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 920, 40))
        self.label_5.setStyleSheet("font:14pt;font-weight:bold")

        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 920, 40))
        self.label_6.setStyleSheet("font:14pt")

        self.mirrorIllusionExperienceLeft_oneScore = QtWidgets.QComboBox(self.page)
        self.mirrorIllusionExperienceLeft_oneScore.setGeometry(QtCore.QRect(955, 200, 120, 40))
        self.mirrorIllusionExperienceLeft_oneScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.mirrorIllusionExperienceLeft_oneScore.setStyleSheet("font:14pt;background:white")

        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(1075, 200, 100, 40))
        self.label_7.setStyleSheet("font:14pt")

        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setGeometry(QtCore.QRect(20, 260, 920, 40))
        self.label_8.setStyleSheet("font:14pt")

        self.mirrorIllusionExperienceLeft_twoScore = QtWidgets.QComboBox(self.page)
        self.mirrorIllusionExperienceLeft_twoScore.setGeometry(QtCore.QRect(955, 260, 120, 40))
        self.mirrorIllusionExperienceLeft_twoScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.mirrorIllusionExperienceLeft_twoScore.setStyleSheet("font:14pt;background:white")

        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setGeometry(QtCore.QRect(1075, 260, 100, 40))
        self.label_9.setStyleSheet("font:14pt")

        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setGeometry(QtCore.QRect(20, 320, 760, 40))
        self.label_10.setStyleSheet("font:14pt")

        self.mirrorIllusionExperienceLeft_threeScore = QtWidgets.QComboBox(self.page)
        self.mirrorIllusionExperienceLeft_threeScore.setGeometry(QtCore.QRect(730, 320, 120, 40))
        self.mirrorIllusionExperienceLeft_threeScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.mirrorIllusionExperienceLeft_threeScore.setStyleSheet("font:14pt;background:white")

        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(855, 320, 760, 40))
        self.label_11.setStyleSheet("font:14pt")

        self.label_12 = QtWidgets.QLabel(self.page)
        self.label_12.setGeometry(QtCore.QRect(20, 380, 800, 40))
        self.label_12.setStyleSheet("font:14pt")

        self.mirrorIllusionExperienceLeft_fourScore = QtWidgets.QComboBox(self.page)
        self.mirrorIllusionExperienceLeft_fourScore.setGeometry(QtCore.QRect(810, 380, 120, 40))
        self.mirrorIllusionExperienceLeft_fourScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.mirrorIllusionExperienceLeft_fourScore.setStyleSheet("font:14pt;background:white")

        self.label_13 = QtWidgets.QLabel(self.page)
        self.label_13.setGeometry(QtCore.QRect(930, 380, 800, 40))
        self.label_13.setStyleSheet("font:14pt")

        self.label_14 = QtWidgets.QLabel(self.page)
        self.label_14.setGeometry(QtCore.QRect(20, 440, 870, 40))
        self.label_14.setStyleSheet("font:14pt")

        self.mirrorIllusionExperienceLeft_fiveScore = QtWidgets.QComboBox(self.page)
        self.mirrorIllusionExperienceLeft_fiveScore.setGeometry(QtCore.QRect(890, 440, 120, 40))
        self.mirrorIllusionExperienceLeft_fiveScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.mirrorIllusionExperienceLeft_fiveScore.setStyleSheet("font:14pt;background:white")

        self.label_15 = QtWidgets.QLabel(self.page)
        self.label_15.setGeometry(QtCore.QRect(1018, 440, 870, 40))
        self.label_15.setStyleSheet("font:14pt")

        self.label_16 = QtWidgets.QLabel(self.page)
        self.label_16.setGeometry(QtCore.QRect(20, 500, 870, 40))
        self.label_16.setStyleSheet("font:14pt")

        self.mirrorIllusionExperienceLeft_sixScore = QtWidgets.QComboBox(self.page)
        self.mirrorIllusionExperienceLeft_sixScore.setGeometry(QtCore.QRect(670, 500, 120, 40))
        self.mirrorIllusionExperienceLeft_sixScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.mirrorIllusionExperienceLeft_sixScore.setStyleSheet("font:14pt;background:white")

        self.label_17 = QtWidgets.QLabel(self.page)
        self.label_17.setGeometry(QtCore.QRect(800, 500, 870, 40))
        self.label_17.setStyleSheet("font:14pt")

        self.label_18 = QtWidgets.QLabel(self.page)
        self.label_18.setGeometry(QtCore.QRect(20, 560, 870, 40))
        self.label_18.setStyleSheet("font:14pt")

        self.mirrorIllusionExperienceLeft_sevenScore = QtWidgets.QComboBox(self.page)
        self.mirrorIllusionExperienceLeft_sevenScore.setGeometry(QtCore.QRect(500, 560, 120, 40))
        self.mirrorIllusionExperienceLeft_sevenScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.mirrorIllusionExperienceLeft_sevenScore.setStyleSheet("font:14pt;background:white")

        self.label_19 = QtWidgets.QLabel(self.page)
        self.label_19.setGeometry(QtCore.QRect(630, 560, 870, 40))
        self.label_19.setStyleSheet("font:14pt")

        self.label_20 = QtWidgets.QLabel(self.page)
        self.label_20.setGeometry(QtCore.QRect(20, 620, 870, 40))
        self.label_20.setStyleSheet("font:14pt")

        self.mirrorIllusionExperienceLeft_eightScore = QtWidgets.QComboBox(self.page)
        self.mirrorIllusionExperienceLeft_eightScore.setGeometry(QtCore.QRect(525, 620, 120, 40))
        self.mirrorIllusionExperienceLeft_eightScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.mirrorIllusionExperienceLeft_eightScore.setStyleSheet("font:14pt;background:white")

        self.label_21 = QtWidgets.QLabel(self.page)
        self.label_21.setGeometry(QtCore.QRect(655, 620, 870, 40))
        self.label_21.setStyleSheet("font:14pt")

        self.mirrorIllusionExperienceLeft_PictureLabel = QtWidgets.QLabel(self.page)
        self.mirrorIllusionExperienceLeft_PictureLabel.setGeometry(QtCore.QRect(150, 710, 1000, 100))
        self.mirrorIllusionExperienceLeft_PictureLabel.setStyleSheet('background-image:url(./src/fig/mirrorLeft.jpg)')

        self.label_22 = QtWidgets.QLabel(self.page)
        self.label_22.setGeometry(QtCore.QRect(20, 850, 870, 40))
        self.label_22.setStyleSheet("font:16pt")

        self.mirrorIllusionExperienceLeft_totalScore = QtWidgets.QLineEdit(self.page)
        self.mirrorIllusionExperienceLeft_totalScore.setGeometry(QtCore.QRect(120, 850, 200, 40))
        self.mirrorIllusionExperienceLeft_totalScore.setStyleSheet("font:16pt;background:white")

        self.label_23 = QtWidgets.QLabel(self.page)
        self.label_23.setGeometry(QtCore.QRect(340, 850, 260, 40))
        self.label_23.setStyleSheet("font:16pt")

        self.mirrorIllusionExperienceLeft_dateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.page)
        self.mirrorIllusionExperienceLeft_dateEdit.setGeometry(QtCore.QRect(490, 850, 260, 40))
        self.mirrorIllusionExperienceLeft_dateEdit.setStyleSheet("font:16pt;background:white")
        self.mirrorIllusionExperienceLeft_dateEdit.setCalendarPopup(True)

        self.mirrorIllusionExperienceLeft_saveButton = QtWidgets.QPushButton(self.page)
        self.mirrorIllusionExperienceLeft_saveButton.setGeometry(QtCore.QRect(770, 850, 120, 40))
        self.mirrorIllusionExperienceLeft_saveButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.mirrorIllusionExperienceLeft_downLoadButton = QtWidgets.QPushButton(self.page)
        self.mirrorIllusionExperienceLeft_downLoadButton.setGeometry(QtCore.QRect(910, 850, 120, 40))
        self.mirrorIllusionExperienceLeft_downLoadButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.stackedWidget.addWidget(self.page)

        self.page_2 = QtWidgets.QWidget()
        self.mirrorIllusionExperienceRight_title = QtWidgets.QLabel(self.page_2)
        self.mirrorIllusionExperienceRight_title.setGeometry(QtCore.QRect(500, 10, 400, 41))
        self.mirrorIllusionExperienceRight_title.setAlignment(Qt.AlignCenter)
        self.mirrorIllusionExperienceRight_title.setStyleSheet('font:16pt')

        self.label_24 = QtWidgets.QLabel(self.page_2)
        self.label_24.setGeometry(QtCore.QRect(80, 60, 200, 40))
        self.label_24.setStyleSheet('font:14pt')

        self.mirrorIllusionExperienceRight_name = QtWidgets.QLabel(self.page_2)
        self.mirrorIllusionExperienceRight_name.setGeometry(QtCore.QRect(160, 60, 200, 40))
        self.mirrorIllusionExperienceRight_name.setStyleSheet('font:14pt')

        self.label_25= QtWidgets.QLabel(self.page_2)
        self.label_25.setGeometry(QtCore.QRect(280, 60, 200, 40))
        self.label_25.setStyleSheet('font:14pt')

        self.mirrorIllusionExperienceRight_gender = QtWidgets.QLabel(self.page_2)
        self.mirrorIllusionExperienceRight_gender.setGeometry(QtCore.QRect(360, 60, 200, 40))
        self.mirrorIllusionExperienceRight_gender.setStyleSheet('font:14pt')

        self.label_26 = QtWidgets.QLabel(self.page_2)
        self.label_26.setGeometry(QtCore.QRect(480, 60, 200, 40))
        self.label_26.setStyleSheet('font:14pt')

        self.mirrorIllusionExperienceRight_age = QtWidgets.QLabel(self.page_2)
        self.mirrorIllusionExperienceRight_age.setGeometry(QtCore.QRect(560, 60, 200, 40))
        self.mirrorIllusionExperienceRight_age.setStyleSheet('font:14pt')

        self.label_27 = QtWidgets.QLabel(self.page_2)
        self.label_27.setGeometry(QtCore.QRect(680, 60, 200, 40))
        self.label_27.setStyleSheet('font:14pt')

        self.mirrorIllusionExperienceRight_hand = QtWidgets.QLabel(self.page_2)
        self.mirrorIllusionExperienceRight_hand.setGeometry(QtCore.QRect(760, 60, 200, 40))
        self.mirrorIllusionExperienceRight_hand.setStyleSheet('font:14pt')

        self.label_28 = QtWidgets.QLabel(self.page_2)
        self.label_28.setGeometry(QtCore.QRect(20, 140, 920, 40))
        self.label_28.setStyleSheet("font:14pt;font-weight:bold")

        self.label_29 = QtWidgets.QLabel(self.page_2)
        self.label_29.setGeometry(QtCore.QRect(20, 200, 920, 40))
        self.label_29.setStyleSheet("font:14pt")

        self.mirrorIllusionExperienceRight_oneScore = QtWidgets.QComboBox(self.page_2)
        self.mirrorIllusionExperienceRight_oneScore.setGeometry(QtCore.QRect(955, 200, 120, 40))
        self.mirrorIllusionExperienceRight_oneScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.mirrorIllusionExperienceRight_oneScore.setStyleSheet("font:14pt;background:white")

        self.label_30 = QtWidgets.QLabel(self.page_2)
        self.label_30.setGeometry(QtCore.QRect(1075, 200, 100, 40))
        self.label_30.setStyleSheet("font:14pt")

        self.label_31= QtWidgets.QLabel(self.page_2)
        self.label_31.setGeometry(QtCore.QRect(20, 260, 920, 40))
        self.label_31.setStyleSheet("font:14pt")

        self.mirrorIllusionExperienceRight_twoScore = QtWidgets.QComboBox(self.page_2)
        self.mirrorIllusionExperienceRight_twoScore.setGeometry(QtCore.QRect(955, 260, 120, 40))
        self.mirrorIllusionExperienceRight_twoScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.mirrorIllusionExperienceRight_twoScore.setStyleSheet("font:14pt;background:white")

        self.label_32 = QtWidgets.QLabel(self.page_2)
        self.label_32.setGeometry(QtCore.QRect(1075, 260, 100, 40))
        self.label_32.setStyleSheet("font:14pt")

        self.label_33 = QtWidgets.QLabel(self.page_2)
        self.label_33.setGeometry(QtCore.QRect(20, 320, 760, 40))
        self.label_33.setStyleSheet("font:14pt")

        self.mirrorIllusionExperienceRight_threeScore = QtWidgets.QComboBox(self.page_2)
        self.mirrorIllusionExperienceRight_threeScore.setGeometry(QtCore.QRect(730, 320, 120, 40))
        self.mirrorIllusionExperienceRight_threeScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.mirrorIllusionExperienceRight_threeScore.setStyleSheet("font:14pt;background:white")

        self.label_34 = QtWidgets.QLabel(self.page_2)
        self.label_34.setGeometry(QtCore.QRect(855, 320, 760, 40))
        self.label_34.setStyleSheet("font:14pt")

        self.label_35 = QtWidgets.QLabel(self.page_2)
        self.label_35.setGeometry(QtCore.QRect(20, 380, 800, 40))
        self.label_35.setStyleSheet("font:14pt")

        self.mirrorIllusionExperienceRight_fourScore = QtWidgets.QComboBox(self.page_2)
        self.mirrorIllusionExperienceRight_fourScore.setGeometry(QtCore.QRect(810, 380, 120, 40))
        self.mirrorIllusionExperienceRight_fourScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.mirrorIllusionExperienceRight_fourScore.setStyleSheet("font:14pt;background:white")

        self.label_36 = QtWidgets.QLabel(self.page_2)
        self.label_36.setGeometry(QtCore.QRect(930, 380, 800, 40))
        self.label_36.setStyleSheet("font:14pt")

        self.label_37 = QtWidgets.QLabel(self.page_2)
        self.label_37.setGeometry(QtCore.QRect(20, 440, 870, 40))
        self.label_37.setStyleSheet("font:14pt")

        self.mirrorIllusionExperienceRight_fiveScore = QtWidgets.QComboBox(self.page_2)
        self.mirrorIllusionExperienceRight_fiveScore.setGeometry(QtCore.QRect(890, 440, 120, 40))
        self.mirrorIllusionExperienceRight_fiveScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.mirrorIllusionExperienceRight_fiveScore.setStyleSheet("font:14pt;background:white")

        self.label_38 = QtWidgets.QLabel(self.page_2)
        self.label_38.setGeometry(QtCore.QRect(1018, 440, 870, 40))
        self.label_38.setStyleSheet("font:14pt")

        self.label_39 = QtWidgets.QLabel(self.page_2)
        self.label_39.setGeometry(QtCore.QRect(20, 500, 870, 40))
        self.label_39.setStyleSheet("font:14pt")

        self.mirrorIllusionExperienceRight_sixScore = QtWidgets.QComboBox(self.page_2)
        self.mirrorIllusionExperienceRight_sixScore.setGeometry(QtCore.QRect(670, 500, 120, 40))
        self.mirrorIllusionExperienceRight_sixScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.mirrorIllusionExperienceRight_sixScore.setStyleSheet("font:14pt;background:white")

        self.label_40 = QtWidgets.QLabel(self.page_2)
        self.label_40.setGeometry(QtCore.QRect(800, 500, 870, 40))
        self.label_40.setStyleSheet("font:14pt")

        self.label_41 = QtWidgets.QLabel(self.page_2)
        self.label_41.setGeometry(QtCore.QRect(20, 560, 870, 40))
        self.label_41.setStyleSheet("font:14pt")

        self.mirrorIllusionExperienceRight_sevenScore = QtWidgets.QComboBox(self.page_2)
        self.mirrorIllusionExperienceRight_sevenScore.setGeometry(QtCore.QRect(500, 560, 120, 40))
        self.mirrorIllusionExperienceRight_sevenScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.mirrorIllusionExperienceRight_sevenScore.setStyleSheet("font:14pt;background:white")

        self.label_42 = QtWidgets.QLabel(self.page_2)
        self.label_42.setGeometry(QtCore.QRect(630, 560, 870, 40))
        self.label_42.setStyleSheet("font:14pt")

        self.label_43 = QtWidgets.QLabel(self.page_2)
        self.label_43.setGeometry(QtCore.QRect(20, 620, 870, 40))
        self.label_43.setStyleSheet("font:14pt")

        self.mirrorIllusionExperienceRight_eightScore = QtWidgets.QComboBox(self.page_2)
        self.mirrorIllusionExperienceRight_eightScore.setGeometry(QtCore.QRect(525, 620, 120, 40))
        self.mirrorIllusionExperienceRight_eightScore.addItems(['', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
        self.mirrorIllusionExperienceRight_eightScore.setStyleSheet("font:14pt;background:white")

        self.label_44 = QtWidgets.QLabel(self.page_2)
        self.label_44.setGeometry(QtCore.QRect(655, 620, 870, 40))
        self.label_44.setStyleSheet("font:14pt")

        self.mirrorIllusionExperienceRight_PictureLabel = QtWidgets.QLabel(self.page_2)
        self.mirrorIllusionExperienceRight_PictureLabel.setGeometry(QtCore.QRect(150, 710, 1000, 100))
        self.mirrorIllusionExperienceRight_PictureLabel.setPixmap(QPixmap('D:\Pycharm\留存\mirrorLeft.jpg'))

        self.label_45 = QtWidgets.QLabel(self.page_2)
        self.label_45.setGeometry(QtCore.QRect(20, 850, 870, 40))
        self.label_45.setStyleSheet("font:16pt")

        self.mirrorIllusionExperienceRight_totalScore = QtWidgets.QLineEdit(self.page_2)
        self.mirrorIllusionExperienceRight_totalScore.setGeometry(QtCore.QRect(120, 850, 200, 40))
        self.mirrorIllusionExperienceRight_totalScore.setStyleSheet("font:16pt;background:white")

        self.label_46 = QtWidgets.QLabel(self.page_2)
        self.label_46.setGeometry(QtCore.QRect(340, 850, 260, 40))
        self.label_46.setStyleSheet("font:16pt")

        self.mirrorIllusionExperienceRight_dateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.page_2)
        self.mirrorIllusionExperienceRight_dateEdit.setGeometry(QtCore.QRect(490, 850, 260, 40))
        self.mirrorIllusionExperienceRight_dateEdit.setStyleSheet("font:16pt;background:white")
        self.mirrorIllusionExperienceRight_dateEdit.setCalendarPopup(True)

        self.mirrorIllusionExperienceRight_saveButton = QtWidgets.QPushButton(self.page_2)
        self.mirrorIllusionExperienceRight_saveButton.setGeometry(QtCore.QRect(770, 850, 120, 40))
        self.mirrorIllusionExperienceRight_saveButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.mirrorIllusionExperienceRight_downLoadButton = QtWidgets.QPushButton(self.page_2)
        self.mirrorIllusionExperienceRight_downLoadButton.setGeometry(QtCore.QRect(910, 850, 120, 40))
        self.mirrorIllusionExperienceRight_downLoadButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.stackedWidget.addWidget(self.page_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.stackedWidget.setCurrentIndex(0)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "视错觉评估"))
        self.title.setText(_translate("MainWindow", "镜像错觉体验"))
        self.mirrorIllusionExperienceLeft_title.setText(_translate("MainWindow", "镜像错觉体验(左)"))
        self.label.setText(_translate("MainWindow", "姓名:"))
        self.mirrorIllusionExperienceLeft_name.setText(_translate("MainWindow", "--"))
        self.label_2.setText(_translate("MainWindow", "性别:"))
        self.mirrorIllusionExperienceLeft_gender.setText(_translate("MainWindow", "--"))
        self.label_3.setText(_translate("MainWindow", "年龄:"))
        self.mirrorIllusionExperienceLeft_age.setText(_translate("MainWindow", "--"))
        self.label_4.setText(_translate("MainWindow", "患手:"))
        self.mirrorIllusionExperienceLeft_hand.setText(_translate("MainWindow", "--"))
        self.label_5.setText(_translate("MainWindow", "注：以左侧肢体（患侧）为例，右侧为主动侧"))
        self.label_6.setText(_translate("MainWindow", "1.我觉得镜子里看到的自己左侧肢体（左手）很自然，不像是别人的(得分:"))
        self.label_7.setText(_translate("MainWindow", ")"))
        self.label_9.setText(_translate("MainWindow", ")"))
        self.label_8.setText(_translate("MainWindow", "2.我觉得镜子里看到的左侧肢体（左手）和镜子后面的肢体是重合的(得分:"))
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
        self.label_23.setText(_translate("MainWindow", "评定日期:"))
        self.mirrorIllusionExperienceLeft_saveButton.setText(_translate("MainWindow", "保存"))
        self.mirrorIllusionExperienceLeft_downLoadButton.setText(_translate("MainWindow", "导出"))
        self.mirrorIllusionExperienceRight_title.setText(_translate("MainWindow", "镜像错觉体验(右)"))
        self.label_24.setText(_translate("MainWindow", "姓名:"))
        self.mirrorIllusionExperienceRight_name.setText(_translate("MainWindow", "--"))
        self.label_25.setText(_translate("MainWindow", "性别:"))
        self.mirrorIllusionExperienceRight_gender.setText(_translate("MainWindow", "--"))
        self.label_26.setText(_translate("MainWindow", "年龄:"))
        self.mirrorIllusionExperienceRight_age.setText(_translate("MainWindow", "--"))
        self.label_27.setText(_translate("MainWindow", "患手:"))
        self.mirrorIllusionExperienceRight_hand.setText(_translate("MainWindow", "--"))
        self.label_28.setText(_translate("MainWindow", "注：以右侧肢体（患侧）为例，左侧为主动侧"))
        self.label_29.setText(_translate("MainWindow", "1.我觉得镜子里看到的自己右侧肢体（右手）很自然，不像是别人的(得分:"))
        self.label_46.setText(_translate("MainWindow", "评定日期:"))
        self.label_30.setText(_translate("MainWindow", ")"))
        self.label_31.setText(_translate("MainWindow", ")"))
        self.label_32.setText(_translate("MainWindow", "2.我觉得镜子里看到的右侧肢体（右手）和镜子后面的肢体是重合的(得分:"))
        self.label_33.setText(_translate("MainWindow", "3.我觉得镜子里看到的右侧肢体就是我的右侧肢体(得分:"))
        self.label_34.setText(_translate("MainWindow", ")"))
        self.label_35.setText(_translate("MainWindow", "4.我觉得镜子里的右侧肢体（右手）是自己身体的一部分(得分:"))
        self.label_36.setText(_translate("MainWindow", ")"))
        self.label_37.setText(_translate("MainWindow", "5.我觉得自己的右侧肢体（右手）也能跟着镜子里的右手动起来(得分:"))
        self.label_38.setText(_translate("MainWindow", ")"))
        self.label_39.setText(_translate("MainWindow", "6.我可以控制镜子里左侧肢体（右手）的运动(得分:"))
        self.label_40.setText(_translate("MainWindow", ")"))
        self.label_41.setText(_translate("MainWindow", "7.我无法分辨我的右手在哪里了(得分:"))
        self.label_42.setText(_translate("MainWindow", ")"))
        self.label_43.setText(_translate("MainWindow", "8.我感觉我的右侧肢体有些不寻常(得分:"))
        self.label_44.setText(_translate("MainWindow", ")"))
        self.label_45.setText(_translate("MainWindow", "总分:"))
        self.mirrorIllusionExperienceRight_saveButton.setText(_translate("MainWindow", "保存"))
        self.mirrorIllusionExperienceRight_downLoadButton.setText(_translate("MainWindow", "导出"))


class mirrorIllusionExperience(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,patient_id):
        super(mirrorIllusionExperience, self).__init__()
        self.setupUi(self)
        self.patient_id = patient_id

        self.patientInfo = \
            json.loads(requests.post(config.patientGetById, data={'id': self.patient_id}).content.decode('utf-8'))[
                'data']
        self.mirrorIllusionExperienceLeft_name = self.mirrorIllusionExperienceLeft_name.setText(self.patientInfo['name'])
        self.mirrorIllusionExperienceLeft_gender = self.mirrorIllusionExperienceLeft_gender.setText(self.patientInfo['gender'])
        self.mirrorIllusionExperienceLeft_age = self.mirrorIllusionExperienceLeft_age.setText(self.patientInfo['age'])
        self.mirrorIllusionExperienceLeft_hand = self.mirrorIllusionExperienceLeft_hand.setText(self.patientInfo['illness'])
        self.mirrorIllusionExperienceRight_name = self.mirrorIllusionExperienceRight_name.setText(self.patientInfo['name'])
        self.mirrorIllusionExperienceRight_gender = self.mirrorIllusionExperienceRight_gender.setText(self.patientInfo['gender'])
        self.mirrorIllusionExperienceRight_age = self.mirrorIllusionExperienceRight_age.setText(self.patientInfo['age'])
        self.mirrorIllusionExperienceRight_hand = self.mirrorIllusionExperienceRight_hand.setText(self.patientInfo['illness'])
        self.totalComBox.currentIndexChanged.connect(self.totalComBoxClick)
        self.mirrorIllusionExperienceLeft_saveButton.clicked.connect(self.mirrorIllusionExperienceLeft_saveButtonClick)
        self.mirrorIllusionExperienceLeft_downLoadButton.clicked.connect(self.mirrorIllusionExperienceLeft_downLoadButtonClick)
        self.mirrorIllusionExperienceRight_saveButton.clicked.connect(self.mirrorIllusionExperienceRight_saveButtonClick)
        self.mirrorIllusionExperienceRight_downLoadButton.clicked.connect(self.mirrorIllusionExperienceRight_downLoadButtonClick)
    def totalComBoxClick(self, *args):
        if(self.totalComBox.currentIndex()==1):
            self.stackedWidget.setCurrentIndex(0)
        else:
            self.stackedWidget.setCurrentIndex(1)

    def mirrorIllusionExperienceLeft_saveButtonClick(self, *args):
        code_1 = self.mirrorIllusionExperienceLeft_totalScore.text()
        code_2 = self.mirrorIllusionExperienceLeft_oneScore.currentText()
        code_3 = self.mirrorIllusionExperienceLeft_twoScore.currentText()
        code_4 = self.mirrorIllusionExperienceLeft_threeScore.currentText()
        code_5 = self.mirrorIllusionExperienceLeft_fourScore.currentText()
        code_6 = self.mirrorIllusionExperienceLeft_fiveScore.currentText()
        code_7 = self.mirrorIllusionExperienceLeft_sixScore.currentText()
        code_8 = self.mirrorIllusionExperienceLeft_sevenScore.currentText()
        code_9 = self.mirrorIllusionExperienceLeft_eightScore.currentText()
        test_date = self.mirrorIllusionExperienceLeft_dateEdit.text().replace('/', '-')
        sheet = {'id': tool.Tools.getTimeStamp(), 'patient_id': self.patient_id, 'code_1': code_1, 'code_2': code_2,
                 'code_3': code_3, 'code_4': code_4, 'code_5': code_5, 'code_6': code_6, 'code_7': code_7,
                 'code_8': code_8,
                 'code_9': code_9, 'test_date': test_date}
        res = requests.post(config.ashworthInsert, data=sheet)
        QMessageBox.information(self, "保存", '保存成功', QMessageBox.Yes, QMessageBox.Yes)
        ...

    def mirrorIllusionExperienceLeft_downLoadButtonClick(self, *args):
        self.mirrorIllusionExperienceLeft_saveButton.hide()
        self.mirrorIllusionExperienceLeft_downLoadButton.hide()
        img = self.grab()
        self.mirrorIllusionExperienceLeft_saveButton.show()
        self.mirrorIllusionExperienceLeft_downLoadButton.show()
        path = QFileDialog.getExistingDirectory()
        img.save(f"{path}/{self.mirrorIllusionExperienceLeft_name.text()}_{self.mirrorIllusionExperienceLeft_dateEdit.text().replace('/', '-')}_{self.totalComBox.currentText()}.png")
        ...

    def mirrorIllusionExperienceRight_saveButtonClick(self, *args):
        code_1 = self.mirrorIllusionExperienceRight_totalScore.text()
        code_2 = self.mirrorIllusionExperienceRight_oneScore.currentText()
        code_3 = self.mirrorIllusionExperienceRight_twoScore.currentText()
        code_4 = self.mirrorIllusionExperienceRight_threeScore.currentText()
        code_5 = self.mirrorIllusionExperienceRight_fourScore.currentText()
        code_6 = self.mirrorIllusionExperienceRight_fiveScore.currentText()
        code_7 = self.mirrorIllusionExperienceRight_sixScore.currentText()
        code_8 = self.mirrorIllusionExperienceRight_sevenScore.currentText()
        code_9 = self.mirrorIllusionExperienceRight_eightScore.currentText()
        test_date = self.mirrorIllusionExperienceRight_dateEdit.text().replace('/', '-')
        sheet = {'id': tool.Tools.getTimeStamp(), 'patient_id': self.patient_id, 'code_1': code_1, 'code_2': code_2,
                 'code_3': code_3, 'code_4': code_4, 'code_5': code_5, 'code_6': code_6, 'code_7': code_7,
                 'code_8': code_8,
                 'code_9': code_9, 'test_date': test_date}
        res = requests.post(config.ashworthInsert, data=sheet)
        QMessageBox.information(self, "保存", '保存成功', QMessageBox.Yes, QMessageBox.Yes)
        ...

    def mirrorIllusionExperienceRight_downLoadButtonClick(self, *args):
        self.mirrorIllusionExperienceRight_saveButton.hide()
        self.mirrorIllusionExperienceRight_downLoadButton.hide()
        img = self.grab()
        self.mirrorIllusionExperienceRight_saveButton.show()
        self.mirrorIllusionExperienceRight_downLoadButton.show()
        path = QFileDialog.getExistingDirectory()
        img.save(f"{path}/{self.mirrorIllusionExperienceRight_name.text()}_{self.mirrorIllusionExperienceRight_dateEdit.text().replace('/', '-')}_{self.totalComBox.currentText()}.png")
        ...


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = mirrorIllusionExperience()
    gui.show()
    sys.exit(app.exec_())
