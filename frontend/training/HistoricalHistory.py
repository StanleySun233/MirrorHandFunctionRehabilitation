# -*- coding: utf-8 -*-
import json
# Form implementation generated from reading ui file '系统设置.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QTableWidget, QHeaderView, QAbstractItemView, QTableWidgetItem

import config


# from SetSystemSpaceImageAddButtonInterface import setSystemSpaceImageAddButtonInterface
# from SetSystemSpaceImageEditDataInterface import setSystemSpaceImageEditDataInterface
# from SetSystemSpaceImageDeleteButtonInterface import setSystemSpaceImageDeleteButtonInterface


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background:rgb(242,249,255)")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 371, 60))
        self.label.setStyleSheet("font:14pt")

        self.traingMode = QtWidgets.QComboBox(self.centralwidget)
        self.traingMode.setGeometry(QtCore.QRect(150, 20, 270, 40))
        self.traingMode.addItems(['', '感觉运动训练', '基本功能训练', '功能动作训练', '自主镜像训练'])
        self.traingMode.setStyleSheet("font:14pt;background:white")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 10, 371, 60))
        self.label_2.setStyleSheet("font:14pt")

        self.savaData = QtWidgets.QDateEdit(QDate.currentDate(), self.centralwidget)
        self.savaData.setGeometry(QtCore.QRect(580, 20, 200, 40))
        self.savaData.setStyleSheet("font:14pt;background:white")
        self.savaData.setCalendarPopup(True)

        self.inquireButton = QtWidgets.QPushButton(self.centralwidget)
        self.inquireButton.setGeometry(QtCore.QRect(800, 20, 120, 40))
        self.inquireButton.setStyleSheet("font:14pt;color:white;background:rgb(0,138,200)")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 100, 1880, 910))
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(19)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.setColumnWidth(0, 420)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(1, 550)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.setColumnWidth(2, 900)
        self.tableWidget.setSelectionBehavior(QHeaderView.SelectRows)
        self.tableWidget.setSelectionMode(QTableWidget.SingleSelection)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "历史记录"))
        self.label.setText(_translate("MainWindow", "训练模式:"))
        self.label_2.setText(_translate("MainWindow", "保存日期:"))
        self.inquireButton.setText(_translate("MainWindow", "查询"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "日期"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "训练模式"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "视频内容"))
        self.inquireButton.clicked.connect(self.refreshTable)


class HistoricalHistory(QtWidgets.QMainWindow, Ui_MainWindow):  # 基本功能动作训练
    def __init__(self, patient_id):
        super(HistoricalHistory, self).__init__()
        self.setupUi(self)
        self.patient_id = patient_id

    def refreshTable(self, *args):
        self.trainInfo = requests.post(config.trainInfoListByIdAndTrain,
                                       data={"train": self.traingMode.currentText(),
                                             "id": self.patient_id,
                                             "save_date": self.savaData.text().replace("/", "-")}).content.decode(
            'utf-8')
        self.trainInfo = json.loads(self.trainInfo)["data"]
        self.tableWidget.setRowCount(max(10, len(self.trainInfo)))
        for i in range(1000):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(""))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(""))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(""))
        for i in range(len(self.trainInfo)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(self.trainInfo[i]['save_date']))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(self.trainInfo[i]['train']))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(self.trainInfo[i]['detail']))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = HistoricalHistory("1")
    gui.show()
    sys.exit(app.exec_())
