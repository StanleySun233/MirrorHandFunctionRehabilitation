import json
import sys

import requests
from PyQt5 import QtCore, QtWidgets
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
        self.table.setGeometry(QtCore.QRect(20, 120, 1460, 700))
        self.table.setStyleSheet('background:white;font:12pt')
        self.table.setColumnCount(5)
        self.table.setRowCount(44)
        self.table.verticalHeader().setVisible(False)

        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)  # 列
        self.table.setColumnWidth(0, 160)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        self.table.setColumnWidth(1, 160)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        self.table.setColumnWidth(2, 160)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        self.table.setColumnWidth(3, 730)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        self.table.setColumnWidth(4, 208)

        item = QtWidgets.QTableWidgetItem('肩')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(0, 0, item)
        self.table.setSpan(0, 0, 17, 1)
        self.table.setSpan(0, 4, 2, 1)

        item = QtWidgets.QTableWidgetItem('1')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(0, 1, item)
        self.table.setSpan(0, 1, 2, 2)
        item = QtWidgets.QTableWidgetItem('A.肩前屈90°，肘0°，前臂中立位')
        self.table.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem('B.如果完成，能否保持位置')
        self.table.setItem(1, 3, item)

        item = QtWidgets.QTableWidgetItem('2')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(2, 1, item)
        self.table.setSpan(2, 1, 2, 2)
        self.table.setSpan(2, 4, 2, 1)
        item = QtWidgets.QTableWidgetItem('A.肩外展90°，肘0°，前臂旋前位')
        self.table.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem('B.如果完成，能否保持位置')
        self.table.setItem(3, 3, item)

        item = QtWidgets.QTableWidgetItem('3')
        self.table.setItem(4, 1, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setSpan(4, 1, 2, 2)
        self.table.setSpan(4, 4, 2, 1)
        item = QtWidgets.QTableWidgetItem('A.肩部前屈90°-150°，肘0°')
        self.table.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem('B.如果完成，能否保持位置')
        self.table.setItem(5, 3, item)

        item = QtWidgets.QTableWidgetItem('4')
        self.table.setItem(6, 1, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setSpan(6, 1, 2, 2)
        self.table.setSpan(6, 4, 2, 1)
        item = QtWidgets.QTableWidgetItem('A.摸头顶')
        self.table.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem('B.如果完成，能否保持位置')
        self.table.setItem(7, 3, item)

        item = QtWidgets.QTableWidgetItem('5')
        self.table.setItem(8, 1, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setSpan(8, 1, 2, 2)
        self.table.setSpan(8, 4, 2, 1)
        item = QtWidgets.QTableWidgetItem('A.摸腰部脊柱')
        self.table.setItem(8, 3, item)
        item = QtWidgets.QTableWidgetItem('B.如果完成，能否保持位置')
        self.table.setItem(9, 3, item)

        item = QtWidgets.QTableWidgetItem('6')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(10, 1, item)
        self.table.setSpan(10, 1, 1, 2)
        item = QtWidgets.QTableWidgetItem('肩部上提')
        self.table.setItem(10, 3, item)

        item = QtWidgets.QTableWidgetItem('7')
        self.table.setItem(11, 1, item)
        self.table.setSpan(11, 1, 1, 2)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item = QtWidgets.QTableWidgetItem('在有支撑的条件下手臂前伸/收回（大腿或桌子）')
        self.table.setItem(11, 3, item)

        item = QtWidgets.QTableWidgetItem('8')
        self.table.setItem(12, 1, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setSpan(12, 1, 2, 2)
        self.table.setSpan(12, 4, 2, 1)
        item = QtWidgets.QTableWidgetItem('A.肘屈曲90°时肩部前屈30°')
        self.table.setItem(12, 3, item)
        item = QtWidgets.QTableWidgetItem('B.前臂支撑桌面，肘屈曲肩部后伸30°')
        self.table.setItem(13, 3, item)

        item = QtWidgets.QTableWidgetItem('9')
        self.table.setItem(14, 1, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setSpan(14, 1, 2, 2)
        self.table.setSpan(14, 4, 2, 1)
        item = QtWidgets.QTableWidgetItem('A.肩0°，肘90°，肩内旋到手触腹部')
        self.table.setItem(14, 3, item)
        item = QtWidgets.QTableWidgetItem('B.肩0°，肘90°，肩部外旋')
        self.table.setItem(15, 3, item)

        item = QtWidgets.QTableWidgetItem('10')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(16, 1, item)
        self.table.setSpan(16, 1, 1, 2)
        item = QtWidgets.QTableWidgetItem('手触对侧膝部')
        self.table.setItem(16, 3, item)

        item = QtWidgets.QTableWidgetItem('肘前臂')
        self.table.setItem(17, 0, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setSpan(17, 0, 6, 1)

        item = QtWidgets.QTableWidgetItem('1')
        self.table.setItem(17, 1, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setSpan(17, 1, 2, 2)
        self.table.setSpan(17, 4, 2, 1)
        item = QtWidgets.QTableWidgetItem('A.肩0°，肘90°，前臂旋前')
        self.table.setItem(16, 3, item)
        item = QtWidgets.QTableWidgetItem('B.肩0°，肘90°，前臂旋后')
        self.table.setItem(18, 3, item)

        item = QtWidgets.QTableWidgetItem('2')
        self.table.setItem(19, 1, item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setSpan(19, 1, 2, 2)
        self.table.setSpan(19, 4, 2, 1)
        item = QtWidgets.QTableWidgetItem('A.肘0°，完全屈曲')
        self.table.setItem(19, 3, item)
        item = QtWidgets.QTableWidgetItem('B.如果完成，能否保持位置')
        self.table.setItem(20, 3, item)

        item = QtWidgets.QTableWidgetItem('3')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(21, 1, item)
        self.table.setSpan(21, 1, 1, 2)
        item = QtWidgets.QTableWidgetItem('肘由屈曲位伸展到0°（减重或抗重）')
        self.table.setItem(21, 3, item)

        item = QtWidgets.QTableWidgetItem('4')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(22, 1, item)
        self.table.setSpan(22, 1, 1, 2)
        item = QtWidgets.QTableWidgetItem('手摸对侧肩部')
        self.table.setItem(22, 3, item)

        item = QtWidgets.QTableWidgetItem('肩肘前臂总分')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(23, 0, item)
        self.table.setSpan(23, 0, 21, 1)

        item = QtWidgets.QTableWidgetItem('腕')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(23, 1, item)
        self.table.setSpan(23, 1, 3, 1)

        item = QtWidgets.QTableWidgetItem('1')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(23, 2, item)
        item = QtWidgets.QTableWidgetItem('肩0°，肘90°，前臂旋前，伸腕')
        self.table.setItem(23, 3, item)

        item = QtWidgets.QTableWidgetItem('2')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(24, 2, item)
        item = QtWidgets.QTableWidgetItem('肩0°，肘90°，前臂旋后，屈腕')
        self.table.setItem(24, 3, item)

        item = QtWidgets.QTableWidgetItem('3')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(25, 2, item)
        item = QtWidgets.QTableWidgetItem('肩0°，肘90°，前臂旋前，腕旋转')
        self.table.setItem(25, 3, item)

        item = QtWidgets.QTableWidgetItem('手')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(26, 1, item)
        self.table.setSpan(26, 1, 17, 1)

        item = QtWidgets.QTableWidgetItem('1')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(26, 2, item)
        item = QtWidgets.QTableWidgetItem('手指集团屈曲')
        self.table.setItem(26, 3, item)

        item = QtWidgets.QTableWidgetItem('2')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(27, 2, item)
        item = QtWidgets.QTableWidgetItem('手指集团伸展')
        self.table.setItem(27, 3, item)

        item = QtWidgets.QTableWidgetItem('3')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(27, 2, item)
        item = QtWidgets.QTableWidgetItem('勾状抓握')
        self.table.setItem(27, 3, item)

        item = QtWidgets.QTableWidgetItem('4')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(28, 2, item)
        item = QtWidgets.QTableWidgetItem('掌指关节屈曲，指间关节')
        self.table.setItem(28, 3, item)

        item = QtWidgets.QTableWidgetItem('5')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(29, 2, item)
        item = QtWidgets.QTableWidgetItem('拇指外展')
        self.table.setItem(29, 3, item)

        item = QtWidgets.QTableWidgetItem('6')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(30, 2, item)
        item = QtWidgets.QTableWidgetItem('拇指内收')
        self.table.setItem(30, 3, item)

        item = QtWidgets.QTableWidgetItem('7')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(31, 2, item)
        item = QtWidgets.QTableWidgetItem('拇指对小指根部')
        self.table.setItem(31, 3, item)

        item = QtWidgets.QTableWidgetItem('8')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(32, 2, item)
        self.table.setSpan(32, 2, 4, 1)
        self.table.setSpan(32, 4, 4, 1)
        item = QtWidgets.QTableWidgetItem('A.拇指对食指指尖')
        self.table.setItem(32, 3, item)
        item = QtWidgets.QTableWidgetItem('B.拇指对中指指尖')
        self.table.setItem(33, 3, item)
        item = QtWidgets.QTableWidgetItem('C.拇指对环指指尖')
        self.table.setItem(34, 3, item)
        item = QtWidgets.QTableWidgetItem('D.拇指对小指指尖')
        self.table.setItem(35, 3, item)

        item = QtWidgets.QTableWidgetItem('9')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(36, 2, item)
        self.table.setSpan(36, 2, 4, 1)
        self.table.setSpan(36, 4, 4, 1)
        item = QtWidgets.QTableWidgetItem('A.拇指对食指指腹')
        self.table.setItem(36, 3, item)
        item = QtWidgets.QTableWidgetItem('B.拇指对中指指腹')
        self.table.setItem(37, 3, item)
        item = QtWidgets.QTableWidgetItem('C.拇指对环指指腹')
        self.table.setItem(38, 3, item)
        item = QtWidgets.QTableWidgetItem('D.拇指对小指指腹')
        self.table.setItem(39, 3, item)

        item = QtWidgets.QTableWidgetItem('10')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(40, 2, item)
        item = QtWidgets.QTableWidgetItem('抓住饮料瓶，放到2-4英寸远并放开')
        self.table.setItem(40, 3, item)

        item = QtWidgets.QTableWidgetItem('11')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(41, 2, item)
        item = QtWidgets.QTableWidgetItem('钳状抓握钢笔，签名，写日期或画3条垂直线')
        self.table.setItem(41, 3, item)

        item = QtWidgets.QTableWidgetItem('12')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(42, 2, item)
        item = QtWidgets.QTableWidgetItem('侧捏钥匙')
        self.table.setItem(42, 3, item)

        item = QtWidgets.QTableWidgetItem('腕指总分')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(43, 1, item)
        self.table.setSpan(43, 2, 1, 2)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 840, 260, 40))
        self.label_6.setStyleSheet("font:16pt")

        self.dateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(170, 840, 260, 40))
        self.dateEdit.setStyleSheet("font:16pt;background:white")
        self.dateEdit.setCalendarPopup(True)

        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(450, 840, 120, 40))
        self.saveButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.downLoadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downLoadButton.setGeometry(QtCore.QRect(590, 840, 120, 40))
        self.downLoadButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "运动功能状态量表（MSS）"))
        self.title.setText(_translate("MainWindow", "运动功能状态量表"))
        self.label.setText(_translate("MainWindow", "姓名:"))
        self.name.setText(_translate("MainWindow", "--"))
        self.label_2.setText(_translate("MainWindow", "性别:"))
        self.gender.setText(_translate("MainWindow", "--"))
        self.label_3.setText(_translate("MainWindow", "年龄:"))
        self.age.setText(_translate("MainWindow", "--"))
        self.label_4.setText(_translate("MainWindow", "患手:"))
        self.hand.setText(_translate("MainWindow", "--"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "评估内容"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "评分"))
        self.label_6.setText(_translate("MainWindow", "评定日期:"))
        self.saveButton.setText(_translate("MainWindow", "保存"))
        self.downLoadButton.setText(_translate("MainWindow", "导出"))


class MSS(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, patient_id):
        super(MSS, self).__init__()
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

    def saveButtonClick(self, *args):
        test_date = self.dateEdit.text().replace('/', '-')
        sheet = {'id': tool.Tools.getTimeStamp(), 'patient_id': self.patient_id,  'test_date': test_date}
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
    gui = MSS('1')
    gui.show()
    sys.exit(app.exec_())
