# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '19uipy.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import json
import sys
import tool

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QMessageBox, QFileDialog

import config


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(1500, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet('background-color:rgb(242, 249, 255)')

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(400, 10, 800, 41))
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
        self.table.setGeometry(QtCore.QRect(20, 120, 1460, 410))
        self.table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table.setStyleSheet('background:white;font:14pt')
        self.table.setColumnCount(6)
        self.table.setRowCount(5)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)

        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)  # ???
        self.table.setColumnWidth(0, 243)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)  # ???
        self.table.setColumnWidth(1, 270)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        self.table.setColumnWidth(2, 260)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        self.table.setColumnWidth(3, 260)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        self.table.setColumnWidth(4, 270)

        item = QtWidgets.QTableWidgetItem('??????????????????Nine Hole Peg Test???')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(0, 0, item)
        self.table.setSpan(0, 0, 1, 6)
        self.table.setRowHeight(0, 80)

        item = QtWidgets.QTableWidgetItem('?????????')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(1, 0, item)
        self.table.setSpan(1, 0, 1, 3)
        self.table.setRowHeight(1, 80)
        self.table.setSpan(1, 3, 1, 3)

        self.handComBox1 = QtWidgets.QComboBox(self.centralwidget)
        self.handComBox1.addItems(['', '???', '???'])
        self.handComBox1.setStyleSheet('font:14pt')

        item = QtWidgets.QTableWidgetItem('????????????????????????')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(2, 0, item)
        self.table.setSpan(2, 0, 1, 2)
        self.table.setRowHeight(2, 80)
        self.table.setCellWidget(2, 2, self.handComBox1)

        self.handComBox2 = QtWidgets.QComboBox(self.centralwidget)
        self.handComBox2.addItems(['', '???', '???'])
        self.handComBox2.setStyleSheet('font:14pt')

        item = QtWidgets.QTableWidgetItem('????????????')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(2, 3, item)
        self.table.setSpan(2, 3, 1, 2)
        self.table.setCellWidget(2, 5, self.handComBox2)

        item = QtWidgets.QTableWidgetItem('??????????????????????????????')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(3, 0, item)
        self.table.setRowHeight(3, 80)
        self.table.setSpan(3, 0, 1, 3)
        self.table.setSpan(3, 3, 1, 3)

        self.dateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.centralwidget)
        self.dateEdit.setStyleSheet("font:16pt;background:white")
        self.dateEdit.setCalendarPopup(True)

        item = QtWidgets.QTableWidgetItem('?????????')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(4, 0, item)
        self.table.setRowHeight(4, 80)
        self.table.setCellWidget(4, 1, self.dateEdit)

        self.handComBox3 = QtWidgets.QComboBox(self.centralwidget)
        self.handComBox3.addItems(['', '???', '???'])
        self.handComBox3.setStyleSheet('font:14pt')

        item = QtWidgets.QTableWidgetItem('????????????')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(4, 2, item)
        self.table.setCellWidget(4, 3, self.handComBox3)

        self.handComBox4 = QtWidgets.QComboBox(self.centralwidget)
        self.handComBox4.addItems(['', '???', '???'])
        self.handComBox4.setStyleSheet('font:14pt')

        item = QtWidgets.QTableWidgetItem('????????????')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(4, 4, item)
        self.table.setCellWidget(4, 5, self.handComBox4)

        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(450, 600, 150, 40))
        self.saveButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.downLoadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downLoadButton.setGeometry(QtCore.QRect(630, 600, 150, 40))
        self.downLoadButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "??????????????????Nine Hole Peg Test???"))
        self.title.setText(_translate("MainWindow", "??????????????????Nine Hole Peg Test???"))
        self.label.setText(_translate("MainWindow", "??????:"))
        self.name.setText(_translate("MainWindow", "--"))
        self.label_2.setText(_translate("MainWindow", "??????:"))
        self.gender.setText(_translate("MainWindow", "--"))
        self.label_3.setText(_translate("MainWindow", "??????:"))
        self.age.setText(_translate("MainWindow", "--"))
        self.label_4.setText(_translate("MainWindow", "??????:"))
        self.hand.setText(_translate("MainWindow", "--"))
        self.saveButton.setText(_translate("MainWindow", "??????"))
        self.downLoadButton.setText(_translate("MainWindow", "??????"))

class NineHolePegTest(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,patient_id):
        super(NineHolePegTest, self).__init__()
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
        code_1 = self.handComBox1.currentText()
        code_2 = self.handComBox2.currentText()
        code_3 = self.handComBox3.currentText()
        code_4 = self.handComBox4.currentText()
        test_date = self.dateEdit.text().replace('/', '-')
        sheet = {'id': tool.Tools.getTimeStamp(), 'patient_id': self.patient_id, 'code_1': code_1, 'code_2': code_2,
                 'code_3': code_3, 'code_4': code_4, 'test_date': test_date}
        res = requests.post(config.ashworthInsert, data=sheet)
        QMessageBox.information(self, "??????", '????????????', QMessageBox.Yes, QMessageBox.Yes)
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
    gui = NineHolePegTest()
    gui.show()
    sys.exit(app.exec_())



