# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import json
import sys

import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QMessageBox, QFileDialog

import config
import tool


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(1500, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.frame_sub = QtWidgets.QFrame(self.centralwidget)
        self.frame_sub.setGeometry(QtCore.QRect(0, 0, 1500, 1000))
        self.frame_sub.setStyleSheet("background-color:rgb(242, 249, 255)")
        self.frame_sub.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sub.setFrameShadow(QtWidgets.QFrame.Raised)

        self.label = QtWidgets.QLabel(self.frame_sub)
        self.label.setGeometry(QtCore.QRect(80, 60, 200, 40))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setStyleSheet('font:14pt')

        self.name = QtWidgets.QLabel(self.frame_sub)
        self.name.setGeometry(QtCore.QRect(160, 60, 200, 40))
        self.name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.name.setText('--')
        self.name.setStyleSheet('font:14pt')

        self.label_2 = QtWidgets.QLabel(self.frame_sub)
        self.label_2.setGeometry(QtCore.QRect(280, 60, 200, 40))
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setStyleSheet('font:14pt')

        self.gender = QtWidgets.QLabel(self.frame_sub)
        self.gender.setGeometry(QtCore.QRect(360, 60, 200, 40))
        self.gender.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gender.setText('--')
        self.gender.setStyleSheet('font:14pt')

        self.label_3 = QtWidgets.QLabel(self.frame_sub)
        self.label_3.setGeometry(QtCore.QRect(480, 60, 200, 40))
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setStyleSheet('font:14pt')

        self.age = QtWidgets.QLabel(self.frame_sub)
        self.age.setGeometry(QtCore.QRect(560, 60, 200, 40))
        self.age.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.age.setText('--')
        self.age.setStyleSheet('font:14pt')

        self.label_4 = QtWidgets.QLabel(self.frame_sub)
        self.label_4.setGeometry(QtCore.QRect(680, 60, 200, 40))
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setStyleSheet('font:14pt')

        self.hand = QtWidgets.QLabel(self.frame_sub)
        self.hand.setGeometry(QtCore.QRect(760, 60, 200, 40))
        self.hand.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.hand.setText('--')
        self.hand.setStyleSheet('font:14pt')

        self.title = QtWidgets.QLabel(self.frame_sub)
        self.title.setGeometry(QtCore.QRect(500, 10, 400, 41))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title.setStyleSheet('font:16pt')

        self.table = QtWidgets.QTableWidget(self.frame_sub)
        self.table.setGeometry(QtCore.QRect(20, 120, 1460, 700))
        self.table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table.setStyleSheet('background:white')
        self.table.setColumnCount(7)
        self.table.setRowCount(11)
        self.table.verticalHeader().setVisible(False)

        item = QtWidgets.QTableWidgetItem()  # 行
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setVerticalHeaderItem(0, item)
        self.table.setRowHeight(0, 60)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setVerticalHeaderItem(1, item)
        self.table.setRowHeight(1, 60)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setVerticalHeaderItem(2, item)
        self.table.setRowHeight(2, 60)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setVerticalHeaderItem(3, item)
        self.table.setRowHeight(3, 60)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(4, item)
        self.table.setRowHeight(4, 60)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(5, item)
        self.table.setRowHeight(5, 60)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(6, item)
        self.table.setRowHeight(6, 60)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(7, item)
        self.table.setRowHeight(7, 60)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(8, item)
        self.table.setRowHeight(8, 60)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(9, item)
        self.table.setRowHeight(9, 60)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(10, item)
        self.table.setRowHeight(10, 60)

        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)  # 列
        self.table.setColumnWidth(0, 208)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        self.table.setColumnWidth(1, 208)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        self.table.setColumnWidth(2, 208)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        self.table.setColumnWidth(3, 208)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        self.table.setColumnWidth(4, 208)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        self.table.setColumnWidth(5, 208)
        item = QtWidgets.QTableWidgetItem()
        self.table.setColumnWidth(6, 208)
        self.table.setHorizontalHeaderItem(6, item)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(0, 0, item)

        item = QtWidgets.QTableWidgetItem('0')
        item.setCheckState(Qt.Unchecked)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(0, 1, item)

        item = QtWidgets.QTableWidgetItem('2')
        item.setCheckState(Qt.Unchecked)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(0, 2, item)

        item = QtWidgets.QTableWidgetItem('5')
        item.setCheckState(Qt.Unchecked)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(0, 3, item)

        item = QtWidgets.QTableWidgetItem('8')
        item.setCheckState(Qt.Unchecked)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(0, 4, item)

        item = QtWidgets.QTableWidgetItem('10')
        item.setCheckState(Qt.Unchecked)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(0, 5, item)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(1, 0, item)

        item = QtWidgets.QTableWidgetItem('0')
        item.setCheckState(Qt.Unchecked)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(1, 1, item)

        item = QtWidgets.QTableWidgetItem('1')
        item.setCheckState(Qt.Unchecked)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(1, 2, item)

        item = QtWidgets.QTableWidgetItem('3')
        item.setCheckState(Qt.Unchecked)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(1, 3, item)

        item = QtWidgets.QTableWidgetItem('4')
        item.setCheckState(Qt.Unchecked)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(1, 4, item)

        item = QtWidgets.QTableWidgetItem('5')
        item.setCheckState(Qt.Unchecked)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(1, 5, item)

        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(2, 0, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        item = QtWidgets.QTableWidgetItem('0')
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(2, 1, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        item = QtWidgets.QTableWidgetItem('1')
        item.setCheckState(Qt.Unchecked)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(2, 2, item)

        item = QtWidgets.QTableWidgetItem('3')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(2, 3, item)

        item = QtWidgets.QTableWidgetItem('4')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(2, 4, item)

        item = QtWidgets.QTableWidgetItem('5')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(2, 5, item)

        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(3, 0, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        item = QtWidgets.QTableWidgetItem('0')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(3, 1, item)

        item = QtWidgets.QTableWidgetItem('2')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(3, 2, item)

        item = QtWidgets.QTableWidgetItem('5')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(3, 3, item)

        item = QtWidgets.QTableWidgetItem('8')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(3, 4, item)

        item = QtWidgets.QTableWidgetItem('10')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(3, 5, item)

        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(4, 0, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        item = QtWidgets.QTableWidgetItem('0')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(4, 1, item)

        item = QtWidgets.QTableWidgetItem('2')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(4, 2, item)

        item = QtWidgets.QTableWidgetItem('5')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(4, 3, item)

        item = QtWidgets.QTableWidgetItem('8')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(4, 4, item)

        item = QtWidgets.QTableWidgetItem('10')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(4, 5, item)

        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(5, 0, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        item = QtWidgets.QTableWidgetItem('0')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(5, 1, item)

        item = QtWidgets.QTableWidgetItem('2')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(5, 2, item)

        item = QtWidgets.QTableWidgetItem('5')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(5, 3, item)

        item = QtWidgets.QTableWidgetItem('8')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(5, 4, item)

        item = QtWidgets.QTableWidgetItem('10')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(5, 5, item)

        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(6, 0, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        item = QtWidgets.QTableWidgetItem('0')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(6, 1, item)

        item = QtWidgets.QTableWidgetItem('2')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(6, 2, item)

        item = QtWidgets.QTableWidgetItem('5')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(6, 3, item)

        item = QtWidgets.QTableWidgetItem('8')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(6, 4, item)

        item = QtWidgets.QTableWidgetItem('10')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(6, 5, item)

        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(7, 0, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        item = QtWidgets.QTableWidgetItem('0')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(7, 1, item)

        item = QtWidgets.QTableWidgetItem('3')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(7, 2, item)

        item = QtWidgets.QTableWidgetItem('8')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(7, 3, item)

        item = QtWidgets.QTableWidgetItem('12')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(7, 4, item)

        item = QtWidgets.QTableWidgetItem('15')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(7, 5, item)

        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(8, 0, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        item = QtWidgets.QTableWidgetItem('0')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(8, 1, item)

        item = QtWidgets.QTableWidgetItem('3')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(8, 2, item)

        item = QtWidgets.QTableWidgetItem('8')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(8, 3, item)

        item = QtWidgets.QTableWidgetItem('12')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(8, 4, item)

        item = QtWidgets.QTableWidgetItem('15')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(8, 5, item)

        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(9, 0, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        item = QtWidgets.QTableWidgetItem('0')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(9, 1, item)

        item = QtWidgets.QTableWidgetItem('1')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(9, 2, item)

        item = QtWidgets.QTableWidgetItem('3')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(9, 3, item)

        item = QtWidgets.QTableWidgetItem('4')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(9, 4, item)

        item = QtWidgets.QTableWidgetItem('5')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(9, 5, item)

        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(10, 0, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        item = QtWidgets.QTableWidgetItem('0')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(10, 1, item)

        item = QtWidgets.QTableWidgetItem('2')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(10, 2, item)

        item = QtWidgets.QTableWidgetItem('5')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(10, 3, item)

        item = QtWidgets.QTableWidgetItem('8')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(10, 4, item)

        item = QtWidgets.QTableWidgetItem('10')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setCheckState(Qt.Unchecked)
        self.table.setItem(10, 5, item)

        self.label_5 = QtWidgets.QLabel(self.frame_sub)
        self.label_5.setGeometry(QtCore.QRect(10, 820, 500, 40))
        self.label_5.setText('注：*表示仅在不能行走时才评定此项')
        self.label_5.setStyleSheet("font:12pt")

        self.label_6 = QtWidgets.QLabel(self.frame_sub)
        self.label_6.setGeometry(QtCore.QRect(40, 870, 500, 40))
        self.label_6.setStyleSheet("font:14pt")

        self.totalscore = QtWidgets.QLabel(self.frame_sub)
        self.totalscore.setGeometry(QtCore.QRect(120, 870, 200, 40))
        self.totalscore.setText('--')
        self.totalscore.setStyleSheet("font:14pt")

        self.label_8 = QtWidgets.QLabel(self.frame_sub)
        self.label_8.setGeometry(QtCore.QRect(600, 870, 500, 40))
        self.label_8.setStyleSheet("font:14pt")

        self.result = QtWidgets.QComboBox(self.frame_sub)
        self.result.setGeometry(QtCore.QRect(740, 870, 600, 40))
        self.result.addItems(
            ['', '正常100分', '≥60分，生活基本自理', '41-59分，中度功能障碍，生活需要帮助', '21-40分，重度功能障碍，生活依赖明显', '≤20分， 生活完全依赖'])
        self.result.setStyleSheet("font:14pt;background:white")

        self.label_7 = QtWidgets.QLabel(self.frame_sub)
        self.label_7.setGeometry(QtCore.QRect(40, 920, 500, 40))
        self.label_7.setText('评定日期:')
        self.label_7.setStyleSheet("font:14pt")

        self.dateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.frame_sub)
        self.dateEdit.setGeometry(QtCore.QRect(180, 920, 200, 40))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setStyleSheet("font:14pt;background:white")

        self.save = QtWidgets.QPushButton(self.frame_sub)
        self.save.setGeometry(QtCore.QRect(400, 920, 120, 40))
        self.save.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.download = QtWidgets.QPushButton(self.frame_sub)
        self.download.setGeometry(QtCore.QRect(540, 920, 120, 40))
        self.download.setText('导出')
        self.download.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "改良Barthel指数（MBI）"))
        self.save.setText(_translate("MainWindow", "保存"))
        self.label_6.setText(_translate("MainWindow", "总分:"))
        self.label_8.setText(_translate("MainWindow", "评定结果:"))
        self.label.setText(_translate("MainWindow", "姓名:"))
        self.label_2.setText(_translate("MainWindow", "性别:"))
        self.label_3.setText(_translate("MainWindow", "年龄:"))
        self.label_4.setText(_translate("MainWindow", "患手:"))
        self.title.setText(_translate("MainWindow", "改良Barthel指数（MBI）"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ADL项目"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "完全依赖1级"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "最大帮助2级"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "中等帮助3级"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "最小帮助4级"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "完全独立5级"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "得分"))
        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        item = self.table.item(0, 0)
        item.setText(_translate("MainWindow", "进   食"))
        item = self.table.item(1, 0)
        item.setText(_translate("MainWindow", "洗   澡"))
        item = self.table.item(2, 0)
        item.setText(_translate("MainWindow", "个人卫生"))
        item = self.table.item(3, 0)
        item.setText(_translate("MainWindow", "穿   衣"))
        item = self.table.item(4, 0)
        item.setText(_translate("MainWindow", "大便控制"))
        item = self.table.item(5, 0)
        item.setText(_translate("MainWindow", "小便控制"))
        item = self.table.item(6, 0)
        item.setText(_translate("MainWindow", "用   厕"))
        item = self.table.item(7, 0)
        item.setText(_translate("MainWindow", "床椅转移"))
        item = self.table.item(8, 0)
        item.setText(_translate("MainWindow", "平地行走"))
        item = self.table.item(9, 0)
        item.setText(_translate("MainWindow", "坐轮椅*"))
        item = self.table.item(10, 0)
        item.setText(_translate("MainWindow", "上下楼梯"))

        self.table.setSortingEnabled(__sortingEnabled)


class MBI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,patient_id):
        super(MBI, self).__init__()
        self.setupUi(self)
        self.patient_id = patient_id

        self.patientInfo = \
            json.loads(requests.post(config.patientGetById, data={'id': self.patient_id}).content.decode('utf-8'))[
                'data']
        self.name.setText(self.patientInfo['name'])
        self.age.setText(str(self.patientInfo['age']))
        self.gender.setText(self.patientInfo['sex'])
        self.hand.setText(self.patientInfo['illness'])
        self.save.clicked.connect(self.saveButtonClick)
        self.download.clicked.connect(self.downloadButtonClick)

    def saveButtonClick(self, *args):
        code_1 = self.totalscore.text()
        code_2 = self.result.currentText()
        test_date = self.dateEdit.text().replace('/', '-')
        sheet = {'id': tool.Tools.getTimeStamp(), 'patient_id': self.patient_id, 'code_1': code_1, 'code_2': code_2, 'test_date': test_date}
        res = requests.post(config.ashworthInsert, data=sheet)
        QMessageBox.information(self, "保存", '保存成功', QMessageBox.Yes, QMessageBox.Yes)
        ...

    def downloadButtonClick(self, *args):
        self.save.hide()
        self.download.hide()
        img = self.grab()
        self.save.show()
        self.download.show()
        path = QFileDialog.getExistingDirectory()
        img.save(f"{path}/{self.name.text()}_{self.dateEdit.text().replace('/', '-')}.png")
        ...


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = MBI()
    gui.show()
    sys.exit(app.exec_())