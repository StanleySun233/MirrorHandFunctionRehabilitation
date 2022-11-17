# 已完成上传
import json
import sys

import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QMessageBox, QFileDialog

import config
import tool.Tools


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(1500, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.frame_sub = QtWidgets.QFrame(self.centralwidget)
        self.frame_sub.setGeometry(QtCore.QRect(0, 0, 1500, 1000))
        self.frame_sub.setStyleSheet("QFrame {\n"
                                     "  background-color:rgb(242, 249, 255);\n"
                                     "}")
        self.frame_sub.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sub.setFrameShadow(QtWidgets.QFrame.Raised)

        self.label_4 = QtWidgets.QLabel(self.frame_sub)
        self.label_4.setGeometry(QtCore.QRect(600, 10, 300, 40))
        self.label_4.setStyleSheet("font:16pt")

        self.label_5 = QtWidgets.QLabel(self.frame_sub)
        self.label_5.setGeometry(QtCore.QRect(80, 80, 300, 40))
        self.label_5.setStyleSheet("font:12pt")

        self.nameLabel = QtWidgets.QLabel(self.frame_sub)
        self.nameLabel.setGeometry(QtCore.QRect(180, 80, 300, 40))
        self.nameLabel.setText('--')
        self.nameLabel.setStyleSheet("font:16pt")

        self.label_6 = QtWidgets.QLabel(self.frame_sub)
        self.label_6.setGeometry(QtCore.QRect(380, 80, 300, 40))
        self.label_6.setStyleSheet("font:12pt")

        self.sexLabel = QtWidgets.QLabel(self.frame_sub)
        self.sexLabel.setGeometry(QtCore.QRect(480, 80, 300, 40))
        self.sexLabel.setText('--')
        self.sexLabel.setStyleSheet("font:16pt")

        self.label_7 = QtWidgets.QLabel(self.frame_sub)
        self.label_7.setGeometry(QtCore.QRect(680, 80, 300, 40))
        self.label_7.setStyleSheet("font:12pt")

        self.ageLabel = QtWidgets.QLabel(self.frame_sub)
        self.ageLabel.setGeometry(QtCore.QRect(780, 80, 300, 40))
        self.ageLabel.setText('--')
        self.ageLabel.setStyleSheet("font:16pt")

        self.label_8 = QtWidgets.QLabel(self.frame_sub)
        self.label_8.setGeometry(QtCore.QRect(980, 80, 300, 40))
        self.label_8.setStyleSheet("font:12pt")

        self.unhealthyHandLabel = QtWidgets.QLabel(self.frame_sub)
        self.unhealthyHandLabel.setGeometry(QtCore.QRect(1080, 80, 300, 40))
        self.unhealthyHandLabel.setText('--')
        self.unhealthyHandLabel.setStyleSheet("font:16pt")

        self.tableWidget = QtWidgets.QTableWidget(self.frame_sub)
        self.tableWidget.setGeometry(QtCore.QRect(80, 140, 1350, 650))
        self.tableWidget.setStyleSheet("background:white;font:14pt")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(6)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.tableWidget.setShowGrid(True)

        item = QtWidgets.QTableWidgetItem('0级')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setRowHeight(0, 99)
        self.tableWidget.setItem(0, 0, item)

        item = QtWidgets.QTableWidgetItem('无肌张力的增加')
        self.tableWidget.setItem(0, 1, item)

        item = QtWidgets.QTableWidgetItem('1级')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setRowHeight(1, 99)
        self.tableWidget.setItem(1, 0, item)

        item = QtWidgets.QTableWidgetItem('肌张力略微增加：受累部分被动屈伸时，在关节活动范围之末时呈现最小的阻力或出现突然卡住和释放')
        self.tableWidget.setItem(1, 1, item)

        item = QtWidgets.QTableWidgetItem('1+级')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setRowHeight(2, 99)
        self.tableWidget.setItem(2, 0, item)

        item = QtWidgets.QTableWidgetItem('肌张力轻度增加：在关节活动范围后50%范围内出现突然卡住，然后再关节活动范围的后50%均呈现最小的阻力')
        self.tableWidget.setItem(2, 1, item)

        item = QtWidgets.QTableWidgetItem('2级')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setRowHeight(3, 99)
        self.tableWidget.setItem(3, 0, item)

        item = QtWidgets.QTableWidgetItem('肌张力较明显地增加：通过关节活动范围的大部分时，肌张力均较明显地增加，但受累部分仍能较容易地被移动')
        self.tableWidget.setItem(3, 1, item)

        item = QtWidgets.QTableWidgetItem('3级')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setRowHeight(4, 99)
        self.tableWidget.setItem(4, 0, item)

        item = QtWidgets.QTableWidgetItem('肌张力严重增高：被动运动困难')
        self.tableWidget.setItem(4, 1, item)

        item = QtWidgets.QTableWidgetItem('4级')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setRowHeight(5, 99)
        self.tableWidget.setItem(5, 0, item)

        item = QtWidgets.QTableWidgetItem('僵直：受累部分被动屈伸时呈现僵直状态，不能活动')
        self.tableWidget.setItem(5, 1, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(1, 1195)

        self.label = QtWidgets.QLabel(self.frame_sub)
        self.label.setGeometry(QtCore.QRect(80, 800, 400, 40))
        self.label.setStyleSheet("font:16pt")

        self.elbowShenJicomboBox = QtWidgets.QComboBox(self.frame_sub)  # 伸肌评定结果
        self.elbowShenJicomboBox.setGeometry(QtCore.QRect(420, 800, 160, 35))
        self.elbowShenJicomboBox.addItems(['', '0级', '1级', '1级+', '2级', '3级', '4级'])
        self.elbowShenJicomboBox.setStyleSheet("font:12pt")

        self.label_2 = QtWidgets.QLabel(self.frame_sub)
        self.label_2.setGeometry(QtCore.QRect(680, 800, 400, 40))
        self.label_2.setStyleSheet("font:16pt")

        self.elbowQuJicomboBox = QtWidgets.QComboBox(self.frame_sub)
        self.elbowQuJicomboBox.setGeometry(QtCore.QRect(1020, 800, 160, 35))
        self.elbowQuJicomboBox.addItems(['', '0级', '1级', '1级+', '2级', '3级', '4级'])
        self.elbowQuJicomboBox.setStyleSheet("font:12pt")

        self.label_9 = QtWidgets.QLabel(self.frame_sub)
        self.label_9.setGeometry(QtCore.QRect(60, 870, 400, 40))
        self.label_9.setStyleSheet("font:16pt")

        self.wristShenJicomboBox = QtWidgets.QComboBox(self.frame_sub)  # 伸肌评定结果
        self.wristShenJicomboBox.setGeometry(QtCore.QRect(420, 870, 160, 35))
        self.wristShenJicomboBox.addItems(['', '0级', '1级', '1级+', '2级', '3级', '4级'])
        self.wristShenJicomboBox.setStyleSheet("font:12pt")

        self.label_10 = QtWidgets.QLabel(self.frame_sub)
        self.label_10.setGeometry(QtCore.QRect(680, 870, 400, 40))
        self.label_10.setStyleSheet("font:16pt")

        self.wristQuJicomboBox = QtWidgets.QComboBox(self.frame_sub)
        self.wristQuJicomboBox.setGeometry(QtCore.QRect(1020, 870, 160, 35))
        self.wristQuJicomboBox.addItems(['', '0级', '1级', '1级+', '2级', '3级', '4级'])
        self.wristQuJicomboBox.setStyleSheet("font:12pt")

        self.label_3 = QtWidgets.QLabel(self.frame_sub)
        self.label_3.setGeometry(QtCore.QRect(80, 940, 260, 40))
        self.label_3.setStyleSheet("font:16pt")

        self.dateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.frame_sub)
        self.dateEdit.setGeometry(QtCore.QRect(270, 940, 260, 40))
        self.dateEdit.setStyleSheet("font:16pt")
        self.dateEdit.setCalendarPopup(True)

        self.saveButton = QtWidgets.QPushButton(self.frame_sub)
        self.saveButton.setGeometry(QtCore.QRect(580, 940, 120, 40))
        self.saveButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.uploadButton = QtWidgets.QPushButton(self.frame_sub)
        self.uploadButton.setGeometry(QtCore.QRect(720, 940, 120, 40))
        self.uploadButton.setText('导出')
        self.uploadButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "改良Ashworth分级"))
        self.label_4.setText(_translate("MainWindow", "  改良Ashworth分级"))
        self.label_5.setText(_translate("MainWindow", "  姓名:"))
        self.label_6.setText(_translate("MainWindow", "  性别:"))
        self.label_7.setText(_translate("MainWindow", "  年龄:"))
        self.label_8.setText(_translate("MainWindow", "  患手:"))
        self.saveButton.setText(_translate("MainWindow", "保存"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "级别"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "评定标准"))
        self.label.setText(_translate("MainWindow", "患侧肘部伸肌评定结果:"))
        self.label_2.setText(_translate("MainWindow", "患侧肘部屈肌评定结果:"))
        self.label_9.setText(_translate("MainWindow", " 患侧腕部伸肌评定结果:"))
        self.label_10.setText(_translate("MainWindow", " 患侧腕部屈肌评定结果:"))
        self.label_3.setText(_translate("MainWindow", "  评定日期:"))


class Ashworth(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, patient_id):
        super(Ashworth, self).__init__()
        self.setupUi(self)

        self.patient_id = patient_id

        self.patientInfo = \
            json.loads(requests.post(config.patientGetById, data={'id': self.patient_id}).content.decode('utf-8'))[
                'data']

        self.nameLabel.setText(self.patientInfo['name'])
        self.ageLabel.setText(str(self.patientInfo['age']))
        self.sexLabel.setText(self.patientInfo['sex'])
        self.unhealthyHandLabel.setText(self.patientInfo['illness'])

        self.saveButton.clicked.connect(self.saveButtonClick)
        self.uploadButton.clicked.connect(self.uploadButtonClick)

    def saveButtonClick(self, *args):
        code_1 = self.elbowShenJicomboBox.currentText()
        code_2 = self.elbowQuJicomboBox.currentText()
        code_3 = self.wristShenJicomboBox.currentText()
        code_4 = self.wristQuJicomboBox.currentText()
        test_date = self.dateEdit.text().replace('/', '-')
        sheet = {'id': tool.Tools.getTimeStamp(), 'patient_id': self.patient_id, 'code_1': code_1, 'code_2': code_2,
                 'code_3': code_3, 'code_4': code_4, 'test_date': test_date}
        res = requests.post(config.ashworthInsert, data=sheet)
        QMessageBox.information(self, "保存", '保存成功', QMessageBox.Yes, QMessageBox.Yes)

        ...

    def uploadButtonClick(self, *args):
        self.saveButton.hide()
        self.uploadButton.hide()
        img = self.grab()
        self.saveButton.show()
        self.uploadButton.show()
        path = QFileDialog.getExistingDirectory()
        img.save(f"{path}/{self.nameLabel.text()}_{self.dateEdit.text().replace('/', '-')}.png")
        ...


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Ashworth(1)
    gui.show()
    sys.exit(app.exec_())
