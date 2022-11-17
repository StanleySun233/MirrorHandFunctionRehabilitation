# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setStyleSheet("background:rgb(242, 249, 255)")
        Form.resize(2100, 1200)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 2100, 82))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.patientInformationButton = QtWidgets.QPushButton(self.frame)
        self.patientInformationButton.setGeometry(QtCore.QRect(0, 0, 250, 80))
        self.patientInformationButton.setStyleSheet("font:16pt;background:#F5F5F5")

        self.trainingPlanButton = QtWidgets.QPushButton(self.frame)
        self.trainingPlanButton.setGeometry(QtCore.QRect(251, 0, 250, 80))
        self.trainingPlanButton.setStyleSheet("font:16pt;background:#F5F5F5")

        self.trainingLogButton = QtWidgets.QPushButton(self.frame)
        self.trainingLogButton.setGeometry(QtCore.QRect(502, 0, 250, 80))
        self.trainingLogButton.setStyleSheet("font:16pt;background:#F5F5F5")

        self.evaluateButton = QtWidgets.QPushButton(self.frame)
        self.evaluateButton.setGeometry(QtCore.QRect(753, 0, 250, 80))
        self.evaluateButton.setStyleSheet("font:16pt;background:#F5F5F5")

        self.logButton = QtWidgets.QPushButton(self.frame)
        self.logButton.setGeometry(QtCore.QRect(1004, 0, 250, 80))
        self.logButton.setStyleSheet("font:16pt;background:rgb(93, 193, 255)")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 80, 2100, 2))
        self.label.setStyleSheet("background:rgb(93, 193, 255)")

        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 83, 2100, 1118))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setStyleSheet("background:white")

        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(80, 30, 150, 40))
        self.label_2.setStyleSheet("font:14pt;")

        self.dateEdit = QtWidgets.QDateEdit(self.frame_2)
        self.dateEdit.setGeometry(QtCore.QRect(260, 25, 200, 40))
        self.dateEdit.setStyleSheet("font:14pt;")

        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(480, 30, 54, 40))
        self.label_3.setStyleSheet("font:14pt;")

        self.dateEdit_2 = QtWidgets.QDateEdit(self.frame_2)
        self.dateEdit_2.setGeometry(QtCore.QRect(520, 25, 200, 40))
        self.dateEdit_2.setStyleSheet("font:14pt;")

        self.InquireButton = QtWidgets.QPushButton(self.frame_2)
        self.InquireButton.setGeometry(QtCore.QRect(760, 25, 150, 40))
        self.InquireButton.setStyleSheet("background:rgb(93, 193, 255);font:14pt")

        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(40, 80, 2000, 1000))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setRowCount(19)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(1, 700)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.setColumnWidth(2, 940)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.setColumnWidth(3, 200)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        self.showLabel = QtWidgets.QLabel(self.frame_2)
        self.showLabel.setGeometry(QtCore.QRect(1260, 1000, 200, 40))
        self.showLabel.setObjectName("showLabel")

        self.frontButton = QtWidgets.QPushButton(self.frame_2)
        self.frontButton.setGeometry(QtCore.QRect(60, 1000, 150, 40))

        self.previousButton = QtWidgets.QPushButton(self.frame_2)
        self.previousButton.setGeometry(QtCore.QRect(210, 1000, 150, 40))

        self.nextButton = QtWidgets.QPushButton(self.frame_2)
        self.nextButton.setGeometry(QtCore.QRect(360, 1000, 150, 40))

        self.lastButton = QtWidgets.QPushButton(self.frame_2)
        self.lastButton.setGeometry(QtCore.QRect(510, 1000, 150, 40))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.patientInformationButton.setText(_translate("Form", "病人信息"))
        self.trainingPlanButton.setText(_translate("Form", "训练方案"))
        self.trainingLogButton.setText(_translate("Form", "训练日志"))
        self.evaluateButton.setText(_translate("Form", "评估量表"))
        self.logButton.setText(_translate("Form", "日志报表"))
        self.label_2.setText(_translate("Form", "训练日期"))
        self.label_3.setText(_translate("Form", "-"))
        self.InquireButton.setText(_translate("Form", "查询"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "训练日期"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "训练"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", ""))

        self.showLabel.setText(_translate("Form", "显示当前多少页"))
        self.frontButton.setText(_translate("Form", "首页"))
        self.previousButton.setText(_translate("Form", "上一页"))
        self.nextButton.setText(_translate("Form", "下一页"))
        self.lastButton.setText(_translate("Form", "尾页"))


class log(QtWidgets.QMainWindow, Ui_Form):  # 日志报表
    def __init__(self):
        super(log, self).__init__()
        self.setupUi(self)
        self.InquireButton.mousePressEvent = self.InquireButtonClick
        self.showLabel.mousePressEvent = self.showLabelClick
        self.frontButton.mousePressEvent = self.frontButtonClick
        self.nextButton.mousePressEvent = self.nextButtonClick
        self.previousButton.mousePressEvent = self.previousButtonClick
        self.lastButton.mousePressEvent = self.lastClick

    def InquireButtonClick(self, *args):  # 查询
        ...

    def showLabelClick(self, *args):  # 显示当前页数

        ...

    def frontButtonClick(self, *args):  # 首页

        ...

    def previousButtonClick(self, *args):  # 上一页

        ...

    def nextButtonClick(self, *args):  # 下一页

        ...

    def lastClick(self, *args):  # 尾页
        ...


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = log()
    gui.show()
    sys.exit(app.exec_())
