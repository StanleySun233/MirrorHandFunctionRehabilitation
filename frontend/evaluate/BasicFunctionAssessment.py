import json
import sys

import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QSlider, QMessageBox, QFileDialog

import config
import tool


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(1600, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet('background-color:rgb(242, 249, 255)')

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(50, 80, 1500, 1000))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(600, 10, 260, 40))
        self.label.setStyleSheet("font:16pt")

        self.totalComBox = QtWidgets.QComboBox(self.centralwidget)
        self.totalComBox.setGeometry(QtCore.QRect(800, 10, 560, 40))
        self.totalComBox.addItems(['', '改良Ashworth分级', '肌力（握力、捏力）', '运动功能状态量表（MSS）', 'Brunnstrom脑卒中运动功能分级', \
                                   '利手调查量表', 'VAS疼痛视觉模拟'])
        self.totalComBox.setStyleSheet("font:16pt;background:white")

        self.page = QtWidgets.QWidget()

        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(600, 10, 300, 40))
        self.label_2.setStyleSheet("font:16pt")

        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(80, 80, 300, 40))
        self.label_3.setStyleSheet("font:12pt")

        self.Ashworth_nameLabel = QtWidgets.QLabel(self.page)
        self.Ashworth_nameLabel.setGeometry(QtCore.QRect(180, 80, 300, 40))
        self.Ashworth_nameLabel.setText('--')
        self.Ashworth_nameLabel.setStyleSheet("font:16pt")

        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(380, 80, 300, 40))
        self.label_4.setStyleSheet("font:12pt")

        self.Ashworth_sexLabel = QtWidgets.QLabel(self.page)
        self.Ashworth_sexLabel.setGeometry(QtCore.QRect(480, 80, 300, 40))
        self.Ashworth_sexLabel.setText('--')
        self.Ashworth_sexLabel.setStyleSheet("font:16pt")

        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(680, 80, 300, 40))
        self.label_5.setStyleSheet("font:12pt")

        self.Ashworth_ageLabel = QtWidgets.QLabel(self.page)
        self.Ashworth_ageLabel.setGeometry(QtCore.QRect(780, 80, 300, 40))
        self.Ashworth_ageLabel.setText('--')
        self.Ashworth_ageLabel.setStyleSheet("font:16pt")

        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(980, 80, 300, 40))
        self.label_6.setStyleSheet("font:12pt")

        self.Ashworth_unhealthyHandLabel = QtWidgets.QLabel(self.page)
        self.Ashworth_unhealthyHandLabel.setGeometry(QtCore.QRect(1080, 80, 300, 40))
        self.Ashworth_unhealthyHandLabel.setText('--')
        self.Ashworth_unhealthyHandLabel.setStyleSheet("font:16pt")

        self.Ashworth_tableWidget = QtWidgets.QTableWidget(self.page)
        self.Ashworth_tableWidget.setGeometry(QtCore.QRect(80, 140, 1350, 650))
        self.Ashworth_tableWidget.setStyleSheet("background:white;font:14pt")
        self.Ashworth_tableWidget.setColumnCount(2)
        self.Ashworth_tableWidget.setRowCount(6)
        self.Ashworth_tableWidget.verticalHeader().setVisible(False)
        self.Ashworth_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.Ashworth_tableWidget.verticalHeader().setStretchLastSection(True)
        self.Ashworth_tableWidget.setShowGrid(True)

        item = QtWidgets.QTableWidgetItem('0级')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.Ashworth_tableWidget.setRowHeight(0, 99)
        self.Ashworth_tableWidget.setItem(0, 0, item)

        item = QtWidgets.QTableWidgetItem('无肌张力的增加')
        self.Ashworth_tableWidget.setItem(0, 1, item)

        item = QtWidgets.QTableWidgetItem('1级')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.Ashworth_tableWidget.setRowHeight(1, 99)
        self.Ashworth_tableWidget.setItem(1, 0, item)

        item = QtWidgets.QTableWidgetItem('肌张力略微增加：受累部分被动屈伸时，在关节活动范围之末时呈现最小的阻力或出现突然卡住和释放')
        self.Ashworth_tableWidget.setItem(1, 1, item)

        item = QtWidgets.QTableWidgetItem('1+级')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.Ashworth_tableWidget.setRowHeight(2, 99)
        self.Ashworth_tableWidget.setItem(2, 0, item)

        item = QtWidgets.QTableWidgetItem('肌张力轻度增加：在关节活动范围后50%范围内出现突然卡住，然后再关节活动范围的后50%均呈现最小的阻力')
        self.Ashworth_tableWidget.setItem(2, 1, item)

        item = QtWidgets.QTableWidgetItem('2级')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.Ashworth_tableWidget.setRowHeight(3, 99)
        self.Ashworth_tableWidget.setItem(3, 0, item)

        item = QtWidgets.QTableWidgetItem('肌张力较明显地增加：通过关节活动范围的大部分时，肌张力均较明显地增加，但受累部分仍能较容易地被移动')
        self.Ashworth_tableWidget.setItem(3, 1, item)

        item = QtWidgets.QTableWidgetItem('3级')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.Ashworth_tableWidget.setRowHeight(4, 99)
        self.Ashworth_tableWidget.setItem(4, 0, item)

        item = QtWidgets.QTableWidgetItem('肌张力严重增高：被动运动困难')
        self.Ashworth_tableWidget.setItem(4, 1, item)

        item = QtWidgets.QTableWidgetItem('4级')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.Ashworth_tableWidget.setRowHeight(5, 99)
        self.Ashworth_tableWidget.setItem(5, 0, item)

        item = QtWidgets.QTableWidgetItem('僵直：受累部分被动屈伸时呈现僵直状态，不能活动')
        self.Ashworth_tableWidget.setItem(5, 1, item)

        item = QtWidgets.QTableWidgetItem()
        self.Ashworth_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Ashworth_tableWidget.setHorizontalHeaderItem(1, item)
        self.Ashworth_tableWidget.setColumnWidth(1, 1195)

        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(80, 800, 400, 40))
        self.label_7.setStyleSheet("font:16pt")

        self.Ashworth_elbowShenJicomboBox = QtWidgets.QComboBox(self.page)  # 伸肌评定结果
        self.Ashworth_elbowShenJicomboBox.setGeometry(QtCore.QRect(420, 800, 160, 35))
        self.Ashworth_elbowShenJicomboBox.addItems(['', '0级', '1级', '1级+', '2级', '3级', '4级'])
        self.Ashworth_elbowShenJicomboBox.setStyleSheet("font:12pt")

        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setGeometry(QtCore.QRect(680, 800, 400, 40))
        self.label_8.setStyleSheet("font:16pt")

        self.Ashworth_elbowQuJicomboBox = QtWidgets.QComboBox(self.page)
        self.Ashworth_elbowQuJicomboBox.setGeometry(QtCore.QRect(1020, 800, 160, 35))
        self.Ashworth_elbowQuJicomboBox.addItems(['', '0级', '1级', '1级+', '2级', '3级', '4级'])
        self.Ashworth_elbowQuJicomboBox.setStyleSheet("font:12pt")

        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setGeometry(QtCore.QRect(60, 870, 400, 40))
        self.label_9.setStyleSheet("font:16pt")

        self.Ashworth_wristShenJicomboBox = QtWidgets.QComboBox(self.page)  # 伸肌评定结果
        self.Ashworth_wristShenJicomboBox.setGeometry(QtCore.QRect(420, 870, 160, 35))
        self.Ashworth_wristShenJicomboBox.addItems(['', '0级', '1级', '1级+', '2级', '3级', '4级'])
        self.Ashworth_wristShenJicomboBox.setStyleSheet("font:12pt")

        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setGeometry(QtCore.QRect(680, 870, 400, 40))
        self.label_10.setStyleSheet("font:16pt")

        self.Ashworth_wristQuJicomboBox = QtWidgets.QComboBox(self.page)
        self.Ashworth_wristQuJicomboBox.setGeometry(QtCore.QRect(1020, 870, 160, 35))
        self.Ashworth_wristQuJicomboBox.addItems(['', '0级', '1级', '1级+', '2级', '3级', '4级'])
        self.Ashworth_wristQuJicomboBox.setStyleSheet("font:12pt")

        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(80, 940, 260, 40))
        self.label_11.setStyleSheet("font:16pt")

        self.Ashworth_dateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.page)
        self.Ashworth_dateEdit.setGeometry(QtCore.QRect(270, 940, 260, 40))
        self.Ashworth_dateEdit.setStyleSheet("font:16pt")
        self.Ashworth_dateEdit.setCalendarPopup(True)

        self.Ashworth_saveButton = QtWidgets.QPushButton(self.page)
        self.Ashworth_saveButton.setGeometry(QtCore.QRect(580, 940, 120, 40))
        self.Ashworth_saveButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.Ashworth_downLoadButton = QtWidgets.QPushButton(self.page)
        self.Ashworth_downLoadButton.setGeometry(QtCore.QRect(720, 940, 120, 40))
        self.Ashworth_downLoadButton.setText('导出')
        self.Ashworth_downLoadButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.stackedWidget.addWidget(self.page)

        self.page_2 = QtWidgets.QWidget()
        self.label_12 = QtWidgets.QLabel(self.page_2)
        self.label_12.setGeometry(QtCore.QRect(600, 10, 300, 40))
        self.label_12.setStyleSheet("font:16pt")

        self.label_13 = QtWidgets.QLabel(self.page_2)
        self.label_13.setGeometry(QtCore.QRect(80, 80, 300, 40))
        self.label_13.setStyleSheet("font:12pt")

        self.muscleStrength_nameLabel = QtWidgets.QLabel(self.page_2)
        self.muscleStrength_nameLabel.setGeometry(QtCore.QRect(180, 80, 300, 40))
        self.muscleStrength_nameLabel.setText('--')
        self.muscleStrength_nameLabel.setStyleSheet("font:16pt")

        self.label_14 = QtWidgets.QLabel(self.page_2)
        self.label_14.setGeometry(QtCore.QRect(380, 80, 300, 40))
        self.label_14.setStyleSheet("font:12pt")

        self.muscleStrength_sexLabel = QtWidgets.QLabel(self.page_2)
        self.muscleStrength_sexLabel.setGeometry(QtCore.QRect(480, 80, 300, 40))
        self.muscleStrength_sexLabel.setText('--')
        self.muscleStrength_sexLabel.setStyleSheet("font:16pt")

        self.label_15 = QtWidgets.QLabel(self.page_2)
        self.label_15.setGeometry(QtCore.QRect(680, 80, 300, 40))
        self.label_15.setStyleSheet("font:12pt")

        self.muscleStrength_ageLabel = QtWidgets.QLabel(self.page_2)
        self.muscleStrength_ageLabel.setGeometry(QtCore.QRect(780, 80, 300, 40))
        self.muscleStrength_ageLabel.setText('--')
        self.muscleStrength_ageLabel.setStyleSheet("font:16pt")

        self.label_16 = QtWidgets.QLabel(self.page_2)
        self.label_16.setGeometry(QtCore.QRect(980, 80, 300, 40))
        self.label_16.setStyleSheet("font:12pt")

        self.muscleStrength_unhealthyHandLabel = QtWidgets.QLabel(self.page_2)
        self.muscleStrength_unhealthyHandLabel.setGeometry(QtCore.QRect(1080, 80, 300, 40))
        self.muscleStrength_unhealthyHandLabel.setText('--')
        self.muscleStrength_unhealthyHandLabel.setStyleSheet("font:16pt")

        self.muscleStrength_tableWidget = QtWidgets.QTableWidget(self.page_2)
        self.muscleStrength_tableWidget.setGeometry(QtCore.QRect(80, 140, 1350, 450))
        self.muscleStrength_tableWidget.setStyleSheet("background:white;font:14pt")
        self.muscleStrength_tableWidget.setColumnCount(3)
        self.muscleStrength_tableWidget.setRowCount(6)
        self.muscleStrength_tableWidget.verticalHeader().setVisible(False)

        item = QtWidgets.QTableWidgetItem()
        self.muscleStrength_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.muscleStrength_tableWidget.setHorizontalHeaderItem(1, item)
        self.muscleStrength_tableWidget.setColumnWidth(1, 794)
        item = QtWidgets.QTableWidgetItem()
        self.muscleStrength_tableWidget.setHorizontalHeaderItem(2, item)
        self.muscleStrength_tableWidget.setColumnWidth(2, 400)

        item = QtWidgets.QTableWidgetItem('0')
        self.muscleStrength_tableWidget.setRowHeight(0, 65)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.muscleStrength_tableWidget.setItem(0, 0, item)

        item = QtWidgets.QTableWidgetItem('肌肉无任何收缩')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.muscleStrength_tableWidget.setItem(0, 1, item)

        item = QtWidgets.QTableWidgetItem('0')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.muscleStrength_tableWidget.setItem(0, 2, item)

        item = QtWidgets.QTableWidgetItem('1')
        self.muscleStrength_tableWidget.setRowHeight(1, 65)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.muscleStrength_tableWidget.setItem(1, 0, item)

        item = QtWidgets.QTableWidgetItem('有轻微肌肉收缩，但不能引起关节活动')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.muscleStrength_tableWidget.setItem(1, 1, item)

        item = QtWidgets.QTableWidgetItem('10')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.muscleStrength_tableWidget.setItem(1, 2, item)

        item = QtWidgets.QTableWidgetItem('2')
        self.muscleStrength_tableWidget.setRowHeight(2, 65)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.muscleStrength_tableWidget.setItem(2, 0, item)

        item = QtWidgets.QTableWidgetItem('在减重状态下，能作关节全范围运动')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.muscleStrength_tableWidget.setItem(2, 1, item)

        item = QtWidgets.QTableWidgetItem('25')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.muscleStrength_tableWidget.setItem(2, 2, item)

        item = QtWidgets.QTableWidgetItem('3')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.muscleStrength_tableWidget.setRowHeight(3, 67)
        self.muscleStrength_tableWidget.setItem(3, 0, item)

        item = QtWidgets.QTableWidgetItem('能抗重力作关节全范围运动，但不能抗阻力')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.muscleStrength_tableWidget.setItem(3, 1, item)

        item = QtWidgets.QTableWidgetItem('50')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.muscleStrength_tableWidget.setItem(3, 2, item)

        item = QtWidgets.QTableWidgetItem('4')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.muscleStrength_tableWidget.setRowHeight(4, 67)
        self.muscleStrength_tableWidget.setItem(4, 0, item)

        item = QtWidgets.QTableWidgetItem('能抗重力，抵抗部分阻力运动')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.muscleStrength_tableWidget.setItem(4, 1, item)

        item = QtWidgets.QTableWidgetItem('75')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.muscleStrength_tableWidget.setItem(4, 2, item)

        item = QtWidgets.QTableWidgetItem('5')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.muscleStrength_tableWidget.setVerticalHeaderItem(5, item)
        self.muscleStrength_tableWidget.setRowHeight(5, 67)
        self.muscleStrength_tableWidget.setItem(5, 0, item)

        item = QtWidgets.QTableWidgetItem('能抗重力，并完全抵抗阻力运动')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.muscleStrength_tableWidget.setItem(5, 1, item)

        item = QtWidgets.QTableWidgetItem('100')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.muscleStrength_tableWidget.setItem(5, 2, item)

        self.label_17 = QtWidgets.QLabel(self.page_2)
        self.label_17.setGeometry(QtCore.QRect(20, 600, 500, 40))
        self.label_17.setStyleSheet("font:16pt")

        self.muscleStrength_shoulderQucomboBox = QtWidgets.QComboBox(self.page_2)
        self.muscleStrength_shoulderQucomboBox.setGeometry(QtCore.QRect(490, 605, 160, 35))
        self.muscleStrength_shoulderQucomboBox.addItems(['', '0', '1', '2', '3', '4', '5'])
        self.muscleStrength_shoulderQucomboBox.setStyleSheet("font:12pt")

        self.label_18 = QtWidgets.QLabel(self.page_2)
        self.label_18.setGeometry(QtCore.QRect(680, 600, 500, 40))
        self.label_18.setStyleSheet("font:16pt")

        self.muscleStrength_shoulderShencomboBox = QtWidgets.QComboBox(self.page_2)
        self.muscleStrength_shoulderShencomboBox.setGeometry(QtCore.QRect(1140, 605, 160, 35))
        self.muscleStrength_shoulderShencomboBox.addItems(['', '0', '1', '2', '3', '4', '5'])
        self.muscleStrength_shoulderShencomboBox.setStyleSheet("font:12pt")

        self.label_19 = QtWidgets.QLabel(self.page_2)
        self.label_19.setGeometry(QtCore.QRect(20, 660, 500, 40))
        self.label_19.setStyleSheet("font:16pt")

        self.muscleStrength_elbowQucomboBox = QtWidgets.QComboBox(self.page_2)
        self.muscleStrength_elbowQucomboBox.setGeometry(QtCore.QRect(490, 665, 160, 35))
        self.muscleStrength_elbowQucomboBox.addItems(['', '0', '1', '2', '3', '4', '5'])
        self.muscleStrength_elbowQucomboBox.setStyleSheet("font:12pt")

        self.label_20 = QtWidgets.QLabel(self.page_2)
        self.label_20.setGeometry(QtCore.QRect(680, 660, 500, 40))
        self.label_20.setStyleSheet("font:16pt")

        self.muscleStrength_elbowShencomboBox = QtWidgets.QComboBox(self.page_2)
        self.muscleStrength_elbowShencomboBox.setGeometry(QtCore.QRect(1140, 665, 160, 35))
        self.muscleStrength_elbowShencomboBox.addItems(['', '0', '1', '2', '3', '4', '5'])
        self.muscleStrength_elbowShencomboBox.setStyleSheet("font:12pt")

        self.label_21 = QtWidgets.QLabel(self.page_2)
        self.label_21.setGeometry(QtCore.QRect(20, 720, 500, 40))
        self.label_21.setStyleSheet("font:16pt")

        self.muscleStrength_wristQuJicomboBox = QtWidgets.QComboBox(self.page_2)
        self.muscleStrength_wristQuJicomboBox.setGeometry(QtCore.QRect(490, 725, 160, 35))
        self.muscleStrength_wristQuJicomboBox.addItems(['', '0', '1', '2', '3', '4', '5'])
        self.muscleStrength_wristQuJicomboBox.setStyleSheet("font:12pt")

        self.label_22 = QtWidgets.QLabel(self.page_2)
        self.label_22.setGeometry(QtCore.QRect(680, 720, 500, 40))
        self.label_22.setStyleSheet("font:16pt")

        self.muscleStrength_wristShenJicomboBox = QtWidgets.QComboBox(self.page_2)
        self.muscleStrength_wristShenJicomboBox.setGeometry(QtCore.QRect(1140, 725, 160, 35))
        self.muscleStrength_wristShenJicomboBox.addItems(['', '0', '1', '2', '3', '4', '5'])
        self.muscleStrength_wristShenJicomboBox.setStyleSheet("font:12pt")

        self.label_23 = QtWidgets.QLabel(self.page_2)
        self.label_23.setGeometry(QtCore.QRect(20, 780, 500, 40))
        self.label_23.setStyleSheet("font:16pt")

        self.muscleStrength_gripStrengthQuJicomboBox = QtWidgets.QComboBox(self.page_2)
        self.muscleStrength_gripStrengthQuJicomboBox.setGeometry(QtCore.QRect(320, 785, 160, 35))
        self.muscleStrength_gripStrengthQuJicomboBox.addItems(['', '0', '1', '2', '3', '4', '5'])
        self.muscleStrength_gripStrengthQuJicomboBox.setStyleSheet("font:12pt")

        self.label_24 = QtWidgets.QLabel(self.page_2)
        self.label_24.setGeometry(QtCore.QRect(680, 780, 500, 40))
        self.label_24.setStyleSheet("font:16pt")

        self.muscleStrength_gripStrengthShenJicomboBox = QtWidgets.QComboBox(self.page_2)
        self.muscleStrength_gripStrengthShenJicomboBox.setGeometry(QtCore.QRect(970, 785, 160, 35))
        self.muscleStrength_gripStrengthShenJicomboBox.addItems(['', '0', '1', '2', '3', '4', '5'])
        self.muscleStrength_gripStrengthShenJicomboBox.setStyleSheet("font:12pt")

        self.label_25 = QtWidgets.QLabel(self.page_2)
        self.label_25.setGeometry(QtCore.QRect(20, 860, 260, 40))
        self.label_25.setStyleSheet("font:16pt")

        self.muscleStrength_dateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.page_2)
        self.muscleStrength_dateEdit.setGeometry(QtCore.QRect(200, 860, 260, 40))
        self.muscleStrength_dateEdit.setStyleSheet("font:16pt")
        self.muscleStrength_dateEdit.setCalendarPopup(True)

        self.muscleStrength_saveButton = QtWidgets.QPushButton(self.page_2)
        self.muscleStrength_saveButton.setGeometry(QtCore.QRect(500, 860, 120, 40))
        self.muscleStrength_saveButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.muscleStrength_uploadButton = QtWidgets.QPushButton(self.page_2)
        self.muscleStrength_uploadButton.setGeometry(QtCore.QRect(680, 860, 120, 40))
        self.muscleStrength_uploadButton.setText('导出')
        self.muscleStrength_uploadButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")
        self.stackedWidget.addWidget(self.page_2)

        self.page_3 = QtWidgets.QWidget()
        self.label_26 = QtWidgets.QLabel(self.page_3)
        self.label_26.setGeometry(QtCore.QRect(500, 10, 400, 41))
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_26.setStyleSheet('font:16pt')

        self.label_27 = QtWidgets.QLabel(self.page_3)
        self.label_27.setGeometry(QtCore.QRect(80, 60, 200, 40))
        self.label_27.setStyleSheet('font:14pt')

        self.MSS_name = QtWidgets.QLabel(self.page_3)
        self.MSS_name.setGeometry(QtCore.QRect(160, 60, 200, 40))
        self.MSS_name.setStyleSheet('font:14pt')

        self.label_28 = QtWidgets.QLabel(self.page_3)
        self.label_28.setGeometry(QtCore.QRect(280, 60, 200, 40))
        self.label_28.setStyleSheet('font:14pt')

        self.MSS_sex = QtWidgets.QLabel(self.page_3)
        self.MSS_sex.setGeometry(QtCore.QRect(360, 60, 200, 40))
        self.MSS_sex.setStyleSheet('font:14pt')

        self.label_29 = QtWidgets.QLabel(self.page_3)
        self.label_29.setGeometry(QtCore.QRect(480, 60, 200, 40))
        self.label_29.setStyleSheet('font:14pt')

        self.MSS_age = QtWidgets.QLabel(self.page_3)
        self.MSS_age.setGeometry(QtCore.QRect(560, 60, 200, 40))
        self.MSS_age.setStyleSheet('font:14pt')

        self.label_30 = QtWidgets.QLabel(self.page_3)
        self.label_30.setGeometry(QtCore.QRect(680, 60, 200, 40))
        self.label_30.setStyleSheet('font:14pt')

        self.MSS_hand = QtWidgets.QLabel(self.page_3)
        self.MSS_hand.setGeometry(QtCore.QRect(760, 60, 200, 40))
        self.MSS_hand.setStyleSheet('font:14pt')

        self.MSS_table = QtWidgets.QTableWidget(self.page_3)
        self.MSS_table.setGeometry(QtCore.QRect(20, 120, 1460, 700))
        self.MSS_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MSS_table.setStyleSheet('background:white;font:12pt')
        self.MSS_table.setColumnCount(5)
        self.MSS_table.setRowCount(44)
        self.MSS_table.verticalHeader().setVisible(False)

        item = QtWidgets.QTableWidgetItem()
        self.MSS_table.setHorizontalHeaderItem(0, item)  # 列
        self.MSS_table.setColumnWidth(0, 160)
        item = QtWidgets.QTableWidgetItem()
        self.MSS_table.setHorizontalHeaderItem(1, item)
        self.MSS_table.setColumnWidth(1, 160)
        item = QtWidgets.QTableWidgetItem()
        self.MSS_table.setHorizontalHeaderItem(2, item)
        self.MSS_table.setColumnWidth(2, 160)
        item = QtWidgets.QTableWidgetItem()
        self.MSS_table.setHorizontalHeaderItem(3, item)
        self.MSS_table.setColumnWidth(3, 730)
        item = QtWidgets.QTableWidgetItem()
        self.MSS_table.setHorizontalHeaderItem(4, item)
        self.MSS_table.setColumnWidth(4, 208)

        item = QtWidgets.QTableWidgetItem('肩')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(0, 0, item)
        self.MSS_table.setSpan(0, 0, 17, 1)
        self.MSS_table.setSpan(0, 4, 2, 1)

        item = QtWidgets.QTableWidgetItem('1')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(0, 1, item)
        self.MSS_table.setSpan(0, 1, 2, 2)
        item = QtWidgets.QTableWidgetItem('A.肩前屈90°，肘0°，前臂中立位')
        self.MSS_table.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem('B.如果完成，能否保持位置')
        self.MSS_table.setItem(1, 3, item)

        item = QtWidgets.QTableWidgetItem('2')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(2, 1, item)
        self.MSS_table.setSpan(2, 1, 2, 2)
        self.MSS_table.setSpan(2, 4, 2, 1)
        item = QtWidgets.QTableWidgetItem('A.肩外展90°，肘0°，前臂旋前位')
        self.MSS_table.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem('B.如果完成，能否保持位置')
        self.MSS_table.setItem(3, 3, item)

        item = QtWidgets.QTableWidgetItem('3')
        self.MSS_table.setItem(4, 1, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setSpan(4, 1, 2, 2)
        self.MSS_table.setSpan(4, 4, 2, 1)
        item = QtWidgets.QTableWidgetItem('A.肩部前屈90°-150°，肘0°')
        self.MSS_table.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem('B.如果完成，能否保持位置')
        self.MSS_table.setItem(5, 3, item)

        item = QtWidgets.QTableWidgetItem('4')
        self.MSS_table.setItem(6, 1, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setSpan(6, 1, 2, 2)
        self.MSS_table.setSpan(6, 4, 2, 1)
        item = QtWidgets.QTableWidgetItem('A.摸头顶')
        self.MSS_table.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem('B.如果完成，能否保持位置')
        self.MSS_table.setItem(7, 3, item)

        item = QtWidgets.QTableWidgetItem('5')
        self.MSS_table.setItem(8, 1, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setSpan(8, 1, 2, 2)
        self.MSS_table.setSpan(8, 4, 2, 1)
        item = QtWidgets.QTableWidgetItem('A.摸腰部脊柱')
        self.MSS_table.setItem(8, 3, item)
        item = QtWidgets.QTableWidgetItem('B.如果完成，能否保持位置')
        self.MSS_table.setItem(9, 3, item)

        item = QtWidgets.QTableWidgetItem('6')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(10, 1, item)
        self.MSS_table.setSpan(10, 1, 1, 2)
        item = QtWidgets.QTableWidgetItem('肩部上提')
        self.MSS_table.setItem(10, 3, item)

        item = QtWidgets.QTableWidgetItem('7')
        self.MSS_table.setItem(11, 1, item)
        self.MSS_table.setSpan(11, 1, 1, 2)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item = QtWidgets.QTableWidgetItem('在有支撑的条件下手臂前伸/收回（大腿或桌子）')
        self.MSS_table.setItem(11, 3, item)

        item = QtWidgets.QTableWidgetItem('8')
        self.MSS_table.setItem(12, 1, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setSpan(12, 1, 2, 2)
        self.MSS_table.setSpan(12, 4, 2, 1)
        item = QtWidgets.QTableWidgetItem('A.肘屈曲90°时肩部前屈30°')
        self.MSS_table.setItem(12, 3, item)
        item = QtWidgets.QTableWidgetItem('B.前臂支撑桌面，肘屈曲肩部后伸30°')
        self.MSS_table.setItem(13, 3, item)

        item = QtWidgets.QTableWidgetItem('9')
        self.MSS_table.setItem(14, 1, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setSpan(14, 1, 2, 2)
        self.MSS_table.setSpan(14, 4, 2, 1)
        item = QtWidgets.QTableWidgetItem('A.肩0°，肘90°，肩内旋到手触腹部')
        self.MSS_table.setItem(14, 3, item)
        item = QtWidgets.QTableWidgetItem('B.肩0°，肘90°，肩部外旋')
        self.MSS_table.setItem(15, 3, item)

        item = QtWidgets.QTableWidgetItem('10')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(16, 1, item)
        self.MSS_table.setSpan(16, 1, 1, 2)
        item = QtWidgets.QTableWidgetItem('手触对侧膝部')
        self.MSS_table.setItem(16, 3, item)

        item = QtWidgets.QTableWidgetItem('肘前臂')
        self.MSS_table.setItem(17, 0, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setSpan(17, 0, 6, 1)

        item = QtWidgets.QTableWidgetItem('1')
        self.MSS_table.setItem(17, 1, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setSpan(17, 1, 2, 2)
        self.MSS_table.setSpan(17, 4, 2, 1)
        item = QtWidgets.QTableWidgetItem('A.肩0°，肘90°，前臂旋前')
        self.MSS_table.setItem(16, 3, item)
        item = QtWidgets.QTableWidgetItem('B.肩0°，肘90°，前臂旋后')
        self.MSS_table.setItem(18, 3, item)

        item = QtWidgets.QTableWidgetItem('2')
        self.MSS_table.setItem(19, 1, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setSpan(19, 1, 2, 2)
        self.MSS_table.setSpan(19, 4, 2, 1)
        item = QtWidgets.QTableWidgetItem('A.肘0°，完全屈曲')
        self.MSS_table.setItem(19, 3, item)
        item = QtWidgets.QTableWidgetItem('B.如果完成，能否保持位置')
        self.MSS_table.setItem(20, 3, item)

        item = QtWidgets.QTableWidgetItem('3')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(21, 1, item)
        self.MSS_table.setSpan(21, 1, 1, 2)
        item = QtWidgets.QTableWidgetItem('肘由屈曲位伸展到0°（减重或抗重）')
        self.MSS_table.setItem(21, 3, item)

        item = QtWidgets.QTableWidgetItem('4')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(22, 1, item)
        self.MSS_table.setSpan(22, 1, 1, 2)
        item = QtWidgets.QTableWidgetItem('手摸对侧肩部')
        self.MSS_table.setItem(22, 3, item)

        item = QtWidgets.QTableWidgetItem('肩肘前臂总分')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(23, 0, item)
        self.MSS_table.setSpan(23, 0, 21, 1)

        item = QtWidgets.QTableWidgetItem('腕')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(23, 1, item)
        self.MSS_table.setSpan(23, 1, 3, 1)

        item = QtWidgets.QTableWidgetItem('1')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(23, 2, item)
        item = QtWidgets.QTableWidgetItem('肩0°，肘90°，前臂旋前，伸腕')
        self.MSS_table.setItem(23, 3, item)

        item = QtWidgets.QTableWidgetItem('2')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(24, 2, item)
        item = QtWidgets.QTableWidgetItem('肩0°，肘90°，前臂旋后，屈腕')
        self.MSS_table.setItem(24, 3, item)

        item = QtWidgets.QTableWidgetItem('3')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(25, 2, item)
        item = QtWidgets.QTableWidgetItem('肩0°，肘90°，前臂旋前，腕旋转')
        self.MSS_table.setItem(25, 3, item)

        item = QtWidgets.QTableWidgetItem('手')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(26, 1, item)
        self.MSS_table.setSpan(26, 1, 17, 1)

        item = QtWidgets.QTableWidgetItem('1')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(26, 2, item)
        item = QtWidgets.QTableWidgetItem('手指集团屈曲')
        self.MSS_table.setItem(26, 3, item)

        item = QtWidgets.QTableWidgetItem('2')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(27, 2, item)
        item = QtWidgets.QTableWidgetItem('手指集团伸展')
        self.MSS_table.setItem(27, 3, item)

        item = QtWidgets.QTableWidgetItem('3')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(27, 2, item)
        item = QtWidgets.QTableWidgetItem('勾状抓握')
        self.MSS_table.setItem(27, 3, item)

        item = QtWidgets.QTableWidgetItem('4')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(28, 2, item)
        item = QtWidgets.QTableWidgetItem('掌指关节屈曲，指间关节')
        self.MSS_table.setItem(28, 3, item)

        item = QtWidgets.QTableWidgetItem('5')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(29, 2, item)
        item = QtWidgets.QTableWidgetItem('拇指外展')
        self.MSS_table.setItem(29, 3, item)

        item = QtWidgets.QTableWidgetItem('6')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(30, 2, item)
        item = QtWidgets.QTableWidgetItem('拇指内收')
        self.MSS_table.setItem(30, 3, item)

        item = QtWidgets.QTableWidgetItem('7')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(31, 2, item)
        item = QtWidgets.QTableWidgetItem('拇指对小指根部')
        self.MSS_table.setItem(31, 3, item)

        item = QtWidgets.QTableWidgetItem('8')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(32, 2, item)
        self.MSS_table.setSpan(32, 2, 4, 1)
        self.MSS_table.setSpan(32, 4, 4, 1)
        item = QtWidgets.QTableWidgetItem('A.拇指对食指指尖')
        self.MSS_table.setItem(32, 3, item)
        item = QtWidgets.QTableWidgetItem('B.拇指对中指指尖')
        self.MSS_table.setItem(33, 3, item)
        item = QtWidgets.QTableWidgetItem('C.拇指对环指指尖')
        self.MSS_table.setItem(34, 3, item)
        item = QtWidgets.QTableWidgetItem('D.拇指对小指指尖')
        self.MSS_table.setItem(35, 3, item)

        item = QtWidgets.QTableWidgetItem('9')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(36, 2, item)
        self.MSS_table.setSpan(36, 2, 4, 1)
        self.MSS_table.setSpan(36, 4, 4, 1)
        item = QtWidgets.QTableWidgetItem('A.拇指对食指指腹')
        self.MSS_table.setItem(36, 3, item)
        item = QtWidgets.QTableWidgetItem('B.拇指对中指指腹')
        self.MSS_table.setItem(37, 3, item)
        item = QtWidgets.QTableWidgetItem('C.拇指对环指指腹')
        self.MSS_table.setItem(38, 3, item)
        item = QtWidgets.QTableWidgetItem('D.拇指对小指指腹')
        self.MSS_table.setItem(39, 3, item)

        item = QtWidgets.QTableWidgetItem('10')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(40, 2, item)
        item = QtWidgets.QTableWidgetItem('抓住饮料瓶，放到2-4英寸远并放开')
        self.MSS_table.setItem(40, 3, item)

        item = QtWidgets.QTableWidgetItem('11')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(41, 2, item)
        item = QtWidgets.QTableWidgetItem('钳状抓握钢笔，签名，写日期或画3条垂直线')
        self.MSS_table.setItem(41, 3, item)

        item = QtWidgets.QTableWidgetItem('12')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(42, 2, item)
        item = QtWidgets.QTableWidgetItem('侧捏钥匙')
        self.MSS_table.setItem(42, 3, item)

        item = QtWidgets.QTableWidgetItem('腕指总分')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MSS_table.setItem(43, 1, item)
        self.MSS_table.setSpan(43, 2, 1, 2)

        self.label_31 = QtWidgets.QLabel(self.page_3)
        self.label_31.setGeometry(QtCore.QRect(20, 840, 260, 40))
        self.label_31.setStyleSheet("font:16pt")

        self.MSS_dateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.page_3)
        self.MSS_dateEdit.setGeometry(QtCore.QRect(170, 840, 260, 40))
        self.MSS_dateEdit.setStyleSheet("font:16pt;background:white")
        self.MSS_dateEdit.setCalendarPopup(True)

        self.MSS_saveButton = QtWidgets.QPushButton(self.page_3)
        self.MSS_saveButton.setGeometry(QtCore.QRect(450, 840, 120, 40))
        self.MSS_saveButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.MSS_downLoadButton = QtWidgets.QPushButton(self.page_3)
        self.MSS_downLoadButton.setGeometry(QtCore.QRect(590, 840, 120, 40))
        self.MSS_downLoadButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")
        self.stackedWidget.addWidget(self.page_3)

        self.page_4 = QtWidgets.QWidget()
        self.label_32 = QtWidgets.QLabel(self.page_4)
        self.label_32.setGeometry(QtCore.QRect(500, 10, 500, 41))
        self.label_32.setAlignment(Qt.AlignCenter)
        self.label_32.setStyleSheet('font:16pt')

        self.label_33 = QtWidgets.QLabel(self.page_4)
        self.label_33.setGeometry(QtCore.QRect(80, 60, 200, 40))
        self.label_33.setStyleSheet('font:14pt')

        self.Brunnstrom_name = QtWidgets.QLabel(self.page_4)
        self.Brunnstrom_name.setGeometry(QtCore.QRect(160, 60, 200, 40))
        self.Brunnstrom_name.setStyleSheet('font:14pt')

        self.label_34 = QtWidgets.QLabel(self.page_4)
        self.label_34.setGeometry(QtCore.QRect(280, 60, 200, 40))
        self.label_34.setStyleSheet('font:14pt')

        self.Brunnstrom_sex = QtWidgets.QLabel(self.page_4)
        self.Brunnstrom_sex.setGeometry(QtCore.QRect(360, 60, 200, 40))
        self.Brunnstrom_sex.setStyleSheet('font:14pt')

        self.label_35 = QtWidgets.QLabel(self.page_4)
        self.label_35.setGeometry(QtCore.QRect(480, 60, 200, 40))
        self.label_35.setStyleSheet('font:14pt')

        self.Brunnstrom_age = QtWidgets.QLabel(self.page_4)
        self.Brunnstrom_age.setGeometry(QtCore.QRect(560, 60, 200, 40))
        self.Brunnstrom_age.setStyleSheet('font:14pt')

        self.label_36 = QtWidgets.QLabel(self.page_4)
        self.label_36.setGeometry(QtCore.QRect(680, 60, 200, 40))
        self.label_36.setStyleSheet('font:14pt')

        self.Brunnstrom_hand = QtWidgets.QLabel(self.page_4)
        self.Brunnstrom_hand.setGeometry(QtCore.QRect(760, 60, 200, 40))
        self.Brunnstrom_hand.setStyleSheet('font:14pt')

        self.Brunnstrom_table = QtWidgets.QTableWidget(self.page_4)
        self.Brunnstrom_table.setGeometry(QtCore.QRect(20, 120, 1460, 600))
        self.Brunnstrom_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Brunnstrom_table.setStyleSheet('background:white;font:12pt')
        self.Brunnstrom_table.setColumnCount(3)
        self.Brunnstrom_table.setRowCount(12)
        self.Brunnstrom_table.verticalHeader().setVisible(False)

        item = QtWidgets.QTableWidgetItem()
        self.Brunnstrom_table.setHorizontalHeaderItem(0, item)  # 列
        self.Brunnstrom_table.setColumnWidth(0, 140)
        item = QtWidgets.QTableWidgetItem()
        self.Brunnstrom_table.setHorizontalHeaderItem(1, item)
        self.Brunnstrom_table.setColumnWidth(1, 680)
        item = QtWidgets.QTableWidgetItem()
        self.Brunnstrom_table.setHorizontalHeaderItem(2, item)
        self.Brunnstrom_table.setColumnWidth(2, 640)

        item = QtWidgets.QTableWidgetItem('Ⅰ')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.Brunnstrom_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem('无随意运动（弛缓期）')
        self.Brunnstrom_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem('无随意运动（弛缓期）')
        self.Brunnstrom_table.setItem(0, 2, item)

        item = QtWidgets.QTableWidgetItem('Ⅱ')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.Brunnstrom_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem('联带运动初期阶段（痉挛期）')
        self.Brunnstrom_table.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem('细微屈伸（痉挛期）')
        self.Brunnstrom_table.setItem(1, 2, item)

        item = QtWidgets.QTableWidgetItem('Ⅲ')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.Brunnstrom_table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem('联带运动达到高峰')
        self.Brunnstrom_table.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem('联带运动达到高峰（钩状抓握不能伸）')
        self.Brunnstrom_table.setItem(2, 2, item)

        item = QtWidgets.QTableWidgetItem('Ⅳ')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.Brunnstrom_table.setItem(3, 0, item)
        self.Brunnstrom_table.setSpan(3, 0, 4, 1)
        self.Brunnstrom_table.setSpan(3, 2, 2, 1)
        self.Brunnstrom_table.setSpan(5, 2, 2, 1)
        item = QtWidgets.QTableWidgetItem('出现部分分离运动:')
        self.Brunnstrom_table.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem('手背到腰后;')
        self.Brunnstrom_table.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem('肘关节伸展，肩关节屈曲90度;')
        self.Brunnstrom_table.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem('肘关节屈曲90度，前臂旋前、旋后;')
        self.Brunnstrom_table.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem('侧捏、松开拇指')
        self.Brunnstrom_table.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem('手指小范围伸')
        self.Brunnstrom_table.setItem(5, 2, item)

        item = QtWidgets.QTableWidgetItem('Ⅴ')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.Brunnstrom_table.setItem(7, 0, item)
        self.Brunnstrom_table.setSpan(7, 0, 4, 1)
        self.Brunnstrom_table.setSpan(7, 2, 2, 1)
        self.Brunnstrom_table.setSpan(9, 2, 2, 1)
        item = QtWidgets.QTableWidgetItem('出现分离运动:')
        self.Brunnstrom_table.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem('肘关节伸展，肩关节外展90度;')
        self.Brunnstrom_table.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem('肘关节伸展，肩关节上举;')
        self.Brunnstrom_table.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem('肘关节伸展，肩关节屈曲90度，前臂旋前、旋后;')
        self.Brunnstrom_table.setItem(10, 1, item)
        item = QtWidgets.QTableWidgetItem('球状、圆柱状抓握')
        self.Brunnstrom_table.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem('手指同时伸展（不能单独伸）')
        self.Brunnstrom_table.setItem(9, 2, item)

        item = QtWidgets.QTableWidgetItem('Ⅵ')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.Brunnstrom_table.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem('指鼻试验（比健侧慢，小于5秒）')
        self.Brunnstrom_table.setItem(11, 1, item)
        item = QtWidgets.QTableWidgetItem('抓握均能完成，速度及准确性差')
        self.Brunnstrom_table.setItem(11, 2, item)

        self.label_37 = QtWidgets.QLabel(self.page_4)
        self.label_37.setGeometry(QtCore.QRect(20, 740, 200, 100))
        self.label_37.setStyleSheet("font:14pt")

        self.Brunnstrom_handFunctionLineEdit = QtWidgets.QLineEdit(self.page_4)
        self.Brunnstrom_handFunctionLineEdit.setGeometry(QtCore.QRect(120, 770, 150, 40))
        self.Brunnstrom_handFunctionLineEdit.setStyleSheet("font:14pt;background:white")

        self.label_38 = QtWidgets.QLabel(self.page_4)
        self.label_38.setGeometry(QtCore.QRect(300, 740, 1460, 100))
        self.label_38.setStyleSheet("font:14pt")

        self.Brunnstrom_upperLimbFunctionLineEdit = QtWidgets.QLineEdit(self.page_4)
        self.Brunnstrom_upperLimbFunctionLineEdit.setGeometry(QtCore.QRect(430, 770, 150, 40))
        self.Brunnstrom_upperLimbFunctionLineEdit.setStyleSheet("font:14pt;background:white")

        self.label_39 = QtWidgets.QLabel(self.page_4)
        self.label_39.setGeometry(QtCore.QRect(600, 770, 260, 40))
        self.label_39.setStyleSheet("font:14pt")

        self.Brunnstrom_dateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.page_4)
        self.Brunnstrom_dateEdit.setGeometry(QtCore.QRect(750, 770, 260, 40))
        self.Brunnstrom_dateEdit.setStyleSheet("font:16pt;background:white")
        self.Brunnstrom_dateEdit.setCalendarPopup(True)

        self.Brunnstrom_saveButton = QtWidgets.QPushButton(self.page_4)
        self.Brunnstrom_saveButton.setGeometry(QtCore.QRect(650, 840, 120, 40))
        self.Brunnstrom_saveButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.Brunnstrom_downLoadButton = QtWidgets.QPushButton(self.page_4)
        self.Brunnstrom_downLoadButton.setGeometry(QtCore.QRect(790, 840, 120, 40))
        self.Brunnstrom_downLoadButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")
        self.stackedWidget.addWidget(self.page_4)

        self.page_5 = QtWidgets.QWidget()
        self.label_40 = QtWidgets.QLabel(self.page_5)
        self.label_40.setGeometry(QtCore.QRect(500, 10, 400, 41))
        self.label_40.setAlignment(Qt.AlignCenter)
        self.label_40.setStyleSheet('font:16pt')

        self.label_41 = QtWidgets.QLabel(self.page_5)
        self.label_41.setGeometry(QtCore.QRect(80, 60, 200, 40))
        self.label_41.setStyleSheet('font:14pt')

        self.HandednessInventory_name = QtWidgets.QLabel(self.page_5)
        self.HandednessInventory_name.setGeometry(QtCore.QRect(160, 60, 200, 40))
        self.HandednessInventory_name.setStyleSheet('font:14pt')

        self.label_42 = QtWidgets.QLabel(self.page_5)
        self.label_42.setGeometry(QtCore.QRect(280, 60, 200, 40))
        self.label_42.setStyleSheet('font:14pt')

        self.HandednessInventory_sex = QtWidgets.QLabel(self.page_5)
        self.HandednessInventory_sex.setGeometry(QtCore.QRect(360, 60, 200, 40))
        self.HandednessInventory_sex.setStyleSheet('font:14pt')

        self.label_43 = QtWidgets.QLabel(self.page_5)
        self.label_43.setGeometry(QtCore.QRect(480, 60, 200, 40))
        self.label_43.setStyleSheet('font:14pt')

        self.HandednessInventory_age = QtWidgets.QLabel(self.page_5)
        self.HandednessInventory_age.setGeometry(QtCore.QRect(560, 60, 200, 40))
        self.HandednessInventory_age.setStyleSheet('font:14pt')

        self.label_44 = QtWidgets.QLabel(self.page_5)
        self.label_44.setGeometry(QtCore.QRect(680, 60, 200, 40))
        self.label_44.setStyleSheet('font:14pt')

        self.HandednessInventory_hand = QtWidgets.QLabel(self.page_5)
        self.HandednessInventory_hand.setGeometry(QtCore.QRect(760, 60, 200, 40))
        self.HandednessInventory_hand.setStyleSheet('font:14pt')

        self.HandednessInventory_table = QtWidgets.QTableWidget(self.page_5)
        self.HandednessInventory_table.setGeometry(QtCore.QRect(20, 120, 1460, 590))
        self.HandednessInventory_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.HandednessInventory_table.setStyleSheet('background:white;font:12pt')
        self.HandednessInventory_table.setColumnCount(3)
        self.HandednessInventory_table.setRowCount(12)
        self.HandednessInventory_table.verticalHeader().setVisible(False)

        item = QtWidgets.QTableWidgetItem()
        self.HandednessInventory_table.setHorizontalHeaderItem(0, item)  # 列
        self.HandednessInventory_table.setColumnWidth(0, 400)
        item = QtWidgets.QTableWidgetItem()
        self.HandednessInventory_table.setHorizontalHeaderItem(1, item)
        self.HandednessInventory_table.setColumnWidth(1, 560)
        item = QtWidgets.QTableWidgetItem()
        self.HandednessInventory_table.setHorizontalHeaderItem(2, item)
        self.HandednessInventory_table.setColumnWidth(2, 500)

        item = QtWidgets.QTableWidgetItem('执笔')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.HandednessInventory_table.setItem(0, 0, item)

        item = QtWidgets.QTableWidgetItem('执筷')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.HandednessInventory_table.setItem(1, 0, item)

        item = QtWidgets.QTableWidgetItem('掷东西')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.HandednessInventory_table.setItem(2, 0, item)

        item = QtWidgets.QTableWidgetItem('持牙刷刷牙')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.HandednessInventory_table.setItem(3, 0, item)

        item = QtWidgets.QTableWidgetItem('持剪刀')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.HandednessInventory_table.setItem(4, 0, item)

        item = QtWidgets.QTableWidgetItem('划火柴')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.HandednessInventory_table.setItem(5, 0, item)

        item = QtWidgets.QTableWidgetItem('持线穿针')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.HandednessInventory_table.setItem(6, 0, item)

        item = QtWidgets.QTableWidgetItem('握钉锤')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.HandednessInventory_table.setItem(7, 0, item)

        item = QtWidgets.QTableWidgetItem('执笔')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.HandednessInventory_table.setItem(8, 0, item)

        item = QtWidgets.QTableWidgetItem('握球拍')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.HandednessInventory_table.setItem(9, 0, item)

        item = QtWidgets.QTableWidgetItem('持毛巾洗脸')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.HandednessInventory_table.setItem(10, 0, item)

        item = QtWidgets.QTableWidgetItem('结论')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.HandednessInventory_table.setItem(11, 0, item)

        self.label_45 = QtWidgets.QLabel(self.page_5)
        self.label_45.setGeometry(QtCore.QRect(20, 660, 1460, 100))
        self.label_45.setStyleSheet("font:14pt")

        self.HandednessInventory_conclusionLineEdit = QtWidgets.QLineEdit(self.page_5)
        self.HandednessInventory_conclusionLineEdit.setGeometry(QtCore.QRect(120, 690, 1200, 40))
        self.HandednessInventory_conclusionLineEdit.setStyleSheet("font:14pt;background:white")

        self.label_46 = QtWidgets.QLabel(self.page_5)
        self.label_46.setGeometry(QtCore.QRect(20, 760, 260, 40))
        self.label_46.setStyleSheet("font:14pt")

        self.HandednessInventory_dateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.page_5)
        self.HandednessInventory_dateEdit.setGeometry(QtCore.QRect(170, 760, 260, 40))
        self.HandednessInventory_dateEdit.setStyleSheet("font:16pt;background:white")
        self.HandednessInventory_dateEdit.setCalendarPopup(True)

        self.HandednessInventory_saveButton = QtWidgets.QPushButton(self.page_5)
        self.HandednessInventory_saveButton.setGeometry(QtCore.QRect(450, 760, 120, 40))
        self.HandednessInventory_saveButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.HandednessInventory_downLoadButton = QtWidgets.QPushButton(self.page_5)
        self.HandednessInventory_downLoadButton.setGeometry(QtCore.QRect(590, 760, 120, 40))
        self.HandednessInventory_downLoadButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.label_47 = QtWidgets.QLabel(self.page_5)
        self.label_47.setGeometry(QtCore.QRect(20, 810, 1460, 220))
        self.label_47.setStyleSheet("font:14pt")
        self.label_47.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_5)

        self.page_6 = QtWidgets.QWidget()
        self.label_48 = QtWidgets.QLabel(self.page_6)
        self.label_48.setGeometry(QtCore.QRect(500, 10, 400, 41))
        self.label_48.setAlignment(Qt.AlignCenter)
        self.label_48.setStyleSheet('font:16pt')

        self.label_49 = QtWidgets.QLabel(self.page_6)
        self.label_49.setGeometry(QtCore.QRect(80, 60, 200, 40))
        self.label_49.setStyleSheet('font:14pt')

        self.vas_name = QtWidgets.QLabel(self.page_6)
        self.vas_name.setGeometry(QtCore.QRect(160, 60, 200, 40))
        self.vas_name.setStyleSheet('font:14pt')

        self.label_50 = QtWidgets.QLabel(self.page_6)
        self.label_50.setGeometry(QtCore.QRect(280, 60, 200, 40))
        self.label_50.setStyleSheet('font:14pt')

        self.vas_sex = QtWidgets.QLabel(self.page_6)
        self.vas_sex.setGeometry(QtCore.QRect(360, 60, 200, 40))
        self.vas_sex.setStyleSheet('font:14pt')

        self.label_51 = QtWidgets.QLabel(self.page_6)
        self.label_51.setGeometry(QtCore.QRect(480, 60, 200, 40))
        self.label_51.setStyleSheet('font:14pt')

        self.vas_age = QtWidgets.QLabel(self.page_6)
        self.vas_age.setGeometry(QtCore.QRect(560, 60, 200, 40))
        self.vas_age.setStyleSheet('font:14pt')

        self.label_52 = QtWidgets.QLabel(self.page_6)
        self.label_52.setGeometry(QtCore.QRect(680, 60, 200, 40))
        self.label_52.setStyleSheet('font:14pt')

        self.vas_hand = QtWidgets.QLabel(self.page_6)
        self.vas_hand.setGeometry(QtCore.QRect(760, 60, 200, 40))
        self.vas_hand.setStyleSheet('font:14pt')

        self.label_53 = QtWidgets.QLabel(self.page_6)
        self.label_53.setGeometry(QtCore.QRect(30, 340, 200, 40))
        self.label_53.setStyleSheet('font:14pt')

        self.label_54 = QtWidgets.QLabel(self.page_6)
        self.label_54.setGeometry(QtCore.QRect(1390, 340, 200, 40))
        self.label_54.setStyleSheet('font:14pt')

        self.label_55 = QtWidgets.QLabel(self.page_6)
        self.label_55.setGeometry(QtCore.QRect(60, 180, 200, 40))
        self.label_55.setStyleSheet('font:14pt')

        self.label_56 = QtWidgets.QLabel(self.page_6)
        self.label_56.setGeometry(QtCore.QRect(200, 180, 200, 40))
        self.label_56.setStyleSheet('font:14pt')

        self.label_57 = QtWidgets.QLabel(self.page_6)
        self.label_57.setGeometry(QtCore.QRect(330, 180, 200, 40))
        self.label_57.setStyleSheet('font:14pt')

        self.label_58 = QtWidgets.QLabel(self.page_6)
        self.label_58.setGeometry(QtCore.QRect(465, 180, 200, 40))
        self.label_58.setStyleSheet('font:14pt')

        self.label_59 = QtWidgets.QLabel(self.page_6)
        self.label_59.setGeometry(QtCore.QRect(600, 180, 200, 40))
        self.label_59.setStyleSheet('font:14pt')

        self.label_60 = QtWidgets.QLabel(self.page_6)
        self.label_60.setGeometry(QtCore.QRect(735, 180, 200, 40))
        self.label_60.setStyleSheet('font:14pt')

        self.label_61 = QtWidgets.QLabel(self.page_6)
        self.label_61.setGeometry(QtCore.QRect(870, 180, 200, 40))
        self.label_61.setStyleSheet('font:14pt')

        self.label_62 = QtWidgets.QLabel(self.page_6)  # 7
        self.label_62.setGeometry(QtCore.QRect(1000, 180, 200, 40))
        self.label_62.setStyleSheet('font:14pt')

        self.label_63 = QtWidgets.QLabel(self.page_6)  # 8
        self.label_63.setGeometry(QtCore.QRect(1135, 180, 200, 40))
        self.label_63.setStyleSheet('font:14pt')

        self.vas_s1 = QSlider(Qt.Horizontal, self.page_6)
        self.vas_s1.setGeometry(QtCore.QRect(60, 230, 1360, 100))
        self.vas_s1.setStyleSheet('font:16pt;')
        # 设置最小值
        self.vas_s1.setMinimum(0)
        # 设置最大值
        self.vas_s1.setMaximum(10)
        # 设置步长
        self.vas_s1.setSingleStep(1)
        # 设置当前值
        self.vas_s1.setValue(0)
        # 刻度位置在下方
        self.vas_s1.setTickPosition(QSlider.TicksBothSides)
        # 设置刻度间隔
        self.vas_s1.setTickInterval(1)

        self.label_64 = QtWidgets.QLabel(self.page_6)  # 9
        self.label_64.setGeometry(QtCore.QRect(1270, 180, 200, 40))
        self.label_64.setStyleSheet('font:14pt')

        self.label_65 = QtWidgets.QLabel(self.page_6)  # 10
        self.label_65.setGeometry(QtCore.QRect(1400, 180, 200, 40))
        self.label_65.setStyleSheet('font:14pt')

        self.label_66 = QtWidgets.QLabel(self.page_6)
        self.label_66.setGeometry(QtCore.QRect(30, 440, 200, 40))
        self.label_66.setStyleSheet('font:14pt')

        self.vas_upperExtremityPain = QtWidgets.QLineEdit(self.page_6)
        self.vas_upperExtremityPain.setGeometry(QtCore.QRect(220, 440, 400, 40))
        self.vas_upperExtremityPain.setStyleSheet('font:14pt;background:white')

        self.label_67 = QtWidgets.QLabel(self.page_6)
        self.label_67.setGeometry(QtCore.QRect(700, 440, 200, 40))
        self.label_67.setStyleSheet('font:14pt')

        self.vas_result = QtWidgets.QComboBox(self.page_6)
        self.vas_result.setGeometry(QtCore.QRect(780, 440, 400, 40))
        self.vas_result.addItems(['', '轻度疼痛（1-3）', '中度疼痛（4-6）', '重度疼痛（7-10）'])
        self.vas_result.setStyleSheet('font:14pt;background:white')

        self.label_68 = QtWidgets.QLabel(self.page_6)
        self.label_68.setGeometry(QtCore.QRect(100, 540, 200, 40))
        self.label_68.setStyleSheet('font:14pt')

        self.vas_dateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.page_6)
        self.vas_dateEdit.setGeometry(QtCore.QRect(270, 540, 260, 40))
        self.vas_dateEdit.setStyleSheet("font:16pt;background:white")
        self.vas_dateEdit.setCalendarPopup(True)

        self.vas_saveButton = QtWidgets.QPushButton(self.page_6)
        self.vas_saveButton.setGeometry(QtCore.QRect(850, 540, 120, 40))
        self.vas_saveButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.vas_downLoadButton = QtWidgets.QPushButton(self.page_6)
        self.vas_downLoadButton.setGeometry(QtCore.QRect(990, 540, 120, 40))
        self.vas_downLoadButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")
        self.stackedWidget.addWidget(self.page_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.stackedWidget.setCurrentIndex(0)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基本功能评定"))
        self.label.setText(_translate("MainWindow", "基本功能评定"))
        self.label_2.setText(_translate("MainWindow", "  改良Ashworth分级"))
        self.label_3.setText(_translate("MainWindow", "  姓名:"))
        self.label_4.setText(_translate("MainWindow", "  性别:"))
        self.label_5.setText(_translate("MainWindow", "  年龄:"))
        self.label_6.setText(_translate("MainWindow", "  患手:"))
        self.Ashworth_saveButton.setText(_translate("MainWindow", "保存"))
        item = self.Ashworth_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "级别"))
        item = self.Ashworth_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "评定标准"))
        self.label_7.setText(_translate("MainWindow", "患侧肘部伸肌评定结果:"))
        self.label_8.setText(_translate("MainWindow", "患侧肘部屈肌评定结果:"))
        self.label_9.setText(_translate("MainWindow", " 患侧腕部伸肌评定结果:"))
        self.label_10.setText(_translate("MainWindow", " 患侧腕部屈肌评定结果:"))
        self.label_11.setText(_translate("MainWindow", "  评定日期:"))
        self.label_12.setText(_translate("MainWindow", "MMT肌力分级标准"))
        self.label_13.setText(_translate("MainWindow", "  姓名:"))
        self.label_14.setText(_translate("MainWindow", "  性别:"))
        self.label_15.setText(_translate("MainWindow", "  年龄:"))
        self.label_16.setText(_translate("MainWindow", "  患手:"))
        self.muscleStrength_saveButton.setText(_translate("MainWindow", "保存"))
        item = self.muscleStrength_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "级别"))
        item = self.muscleStrength_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "标准"))
        item = self.muscleStrength_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "相当于正常肌力%"))
        self.label_17.setText(_translate("MainWindow", "肩关节屈曲肌力（健侧/患侧）:"))
        self.label_18.setText(_translate("MainWindow", "肩关节伸展肌力（健侧/患侧）:"))
        self.label_19.setText(_translate("MainWindow", "肘关节屈曲肌力（健侧/患侧）:"))
        self.label_20.setText(_translate("MainWindow", "肘关节伸展肌力（健侧/患侧）:"))
        self.label_21.setText(_translate("MainWindow", "腕关节屈曲肌力（健侧/患侧）:"))
        self.label_22.setText(_translate("MainWindow", "腕关节伸展肌力（健侧/患侧）:"))
        self.label_23.setText(_translate("MainWindow", "握力（健侧/患侧）:"))
        self.label_24.setText(_translate("MainWindow", "捏力（健侧/患侧）:"))
        self.label_25.setText(_translate("MainWindow", "  评定日期:"))
        self.label_26.setText(_translate("MainWindow", "运动功能状态量表"))
        self.label_27.setText(_translate("MainWindow", "姓名:"))
        self.MSS_name.setText(_translate("MainWindow", "--"))
        self.label_28.setText(_translate("MainWindow", "性别:"))
        self.MSS_sex.setText(_translate("MainWindow", "--"))
        self.label_29.setText(_translate("MainWindow", "年龄:"))
        self.MSS_age.setText(_translate("MainWindow", "--"))
        self.label_30.setText(_translate("MainWindow", "患手:"))
        self.MSS_hand.setText(_translate("MainWindow", "--"))
        item = self.MSS_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "评估内容"))
        item = self.MSS_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "评分"))
        self.label_31.setText(_translate("MainWindow", "评定日期:"))
        self.MSS_saveButton.setText(_translate("MainWindow", "保存"))
        self.MSS_downLoadButton.setText(_translate("MainWindow", "导出"))
        self.label_32.setText(_translate("MainWindow", "Brunnstrom脑卒中运动功能分级"))
        self.label_33.setText(_translate("MainWindow", "姓名:"))
        self.Brunnstrom_name.setText(_translate("MainWindow", "--"))
        self.label_34.setText(_translate("MainWindow", "性别:"))
        self.Brunnstrom_sex.setText(_translate("MainWindow", "--"))
        self.label_35.setText(_translate("MainWindow", "年龄:"))
        self.Brunnstrom_age.setText(_translate("MainWindow", "--"))
        self.label_36.setText(_translate("MainWindow", "患手:"))
        self.Brunnstrom_hand.setText(_translate("MainWindow", "--"))
        item = self.Brunnstrom_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "阶段"))
        item = self.Brunnstrom_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "上肢功能评价标准"))
        item = self.Brunnstrom_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "手功能评价标准"))
        self.label_37.setText(_translate("MainWindow", "手功能:"))
        self.label_38.setText(_translate("MainWindow", "上肢功能:"))
        self.label_39.setText(_translate("MainWindow", "评定日期:"))
        self.Brunnstrom_saveButton.setText(_translate("MainWindow", "保存"))
        self.Brunnstrom_downLoadButton.setText(_translate("MainWindow", "导出"))
        self.label_40.setText(_translate("MainWindow", "中国人利手量表"))
        self.label_41.setText(_translate("MainWindow", "姓名:"))
        self.HandednessInventory_name.setText(_translate("MainWindow", "--"))
        self.label_42.setText(_translate("MainWindow", "性别:"))
        self.HandednessInventory_sex.setText(_translate("MainWindow", "--"))
        self.label_43.setText(_translate("MainWindow", "年龄:"))
        self.HandednessInventory_age.setText(_translate("MainWindow", "--"))
        self.label_44.setText(_translate("MainWindow", "患手:"))
        self.HandednessInventory_hand.setText(_translate("MainWindow", "--"))
        item = self.HandednessInventory_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "检查项目"))
        item = self.HandednessInventory_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "左手"))
        item = self.HandednessInventory_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "右手"))
        self.label_45.setText(_translate("MainWindow", "结论:"))
        self.label_46.setText(_translate("MainWindow", "评定日期:"))
        self.HandednessInventory_saveButton.setText(_translate("MainWindow", "保存"))
        self.HandednessInventory_downLoadButton.setText(_translate("MainWindow", "导出"))
        # self.label_47.setText(_translate("MainWindow","PS：评定项目、分型标准共有10个问题，如果十个项目都习用右手或左手，则称为强右利或强左利。如果前六项都习用右手或左手，后四项中任何一至四项用另一手，则称为右利或左利。如果前六项中，有一至五项习用一手，其余则习用另一手，则称为混合利。在混合利中如发执笔为标准，则右手称执笔混合利偏右，左手执笔称混合利偏左。据此，利手可细分为六种：强右利、右利、混合利偏右、混合利偏左、左利、强左利。"))
        self.label_48.setText(_translate("MainWindow", "VAS疼痛视觉模拟"))
        self.label_49.setText(_translate("MainWindow", "姓名:"))
        self.vas_name.setText(_translate("MainWindow", "--"))
        self.label_50.setText(_translate("MainWindow", "性别:"))
        self.vas_sex.setText(_translate("MainWindow", "--"))
        self.label_51.setText(_translate("MainWindow", "年龄:"))
        self.vas_age.setText(_translate("MainWindow", "--"))
        self.label_52.setText(_translate("MainWindow", "患手:"))
        self.vas_hand.setText(_translate("MainWindow", "--"))
        self.label_53.setText(_translate("MainWindow", "无痛"))
        self.label_54.setText(_translate("MainWindow", "剧痛"))
        self.label_55.setText(_translate("MainWindow", "0"))
        self.label_56.setText(_translate("MainWindow", "1"))
        self.label_57.setText(_translate("MainWindow", "2"))
        self.label_58.setText(_translate("MainWindow", "3"))
        self.label_58.setText(_translate("MainWindow", "4"))
        self.label_60.setText(_translate("MainWindow", "5"))
        self.label_61.setText(_translate("MainWindow", "6"))
        self.label_62.setText(_translate("MainWindow", "7"))
        self.label_63.setText(_translate("MainWindow", "8"))
        self.label_64.setText(_translate("MainWindow", "9"))
        self.label_65.setText(_translate("MainWindow", "10"))
        self.label_66.setText(_translate("MainWindow", "上肢疼痛部位:"))
        self.label_67.setText(_translate("MainWindow", "结果:"))
        self.label_68.setText(_translate("MainWindow", "评定日期:"))
        self.vas_saveButton.setText(_translate("MainWindow", "保存"))
        self.vas_downLoadButton.setText(_translate("MainWindow", "导出"))


class BasicFunctionAssessment(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, patient_id):
        super(BasicFunctionAssessment, self).__init__()
        self.setupUi(self)

        self.patient_id = patient_id

        self.patientInfo = \
            json.loads(requests.post(config.patientGetById, data={'id': self.patient_id}).content.decode('utf-8'))[
                'data']

        self.Ashworth_nameLabel.setText(self.patientInfo['name'])
        self.Ashworth_ageLabel.setText(str(self.patientInfo['age']))
        self.Ashworth_sexLabel.setText(self.patientInfo['sex'])
        self.Ashworth_unhealthyHandLabel.setText(self.patientInfo['illness'])

        self.muscleStrength_nameLabel.setText(self.patientInfo['name'])
        self.muscleStrength_ageLabel.setText(str(self.patientInfo['age']))
        self.muscleStrength_sexLabel.setText(self.patientInfo['sex'])
        self.muscleStrength_unhealthyHandLabel.setText(self.patientInfo['illness'])

        self.MSS_name.setText(self.patientInfo['name'])
        self.MSS_age.setText(str(self.patientInfo['age']))
        self.MSS_sex.setText(self.patientInfo['sex'])
        self.MSS_hand.setText(self.patientInfo['illness'])

        self.Brunnstrom_name.setText(self.patientInfo['name'])
        self.Brunnstrom_age.setText(str(self.patientInfo['age']))
        self.Brunnstrom_sex.setText(self.patientInfo['sex'])
        self.Brunnstrom_hand.setText(self.patientInfo['illness'])

        self.HandednessInventory_name.setText(self.patientInfo['name'])
        self.HandednessInventory_age.setText(str(self.patientInfo['age']))
        self.HandednessInventory_sex.setText(self.patientInfo['sex'])
        self.HandednessInventory_hand.setText(self.patientInfo['illness'])

        self.vas_name.setText(self.patientInfo['name'])
        self.vas_age.setText(str(self.patientInfo['age']))
        self.vas_sex.setText(self.patientInfo['sex'])
        self.vas_hand.setText(self.patientInfo['illness'])

        self.totalComBox.currentIndexChanged.connect(self.totalComBoxClick)
        self.Ashworth_saveButton.clicked.connect(self.Ashworth_saveButtonClick)
        self.Ashworth_downLoadButton.clicked.connect(self.Ashworth_downLoadButtonClick)
        self.muscleStrength_saveButton.clicked.connect(self.muscleStrength_saveButtonClick)
        self.muscleStrength_uploadButton.clicked.connect(self.muscleStrength_uploadButtonClick)
        self.MSS_saveButton.clicked.connect(self.MSS_saveButtonClick)
        self.MSS_downLoadButton.clicked.connect(self.MSS_downLoadButtonClick)
        self.Brunnstrom_saveButton.clicked.connect(self.Brunnstrom_saveButtonClick)
        self.Brunnstrom_downLoadButton.clicked.connect(self.Brunnstrom_downLoadButtonClick)
        self.HandednessInventory_saveButton.clicked.connect(self.HandednessInventory_saveButtonClick)
        self.HandednessInventory_downLoadButton.clicked.connect(self.HandednessInventory_downLoadButtonClick)
        self.vas_saveButton.clicked.connect(self.vas_saveButtonClick)
        self.vas_downLoadButton.clicked.connect(self.vas_downLoadButtonClick)

    def totalComBoxClick(self, *args):
        if self.totalComBox.currentIndex() == 1:
            self.stackedWidget.setCurrentIndex(0)
        elif self.totalComBox.currentIndex() == 2:
            self.stackedWidget.setCurrentIndex(1)
        elif self.totalComBox.currentIndex() == 3:
            self.stackedWidget.setCurrentIndex(2)
        elif self.totalComBox.currentIndex() == 4:
            self.stackedWidget.setCurrentIndex(3)
        elif self.totalComBox.currentIndex() == 5:
            self.stackedWidget.setCurrentIndex(4)
        else:
            self.stackedWidget.setCurrentIndex(5)

    def Ashworth_saveButtonClick(self, *args):
        code_1 = self.Ashworth_elbowShenJicomboBox.currentText()
        code_2 = self.Ashworth_elbowQuJicomboBox.currentText()
        code_3 = self.Ashworth_wristShenJicomboBox.currentText()
        code_4 = self.Ashworth_wristQuJicomboBox.currentText()
        test_date = self.Ashworth_dateEdit.text().replace('/', '-')
        sheet = {'id': tool.Tools.getTimeStamp(), 'patient_id': self.patient_id, 'code_1': code_1, 'code_2': code_2,
                 'code_3': code_3, 'code_4': code_4, 'test_date': test_date}
        res = requests.post(config.ashworthInsert, data=sheet)
        QMessageBox.information(self, "保存", '保存成功', QMessageBox.Yes, QMessageBox.Yes)
        ...

    def Ashworth_downLoadButtonClick(self, *args):
        self.Ashworth_saveButton.hide()
        self.Ashworth_downLoadButton.hide()
        img = self.grab()
        self.Ashworth_saveButton.show()
        self.Ashworth_downLoadButton.show()
        path = QFileDialog.getExistingDirectory()
        img.save(
            f"{path}/{self.Ashworth_nameLabel.text()}_{self.Ashworth_dateEdit.text().replace('/', '-')}_{self.totalComBox.currentText()}.png")
        QMessageBox.information(self, "导出", '导出成功', QMessageBox.Yes, QMessageBox.Yes)
        ...

    def muscleStrength_saveButtonClick(self, *args):
        code_1 = self.muscleStrength_shoulderQucomboBox.currentText()
        code_2 = self.muscleStrength_shoulderShencomboBox.currentText()
        code_3 = self.muscleStrength_elbowQucomboBox.currentText()
        code_4 = self.muscleStrength_elbowShencomboBox.currentText()
        code_5 = self.muscleStrength_wristQuJicomboBox.currentText()
        code_6 = self.muscleStrength_wristShenJicomboBox.currentText()
        code_7 = self.muscleStrength_gripStrengthQuJicomboBox.currentText()
        code_8 = self.muscleStrength_gripStrengthShenJicomboBox.currentText()
        test_date = self.Ashworth_dateEdit.text().replace('/', '-')
        sheet = {'id': tool.Tools.getTimeStamp(), 'patient_id': self.patient_id, 'code_1': code_1, 'code_2': code_2,
                 'code_3': code_3, 'code_4': code_4, 'code_5': code_5, 'code_6': code_6,
                 'code_7': code_7, 'code_8': code_8, 'test_date': test_date}
        res = requests.post(config.muscleStrengthInsert, data=sheet)
        QMessageBox.information(self, "保存", '保存成功', QMessageBox.Yes, QMessageBox.Yes)
        ...

    def muscleStrength_uploadButtonClick(self, *args):
        self.muscleStrength_saveButton.hide()
        self.muscleStrength_uploadButton.hide()
        img = self.grab()
        self.muscleStrength_saveButton.show()
        self.muscleStrength_uploadButton.show()
        path = QFileDialog.getExistingDirectory()
        img.save(
            f"{path}/{self.muscleStrength_nameLabel.text()}_{self.muscleStrength_dateEdit.text().replace('/', '-')}_{self.totalComBox.currentText()}.png")
        QMessageBox.information(self, "导出", '导出成功', QMessageBox.Yes, QMessageBox.Yes)
        ...

    def MSS_saveButtonClick(self, *args):
        test_date = self.MSS_dateEdit.text().replace('/', '-')
        sheet = {'id': tool.Tools.getTimeStamp(), 'patient_id': self.patient_id, 'test_date': test_date}
        res = requests.post(config.ashworthInsert, data=sheet)
        QMessageBox.information(self, "保存", '保存成功', QMessageBox.Yes, QMessageBox.Yes)
        ...

    def MSS_downLoadButtonClick(self, *args):
        self.MSS_saveButton.hide()
        self.MSS_downLoadButton.hide()
        img = self.grab()
        self.MSS_saveButton.show()
        self.MSS_downLoadButton.show()
        path = QFileDialog.getExistingDirectory()
        img.save(f"{path}/{self.MSS_name.text()}_{self.MSS_dateEdit.text().replace('/', '-')}_{self.totalComBox.currentText()}.png")
        ...

    def Brunnstrom_saveButtonClick(self, *args):
        code_1 = self.Brunnstrom_handFunctionLineEdit.text()
        code_2 = self.Brunnstrom_upperLimbFunctionLineEdit.text()
        test_date = self.Brunnstrom_dateEdit.text().replace('/', '-')
        sheet = {'id': tool.Tools.getTimeStamp(), 'patient_id': self.patient_id, 'code_1': code_1, 'code_2': code_2,
                 'test_date': test_date}
        res = requests.post(config.muscleStrengthInsert, data=sheet)
        QMessageBox.information(self, "保存", '保存成功', QMessageBox.Yes, QMessageBox.Yes)
        ...

    def Brunnstrom_downLoadButtonClick(self, *args):
        self.Brunnstrom_saveButton.hide()
        self.Brunnstrom_downLoadButton.hide()
        img = self.grab()
        self.Brunnstrom_saveButton.show()
        self.Brunnstrom_downLoadButton.show()
        path = QFileDialog.getExistingDirectory()
        img.save(f"{path}/{self.Brunnstrom_name.text()}_{self.Brunnstrom_dateEdit.text().replace('/', '-')}_{self.totalComBox.currentText()}.png")
        ...

    def HandednessInventory_saveButtonClick(self, *args):
        code_1 = self.HandednessInventory_conclusionLineEdit.text()
        test_date = self.HandednessInventory_dateEdit.text().replace('/', '-')
        sheet = {'id': tool.Tools.getTimeStamp(), 'patient_id': self.patient_id, 'code_1': code_1,
                 'test_date': test_date}
        res = requests.post(config.ashworthInsert, data=sheet)
        QMessageBox.information(self, "保存", '保存成功', QMessageBox.Yes, QMessageBox.Yes)
        ...

    def HandednessInventory_downLoadButtonClick(self, *args):
        self.HandednessInventory_saveButton.hide()
        self.HandednessInventory_downLoadButton.hide()
        img = self.grab()
        self.HandednessInventory_saveButton.show()
        self.HandednessInventory_downLoadButton.show()
        path = QFileDialog.getExistingDirectory()
        img.save(f"{path}/{self.HandednessInventory_name.text()}_{self.HandednessInventory_dateEdit.text().replace('/', '-')}_{self.totalComBox.currentText()}.png")
        ...

    def vas_saveButtonClick(self, *args):
        code_1 = str(self.vas_s1.value())
        code_2 = self.vas_upperExtremityPain.text()
        code_3 = self.vas_result
        test_date = self.vas_dateEdit.text().replace("/", "-")
        sheet = {'id': tool.Tools.getTimeStamp(), 'patient_id': self.patient_id, 'code_1': code_1, 'code_2': code_2,
                 'code_3': code_3, 'test_date': test_date}
        res = requests.post(config.VASInsert, data=sheet)
        QMessageBox.information(self, "保存", '保存成功', QMessageBox.Yes, QMessageBox.Yes)
        ...

    def vas_downLoadButtonClick(self, *args):
        self.vas_saveButton.hide()
        self.vas_downLoadButton.hide()
        img = self.grab()
        self.vas_saveButton.show()
        self.vas_downLoadButton.show()
        path = QFileDialog.getExistingDirectory()
        img.save(
            f"{path}/{self.vas_name.text()}_{self.vas_dateEdit.text().replace('/', '-')}_{self.totalComBox.currentText()}.png")
        QMessageBox.information(self, "导出", '导出成功', QMessageBox.Yes, QMessageBox.Yes)
        ...


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = BasicFunctionAssessment(1)
    gui.show()
    sys.exit(app.exec_())
