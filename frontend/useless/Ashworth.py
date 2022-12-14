# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.frame_sub = QtWidgets.QFrame(self.centralwidget)
        self.frame_sub.setGeometry(QtCore.QRect(0, 0,1500, 1000))
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

        self.label_6 = QtWidgets.QLabel(self.frame_sub)
        self.label_6.setGeometry(QtCore.QRect(380, 80, 300, 40))
        self.label_6.setStyleSheet("font:12pt")

        self.label_7 = QtWidgets.QLabel(self.frame_sub)
        self.label_7.setGeometry(QtCore.QRect(680, 80, 300, 40))
        self.label_7.setStyleSheet("font:12pt")

        self.label_8 = QtWidgets.QLabel(self.frame_sub)
        self.label_8.setGeometry(QtCore.QRect(980, 80, 300, 40))
        self.label_8.setStyleSheet("font:12pt")


        self.tableWidget = QtWidgets.QTableWidget(self.frame_sub)
        self.tableWidget.setGeometry(QtCore.QRect(80, 140,1350, 650))

        self.tableWidget.setFrameShape(QtWidgets.QFrame.Panel)
        self.tableWidget.setAutoScrollMargin(100)

        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        self.tableWidget.setRowHeight(0, 100)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        self.tableWidget.setRowHeight(1,100)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        self.tableWidget.setRowHeight(2, 100)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        self.tableWidget.setRowHeight(3, 100)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        self.tableWidget.setRowHeight(4, 100)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        self.tableWidget.setRowHeight(5, 110)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.setColumnWidth(0,1290)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        self.tableWidget.setStyleSheet("font:14pt")
        self.tableWidget.setStyleSheet("background:white")



        self.label = QtWidgets.QLabel(self.frame_sub)
        self.label.setGeometry(QtCore.QRect(80, 800, 260, 40))
        self.label.setStyleSheet("font:16pt")

        self.shenJicomboBox = QtWidgets.QComboBox(self.frame_sub)#伸肌评定结果
        self.shenJicomboBox.setGeometry(QtCore.QRect(300, 800, 160,35))
        self.shenJicomboBox.addItems(['','0级','1级','1级+','2级','3级','4级','5级'])
        self.shenJicomboBox.setStyleSheet("font:12pt")

        self.label_2 = QtWidgets.QLabel(self.frame_sub)
        self.label_2.setGeometry(QtCore.QRect(480,800, 260, 40))
        self.label_2.setStyleSheet("font:16pt")

        self.quJicomboBox= QtWidgets.QComboBox(self.frame_sub)
        self.quJicomboBox.setGeometry(QtCore.QRect(690, 800, 160,35))
        self.quJicomboBox.addItems(['', '0级', '1级', '1级+', '2级', '3级', '4级', '5级'])
        self.quJicomboBox.setStyleSheet("font:12pt")

        self.label_3 = QtWidgets.QLabel(self.frame_sub)
        self.label_3.setGeometry(QtCore.QRect(80, 880, 260, 40))
        self.label_3.setStyleSheet("font:16pt")

        self.dateEdit = QtWidgets.QDateEdit(self.frame_sub)
        self.dateEdit.setGeometry(QtCore.QRect(270, 880, 260, 40))
        self.dateEdit.setStyleSheet("font:16pt")

        self.saveButton = QtWidgets.QPushButton(self.frame_sub)
        self.saveButton.setGeometry(QtCore.QRect(640, 880, 140, 40))
        self.saveButton.setStyleSheet("background-color:rgb(1, 144, 202);\n")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "  改良Ashworth分级"))
        self.label_5.setText(_translate("MainWindow", "  姓名"))
        self.label_6.setText(_translate("MainWindow", "  性别"))
        self.label_7.setText(_translate("MainWindow", "  年龄"))
        self.label_8.setText(_translate("MainWindow", "  患手"))
        self.label_9.setText(_translate("MainWindow", "  分级"))
        self.saveButton.setText(_translate("MainWindow", "保存"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", " 0 级"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", " 1 级"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", " 1+级"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", " 2 级"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", " 3 级"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", " 4 级"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "评定标准"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "无肌张力的增加"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "肌张力略微增加；受累部分被动屈伸时，在关节活动范围指末时呈现最小的阻力或出现突然卡住和释放"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "肌张力轻度增加：在关节活动范围后50%范围内出现突然卡住，并在关节活动范围的后50%均呈现最小的阻力"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "肌张力较明显地增加：通过关节活动范围的大部分时，肌张力均较明显地增加，但受累部分仍然能较容易地被移动"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "肌张力严重增高：被动运动困难"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("MainWindow", "僵直：受累部分被动屈伸时呈现僵直状态，不能活动"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "伸肌评定结果:"))
        self.label_2.setText(_translate("MainWindow", "屈肌评定结果:"))
        self.label_3.setText(_translate("MainWindow", "  评定日期:"))



class Ashworth(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Ashworth, self).__init__()
        self.setupUi(self)
        self.saveButton.mousePressEvent=self.saveButtonClick

    def saveButtonClick(self, *args):
        ...



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Ashworth()
    gui.show()
    sys.exit(app.exec_())