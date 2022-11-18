# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '10.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import json
import sys

import requests
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QFileDialog, QMessageBox

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

        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(20, 120, 1460, 590))
        self.table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table.setStyleSheet('background:white;font:12pt')
        self.table.setColumnCount(3)
        self.table.setRowCount(12)
        self.table.verticalHeader().setVisible(False)

        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)  # 列
        self.table.setColumnWidth(0, 400)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        self.table.setColumnWidth(1, 560)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        self.table.setColumnWidth(2, 500)

        item = QtWidgets.QTableWidgetItem('执笔')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(0, 0, item)

        item = QtWidgets.QTableWidgetItem('执筷')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(1, 0, item)

        item = QtWidgets.QTableWidgetItem('掷东西')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(2, 0, item)

        item = QtWidgets.QTableWidgetItem('持牙刷刷牙')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(3, 0, item)

        item = QtWidgets.QTableWidgetItem('持剪刀')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(4, 0, item)

        item = QtWidgets.QTableWidgetItem('划火柴')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(5, 0, item)

        item = QtWidgets.QTableWidgetItem('持线穿针')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(6, 0, item)

        item = QtWidgets.QTableWidgetItem('握钉锤')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(7, 0, item)

        item = QtWidgets.QTableWidgetItem('执笔')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(8, 0, item)

        item = QtWidgets.QTableWidgetItem('握球拍')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(9, 0, item)

        item = QtWidgets.QTableWidgetItem('持毛巾洗脸')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(10, 0, item)

        item = QtWidgets.QTableWidgetItem('结论')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(11, 0, item)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 660, 1460, 100))
        self.label_5.setStyleSheet("font:14pt")

        self.conclusionLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.conclusionLineEdit.setGeometry(QtCore.QRect(120, 690, 1200, 40))
        self.conclusionLineEdit.setStyleSheet("font:14pt;background:white")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 760, 260, 40))
        self.label_6.setStyleSheet("font:14pt")

        self.dateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(170, 760, 260, 40))
        self.dateEdit.setStyleSheet("font:16pt;background:white")
        self.dateEdit.setCalendarPopup(True)

        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(450, 760, 120, 40))
        self.saveButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.downLoadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downLoadButton.setGeometry(QtCore.QRect(590,760, 120, 40))
        self.downLoadButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 810, 1460, 220))
        self.label_7.setStyleSheet("font:14pt")
        self.label_7.setWordWrap(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "利手调查量表"))
        self.title.setText(_translate("MainWindow", "中国人利手量表"))
        self.label.setText(_translate("MainWindow", "姓名:"))
        self.name.setText(_translate("MainWindow", "--"))
        self.label_2.setText(_translate("MainWindow", "性别:"))
        self.gender.setText(_translate("MainWindow", "--"))
        self.label_3.setText(_translate("MainWindow", "年龄:"))
        self.age.setText(_translate("MainWindow", "--"))
        self.label_4.setText(_translate("MainWindow", "患手:"))
        self.hand.setText(_translate("MainWindow", "--"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "检查项目"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "左手"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "右手"))
        self.label_5.setText(_translate("MainWindow", "结论:"))
        self.label_6.setText(_translate("MainWindow", "评定日期:"))
        self.saveButton.setText(_translate("MainWindow", "保存"))
        self.downLoadButton.setText(_translate("MainWindow", "导出"))
        self.label_7.setText(_translate("MainWindow", "PS：评定项目、分型标准共有10个问题，如果十个项目都习用右手或左手，则称为强右利或强左利。如果前六项都习用右手或左手，后四项中任何一至四项用另一手，则称为右利或左利。如果前六项中，有一至五项习用一手，其余则习用另一手，则称为混合利。在混合利中如发执笔为标准，则右手称执笔混合利偏右，左手执笔称混合利偏左。据此，利手可细分为六种：强右利、右利、混合利偏右、混合利偏左、左利、强左利。"))


class HandednessInventory(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, patient_id):
        super(HandednessInventory, self).__init__()
        self.setupUi(self)
        self.patient_id = patient_id

        self.patientInfo = \
            json.loads(requests.post(config.patientGetById, data={'id': self.patient_id}).content.decode('utf-8'))[
                'data']

        self.name.setText(self.patientInfo['name'])
        self.age.setText(str(self.patientInfo['age']))
        self.gender.setText(self.patientInfo['sex'])
        self.hand.setText(self.patientInfo['illness'])

        self.saveButton.clicked.connect(self.saveButtonClick)
        self.downLoadButton.clicked.connect(self.downLoadButtonClick)
    #
    def saveButtonClick(self, *args):
        code_1 = self.conclusionLineEdit.text()
        test_date = self.dateEdit.text().replace('/', '-')
        sheet = {'id': tool.Tools.getTimeStamp(), 'patient_id': self.patient_id, 'code_1': code_1,  'test_date': test_date}
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
    gui = HandednessInventory()
    gui.show()
    sys.exit(app.exec_())