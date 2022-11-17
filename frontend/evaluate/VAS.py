#已完成
import json
import sys

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QSlider, QVBoxLayout
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import config
import tool.Tools

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

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 180, 200, 40))
        self.label_7.setStyleSheet('font:14pt')

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 180, 200, 40))
        self.label_8.setStyleSheet('font:14pt')

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(330, 180, 200, 40))
        self.label_9.setStyleSheet('font:14pt')

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(465, 180, 200, 40))
        self.label_10.setStyleSheet('font:14pt')

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(600, 180, 200, 40))
        self.label_11.setStyleSheet('font:14pt')

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(735, 180, 200, 40))
        self.label_12.setStyleSheet('font:14pt')

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(870, 180, 200, 40))
        self.label_13.setStyleSheet('font:14pt')

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1000, 180, 200, 40))
        self.label_14.setStyleSheet('font:14pt')

        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1135, 180, 200, 40))
        self.label_15.setStyleSheet('font:14pt')

        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(1270, 180, 200, 40))
        self.label_16.setStyleSheet('font:14pt')

        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(1400, 180, 200, 40))
        self.label_17.setStyleSheet('font:14pt')

        self.s1 = QSlider(Qt.Horizontal,self.centralwidget)
        self.s1.setGeometry(QtCore.QRect(60, 230, 1360,100))
        self.s1.setStyleSheet('font:16pt;')
        # 设置最小值
        self.s1.setMinimum(0)
        # 设置最大值
        self.s1.setMaximum(10)
        # 设置步长
        self.s1.setSingleStep(1)
        # 设置当前值
        self.s1.setValue(0)
        # 刻度位置在下方
        self.s1.setTickPosition(QSlider.TicksBothSides)
        # 设置刻度间隔
        self.s1.setTickInterval(1)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30,340, 200, 40))
        self.label_5.setStyleSheet('font:14pt')

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1390, 340, 200, 40))
        self.label_6.setStyleSheet('font:14pt')

        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(30, 440, 200, 40))
        self.label_18.setStyleSheet('font:14pt')

        self.upperExtremityPain=QtWidgets.QLineEdit(self.centralwidget)
        self.upperExtremityPain.setGeometry(QtCore.QRect(220, 440, 400, 40))
        self.upperExtremityPain.setStyleSheet('font:14pt;background:white')

        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(700, 440, 200, 40))
        self.label_19.setStyleSheet('font:14pt')

        self.result = QtWidgets.QComboBox(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(780, 440, 400, 40))
        self.result.addItems(['','轻度疼痛（1-3）','中度疼痛（4-6）','重度疼痛（7-10）'])
        self.result.setStyleSheet('font:14pt;background:white')

        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(100, 540, 200, 40))
        self.label_20.setStyleSheet('font:14pt')

        self.dateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(270, 540, 260, 40))
        self.dateEdit.setStyleSheet("font:16pt;background:white")
        self.dateEdit.setCalendarPopup(True)

        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(850, 540, 120, 40))
        self.saveButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.downLoadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downLoadButton.setGeometry(QtCore.QRect(990, 540, 120, 40))
        self.downLoadButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VAS疼痛视觉模拟"))
        self.title.setText(_translate("MainWindow", "VAS疼痛视觉模拟"))
        self.label.setText(_translate("MainWindow", "姓名:"))
        self.name.setText(_translate("MainWindow", "--"))
        self.label_2.setText(_translate("MainWindow", "性别:"))
        self.gender.setText(_translate("MainWindow", "--"))
        self.label_3.setText(_translate("MainWindow", "年龄:"))
        self.age.setText(_translate("MainWindow", "--"))
        self.label_4.setText(_translate("MainWindow", "患手:"))
        self.hand.setText(_translate("MainWindow", "--"))
        self.label_5.setText(_translate("MainWindow", "无痛"))
        self.label_6.setText(_translate("MainWindow", "剧痛"))
        self.label_7.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "1"))
        self.label_9.setText(_translate("MainWindow", "2"))
        self.label_10.setText(_translate("MainWindow", "3"))
        self.label_11.setText(_translate("MainWindow", "4"))
        self.label_12.setText(_translate("MainWindow", "5"))
        self.label_13.setText(_translate("MainWindow", "6"))
        self.label_14.setText(_translate("MainWindow", "7"))
        self.label_15.setText(_translate("MainWindow", "8"))
        self.label_16.setText(_translate("MainWindow", "9"))
        self.label_17.setText(_translate("MainWindow", "10"))
        self.label_18.setText(_translate("MainWindow", "上肢疼痛部位:"))
        self.label_19.setText(_translate("MainWindow", "结果:"))
        self.label_20.setText(_translate("MainWindow", "评定日期:"))
        self.saveButton.setText(_translate("MainWindow", "保存"))
        self.downLoadButton.setText(_translate("MainWindow", "导出"))


class VAS(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,patient_id):
        super(VAS, self).__init__()
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
        code_1 = str(self.s1.value())
        code_2 = self.upperExtremityPain.text()
        code_3 = self.result
        test_date = self.dateEdit.text().replace("/", "-")
        sheet = {'id': tool.Tools.getTimeStamp(), 'patient_id': self.patient_id, 'code_1': code_1, 'code_2': code_2,
                 'code_3': code_3, 'test_date': test_date}
        res = requests.post(config.VASInsert, data=sheet)
        QMessageBox.information(self, "保存", '保存成功', QMessageBox.Yes, QMessageBox.Yes)
        ...

    def downLoadButtonClick(self, *args):
        self.saveButton.hide()
        self.downLoadButton.hide()
        img = self.grab()
        self.saveButton.show()
        self.downLoadButton.show()
        path = QFileDialog.getExistingDirectory()
        img.save(
            f"{path}/{self.name.text()}_{self.dateEdit.text().replace('/', '-')}.png")
        QMessageBox.information(self, "导出", '导出成功', QMessageBox.Yes, QMessageBox.Yes)
        ...


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = VAS()
    gui.show()
    sys.exit(app.exec_())
