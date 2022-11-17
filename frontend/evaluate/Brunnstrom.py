# 已完成上传
import json
import sys
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import config
import tool.Tools


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(1500, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet('background-color:rgb(242, 249, 255)')

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(500, 10, 500, 41))
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
        self.table.setGeometry(QtCore.QRect(20, 120, 1460, 600))
        self.table.setStyleSheet('background:white;font:12pt')
        self.table.setColumnCount(3)
        self.table.setRowCount(12)
        self.table.verticalHeader().setVisible(False)

        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)  # 列
        self.table.setColumnWidth(0, 140)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        self.table.setColumnWidth(1, 680)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        self.table.setColumnWidth(2, 640)

        item = QtWidgets.QTableWidgetItem('Ⅰ')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem('无随意运动（弛缓期）')
        self.table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem('无随意运动（弛缓期）')
        self.table.setItem(0, 2, item)

        item = QtWidgets.QTableWidgetItem('Ⅱ')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem('联带运动初期阶段（痉挛期）')
        self.table.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem('细微屈伸（痉挛期）')
        self.table.setItem(1, 2, item)

        item = QtWidgets.QTableWidgetItem('Ⅲ')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem('联带运动达到高峰')
        self.table.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem('联带运动达到高峰（钩状抓握不能伸）')
        self.table.setItem(2, 2, item)

        item = QtWidgets.QTableWidgetItem('Ⅳ')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(3, 0, item)
        self.table.setSpan(3,0,4,1)
        self.table.setSpan(3,2, 2, 1)
        self.table.setSpan(5, 2, 2, 1)
        item = QtWidgets.QTableWidgetItem('出现部分分离运动:')
        self.table.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem('手背到腰后;')
        self.table.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem('肘关节伸展，肩关节屈曲90度;')
        self.table.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem('肘关节屈曲90度，前臂旋前、旋后;')
        self.table.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem('侧捏、松开拇指')
        self.table.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem('手指小范围伸')
        self.table.setItem(5, 2, item)

        item = QtWidgets.QTableWidgetItem('Ⅴ')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(7, 0, item)
        self.table.setSpan(7, 0, 4, 1)
        self.table.setSpan(7, 2, 2, 1)
        self.table.setSpan(9, 2, 2, 1)
        item = QtWidgets.QTableWidgetItem('出现分离运动:')
        self.table.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem('肘关节伸展，肩关节外展90度;')
        self.table.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem('肘关节伸展，肩关节上举;')
        self.table.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem('肘关节伸展，肩关节屈曲90度，前臂旋前、旋后;')
        self.table.setItem(10, 1, item)
        item = QtWidgets.QTableWidgetItem('球状、圆柱状抓握')
        self.table.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem('手指同时伸展（不能单独伸）')
        self.table.setItem(9, 2, item)

        item = QtWidgets.QTableWidgetItem('Ⅵ')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem('指鼻试验（比健侧慢，小于5秒）')
        self.table.setItem(11, 1, item)
        item = QtWidgets.QTableWidgetItem('抓握均能完成，速度及准确性差')
        self.table.setItem(11, 2, item)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20,740, 200, 100))
        self.label_5.setStyleSheet("font:14pt")

        self.handFunctionLineEdit=QtWidgets.QLineEdit(self.centralwidget)
        self.handFunctionLineEdit.setGeometry(QtCore.QRect(120, 770, 150,40))
        self.handFunctionLineEdit.setStyleSheet("font:14pt;background:white")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(300, 740, 1460, 100))
        self.label_7.setStyleSheet("font:14pt")

        self.upperLimbFunctionLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.upperLimbFunctionLineEdit.setGeometry(QtCore.QRect(430, 770, 150, 40))
        self.upperLimbFunctionLineEdit.setStyleSheet("font:14pt;background:white")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(600, 770, 260, 40))
        self.label_6.setStyleSheet("font:14pt")

        self.dateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(750, 770, 260, 40))
        self.dateEdit.setStyleSheet("font:16pt;background:white")
        self.dateEdit.setCalendarPopup(True)

        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(650, 840, 120, 40))
        self.saveButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.downLoadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downLoadButton.setGeometry(QtCore.QRect(790, 840, 120, 40))
        self.downLoadButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Brunnstrom脑卒中运动功能分级"))
        self.title.setText(_translate("MainWindow", "Brunnstrom脑卒中运动功能分级"))
        self.label.setText(_translate("MainWindow", "姓名:"))
        self.name.setText(_translate("MainWindow", "--"))
        self.label_2.setText(_translate("MainWindow", "性别:"))
        self.gender.setText(_translate("MainWindow", "--"))
        self.label_3.setText(_translate("MainWindow", "年龄:"))
        self.age.setText(_translate("MainWindow", "--"))
        self.label_4.setText(_translate("MainWindow", "患手:"))
        self.hand.setText(_translate("MainWindow", "--"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "阶段"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "上肢功能评价标准"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "手功能评价标准"))
        self.label_5.setText(_translate("MainWindow", "手功能:"))
        self.label_7.setText(_translate("MainWindow", "上肢功能:"))
        self.label_6.setText(_translate("MainWindow", "评定日期:"))
        self.saveButton.setText(_translate("MainWindow", "保存"))
        self.downLoadButton.setText(_translate("MainWindow", "导出"))

#Brunnstrom脑卒中运动功能分级
class Brunnstrom(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, patient_id):
        super(Brunnstrom, self).__init__()
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
        code_1=self.handFunctionLineEdit.text()
        code_2=self.upperLimbFunctionLineEdit.text()
        test_date = self.dateEdit.text().replace('/', '-')
        sheet = {'id': tool.Tools.getTimeStamp(), 'patient_id': self.patient_id, 'code_1': code_1, 'code_2': code_2,
                  'test_date': test_date}
        res = requests.post(config.muscleStrengthInsert, data=sheet)
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
    gui = Brunnstrom()
    gui.show()
    sys.exit(app.exec_())