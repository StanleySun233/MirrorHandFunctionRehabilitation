# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '25uipy.ui'
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

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(830,60, 260, 40))
        self.label_6.setStyleSheet("font:14pt")

        self.dateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(950, 60, 200, 40))
        self.dateEdit.setStyleSheet("font:14pt;background:white")
        self.dateEdit.setCalendarPopup(True)

        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(1170, 60, 120, 40))
        self.saveButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.downLoadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downLoadButton.setGeometry(QtCore.QRect(1320, 60, 120, 40))
        self.downLoadButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(20, 120, 1460, 350))
        self.table.setStyleSheet('background:white;font:14pt')
        self.table.setColumnCount(5)
        self.table.setRowCount(22)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)

        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)  # 列
        self.table.setColumnWidth(0, 220)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        self.table.setColumnWidth(1, 280)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        self.table.setColumnWidth(2, 208)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        self.table.setColumnWidth(3, 408)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        self.table.setColumnWidth(4, 308)

        item = QtWidgets.QTableWidgetItem('项目')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(0, 0, item)
        self.table.setSpan(0,0,1,4)
        item = QtWidgets.QTableWidgetItem('得分')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(0, 4, item)

        item = QtWidgets.QTableWidgetItem('运动功能')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(1, 0, item)
        self.table.setSpan(1, 0, 14, 1)
        item = QtWidgets.QTableWidgetItem('自理能力')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(1, 1, item)
        self.table.setSpan(1,1, 6, 1)
        item = QtWidgets.QTableWidgetItem('1')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem('2')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem('3')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem('4')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem('5')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem('6')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem('进食')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem('梳洗修饰')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem('洗澡')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem('穿裤子')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem('穿上衣')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem('上厕所')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem('括约肌控制')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(7, 1, item)
        self.table.setSpan(7, 1, 2, 1)
        item = QtWidgets.QTableWidgetItem('7')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem('8')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem('膀胱管理')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(7, 3, item)
        item = QtWidgets.QTableWidgetItem('直肠管理')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(8, 3, item)
        item = QtWidgets.QTableWidgetItem('转移')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(9, 1, item)
        self.table.setSpan(9, 1, 3, 1)
        item = QtWidgets.QTableWidgetItem('9')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(9, 2, item)
        item = QtWidgets.QTableWidgetItem('10')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(10, 2, item)
        item = QtWidgets.QTableWidgetItem('11')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(11, 2, item)
        item = QtWidgets.QTableWidgetItem('床、椅、轮椅间')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(9, 3, item)
        item = QtWidgets.QTableWidgetItem('入厕')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(10, 3, item)
        item = QtWidgets.QTableWidgetItem('盆浴或淋浴')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(11, 3, item)
        item = QtWidgets.QTableWidgetItem('行走')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(12, 1, item)
        self.table.setSpan(12, 1, 2, 1)
        item = QtWidgets.QTableWidgetItem('12')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(12, 2, item)
        item = QtWidgets.QTableWidgetItem('13')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(13, 2, item)
        item = QtWidgets.QTableWidgetItem('步行/轮椅')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(12, 3, item)
        item = QtWidgets.QTableWidgetItem('上下楼梯')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(13, 3, item)
        item = QtWidgets.QTableWidgetItem('运动功能评分')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(14, 1, item)
        self.table.setSpan(14, 1, 1, 3)

        item = QtWidgets.QTableWidgetItem('认知功能')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(15, 0, item)
        self.table.setSpan(15, 0, 6,1)
        item = QtWidgets.QTableWidgetItem('交流')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(15, 1, item)
        self.table.setSpan(15, 1, 2, 1)
        item = QtWidgets.QTableWidgetItem('14')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(15, 2, item)
        item = QtWidgets.QTableWidgetItem('15')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(16, 2, item)
        item = QtWidgets.QTableWidgetItem('理解')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(15, 3, item)
        item = QtWidgets.QTableWidgetItem('表达')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(16, 3, item)
        item = QtWidgets.QTableWidgetItem('社会认知')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(17, 1, item)
        self.table.setSpan(17, 1, 3, 1)
        item = QtWidgets.QTableWidgetItem('16')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(17, 2, item)
        item = QtWidgets.QTableWidgetItem('17')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(18, 2, item)
        item = QtWidgets.QTableWidgetItem('18')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(19, 2, item)
        item = QtWidgets.QTableWidgetItem('社会交往')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(17, 3, item)
        item = QtWidgets.QTableWidgetItem('解决问题')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(18, 3, item)
        item = QtWidgets.QTableWidgetItem('记忆')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(19, 3, item)
        item = QtWidgets.QTableWidgetItem('认知功能评分')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(20, 1, item)
        self.table.setSpan(20, 1, 1, 3)

        item = QtWidgets.QTableWidgetItem('FIM 总分')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(21, 0, item)
        self.table.setSpan(21, 0, 1, 4)

        item = QtWidgets.QTableWidgetItem('评估人')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(21, 0, item)
        self.table.setSpan(21, 0, 1, 4)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 480, 1460, 500))
        self.label_5.setStyleSheet("font:12pt")
        self.label_5.setWordWrap(True)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "功能独立性测评（FIM）"))
        self.title.setText(_translate("MainWindow", "功能独立性测评（FIM）"))
        self.label.setText(_translate("MainWindow", "姓名:"))
        self.name.setText(_translate("MainWindow", "--"))
        self.label_2.setText(_translate("MainWindow", "性别:"))
        self.gender.setText(_translate("MainWindow", "--"))
        self.label_3.setText(_translate("MainWindow", "年龄:"))
        self.age.setText(_translate("MainWindow", "--"))
        self.label_4.setText(_translate("MainWindow", "患手:"))
        self.hand.setText(_translate("MainWindow", "--"))
        self.label_5.setText(_translate("MainWindow","功能水平和评分标准：\r\n1、独立：活动中不需他人帮助。\r\n完全独立（7 分）-- 构成活动的所有作业均能规范、完全地完成，不需修改和辅助设备或用品，并在合理的时间内完成\r\n\
 有条件的独立（6分）-- 具有下列一项或几项：活动中需要辅助设备；活动需要比正常长的时间；或需要安全方面的考虑\r\n2、依赖：为了进行活动，患者需要另一个人予以监护或身体的接触性帮助，或者不进行活动。\r\n有条件的依赖--患者付出50%或更多的努力，其所需的辅助水平如下：\r\n\
 （1） 监护和准备（5 分）-- 患者所需的帮助只限于备用、提示或劝告，帮助者和患者之间没有身体的\r\n接触或帮助者仅需要帮助准备必需用品；或帮助带上矫形器。\r\n\
 （2）少量身体接触的帮助（4 分）-- 患者所需的帮助只限于轻轻接触，自己能付出75%或以上的努力。\r\n（3）中度身体接触的帮助（3 分）-- 患者需要中度的帮助，自己能付出50%~75%的努力。\r\n\
 完全依赖 -- 患者需要一半以上的帮助或完全依赖他人，否则活动就不能进行。\r\n（1）大量身体接触的帮助（2 分）-- 患者付出的努力小于50%，但大于25%。\r\n（2）完全依赖（1 分）-- 患者付出的努力小于25%。\r\n\
 FIM 的最高分为126 分（运动功能评分91 分，认知功能评分35 分），最低分18 分。126 分=完全独立；108 分~125 分=基本独立；90~107 分=有条件的独立或极轻度依赖；72~89 分轻度依赖；54~71 分中度依赖；36~53 分=重度依赖；19~35 分=极重度依赖；18 分=完全依赖。"))
        self.label_6.setText(_translate("MainWindow", "评定日期:"))

        self.saveButton.setText(_translate("MainWindow", "保存"))
        self.downLoadButton.setText(_translate("MainWindow", "导出"))


class FIM(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, patient_id):
        super(FIM, self).__init__()
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
        test_date = self.dateEdit.text().replace('/', '-')
        sheet = {'id': tool.Tools.getTimeStamp(), 'patient_id': self.patient_id, 'test_date': test_date}
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
    gui = FIM()
    gui.show()
    sys.exit(app.exec_())
