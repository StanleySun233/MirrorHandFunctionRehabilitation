#已完成
import json
import sys

import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QMessageBox, QFileDialog

import config
import tool


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

        self.unhealthHandLabel = QtWidgets.QLabel(self.frame_sub)
        self.unhealthHandLabel.setGeometry(QtCore.QRect(1080, 80, 300, 40))
        self.unhealthHandLabel.setText('--')
        self.unhealthHandLabel.setStyleSheet("font:16pt")

        self.tableWidget = QtWidgets.QTableWidget(self.frame_sub)
        self.tableWidget.setGeometry(QtCore.QRect(80, 140, 1350, 450))
        self.tableWidget.setStyleSheet("background:white;font:14pt")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(6)
        self.tableWidget.verticalHeader().setVisible(False)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(1, 794)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.setColumnWidth(2, 400)

        item = QtWidgets.QTableWidgetItem('0')
        self.tableWidget.setRowHeight(0, 65)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(0, 0, item)

        item = QtWidgets.QTableWidgetItem('肌肉无任何收缩')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(0, 1, item)

        item = QtWidgets.QTableWidgetItem('0')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(0, 2, item)

        item = QtWidgets.QTableWidgetItem('1')
        self.tableWidget.setRowHeight(1, 65)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(1, 0, item)

        item = QtWidgets.QTableWidgetItem('有轻微肌肉收缩，但不能引起关节活动')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(1, 1, item)

        item = QtWidgets.QTableWidgetItem('10')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(1, 2, item)

        item = QtWidgets.QTableWidgetItem('2')
        self.tableWidget.setRowHeight(2, 65)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(2, 0, item)

        item = QtWidgets.QTableWidgetItem('在减重状态下，能作关节全范围运动')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(2, 1, item)

        item = QtWidgets.QTableWidgetItem('25')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(2, 2, item)

        item = QtWidgets.QTableWidgetItem('3')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setRowHeight(3, 67)
        self.tableWidget.setItem(3, 0, item)

        item = QtWidgets.QTableWidgetItem('能抗重力作关节全范围运动，但不能抗阻力')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(3, 1, item)

        item = QtWidgets.QTableWidgetItem('50')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(3, 2, item)

        item = QtWidgets.QTableWidgetItem('4')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setRowHeight(4, 67)
        self.tableWidget.setItem(4, 0, item)

        item = QtWidgets.QTableWidgetItem('能抗重力，抵抗部分阻力运动')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(4, 1, item)

        item = QtWidgets.QTableWidgetItem('75')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(4, 2, item)

        item = QtWidgets.QTableWidgetItem('5')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setVerticalHeaderItem(5, item)
        self.tableWidget.setRowHeight(5, 67)
        self.tableWidget.setItem(5, 0, item)

        item = QtWidgets.QTableWidgetItem('能抗重力，并完全抵抗阻力运动')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(5, 1, item)

        item = QtWidgets.QTableWidgetItem('100')
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(5, 2, item)

        self.label = QtWidgets.QLabel(self.frame_sub)
        self.label.setGeometry(QtCore.QRect(20, 600, 500, 40))
        self.label.setStyleSheet("font:16pt")

        self.shoulderQucomboBox = QtWidgets.QComboBox(self.frame_sub)
        self.shoulderQucomboBox.setGeometry(QtCore.QRect(490, 605, 160, 35))
        self.shoulderQucomboBox.addItems(['', '0', '1', '2', '3', '4', '5'])
        self.shoulderQucomboBox.setStyleSheet("font:12pt")

        self.label_2 = QtWidgets.QLabel(self.frame_sub)
        self.label_2.setGeometry(QtCore.QRect(680, 600, 500, 40))
        self.label_2.setStyleSheet("font:16pt")

        self.shoulderShencomboBox = QtWidgets.QComboBox(self.frame_sub)
        self.shoulderShencomboBox.setGeometry(QtCore.QRect(1140, 605, 160, 35))
        self.shoulderShencomboBox.addItems(['', '0', '1', '2', '3', '4', '5'])
        self.shoulderShencomboBox.setStyleSheet("font:12pt")

        self.label_9 = QtWidgets.QLabel(self.frame_sub)
        self.label_9.setGeometry(QtCore.QRect(20, 660, 500, 40))
        self.label_9.setStyleSheet("font:16pt")

        self.elbowQucomboBox = QtWidgets.QComboBox(self.frame_sub)
        self.elbowQucomboBox.setGeometry(QtCore.QRect(490, 665, 160, 35))
        self.elbowQucomboBox.addItems(['', '0', '1', '2', '3', '4', '5'])
        self.elbowQucomboBox.setStyleSheet("font:12pt")

        self.label_10 = QtWidgets.QLabel(self.frame_sub)
        self.label_10.setGeometry(QtCore.QRect(680, 660, 500, 40))
        self.label_10.setStyleSheet("font:16pt")

        self.elbowShencomboBox = QtWidgets.QComboBox(self.frame_sub)
        self.elbowShencomboBox.setGeometry(QtCore.QRect(1140, 665, 160, 35))
        self.elbowShencomboBox.addItems(['', '0', '1', '2', '3', '4', '5'])
        self.elbowShencomboBox.setStyleSheet("font:12pt")

        self.label_14 = QtWidgets.QLabel(self.frame_sub)
        self.label_14.setGeometry(QtCore.QRect(20, 720, 500, 40))
        self.label_14.setStyleSheet("font:16pt")

        self.wristQuJicomboBox = QtWidgets.QComboBox(self.frame_sub)
        self.wristQuJicomboBox.setGeometry(QtCore.QRect(490, 725, 160, 35))
        self.wristQuJicomboBox.addItems(['', '0', '1', '2', '3', '4', '5'])
        self.wristQuJicomboBox.setStyleSheet("font:12pt")

        self.label_11 = QtWidgets.QLabel(self.frame_sub)
        self.label_11.setGeometry(QtCore.QRect(680, 720, 500, 40))
        self.label_11.setStyleSheet("font:16pt")

        self.wristShenJicomboBox = QtWidgets.QComboBox(self.frame_sub)
        self.wristShenJicomboBox.setGeometry(QtCore.QRect(1140, 725, 160, 35))
        self.wristShenJicomboBox.addItems(['', '0', '1', '2', '3', '4', '5'])
        self.wristShenJicomboBox.setStyleSheet("font:12pt")

        self.label_12 = QtWidgets.QLabel(self.frame_sub)
        self.label_12.setGeometry(QtCore.QRect(20, 780, 500, 40))
        self.label_12.setStyleSheet("font:16pt")

        self.gripStrengthQuJicomboBox = QtWidgets.QComboBox(self.frame_sub)
        self.gripStrengthQuJicomboBox.setGeometry(QtCore.QRect(320, 785, 160, 35))
        self.gripStrengthQuJicomboBox.addItems(['', '0', '1', '2', '3', '4', '5'])
        self.gripStrengthQuJicomboBox.setStyleSheet("font:12pt")

        self.label_13 = QtWidgets.QLabel(self.frame_sub)
        self.label_13.setGeometry(QtCore.QRect(680, 780, 500, 40))
        self.label_13.setStyleSheet("font:16pt")

        self.gripStrengthShenJicomboBox = QtWidgets.QComboBox(self.frame_sub)
        self.gripStrengthShenJicomboBox.setGeometry(QtCore.QRect(970, 785, 160, 35))
        self.gripStrengthShenJicomboBox.addItems(['', '0', '1', '2', '3', '4', '5'])
        self.gripStrengthShenJicomboBox.setStyleSheet("font:12pt")

        self.label_3 = QtWidgets.QLabel(self.frame_sub)
        self.label_3.setGeometry(QtCore.QRect(20, 860, 260, 40))
        self.label_3.setStyleSheet("font:16pt")

        self.dateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.frame_sub)
        self.dateEdit.setGeometry(QtCore.QRect(200, 860, 260, 40))
        self.dateEdit.setStyleSheet("font:16pt")
        self.dateEdit.setCalendarPopup(True)

        self.saveButton = QtWidgets.QPushButton(self.frame_sub)
        self.saveButton.setGeometry(QtCore.QRect(500, 860, 120, 40))
        self.saveButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        self.uploadButton = QtWidgets.QPushButton(self.frame_sub)
        self.uploadButton.setGeometry(QtCore.QRect(680, 860, 120, 40))
        self.uploadButton.setText('导出')
        self.uploadButton.setStyleSheet("background-color:rgb(1, 144, 202);font:12pt;color:white")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "肌力"))
        self.label_4.setText(_translate("MainWindow", "MMT肌力分级标准"))
        self.label_5.setText(_translate("MainWindow", "  姓名:"))
        self.label_6.setText(_translate("MainWindow", "  性别:"))
        self.label_7.setText(_translate("MainWindow", "  年龄:"))
        self.label_8.setText(_translate("MainWindow", "  患手:"))
        self.saveButton.setText(_translate("MainWindow", "保存"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "级别"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "标准"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "相当于正常肌力%"))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        self.label.setText(_translate("MainWindow", "肩关节屈曲肌力（健侧/患侧）:"))
        self.label_2.setText(_translate("MainWindow", "肩关节伸展肌力（健侧/患侧）:"))
        self.label_9.setText(_translate("MainWindow", "肘关节屈曲肌力（健侧/患侧）:"))
        self.label_10.setText(_translate("MainWindow", "肘关节伸展肌力（健侧/患侧）:"))
        self.label_14.setText(_translate("MainWindow", "腕关节屈曲肌力（健侧/患侧）:"))
        self.label_11.setText(_translate("MainWindow", "腕关节伸展肌力（健侧/患侧）:"))
        self.label_12.setText(_translate("MainWindow", "握力（健侧/患侧）:"))
        self.label_13.setText(_translate("MainWindow", "捏力（健侧/患侧）:"))
        self.label_3.setText(_translate("MainWindow", "  评定日期:"))


class muscleStrength(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, patient_id):
        super(muscleStrength, self).__init__()
        self.setupUi(self)
        self.patient_id = patient_id

        self.patientInfo = \
            json.loads(requests.post(config.patientGetById, data={'id': self.patient_id}).content.decode('utf-8'))[
                'data']
        self.nameLabel.setText(self.patientInfo['name'])
        self.ageLabel.setText(str(self.patientInfo['age']))
        self.sexLabel.setText(self.patientInfo['sex'])
        self.unhealthHandLabel.setText(self.patientInfo['illness'])

        self.saveButton.clicked.connect(self.saveButtonClick)
        self.uploadButton.clicked.connect(self.uploadButtonClick)

    def saveButtonClick(self, *args):
        code_1 = self.shoulderQucomboBox.currentText()
        code_2 = self.shoulderShencomboBox.currentText()
        code_3 = self.elbowQucomboBox.currentText()
        code_4 = self.elbowShencomboBox.currentText()
        code_5 = self.wristQuJicomboBox.currentText()
        code_6 = self.wristShenJicomboBox.currentText()
        code_7 = self.gripStrengthQuJicomboBox.currentText()
        code_8 = self.gripStrengthShenJicomboBox.currentText()
        test_date = self.dateEdit.text().replace('/', '-')
        sheet = {'id': tool.Tools.getTimeStamp(), 'patient_id': self.patient_id, 'code_1': code_1, 'code_2': code_2,
                 'code_3': code_3, 'code_4': code_4, 'code_5': code_5, 'code_6': code_6,
                 'code_7': code_7, 'code_8': code_8, 'test_date': test_date}
        res = requests.post(config.muscleStrengthInsert, data=sheet)
        QMessageBox.information(self, "保存", '保存成功', QMessageBox.Yes, QMessageBox.Yes)
        ...



    def uploadButtonClick(self, *args):
        self.saveButton.hide()
        self.uploadButton.hide()
        img = self.grab()
        self.saveButton.show()
        self.uploadButton.show()
        path = QFileDialog.getExistingDirectory()
        img.save(
            f"{path}/{self.nameLabel.text()}_{self.dateEdit.text().replace('/', '-')}.png")
        QMessageBox.information(self, "导出", '导出成功', QMessageBox.Yes, QMessageBox.Yes)
        ...


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = muscleStrength()
    gui.show()
    sys.exit(app.exec_())
