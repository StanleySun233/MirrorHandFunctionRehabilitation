import json
import sys
import cv2
import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QDateTime, QTimer, Qt, QDate
from PyQt5.QtWidgets import QToolButton, QMenu, QTableWidgetItem, QHeaderView, QTableWidget, QAbstractItemView

import config
import frontend


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1080)
        self.accountId = 0
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1920, 80))
        self.frame.setStyleSheet("background:rgb(85, 170, 255)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 500, 50))
        self.label.setStyleSheet("font:16pt;color:white")

        self.changePasswordLabel = QtWidgets.QLabel(self.frame)  # 主界面-密码修改
        self.changePasswordLabel.setGeometry(QtCore.QRect(1600, 5, 120, 40))
        self.changePasswordLabel.setStyleSheet("color:white;font:12pt")

        self.exitSystemLabel = QtWidgets.QLabel(self.frame)  # 主界面-退出系统
        self.exitSystemLabel.setGeometry(QtCore.QRect(1760, 5, 120, 40))
        self.exitSystemLabel.setStyleSheet("color:white;font:12pt")

        self.showTimeLabel = QtWidgets.QLabel(self.frame)  # 主界面-显示时间
        self.showTimeLabel.setGeometry(QtCore.QRect(1600, 45, 500, 30))
        self.showTimeLabel.setStyleSheet("font:12pt\n")

        self.mainFrame = QtWidgets.QFrame(Form)
        self.mainFrame.setGeometry(QtCore.QRect(0, 80, 1920, 930))
        self.mainFrame.setStyleSheet("background:rgb(242,249,255)")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.dataBaseFrame = QtWidgets.QFrame(self.mainFrame)
        self.dataBaseFrame.setGeometry(QtCore.QRect(10, 10, 500, 910))
        self.dataBaseFrame.setStyleSheet("background:white")
        self.dataBaseFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dataBaseFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.dataBase_inquireFrame = QtWidgets.QFrame(self.dataBaseFrame)
        self.dataBase_inquireFrame.setGeometry(QtCore.QRect(0, 0, 500, 100))
        self.dataBase_inquireFrame.setStyleSheet("background:rgb(85, 170, 255)")
        self.dataBase_inquireFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dataBase_inquireFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.label_3 = QtWidgets.QLabel(self.dataBase_inquireFrame)
        self.label_3.setGeometry(QtCore.QRect(20, 5, 200, 40))
        self.label_3.setStyleSheet("font:12pt;color:white")

        # 主界面-数据库-关键字查询
        self.databaseNameQueryLineEdit = QtWidgets.QLineEdit(self.dataBase_inquireFrame)
        self.databaseNameQueryLineEdit.setGeometry(QtCore.QRect(10, 50, 300, 40))
        self.databaseNameQueryLineEdit.setStyleSheet("background:white;font:12pt\n")

        # 主界面-数据库-简单查询
        self.databaseSimpleQueryButton = QtWidgets.QPushButton(self.dataBase_inquireFrame)
        self.databaseSimpleQueryButton.setGeometry(QtCore.QRect(320, 50, 80, 40))
        self.databaseSimpleQueryButton.setStyleSheet("font:10pt;color:white;background: rgb(0,138,200)")

        # 主界面-数据库-高级查询
        self.dataBase_highLevelInquireButton = QtWidgets.QPushButton(self.dataBase_inquireFrame)
        self.dataBase_highLevelInquireButton.setGeometry(QtCore.QRect(410, 50, 80, 40))
        self.dataBase_highLevelInquireButton.setStyleSheet("font:10pt;color:white;background: rgb(0,138,200)")

        # 主界面-数据库-表格
        self.patientInfoTable = QtWidgets.QTableWidget(self.dataBaseFrame)
        self.patientInfoTable.setGeometry(QtCore.QRect(0, 100, 600, 750))
        self.patientInfoTable.setStyleSheet("background:rgb(255,182,193)")

        # 主界面-数据库-首页
        self.databaseHeadPageButton = QtWidgets.QPushButton(self.dataBaseFrame)
        self.databaseHeadPageButton.setGeometry(QtCore.QRect(10, 860, 100, 40))

        # 主界面-数据库-上一页
        self.dataBasePriorPageButton = QtWidgets.QPushButton(self.dataBaseFrame)
        self.dataBasePriorPageButton.setGeometry(QtCore.QRect(130, 860, 100, 40))

        # 主界面-数据库-下一页
        self.databaseNextPageButton = QtWidgets.QPushButton(self.dataBaseFrame)
        self.databaseNextPageButton.setGeometry(QtCore.QRect(250, 860, 100, 40))

        # 主界面-数据库-尾页
        self.databaseTailPageButton = QtWidgets.QPushButton(self.dataBaseFrame)
        self.databaseTailPageButton.setGeometry(QtCore.QRect(370, 860, 100, 40))

        self.label_4 = QtWidgets.QLabel(self.mainFrame)
        self.label_4.setGeometry(QtCore.QRect(520, 65, 1390, 3))
        self.label_4.setStyleSheet("background:rgb(0,138,200)")

        # 主界面-数据库-病人基本信息
        self.patientBasicInformationButton = QtWidgets.QPushButton(self.mainFrame)
        self.patientBasicInformationButton.setGeometry(QtCore.QRect(520, 10, 200, 55))
        self.patientBasicInformationButton.setStyleSheet("font:12pt;background:white;font:12pt")

        # 主界面-数据库-训练方案
        self.trainingProgramButton = QtWidgets.QPushButton(self.mainFrame)
        self.trainingProgramButton.setGeometry(QtCore.QRect(720, 10, 200, 55))
        self.trainingProgramButton.setStyleSheet("font:12pt;background:white\n")

        # 主界面-数据库-训练日志
        self.trainingLogButton = QtWidgets.QPushButton(self.mainFrame)
        self.trainingLogButton.setGeometry(QtCore.QRect(920, 10, 200, 55))
        self.trainingLogButton.setStyleSheet("font:12pt;background:white\n")

        # 主界面-数据库-随访评估
        self.evaluateButton = QtWidgets.QPushButton(self.mainFrame)
        self.evaluateButton.setGeometry(QtCore.QRect(1120, 10, 200, 55))
        self.evaluateButton.setStyleSheet("font:12pt;background:white\n")

        # 主界面-数据库-日志报表
        self.logButton = QtWidgets.QPushButton(self.mainFrame)
        self.logButton.setGeometry(QtCore.QRect(1320, 10, 200, 55))
        self.logButton.setStyleSheet("font:12pt;background:white")

        self.stackedWidget = QtWidgets.QStackedWidget(self.mainFrame)
        self.stackedWidget.setGeometry(QtCore.QRect(520, 70, 1390, 910))

        self.page = QtWidgets.QWidget()

        self.label_5 = QtWidgets.QLabel(self.page)  # 详细信息
        self.label_5.setGeometry(QtCore.QRect(30, 10, 120, 40))
        self.label_5.setStyleSheet("font:14pt\n")

        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(30, 65, 54, 20))
        self.label_6.setStyleSheet("font:12pt;color:red\n")

        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(50, 60, 54, 30))
        self.label_7.setStyleSheet("font:12pt\n")

        self.patientInfoNameLineEdit = QtWidgets.QLineEdit(self.page)
        self.patientInfoNameLineEdit.setGeometry(QtCore.QRect(110, 55, 160, 40))
        self.patientInfoNameLineEdit.setStyleSheet("font:12pt;background:white")

        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setGeometry(QtCore.QRect(290, 60, 54, 30))
        self.label_8.setStyleSheet("font:12pt;color:red\n")

        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setGeometry(QtCore.QRect(310, 60, 100, 30))
        self.label_9.setStyleSheet("font:12pt\n")

        self.patientInfoIdTypeComboBox = QtWidgets.QComboBox(self.page)
        self.patientInfoIdTypeComboBox.setGeometry(QtCore.QRect(390, 55, 200, 40))
        self.patientInfoIdTypeComboBox.setStyleSheet("font:12pt;background:white")
        self.patientInfoIdTypeComboBox.addItems(['身份证', '士官证', '护照', '港澳通行证', '其它'])

        self.patientInfoIdLineEdit = QtWidgets.QLineEdit(self.page)
        self.patientInfoIdLineEdit.setGeometry(QtCore.QRect(600, 55, 260, 40))
        self.patientInfoIdLineEdit.setStyleSheet("font:12pt;background:white")

        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setGeometry(QtCore.QRect(880, 60, 54, 30))
        self.label_10.setStyleSheet("font:12pt\n")

        self.patientInfoSexComboBox = QtWidgets.QComboBox(self.page)
        self.patientInfoSexComboBox.setGeometry(QtCore.QRect(940, 55, 120, 40))
        self.patientInfoSexComboBox.addItems(['男', '女'])
        self.patientInfoSexComboBox.setStyleSheet("font:12pt;background:white")

        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(1080, 60, 100, 40))
        self.label_11.setStyleSheet("font:12pt\n")

        self.patientInfoAgeLineEdit = QtWidgets.QLineEdit(self.page)
        self.patientInfoAgeLineEdit.setGeometry(QtCore.QRect(1140, 55, 120, 40))
        self.patientInfoAgeLineEdit.setStyleSheet("font:12pt;background:white")

        self.label_12 = QtWidgets.QLabel(self.page)
        self.label_12.setGeometry(QtCore.QRect(50, 120, 120, 40))
        self.label_12.setStyleSheet("font:12pt\n")

        self.patientInfoTelLineEdit = QtWidgets.QLineEdit(self.page)
        self.patientInfoTelLineEdit.setGeometry(QtCore.QRect(110, 115, 250, 40))
        self.patientInfoTelLineEdit.setStyleSheet("font:12pt;background:white")

        self.label_13 = QtWidgets.QLabel(self.page)
        self.label_13.setGeometry(QtCore.QRect(380, 120, 120, 40))
        self.label_13.setStyleSheet("font:12pt\n")

        self.patientInfoEducationCombobox = QtWidgets.QComboBox(self.page)
        self.patientInfoEducationCombobox.setGeometry(QtCore.QRect(480, 115, 150, 40))
        self.patientInfoEducationCombobox.addItems(['小学', '初中', '高中', '大学', '无'])
        self.patientInfoEducationCombobox.setStyleSheet("font:12pt;background:white")

        self.label_14 = QtWidgets.QLabel(self.page)
        self.label_14.setGeometry(QtCore.QRect(650, 120, 150, 40))
        self.label_14.setStyleSheet("font:12pt\n")

        self.patientInfoJobLineEdit = QtWidgets.QLineEdit(self.page)
        self.patientInfoJobLineEdit.setGeometry(QtCore.QRect(710, 115, 200, 40))
        self.patientInfoJobLineEdit.setStyleSheet("font:12pt;background:white")

        self.label_39 = QtWidgets.QLabel(self.page)
        self.label_39.setGeometry(QtCore.QRect(920, 120, 200, 40))
        self.label_39.setStyleSheet("font:12pt\n")

        self.patientInformAidDateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.page)
        self.patientInformAidDateEdit.setGeometry(QtCore.QRect(1030, 115, 200, 40))
        self.patientInformAidDateEdit.setStyleSheet("background:white;font:12pt\n")
        self.patientInformAidDateEdit.setCalendarPopup(True)

        self.label_15 = QtWidgets.QLabel(self.page)
        self.label_15.setGeometry(QtCore.QRect(50, 180, 54, 40))
        self.label_15.setStyleSheet("font:12pt\n")

        self.patientInfoHandedCombobox = QtWidgets.QComboBox(self.page)
        self.patientInfoHandedCombobox.setGeometry(QtCore.QRect(110, 175, 120, 40))
        self.patientInfoHandedCombobox.addItems(['', '左', '右'])
        self.patientInfoHandedCombobox.setStyleSheet("font:12pt;background:white")

        self.label_16 = QtWidgets.QLabel(self.page)
        self.label_16.setGeometry(QtCore.QRect(240, 180, 54, 40))
        self.label_16.setStyleSheet("font:12pt\n")

        self.patientInfoIllnessComboBox = QtWidgets.QComboBox(self.page)
        self.patientInfoIllnessComboBox.setGeometry(QtCore.QRect(300, 175, 120, 40))
        self.patientInfoIllnessComboBox.addItems(['', '左', '右'])
        self.patientInfoIllnessComboBox.setStyleSheet("font:12pt;background:white")

        self.label_17 = QtWidgets.QLabel(self.page)
        self.label_17.setGeometry(QtCore.QRect(440, 180, 120, 40))
        self.label_17.setStyleSheet("font:12pt\n")

        self.patientInformation_diseaseTypeComboBox_1 = QtWidgets.QComboBox(self.page)
        self.patientInformation_diseaseTypeComboBox_1.setGeometry(QtCore.QRect(550, 175, 200, 40))
        self.patientInformation_diseaseTypeComboBox_1.addItems(
            ['', '脑卒中', '脑外伤', '颅脑损伤', '周围神经损伤', '乳腺癌术后', '疼痛', '认知障碍', '脊髓损伤', '自定义'])
        self.patientInformation_diseaseTypeComboBox_1.setStyleSheet("font:12pt;background:white")

        self.patientInformation_diseaseTypeFrame1 = QtWidgets.QFrame(self.page)
        self.patientInformation_diseaseTypeFrame1.setGeometry(QtCore.QRect(760, 175, 200, 40))
        self.patientInformation_diseaseTypeFrame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.patientInformation_diseaseTypeFrame1.setFrameShadow(QtWidgets.QFrame.Raised)

        self.patientInformation_diseaseTypeComboBox_2 = QtWidgets.QComboBox(self.patientInformation_diseaseTypeFrame1)
        self.patientInformation_diseaseTypeComboBox_2.setGeometry(QtCore.QRect(0, 0, 200, 40))
        self.patientInformation_diseaseTypeComboBox_2.addItems(['', '脑梗死', '脑出血'])
        self.patientInformation_diseaseTypeComboBox_2.setStyleSheet("font:12pt;background:white")

        self.patientInformation_diseaseTypeFrame1_2 = QtWidgets.QFrame(self.page)
        self.patientInformation_diseaseTypeFrame1_2.setGeometry(QtCore.QRect(760, 175, 200, 40))
        self.patientInformation_diseaseTypeFrame1_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.patientInformation_diseaseTypeFrame1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.patientInformation_diseaseTypeFrame1_2.setVisible(False)

        self.patientInformation_diseaseTypeLineEdit = QtWidgets.QLineEdit(self.patientInformation_diseaseTypeFrame1_2)
        self.patientInformation_diseaseTypeLineEdit.setGeometry(QtCore.QRect(0, 0, 200, 40))
        self.patientInformation_diseaseTypeLineEdit.setStyleSheet("font:12pt;background:white")

        self.label_18 = QtWidgets.QLabel(self.page)
        self.label_18.setGeometry(QtCore.QRect(980, 180, 200, 40))
        self.label_18.setStyleSheet("font:12pt\n")

        self.patientInformation_cognititveSituationComboBox = QtWidgets.QComboBox(self.page)
        self.patientInformation_cognititveSituationComboBox.setGeometry(QtCore.QRect(1080, 175, 200, 40))
        self.patientInformation_cognititveSituationComboBox.addItems(['优', '良', '差'])
        self.patientInformation_cognititveSituationComboBox.setStyleSheet("font:12pt;background:white")

        self.patientInformation_brainInjuryAreaFrame = QtWidgets.QFrame(self.page)
        self.patientInformation_brainInjuryAreaFrame.setGeometry(QtCore.QRect(30, 235, 1330, 310))
        self.patientInformation_brainInjuryAreaFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.patientInformation_brainInjuryAreaFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.patientInformation_brainInjuryAreaFrame.setVisible(False)

        self.patientInformation_frontalLobeCheckBox = QtWidgets.QCheckBox(self.patientInformation_brainInjuryAreaFrame)
        self.patientInformation_frontalLobeCheckBox.setGeometry(QtCore.QRect(10, 10, 120, 40))
        self.patientInformation_frontalLobeCheckBox.setStyleSheet("font:12pt")

        self.patientInformation_occipitalLobeCheckBox = QtWidgets.QCheckBox(
            self.patientInformation_brainInjuryAreaFrame)
        self.patientInformation_occipitalLobeCheckBox.setGeometry(QtCore.QRect(150, 10, 120, 40))
        self.patientInformation_occipitalLobeCheckBox.setStyleSheet("font:12pt")

        self.patientInformation_basalGangliaCheckBox = QtWidgets.QCheckBox(self.patientInformation_brainInjuryAreaFrame)
        self.patientInformation_basalGangliaCheckBox.setGeometry(QtCore.QRect(290, 10, 120, 40))
        self.patientInformation_basalGangliaCheckBox.setStyleSheet("font:12pt")

        self.patientInformation_cerebellumCheckBox = QtWidgets.QCheckBox(self.patientInformation_brainInjuryAreaFrame)
        self.patientInformation_cerebellumCheckBox.setGeometry(QtCore.QRect(430, 10, 120, 40))
        self.patientInformation_cerebellumCheckBox.setStyleSheet("font:12pt")

        self.patientInformation_parietalLobeCheckBox = QtWidgets.QCheckBox(self.patientInformation_brainInjuryAreaFrame)
        self.patientInformation_parietalLobeCheckBox.setGeometry(QtCore.QRect(570, 10, 120, 40))
        self.patientInformation_parietalLobeCheckBox.setStyleSheet("font:12pt")

        self.patientInformation_internalCapsuleCheckBox = QtWidgets.QCheckBox(
            self.patientInformation_brainInjuryAreaFrame)
        self.patientInformation_internalCapsuleCheckBox.setGeometry(QtCore.QRect(730, 10, 120, 40))
        self.patientInformation_internalCapsuleCheckBox.setStyleSheet("font:12pt")

        self.patientInformation_halfEggAreaCheckBox = QtWidgets.QCheckBox(self.patientInformation_brainInjuryAreaFrame)
        self.patientInformation_halfEggAreaCheckBox.setGeometry(QtCore.QRect(870, 10, 120, 40))
        self.patientInformation_halfEggAreaCheckBox.setStyleSheet("font:12pt")

        self.patientInformation_brainStemCheckBox = QtWidgets.QCheckBox(self.patientInformation_brainInjuryAreaFrame)
        self.patientInformation_brainStemCheckBox.setGeometry(QtCore.QRect(10, 70, 120, 40))
        self.patientInformation_brainStemCheckBox.setStyleSheet("font:12pt")

        self.patientInformation_temporalLobeCheckBox = QtWidgets.QCheckBox(self.patientInformation_brainInjuryAreaFrame)
        self.patientInformation_temporalLobeCheckBox.setGeometry(QtCore.QRect(150, 70, 120, 40))
        self.patientInformation_temporalLobeCheckBox.setStyleSheet("font:12pt")

        self.patientInformation_outerCapsuleCheckBox = QtWidgets.QCheckBox(self.patientInformation_brainInjuryAreaFrame)
        self.patientInformation_outerCapsuleCheckBox.setGeometry(QtCore.QRect(290, 70, 120, 40))
        self.patientInformation_outerCapsuleCheckBox.setStyleSheet("font:12pt")

        self.patientInformation_thalamusCheckBox = QtWidgets.QCheckBox(self.patientInformation_brainInjuryAreaFrame)
        self.patientInformation_thalamusCheckBox.setGeometry(QtCore.QRect(430, 70, 120, 40))
        self.patientInformation_thalamusCheckBox.setStyleSheet("font:12pt")
        self.patientInformation_thalamusCheckBox.setObjectName("patientInformation_thalamusCheckBox")

        self.label_19 = QtWidgets.QLabel(self.patientInformation_brainInjuryAreaFrame)
        self.label_19.setGeometry(QtCore.QRect(10, 130, 100, 40))
        self.label_19.setStyleSheet("font:12pt\n")

        self.patientInformation_diseaseCourseComboBox = QtWidgets.QComboBox(
            self.patientInformation_brainInjuryAreaFrame)
        self.patientInformation_diseaseCourseComboBox.setGeometry(QtCore.QRect(80, 125, 300, 40))
        self.patientInformation_diseaseCourseComboBox.addItems(['', '急性期（0-3个月）', '亚急性期（3-6个月）', '慢性期（6个月以上）'])
        self.patientInformation_diseaseCourseComboBox.setStyleSheet("font:12pt;background:white")

        self.label_20 = QtWidgets.QLabel(self.patientInformation_brainInjuryAreaFrame)
        self.label_20.setGeometry(QtCore.QRect(400, 130, 180, 40))
        self.label_20.setStyleSheet("font:12pt\n")

        self.patientInformation_BurnnstormComboBox = QtWidgets.QComboBox(self.patientInformation_brainInjuryAreaFrame)
        self.patientInformation_BurnnstormComboBox.setGeometry(QtCore.QRect(580, 125, 600, 40))
        self.patientInformation_BurnnstormComboBox.addItems(
            ['', 'Ⅰ-Ⅱ（无或极细微运动）', 'Ⅲ-Ⅳ（全指屈曲或轻微手指伸展）', 'Ⅴ-Ⅵ（拇指运动、伴随意屈伸/手指部分伸展）'])
        self.patientInformation_BurnnstormComboBox.setStyleSheet("font:12pt;background:white")

        self.label_21 = QtWidgets.QLabel(self.patientInformation_brainInjuryAreaFrame)
        self.label_21.setGeometry(QtCore.QRect(10, 190, 150, 40))
        self.label_21.setStyleSheet("font:12pt\n")

        self.label_22 = QtWidgets.QLabel(self.patientInformation_brainInjuryAreaFrame)
        self.label_22.setGeometry(QtCore.QRect(220, 190, 100, 40))
        self.label_22.setStyleSheet("font:12pt")

        self.patientInformation_elbowJointQuComboBox = QtWidgets.QComboBox(self.patientInformation_brainInjuryAreaFrame)
        self.patientInformation_elbowJointQuComboBox.setGeometry(QtCore.QRect(300, 185, 150, 40))
        self.patientInformation_elbowJointQuComboBox.addItems(['', '0-1级', '1+级', '2级'])
        self.patientInformation_elbowJointQuComboBox.setStyleSheet("font:12pt;background:white")

        self.label_23 = QtWidgets.QLabel(self.patientInformation_brainInjuryAreaFrame)
        self.label_23.setGeometry(QtCore.QRect(530, 190, 120, 40))
        self.label_23.setStyleSheet("font:12pt\n")

        self.patientInformation_armJointQuComboBox = QtWidgets.QComboBox(self.patientInformation_brainInjuryAreaFrame)
        self.patientInformation_armJointQuComboBox.setGeometry(QtCore.QRect(610, 185, 150, 40))
        self.patientInformation_armJointQuComboBox.addItems(['', '0-1级', '1+级', '2级'])
        self.patientInformation_armJointQuComboBox.setStyleSheet("font:12pt;background:white")

        self.label_24 = QtWidgets.QLabel(self.patientInformation_brainInjuryAreaFrame)
        self.label_24.setGeometry(QtCore.QRect(840, 190, 120, 40))
        self.label_24.setStyleSheet("font:12pt\n")

        self.patientInformation_fingerJointsQuComboBox = QtWidgets.QComboBox(
            self.patientInformation_brainInjuryAreaFrame)
        self.patientInformation_fingerJointsQuComboBox.setGeometry(QtCore.QRect(950, 185, 150, 40))
        self.patientInformation_fingerJointsQuComboBox.addItems(['', '0-1级', '1+级', '2级'])
        self.patientInformation_fingerJointsQuComboBox.setStyleSheet("font:12pt;background:white")

        self.label_25 = QtWidgets.QLabel(self.patientInformation_brainInjuryAreaFrame)
        self.label_25.setGeometry(QtCore.QRect(10, 250, 150, 40))
        self.label_25.setStyleSheet("font:12pt\n")

        self.label_33 = QtWidgets.QLabel(self.patientInformation_brainInjuryAreaFrame)
        self.label_33.setGeometry(QtCore.QRect(220, 250, 100, 40))
        self.label_33.setStyleSheet("font:12pt\n")

        self.patientInformation_elbowJointShenComboBox = QtWidgets.QComboBox(
            self.patientInformation_brainInjuryAreaFrame)
        self.patientInformation_elbowJointShenComboBox.setGeometry(QtCore.QRect(300, 245, 150, 40))
        self.patientInformation_elbowJointShenComboBox.addItems(['', '0-1级', '1+级', '2级'])
        self.patientInformation_elbowJointShenComboBox.setStyleSheet("font:12pt;background:white")

        self.label_34 = QtWidgets.QLabel(self.patientInformation_brainInjuryAreaFrame)
        self.label_34.setGeometry(QtCore.QRect(530, 250, 120, 40))
        self.label_34.setStyleSheet("font:12pt\n")

        self.patientInformation_armJointShenComboBox = QtWidgets.QComboBox(self.patientInformation_brainInjuryAreaFrame)
        self.patientInformation_armJointShenComboBox.setGeometry(QtCore.QRect(610, 245, 150, 40))
        self.patientInformation_armJointShenComboBox.addItems(['', '0-1级', '1+级', '2级'])
        self.patientInformation_armJointShenComboBox.setStyleSheet("font:12pt;background:white")

        self.label_35 = QtWidgets.QLabel(self.patientInformation_brainInjuryAreaFrame)
        self.label_35.setGeometry(QtCore.QRect(840, 250, 120, 40))
        self.label_35.setStyleSheet("font:12pt\n")

        self.patientInformation_fingerJointsShenComboBox = QtWidgets.QComboBox(
            self.patientInformation_brainInjuryAreaFrame)
        self.patientInformation_fingerJointsShenComboBox.setGeometry(QtCore.QRect(950, 245, 150, 40))
        self.patientInformation_fingerJointsShenComboBox.addItems(['', '0-1级', '1+级', '2级'])
        self.patientInformation_fingerJointsShenComboBox.setStyleSheet("font:12pt;background:white")

        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setGeometry(QtCore.QRect(30, 235, 1330, 250))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)

        self.label_36 = QtWidgets.QLabel(self.frame_2)
        self.label_36.setGeometry(QtCore.QRect(10, 10, 200, 40))
        self.label_36.setStyleSheet("font:12pt\n")

        self.patientInformation_vasComboBox = QtWidgets.QComboBox(self.frame_2)
        self.patientInformation_vasComboBox.setGeometry(QtCore.QRect(180, 5, 180, 40))
        self.patientInformation_vasComboBox.addItems(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        self.patientInformation_vasComboBox.setStyleSheet("font:12pt;background:white")

        self.label_37 = QtWidgets.QLabel(self.frame_2)
        self.label_37.setGeometry(QtCore.QRect(400, 10, 150, 40))
        self.label_37.setStyleSheet("font:12pt\n")

        self.patientInformation_painfulAeraLineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.patientInformation_painfulAeraLineEdit.setGeometry(QtCore.QRect(510, 5, 800, 40))
        self.patientInformation_painfulAeraLineEdit.setStyleSheet("font:12pt;background:white")

        self.label_38 = QtWidgets.QLabel(self.frame_2)
        self.label_38.setGeometry(QtCore.QRect(20, 60, 150, 40))
        self.label_38.setStyleSheet("font:12pt\n")

        self.patientInformation_medicalHistorySummaryTextEdit = QtWidgets.QTextEdit(self.frame_2)
        self.patientInformation_medicalHistorySummaryTextEdit.setGeometry(QtCore.QRect(130, 60, 1100, 180))
        self.patientInformation_medicalHistorySummaryTextEdit.setStyleSheet("font:12pt;background:white")

        self.patientInformation_addButton = QtWidgets.QPushButton(self.page)
        self.patientInformation_addButton.setGeometry(QtCore.QRect(50, 800, 120, 50))
        self.patientInformation_addButton.setStyleSheet("font:12pt;color:white;background: rgb(0,138,200)")

        self.patientInformation_deleteButton = QtWidgets.QPushButton(self.page)
        self.patientInformation_deleteButton.setGeometry(QtCore.QRect(270, 800, 120, 50))
        self.patientInformation_deleteButton.setStyleSheet("font:12pt;color:white;background: rgb(0,138,200)")

        self.patientInformation_savaButton = QtWidgets.QPushButton(self.page)
        self.patientInformation_savaButton.setGeometry(QtCore.QRect(490, 800, 120, 50))
        self.patientInformation_savaButton.setStyleSheet("font:12pt;color:white;background: rgb(0,138,200)")
        self.stackedWidget.addWidget(self.page)

        self.page_2 = QtWidgets.QWidget()

        self.label_40 = QtWidgets.QLabel(self.page_2)
        self.label_40.setGeometry(QtCore.QRect(30, 20, 150, 40))
        self.label_40.setStyleSheet("font:12pt\n")

        self.trainingProgram_planStratdateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.page_2)
        self.trainingProgram_planStratdateEdit.setGeometry(QtCore.QRect(150, 20, 200, 40))
        self.trainingProgram_planStratdateEdit.setStyleSheet("font:12pt;background:white")
        self.trainingProgram_planStratdateEdit.setCalendarPopup(True)

        self.label_41 = QtWidgets.QLabel(self.page_2)
        self.label_41.setGeometry(QtCore.QRect(360, 20, 150, 40))
        self.label_41.setStyleSheet("font:12pt\n")

        self.trainingProgram_planEnddateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.page_2)
        self.trainingProgram_planEnddateEdit.setGeometry(QtCore.QRect(400, 20, 200, 40))
        self.trainingProgram_planEnddateEdit.setStyleSheet("font:12pt;background:white")
        self.trainingProgram_planEnddateEdit.setCalendarPopup(True)

        self.traingProgram_inquireButton = QtWidgets.QPushButton(self.page_2)
        self.traingProgram_inquireButton.setGeometry(QtCore.QRect(630, 20, 150, 45))
        self.traingProgram_inquireButton.setStyleSheet("font:12pt;color:white;background: rgb(0,138,200)")

        self.traingProgram_addButton = QtWidgets.QPushButton(self.page_2)
        self.traingProgram_addButton.setGeometry(QtCore.QRect(800, 20, 150, 45))
        self.traingProgram_addButton.setStyleSheet("font:12pt;color:white;background: rgb(0,138,200)")

        self.trainingProgram_tableWidget = QtWidgets.QTableWidget(self.page_2)
        self.trainingProgram_tableWidget.setGeometry(QtCore.QRect(30, 70, 1330, 700))
        self.trainingProgram_tableWidget.setStyleSheet("background:white;font:12pt")
        self.trainingProgram_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.trainingProgram_showPageLabel = QtWidgets.QLabel(self.page_2)
        self.trainingProgram_showPageLabel.setGeometry(QtCore.QRect(850, 790, 150, 40))
        self.trainingProgram_showPageLabel.setStyleSheet("font:12pt\n")
        self.stackedWidget.addWidget(self.page_2)

        self.page_3 = QtWidgets.QWidget()

        self.label_42 = QtWidgets.QLabel(self.page_3)
        self.label_42.setGeometry(QtCore.QRect(10, 20, 250, 40))
        self.label_42.setStyleSheet("font:12pt")

        self.trainingLog_trainingModeComboBox = QtWidgets.QComboBox(self.page_3)
        self.trainingLog_trainingModeComboBox.setGeometry(QtCore.QRect(110, 20, 250, 40))
        self.trainingLog_trainingModeComboBox.addItems(['', '空间想象训练', '感觉运动观察训练', '基本动作运动训练', '功能动作运动训练'])
        self.trainingLog_trainingModeComboBox.setStyleSheet("font:12pt;background:white")

        self.label_43 = QtWidgets.QLabel(self.page_3)
        self.label_43.setGeometry(QtCore.QRect(380, 20, 120, 40))
        self.label_43.setStyleSheet("font:12pt")

        self.trainingLog_trainingStartDateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.page_3)
        self.trainingLog_trainingStartDateEdit.setGeometry(QtCore.QRect(490, 20, 200, 40))
        self.trainingLog_trainingStartDateEdit.setStyleSheet("font:12pt;background:white")
        self.trainingLog_trainingStartDateEdit.setCalendarPopup(True)

        self.label_44 = QtWidgets.QLabel(self.page_3)
        self.label_44.setGeometry(QtCore.QRect(700, 20, 120, 40))
        self.label_44.setStyleSheet("font:12pt")

        self.trainingLog_trainingEndDateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.page_3)
        self.trainingLog_trainingEndDateEdit.setGeometry(QtCore.QRect(730, 20, 200, 40))
        self.trainingLog_trainingEndDateEdit.setStyleSheet("font:12pt;background:white")
        self.trainingLog_trainingEndDateEdit.setCalendarPopup(True)

        self.trainingLog_inquireButton = QtWidgets.QPushButton(self.page_3)
        self.trainingLog_inquireButton.setGeometry(QtCore.QRect(980, 20, 120, 40))
        self.trainingLog_inquireButton.setStyleSheet("font:12pt;color:white;background: rgb(0,138,200)")

        self.label_45 = QtWidgets.QLabel(self.page_3)
        self.label_45.setGeometry(QtCore.QRect(0, 131, 1591, 2))
        self.label_45.setStyleSheet("background:rgb(0,138,200)")

        self.trainingLog_trainingListButton = QtWidgets.QPushButton(self.page_3)
        self.trainingLog_trainingListButton.setGeometry(QtCore.QRect(0, 90, 150, 40))
        self.trainingLog_trainingListButton.setStyleSheet("font:12pt;background:rgb(0,138,200);color:white")

        self.trainingLog_summaryGraphButton = QtWidgets.QPushButton(self.page_3)
        self.trainingLog_summaryGraphButton.setGeometry(QtCore.QRect(151, 90, 150, 40))
        self.trainingLog_summaryGraphButton.setStyleSheet("font:12pt;background:rgb(0,138,200);color:white")

        self.trainingLog_trainingListFrame = QtWidgets.QFrame(self.page_3)
        self.trainingLog_trainingListFrame.setGeometry(QtCore.QRect(0, 135, 1390, 725))
        self.trainingLog_trainingListFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.trainingLog_trainingListFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.trainingLog_tableWidget = QtWidgets.QTableWidget(self.trainingLog_trainingListFrame)
        self.trainingLog_tableWidget.setGeometry(QtCore.QRect(0, 0, 1390, 725))
        self.trainingLog_tableWidget.setStyleSheet("background:white")
        self.trainingLog_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.trainingLog_showPageLabel = QtWidgets.QLabel(self.trainingLog_trainingListFrame)
        self.trainingLog_showPageLabel.setGeometry(QtCore.QRect(720, 650, 150, 40))

        self.trainingLog_summaryGraphFrame = QtWidgets.QFrame(self.page_3)
        self.trainingLog_summaryGraphFrame.setGeometry(QtCore.QRect(0, 135, 1390, 725))
        self.trainingLog_summaryGraphFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.trainingLog_summaryGraphFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.trainingLog_summaryGraphFrame.setVisible(False)
        self.stackedWidget.addWidget(self.page_3)

        self.page_4 = QtWidgets.QWidget()

        self.label_46 = QtWidgets.QLabel(self.page_4)
        self.label_46.setGeometry(QtCore.QRect(10, 20, 120, 40))
        self.label_46.setStyleSheet("font:12pt")

        self.evaluate_startDateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.page_4)
        self.evaluate_startDateEdit.setGeometry(QtCore.QRect(120, 20, 170, 40))
        self.evaluate_startDateEdit.setStyleSheet("background:white;font:12pt")
        # 允许弹出日历控件
        self.evaluate_startDateEdit.setCalendarPopup(True)

        self.label_47 = QtWidgets.QLabel(self.page_4)
        self.label_47.setGeometry(QtCore.QRect(295, 20, 71, 40))
        self.label_47.setStyleSheet("font:12pt")

        self.evaluate_endDateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.page_4)
        self.evaluate_endDateEdit.setGeometry(QtCore.QRect(310, 20, 170, 40))
        self.evaluate_endDateEdit.setStyleSheet("background:white;font:12pt")
        self.evaluate_endDateEdit.setCalendarPopup(True)

        self.label_48 = QtWidgets.QLabel(self.page_4)
        self.label_48.setGeometry(QtCore.QRect(500, 20, 150, 40))
        self.label_48.setStyleSheet("font:12pt")

        self.evaluate_scaleTypeQToolButton = QtWidgets.QToolButton(self.page_4)
        self.evaluate_scaleTypeQToolButton.setGeometry(QtCore.QRect(620, 20, 400, 40))
        self.evaluate_scaleTypeQToolButton.setStyleSheet("color:black;font:12pt;background:white")

        self.evaluate_scaleTypeQToolButtonMainMenu = QMenu(self.evaluate_scaleTypeQToolButton)

        self.evaluate_scaleTypeBasicFunctionAssessmentQMenu = QMenu(self.evaluate_scaleTypeQToolButtonMainMenu)
        self.evaluate_scaleTypeBasicFunctionAssessmentQMenu.setTitle('基本功能评定')

        self.evaluate_scaleTypeBasicFunctionAssessmentAshworthQaction = QtWidgets.QAction(
            self.evaluate_scaleTypeBasicFunctionAssessmentQMenu)
        self.evaluate_scaleTypeBasicFunctionAssessmentAshworthQaction.setText('改良Ashworth分级')
        self.evaluate_scaleTypeBasicFunctionAssessmentMuscleQaction = QtWidgets.QAction(
            self.evaluate_scaleTypeBasicFunctionAssessmentQMenu)
        self.evaluate_scaleTypeBasicFunctionAssessmentMuscleQaction.setText('肌力（握力、捏力）')
        self.evaluate_scaleTypeBasicFunctionAssessmentMssQaction = QtWidgets.QAction(
            self.evaluate_scaleTypeBasicFunctionAssessmentQMenu)
        self.evaluate_scaleTypeBasicFunctionAssessmentMssQaction.setText('运动功能状态量表（MSS）')
        self.evaluate_scaleTypeBasicFunctionAssessmentBrunnstromQaction = QtWidgets.QAction(
            self.evaluate_scaleTypeBasicFunctionAssessmentQMenu)
        self.evaluate_scaleTypeBasicFunctionAssessmentBrunnstromQaction.setText('Brunnstrom脑卒中运动功能分级')
        self.evaluate_scaleTypeBasicFunctionAssessmentHealthHandQaction = QtWidgets.QAction(
            self.evaluate_scaleTypeBasicFunctionAssessmentQMenu)
        self.evaluate_scaleTypeBasicFunctionAssessmentHealthHandQaction.setText('利手调查量表')
        self.evaluate_scaleTypeBasicFunctionAssessmentVasQaction = QtWidgets.QAction(
            self.evaluate_scaleTypeBasicFunctionAssessmentQMenu)
        self.evaluate_scaleTypeBasicFunctionAssessmentVasQaction.setText('VAS疼痛视觉模拟')

        self.evaluate_scaleTypeBasicFunctionAssessmentQMenu.addAction(
            self.evaluate_scaleTypeBasicFunctionAssessmentAshworthQaction)
        self.evaluate_scaleTypeBasicFunctionAssessmentQMenu.addAction(
            self.evaluate_scaleTypeBasicFunctionAssessmentMuscleQaction)
        self.evaluate_scaleTypeBasicFunctionAssessmentQMenu.addAction(
            self.evaluate_scaleTypeBasicFunctionAssessmentMssQaction)
        self.evaluate_scaleTypeBasicFunctionAssessmentQMenu.addAction(
            self.evaluate_scaleTypeBasicFunctionAssessmentBrunnstromQaction)
        self.evaluate_scaleTypeBasicFunctionAssessmentQMenu.addAction(
            self.evaluate_scaleTypeBasicFunctionAssessmentHealthHandQaction)
        self.evaluate_scaleTypeBasicFunctionAssessmentQMenu.addAction(
            self.evaluate_scaleTypeBasicFunctionAssessmentVasQaction)

        self.evaluate_scaleTypeHandAndUpperLimbAssessmentQMenu = QMenu(self.evaluate_scaleTypeQToolButtonMainMenu)
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentQMenu.setTitle('手与上肢感觉运动功能评定')

        self.evaluate_scaleTypeHandAndUpperLimbAssessmentVasQaction = QtWidgets.QAction(
            self.evaluate_scaleTypeHandAndUpperLimbAssessmentQMenu)
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentVasQaction.setText('VAS疼痛视觉模拟')
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentFuglMoveQaction = QtWidgets.QAction(
            self.evaluate_scaleTypeHandAndUpperLimbAssessmentQMenu)
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentFuglMoveQaction.setText('Fugl-Meyer上肢运动功能评定')
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentFuglSensorimotorQaction = QtWidgets.QAction(
            self.evaluate_scaleTypeHandAndUpperLimbAssessmentQMenu)
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentFuglSensorimotorQaction.setText('Fugl-Meyer上肢感觉功能评定')
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentHandSensorimotorQaction = QtWidgets.QAction(
            self.evaluate_scaleTypeHandAndUpperLimbAssessmentQMenu)
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentHandSensorimotorQaction.setText('手运动功能状态评分')
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentBlockObstacleTestQaction = QtWidgets.QAction(
            self.evaluate_scaleTypeHandAndUpperLimbAssessmentQMenu)
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentBlockObstacleTestQaction.setText('积木障碍盒测试')
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentNineColumnTestQaction = QtWidgets.QAction(
            self.evaluate_scaleTypeHandAndUpperLimbAssessmentQMenu)
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentNineColumnTestQaction.setText('九孔柱测试')
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentAratQaction = QtWidgets.QAction(
            self.evaluate_scaleTypeHandAndUpperLimbAssessmentQMenu)
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentAratQaction.setText('ARAT上肢动作研究量表')
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentWolfQaction = QtWidgets.QAction(
            self.evaluate_scaleTypeHandAndUpperLimbAssessmentQMenu)
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentWolfQaction.setText('WOLF运动功能测试')

        self.evaluate_scaleTypeHandAndUpperLimbAssessmentQMenu.addAction(
            self.evaluate_scaleTypeHandAndUpperLimbAssessmentVasQaction)
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentQMenu.addAction(
            self.evaluate_scaleTypeHandAndUpperLimbAssessmentFuglMoveQaction)
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentQMenu.addAction(
            self.evaluate_scaleTypeHandAndUpperLimbAssessmentFuglSensorimotorQaction)
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentQMenu.addAction(
            self.evaluate_scaleTypeHandAndUpperLimbAssessmentHandSensorimotorQaction)
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentQMenu.addAction(
            self.evaluate_scaleTypeHandAndUpperLimbAssessmentBlockObstacleTestQaction)
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentQMenu.addAction(
            self.evaluate_scaleTypeHandAndUpperLimbAssessmentNineColumnTestQaction)
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentQMenu.addAction(
            self.evaluate_scaleTypeHandAndUpperLimbAssessmentAratQaction)
        self.evaluate_scaleTypeHandAndUpperLimbAssessmentQMenu.addAction(
            self.evaluate_scaleTypeHandAndUpperLimbAssessmentWolfQaction)

        self.evaluate_scaleTypeCognitiveFunctionAssessmentQMenu = QMenu(self.evaluate_scaleTypeQToolButtonMainMenu)
        self.evaluate_scaleTypeCognitiveFunctionAssessmentQMenu.setTitle('认知功能评定')

        self.evaluate_scaleTypeCognitiveFunctionAssessmentMocaQaction = QtWidgets.QAction(
            self.evaluate_scaleTypeCognitiveFunctionAssessmentQMenu)
        self.evaluate_scaleTypeCognitiveFunctionAssessmentMocaQaction.setText('蒙特利尔认知评估量表(MoCA)')
        self.evaluate_scaleTypeCognitiveFunctionAssessmentMmseQaction = QtWidgets.QAction(
            self.evaluate_scaleTypeCognitiveFunctionAssessmentQMenu)
        self.evaluate_scaleTypeCognitiveFunctionAssessmentMmseQaction.setText('简易智力状态检查量表（MMSE）')
        self.evaluate_scaleTypeCognitiveFunctionAssessmentBntQaction = QtWidgets.QAction(
            self.evaluate_scaleTypeCognitiveFunctionAssessmentQMenu)
        self.evaluate_scaleTypeCognitiveFunctionAssessmentBntQaction.setText('波士顿命名测试（BNT）')

        self.evaluate_scaleTypeCognitiveFunctionAssessmentQMenu.addAction(
            self.evaluate_scaleTypeCognitiveFunctionAssessmentMocaQaction)
        self.evaluate_scaleTypeCognitiveFunctionAssessmentQMenu.addAction(
            self.evaluate_scaleTypeCognitiveFunctionAssessmentMmseQaction)
        self.evaluate_scaleTypeCognitiveFunctionAssessmentQMenu.addAction(
            self.evaluate_scaleTypeCognitiveFunctionAssessmentBntQaction)

        self.evaluate_scaleTypeDailyLivingAbilityAssessmentQMenu = QMenu(self.evaluate_scaleTypeQToolButtonMainMenu)
        self.evaluate_scaleTypeDailyLivingAbilityAssessmentQMenu.setTitle('日常生活能力评定')

        self.evaluate_scaleTypeDailyLivingAbilityAssessmentMbiQaction = QtWidgets.QAction(
            self.evaluate_scaleTypeDailyLivingAbilityAssessmentQMenu)
        self.evaluate_scaleTypeDailyLivingAbilityAssessmentMbiQaction.setText('改良Barthel指数（MBI）')
        self.evaluate_scaleTypeDailyLivingAbilityAssessmentFimQaction = QtWidgets.QAction(
            self.evaluate_scaleTypeDailyLivingAbilityAssessmentQMenu)
        self.evaluate_scaleTypeDailyLivingAbilityAssessmentFimQaction.setText('功能独立性测评（FIM）')

        self.evaluate_scaleTypeDailyLivingAbilityAssessmentQMenu.addAction(
            self.evaluate_scaleTypeDailyLivingAbilityAssessmentMbiQaction)
        self.evaluate_scaleTypeDailyLivingAbilityAssessmentQMenu.addAction(
            self.evaluate_scaleTypeDailyLivingAbilityAssessmentFimQaction)

        self.evaluate_scaleTypeDailyLivingAbilityAssessmentQMenu.addAction(
            self.evaluate_scaleTypeDailyLivingAbilityAssessmentMbiQaction)
        self.evaluate_scaleTypeDailyLivingAbilityAssessmentQMenu.addAction(
            self.evaluate_scaleTypeDailyLivingAbilityAssessmentFimQaction)

        self.evaluate_scaleTypeOpticalIllusionAssessmentQMenu = QMenu(self.evaluate_scaleTypeQToolButtonMainMenu)
        self.evaluate_scaleTypeOpticalIllusionAssessmentQMenu.setTitle('视错觉评估')

        self.evaluate_scaleTypeOpticalIllusionAssessmentMirrorLeftQaction = QtWidgets.QAction(
            self.evaluate_scaleTypeOpticalIllusionAssessmentQMenu)
        self.evaluate_scaleTypeOpticalIllusionAssessmentMirrorLeftQaction.setText('镜像错觉体验调查(左)')
        self.evaluate_scaleTypeOpticalIllusionAssessmentMirrorRightQaction = QtWidgets.QAction(
            self.evaluate_scaleTypeOpticalIllusionAssessmentQMenu)
        self.evaluate_scaleTypeOpticalIllusionAssessmentMirrorRightQaction.setText('镜像错觉体验调查(右)')

        self.evaluate_scaleTypeOpticalIllusionAssessmentQMenu.addAction(
            self.evaluate_scaleTypeOpticalIllusionAssessmentMirrorLeftQaction)
        self.evaluate_scaleTypeOpticalIllusionAssessmentQMenu.addAction(
            self.evaluate_scaleTypeOpticalIllusionAssessmentMirrorRightQaction)

        self.evaluate_scaleTypeQToolButtonMainMenu.addMenu(self.evaluate_scaleTypeBasicFunctionAssessmentQMenu)
        self.evaluate_scaleTypeQToolButtonMainMenu.addMenu(self.evaluate_scaleTypeHandAndUpperLimbAssessmentQMenu)
        self.evaluate_scaleTypeQToolButtonMainMenu.addMenu(self.evaluate_scaleTypeCognitiveFunctionAssessmentQMenu)
        self.evaluate_scaleTypeQToolButtonMainMenu.addMenu(self.evaluate_scaleTypeDailyLivingAbilityAssessmentQMenu)
        self.evaluate_scaleTypeQToolButtonMainMenu.addMenu(self.evaluate_scaleTypeOpticalIllusionAssessmentQMenu)

        self.evaluate_scaleTypeQToolButton.setPopupMode(QToolButton.InstantPopup)
        self.evaluate_scaleTypeQToolButton.setAutoRaise(True)
        self.evaluate_scaleTypeQToolButton.setMenu(self.evaluate_scaleTypeQToolButtonMainMenu)

        self.evaluate_inquireButton = QtWidgets.QPushButton(self.page_4)
        self.evaluate_inquireButton.setGeometry(QtCore.QRect(1040, 20, 100, 40))
        self.evaluate_inquireButton.setStyleSheet("font:12pt;color:white;background: rgb(0,138,200)")

        self.evaluate_addToolButton = QtWidgets.QToolButton(self.page_4)
        self.evaluate_addToolButton.setGeometry(QtCore.QRect(1160, 20, 100, 40))
        self.evaluate_addToolButton.setStyleSheet("font:12pt;color:white;background: rgb(0,138,200)")

        self.main_menu = QMenu(self.evaluate_addToolButton)

        self.evaluate_basicFunctionAssessmentQMenu = QMenu(self.main_menu)
        self.evaluate_basicFunctionAssessmentQMenu.setTitle('基本功能评定')

        self.evaluate_basicFunctionAssessmentAshworthQaction = QtWidgets.QAction(
            self.evaluate_basicFunctionAssessmentQMenu)
        self.evaluate_basicFunctionAssessmentAshworthQaction.setText('改良Ashworth分级')
        self.evaluate_basicFunctionAssessmentMuscleQaction = QtWidgets.QAction(
            self.evaluate_basicFunctionAssessmentQMenu)
        self.evaluate_basicFunctionAssessmentMuscleQaction.setText('肌力（握力、捏力）')
        self.evaluate_basicFunctionAssessmentMssQaction = QtWidgets.QAction(self.evaluate_basicFunctionAssessmentQMenu)
        self.evaluate_basicFunctionAssessmentMssQaction.setText('运动功能状态量表（MSS）')
        self.evaluate_basicFunctionAssessmentBrunnstromQaction = QtWidgets.QAction(
            self.evaluate_basicFunctionAssessmentQMenu)
        self.evaluate_basicFunctionAssessmentBrunnstromQaction.setText('Brunnstrom脑卒中运动功能分级')
        self.evaluate_basicFunctionAssessmentHealthHandQaction = QtWidgets.QAction(
            self.evaluate_basicFunctionAssessmentQMenu)
        self.evaluate_basicFunctionAssessmentHealthHandQaction.setText('利手调查量表')
        self.evaluate_basicFunctionAssessmentVasQaction = QtWidgets.QAction(self.evaluate_basicFunctionAssessmentQMenu)
        self.evaluate_basicFunctionAssessmentVasQaction.setText('VAS疼痛视觉模拟')

        self.evaluate_basicFunctionAssessmentQMenu.addAction(self.evaluate_basicFunctionAssessmentAshworthQaction)
        self.evaluate_basicFunctionAssessmentQMenu.addAction(self.evaluate_basicFunctionAssessmentMuscleQaction)
        self.evaluate_basicFunctionAssessmentQMenu.addAction(self.evaluate_basicFunctionAssessmentMssQaction)
        self.evaluate_basicFunctionAssessmentQMenu.addAction(self.evaluate_basicFunctionAssessmentBrunnstromQaction)
        self.evaluate_basicFunctionAssessmentQMenu.addAction(self.evaluate_basicFunctionAssessmentHealthHandQaction)
        self.evaluate_basicFunctionAssessmentQMenu.addAction(self.evaluate_basicFunctionAssessmentVasQaction)

        self.evaluate_handAndUpperLimbAssessmentQMenu = QMenu(self.main_menu)
        self.evaluate_handAndUpperLimbAssessmentQMenu.setTitle('手与上肢感觉运动功能评定')

        self.evaluate_handAndUpperLimbAssessmentVasQaction = QtWidgets.QAction(
            self.evaluate_handAndUpperLimbAssessmentQMenu)
        self.evaluate_handAndUpperLimbAssessmentVasQaction.setText('VAS疼痛视觉模拟')
        self.evaluate_handAndUpperLimbAssessmentFuglMoveQaction = QtWidgets.QAction(
            self.evaluate_handAndUpperLimbAssessmentQMenu)
        self.evaluate_handAndUpperLimbAssessmentFuglMoveQaction.setText('Fugl-Meyer上肢运动功能评定')
        self.evaluate_handAndUpperLimbAssessmentFuglSensorimotorQaction = QtWidgets.QAction(
            self.evaluate_handAndUpperLimbAssessmentQMenu)
        self.evaluate_handAndUpperLimbAssessmentFuglSensorimotorQaction.setText('Fugl-Meyer上肢感觉功能评定')
        self.evaluate_handAndUpperLimbAssessmentHandSensorimotorQaction = QtWidgets.QAction(
            self.evaluate_handAndUpperLimbAssessmentQMenu)
        self.evaluate_handAndUpperLimbAssessmentHandSensorimotorQaction.setText('手运动功能状态评分')
        self.evaluate_handAndUpperLimbAssessmentBlockObstacleTestQaction = QtWidgets.QAction(
            self.evaluate_handAndUpperLimbAssessmentQMenu)
        self.evaluate_handAndUpperLimbAssessmentBlockObstacleTestQaction.setText('积木障碍盒测试')
        self.evaluate_handAndUpperLimbAssessmentNineColumnTestQaction = QtWidgets.QAction(
            self.evaluate_handAndUpperLimbAssessmentQMenu)
        self.evaluate_handAndUpperLimbAssessmentNineColumnTestQaction.setText('九孔柱测试')
        self.evaluate_handAndUpperLimbAssessmentAratQaction = QtWidgets.QAction(
            self.evaluate_handAndUpperLimbAssessmentQMenu)
        self.evaluate_handAndUpperLimbAssessmentAratQaction.setText('ARAT上肢动作研究量表')
        self.evaluate_handAndUpperLimbAssessmentWolfQaction = QtWidgets.QAction(
            self.evaluate_handAndUpperLimbAssessmentQMenu)
        self.evaluate_handAndUpperLimbAssessmentWolfQaction.setText('WOLF运动功能测试')

        self.evaluate_handAndUpperLimbAssessmentQMenu.addAction(self.evaluate_handAndUpperLimbAssessmentVasQaction)
        self.evaluate_handAndUpperLimbAssessmentQMenu.addAction(self.evaluate_handAndUpperLimbAssessmentFuglMoveQaction)
        self.evaluate_handAndUpperLimbAssessmentQMenu.addAction(
            self.evaluate_handAndUpperLimbAssessmentFuglSensorimotorQaction)
        self.evaluate_handAndUpperLimbAssessmentQMenu.addAction(
            self.evaluate_handAndUpperLimbAssessmentHandSensorimotorQaction)
        self.evaluate_handAndUpperLimbAssessmentQMenu.addAction(
            self.evaluate_handAndUpperLimbAssessmentBlockObstacleTestQaction)
        self.evaluate_handAndUpperLimbAssessmentQMenu.addAction(
            self.evaluate_handAndUpperLimbAssessmentNineColumnTestQaction)
        self.evaluate_handAndUpperLimbAssessmentQMenu.addAction(self.evaluate_handAndUpperLimbAssessmentAratQaction)
        self.evaluate_handAndUpperLimbAssessmentQMenu.addAction(self.evaluate_handAndUpperLimbAssessmentWolfQaction)

        self.evaluate_cognitiveFunctionAssessmentQMenu = QMenu(self.main_menu)
        self.evaluate_cognitiveFunctionAssessmentQMenu.setTitle('认知功能评定')

        self.evaluate_cognitiveFunctionAssessmentMocaQaction = QtWidgets.QAction(
            self.evaluate_cognitiveFunctionAssessmentQMenu)
        self.evaluate_cognitiveFunctionAssessmentMocaQaction.setText('蒙特利尔认知评估量表(MoCA)')
        self.evaluate_cognitiveFunctionAssessmentMmseQaction = QtWidgets.QAction(
            self.evaluate_cognitiveFunctionAssessmentQMenu)
        self.evaluate_cognitiveFunctionAssessmentMmseQaction.setText('简易智力状态检查量表（MMSE）')
        self.evaluate_cognitiveFunctionAssessmentBntQaction = QtWidgets.QAction(
            self.evaluate_cognitiveFunctionAssessmentQMenu)
        self.evaluate_cognitiveFunctionAssessmentBntQaction.setText('波士顿命名测试（BNT）')

        self.evaluate_cognitiveFunctionAssessmentQMenu.addAction(self.evaluate_cognitiveFunctionAssessmentMocaQaction)
        self.evaluate_cognitiveFunctionAssessmentQMenu.addAction(self.evaluate_cognitiveFunctionAssessmentMmseQaction)
        self.evaluate_cognitiveFunctionAssessmentQMenu.addAction(self.evaluate_cognitiveFunctionAssessmentBntQaction)

        self.evaluate_dailyLivingAbilityAssessmentQMenu = QMenu(self.main_menu)
        self.evaluate_dailyLivingAbilityAssessmentQMenu.setTitle('日常生活能力评定')

        self.evaluate_dailyLivingAbilityAssessmentMbiQaction = QtWidgets.QAction(
            self.evaluate_dailyLivingAbilityAssessmentQMenu)
        self.evaluate_dailyLivingAbilityAssessmentMbiQaction.setText('改良Barthel指数（MBI）')
        self.evaluate_dailyLivingAbilityAssessmentFimQaction = QtWidgets.QAction(
            self.evaluate_dailyLivingAbilityAssessmentQMenu)
        self.evaluate_dailyLivingAbilityAssessmentFimQaction.setText('功能独立性测评（FIM）')

        self.evaluate_dailyLivingAbilityAssessmentQMenu.addAction(self.evaluate_dailyLivingAbilityAssessmentMbiQaction)
        self.evaluate_dailyLivingAbilityAssessmentQMenu.addAction(self.evaluate_dailyLivingAbilityAssessmentFimQaction)

        self.evaluate_opticalIllusionAssessmentQMenu = QMenu(self.main_menu)
        self.evaluate_opticalIllusionAssessmentQMenu.setTitle('视错觉评估')

        self.evaluate_opticalIllusionAssessmentMirrorLeftQaction = QtWidgets.QAction(
            self.evaluate_opticalIllusionAssessmentQMenu)
        self.evaluate_opticalIllusionAssessmentMirrorLeftQaction.setText('镜像错觉体验调查(左)')
        self.evaluate_opticalIllusionAssessmentQMenu.addAction(self.evaluate_opticalIllusionAssessmentMirrorLeftQaction)
        self.evaluate_opticalIllusionAssessmentMirrorRightQaction = QtWidgets.QAction(
            self.evaluate_opticalIllusionAssessmentQMenu)
        self.evaluate_opticalIllusionAssessmentMirrorRightQaction.setText('镜像错觉体验调查(右)')
        self.evaluate_opticalIllusionAssessmentQMenu.addAction(
            self.evaluate_opticalIllusionAssessmentMirrorRightQaction)

        self.main_menu.addMenu(self.evaluate_basicFunctionAssessmentQMenu)
        self.main_menu.addMenu(self.evaluate_handAndUpperLimbAssessmentQMenu)
        self.main_menu.addMenu(self.evaluate_cognitiveFunctionAssessmentQMenu)
        self.main_menu.addMenu(self.evaluate_dailyLivingAbilityAssessmentQMenu)
        self.main_menu.addMenu(self.evaluate_opticalIllusionAssessmentQMenu)

        self.evaluate_addToolButton.setPopupMode(QToolButton.InstantPopup)
        self.evaluate_addToolButton.setAutoRaise(True)
        self.evaluate_addToolButton.setMenu(self.main_menu)

        self.evaluate_summaryGraphButton = QtWidgets.QPushButton(self.page_4)
        self.evaluate_summaryGraphButton.setGeometry(QtCore.QRect(1280, 20, 100, 40))
        self.evaluate_summaryGraphButton.setStyleSheet("font:12pt;color:white;background: rgb(0,138,200)")

        self.evaluate_tableWidget = QtWidgets.QTableWidget(self.page_4)
        self.evaluate_tableWidget.setGeometry(QtCore.QRect(10, 70, 1380, 785))
        self.evaluate_tableWidget.setColumnCount(4)
        self.evaluate_tableWidget.setRowCount(15)
        self.evaluate_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.evaluate_tableWidget.setStyleSheet('background:white')
        self.evaluate_tableWidget.verticalHeader().setVisible(False)
        item = QtWidgets.QTableWidgetItem()
        self.evaluate_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.evaluate_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.evaluate_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.evaluate_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.evaluate_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.evaluate_tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.evaluate_tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.evaluate_tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.evaluate_tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.evaluate_tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.evaluate_tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.evaluate_tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.evaluate_tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.evaluate_tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.evaluate_tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.evaluate_tableWidget.setHorizontalHeaderItem(0, item)
        self.evaluate_tableWidget.setColumnWidth(0, 100)
        item = QtWidgets.QTableWidgetItem()
        self.evaluate_tableWidget.setHorizontalHeaderItem(1, item)
        self.evaluate_tableWidget.setColumnWidth(1, 300)
        item = QtWidgets.QTableWidgetItem()
        self.evaluate_tableWidget.setHorizontalHeaderItem(2, item)
        self.evaluate_tableWidget.setColumnWidth(2, 674)
        item = QtWidgets.QTableWidgetItem()
        self.evaluate_tableWidget.setHorizontalHeaderItem(3, item)
        self.evaluate_tableWidget.setColumnWidth(3, 300)

        self.evaluate_showPageLabel = QtWidgets.QLabel(self.page_4)
        self.evaluate_showPageLabel.setGeometry(QtCore.QRect(860, 802, 150, 40))

        self.stackedWidget.addWidget(self.page_4)

        self.page_5 = QtWidgets.QWidget()

        self.label_26 = QtWidgets.QLabel(self.page_5)
        self.label_26.setGeometry(QtCore.QRect(10, 20, 150, 40))
        self.label_26.setStyleSheet("font:12pt")

        self.log_stratDateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.page_5)
        self.log_stratDateEdit.setGeometry(QtCore.QRect(120, 20, 200, 40))
        self.log_stratDateEdit.setStyleSheet("background:white;font:12pt")
        self.log_stratDateEdit.setCalendarPopup(True)

        self.label_27 = QtWidgets.QLabel(self.page_5)
        self.label_27.setGeometry(QtCore.QRect(325, 20, 120, 40))
        self.label_27.setStyleSheet("font:12pt")

        self.log_endDateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.page_5)
        self.log_endDateEdit.setGeometry(QtCore.QRect(350, 20, 200, 40))
        self.log_endDateEdit.setStyleSheet("background:white;font:12pt")
        self.log_endDateEdit.setCalendarPopup(True)

        self.log_inquireButton = QtWidgets.QPushButton(self.page_5)
        self.log_inquireButton.setGeometry(QtCore.QRect(570, 20, 150, 40))
        self.log_inquireButton.setStyleSheet("font:12pt;color:white;background: rgb(0,138,200)")

        self.log_tableWidget = QtWidgets.QTableWidget(self.page_5)
        self.log_tableWidget.setGeometry(QtCore.QRect(10, 70, 1370, 786))
        self.log_tableWidget.setColumnCount(3)
        self.log_tableWidget.setRowCount(15)
        self.log_tableWidget.verticalHeader().setVisible(False)
        self.log_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.log_tableWidget.setStyleSheet('background:white')
        item = QtWidgets.QTableWidgetItem()
        self.log_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.log_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.log_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.log_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.log_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.log_tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.log_tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.log_tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.log_tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.log_tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.log_tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.log_tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.log_tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.log_tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.log_tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.log_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.log_tableWidget.setHorizontalHeaderItem(1, item)
        self.log_tableWidget.setColumnWidth(1, 250)
        item = QtWidgets.QTableWidgetItem()
        self.log_tableWidget.setHorizontalHeaderItem(2, item)
        self.log_tableWidget.setColumnWidth(2, 965)

        self.log_showPageLabel = QtWidgets.QLabel(self.page_5)
        self.log_showPageLabel.setGeometry(QtCore.QRect(830, 800, 150, 40))
        self.stackedWidget.addWidget(self.page_5)

        self.patientInformationButton = QtWidgets.QPushButton(Form)
        self.patientInformationButton.setGeometry(QtCore.QRect(190, 1020, 150, 50))
        self.patientInformationButton.setStyleSheet("font:12pt")

        self.trainingButton = QtWidgets.QPushButton(Form)
        self.trainingButton.setGeometry(QtCore.QRect(400, 1020, 150, 50))
        self.trainingButton.setStyleSheet("font:12pt")

        self.setSystemButton = QtWidgets.QPushButton(Form)
        self.setSystemButton.setGeometry(QtCore.QRect(610, 1020, 150, 50))
        self.setSystemButton.setStyleSheet("font:12pt")

        self.gameButton = QtWidgets.QPushButton(Form)
        self.gameButton.setGeometry(QtCore.QRect(810, 1020, 150, 50))
        self.gameButton.setStyleSheet("font:12pt")
        self.gameButton.setVisible(False)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "智能多模态镜像评估与训练系统"))
        self.changePasswordLabel.setText(_translate("Form", "密码修改"))
        self.exitSystemLabel.setText(_translate("Form", "系统退出"))
        self.showTimeLabel.setText(_translate("Form", "显示时间"))
        self.label_3.setText(_translate("Form", "关键字查询"))
        self.databaseSimpleQueryButton.setText(_translate("Form", "简单"))
        self.dataBase_highLevelInquireButton.setText(_translate("Form", "高级"))
        self.databaseHeadPageButton.setText(_translate("Form", "首页"))
        self.dataBasePriorPageButton.setText(_translate("Form", "上一页"))
        self.databaseNextPageButton.setText(_translate("Form", "下一页"))
        self.databaseTailPageButton.setText(_translate("Form", "尾页"))
        self.label_5.setText(_translate("Form", "详细信息"))
        self.label_6.setText(_translate("Form", "*"))
        self.label_7.setText(_translate("Form", "姓名"))
        self.label_8.setText(_translate("Form", "*"))
        self.label_9.setText(_translate("Form", "身份证"))
        self.label_10.setText(_translate("Form", "性别"))
        self.label_11.setText(_translate("Form", "年龄"))
        self.label_12.setText(_translate("Form", "电话"))
        self.label_13.setText(_translate("Form", "文化程度"))
        self.label_14.setText(_translate("Form", "职业"))
        self.label_15.setText(_translate("Form", "利手"))
        self.label_16.setText(_translate("Form", "患手"))
        self.label_17.setText(_translate("Form", "疾病类型"))
        self.label_18.setText(_translate("Form", "认知情况"))
        self.patientInformation_frontalLobeCheckBox.setText(_translate("Form", "额叶"))
        self.patientInformation_occipitalLobeCheckBox.setText(_translate("Form", "枕叶"))
        self.patientInformation_basalGangliaCheckBox.setText(_translate("Form", "基底节"))
        self.patientInformation_cerebellumCheckBox.setText(_translate("Form", "小脑"))
        self.patientInformation_parietalLobeCheckBox.setText(_translate("Form", "顶叶"))
        self.patientInformation_internalCapsuleCheckBox.setText(_translate("Form", "内囊"))
        self.patientInformation_halfEggAreaCheckBox.setText(_translate("Form", "半卵脑区"))
        self.patientInformation_brainStemCheckBox.setText(_translate("Form", "脑干"))
        self.patientInformation_temporalLobeCheckBox.setText(_translate("Form", "颞叶"))
        self.patientInformation_outerCapsuleCheckBox.setText(_translate("Form", "外囊"))
        self.patientInformation_thalamusCheckBox.setText(_translate("Form", "丘脑"))
        self.label_19.setText(_translate("Form", "病程"))
        self.label_20.setText(_translate("Form", "Burnnstorm分期"))
        self.label_21.setText(_translate("Form", "肌张力（曲）"))
        self.label_22.setText(_translate("Form", "肘关节"))
        self.label_23.setText(_translate("Form", "腕关节"))
        self.label_24.setText(_translate("Form", "指尖关节"))
        self.label_25.setText(_translate("Form", "肌张力（伸）"))
        self.label_33.setText(_translate("Form", "肘关节"))
        self.label_34.setText(_translate("Form", "腕关节"))
        self.label_35.setText(_translate("Form", "指尖关节"))
        self.label_36.setText(_translate("Form", "VAS疼痛评分"))
        self.label_37.setText(_translate("Form", "疼痛部位"))
        self.label_38.setText(_translate("Form", "病史摘要"))
        self.patientInformation_addButton.setText(_translate("Form", "新增"))
        self.patientInformation_deleteButton.setText(_translate("Form", "删除"))
        self.patientInformation_savaButton.setText(_translate("Form", "保存"))
        self.label_39.setText(_translate("Form", "治疗日期"))
        self.label_40.setText(_translate("Form", "计划时间"))
        self.label_41.setText(_translate("Form", "—"))
        self.traingProgram_inquireButton.setText(_translate("Form", "查询"))
        self.traingProgram_addButton.setText(_translate("Form", "新增"))
        self.label_42.setText(_translate("Form", "训练模式"))
        self.label_43.setText(_translate("Form", "训练日期"))
        self.label_44.setText(_translate("Form", "—"))
        self.trainingLog_inquireButton.setText(_translate("Form", "查询"))

        self.trainingLog_trainingListButton.setText(_translate("Form", "训练列表"))
        self.trainingLog_summaryGraphButton.setText(_translate("Form", "统计图"))
        self.label_46.setText(_translate("Form", "评定时间"))
        self.label_47.setText(_translate("Form", "—"))
        self.label_48.setText(_translate("Form", "量表类型"))

        self.evaluate_inquireButton.setText(_translate("Form", "查询"))
        self.evaluate_addToolButton.setText(_translate("Form", "新增"))
        self.evaluate_summaryGraphButton.setText(_translate("Form", "统计图"))
        item = self.evaluate_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "序号"))
        item = self.evaluate_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "评定时间"))
        item = self.evaluate_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "量表类型"))
        item = self.evaluate_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "评定结果"))
        self.evaluate_showPageLabel.setText(_translate("Form", "TextLabel"))
        self.label_26.setText(_translate("Form", "训练日期"))
        self.label_27.setText(_translate("Form", "—"))
        self.log_inquireButton.setText(_translate("Form", "查询"))
        item = self.log_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "序号"))
        item = self.log_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "训练日期"))
        item = self.log_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "训练"))
        self.patientBasicInformationButton.setText(_translate("Form", "病人基本信息"))
        self.trainingProgramButton.setText(_translate("Form", "训练方案"))
        self.trainingLogButton.setText(_translate("Form", "训练日志"))
        self.evaluateButton.setText(_translate("Form", "随访评估"))
        self.logButton.setText(_translate("Form", "日志报表"))
        self.patientInformationButton.setText(_translate("Form", "病人信息"))
        self.trainingButton.setText(_translate("Form", "训练"))
        self.setSystemButton.setText(_translate("Form", "系统设置"))
        self.gameButton.setText(_translate("Form", "游戏"))


class mainInterface(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, doctor_id):
        super(mainInterface, self).__init__()
        self.doctor_id = doctor_id
        self.patientSelectedInfo = None
        self.patientInfoSheetLength = 0
        self.patientInfoSheet = None
        self.patientSelectedId = None
        self.patientInfoSheetMaxPages = None
        self.nowPage = 1

        self.idTypeComboboxItems = ['身份证', '士官证', '护照', '港澳通行证', '其它']
        self.sexComboboxItems = ['男', '女']
        self.handComboboxItems = ['', '左', '右']
        self.patientInfoSheetColumnsCn = ['物理id', '姓名', '性别', '年龄', '患手']
        self.patientInfoSheetColumnsEn = ['id', 'name', 'sex', 'age', 'illness']
        self.trainingProgramSheetColumnsEn = ['id', 'date', 'detail', 'status']
        self.trainingProgramSheetColumnsCn = ['物理id', '计划时间', '训练内容', '状态']
        self.trainingLogSheetColumnsCn = ['训练项目', '训练开始时间', '训练结束时间', '训练内容']
        self.educationComboboxItems = ['小学', '初中', '高中', '大学', '无', '']
        self.congnizeComboboxItems = ['优', '良', '差']

        self.setupUi(self)
        self.exitSystemLabel.mousePressEvent = self.exitSystemLabelClick  # 主界面-退出系统
        self.showTimeLabelClick()  # 主界面-显示时间
        self.databaseSimpleQueryButton.clicked.connect(self.databaseSimpleQueryButtonClick)  # 主界面-数据库-简单查询
        self.databaseNextPageButton.clicked.connect(self.nextPageButtonClick)  # 主页面-数据库-下一页
        self.dataBasePriorPageButton.clicked.connect(self.priorPageButtonClick)  # 主页面-数据库-上一页
        self.databaseTailPageButton.clicked.connect(self.tailPageButtonClick)  # 主页面-数据库-尾页
        self.databaseHeadPageButton.clicked.connect(self.headPageButtonClick)  # 主页面-数据库-首页
        self.patientInfoTable.clicked.connect(self.patientInfoTableClick)  # 主页面-数据库-选择病人
        self.dataBase_highLevelInquireButton.clicked.connect(self.dataBase_highLevelInquireButtonClick)  # 主界面-数据库-高级查询
        self.patientBasicInformationButton.clicked.connect(self.patientBasicInformationButtonClick)  # 主界面-病人基本信息
        self.patientInformation_addButton.clicked.connect(self.patientInformation_addButtonClick)  # 主界面-病人基本信息-新增
        self.patientInformation_deleteButton.clicked.connect(self.patientInformation_deleteButtonClick)  # 主界面-病人基本信息-删除
        self.patientInformation_savaButton.clicked.connect(self.patientInformation_savaButtonClick)  # 主界面-病人基本信息-保存
        self.patientInformation_diseaseTypeComboBox_1.currentIndexChanged.connect(
            self.patientInformation_diseaseTypeComboBox_1Click)
        self.trainingProgramButton.clicked.connect(self.trainingProgramButtonClick)  # 主界面-训练方案
        self.traingProgram_inquireButton.clicked.connect(self.trainingProgramInquireButtonClick)  # 主界面-训练方案-查询
        self.traingProgram_addButton.clicked.connect(self.trainingProgramAddButtonClick)  # 主界面-训练方案-新增
        self.trainingLogButton.clicked.connect(self.trainingLogButtonClick)  # 主界面-训练日志
        self.trainingLog_inquireButton.clicked.connect(self.trainingLogInquireButtonClick)  # 主界面-训练日志-查询
        self.trainingLog_trainingListButton.clicked.connect(self.trainingLog_trainingListButtonClick)  # 主界面-训练日志-训练列表
        self.trainingLog_summaryGraphButton.clicked.connect(self.trainingLog_summaryGraphButtonClick)  # 主界面-训练日志-统计图
        self.evaluateButton.clicked.connect(self.evaluateButtonClick)  # 主界面-数据库-随访评估
        # self.evaluate_cognitiveFunctionAssessmentQMenu.clicked.connect(self.evaluate_cognitiveFunctionAssessmentQMenuClick) # 主界面-数据库-随访评估-认知功能评定

        self.logButton.clicked.connect(self.logButtonClick)  # 主界面-数据库-日志报表
        self.log_stratDateEdit.dateChanged.connect(self.log_startDateEditClick)  # 主界面-日志报表-训练开始日期
        self.trainingButton.clicked.connect(self.trainButtonClicked)
        self.setSystemButton.clicked.connect(self.setSystemButtonClicked)

        self.trainingLog_tableWidget.doubleClicked.connect(self.trainingLog_tableWidgetDoubleClick)

        self.initPatientInfoTable()
        self.initTrainProgramTable()
        self.initTrainLogTable()

    def trainingLog_tableWidgetDoubleClick(self, *args):
        try:
            idx = int(self.trainingLog_tableWidget.selectedItems()[0].row())
        except:
            return
        loc = self.trainingLogList[idx]['train']
        if loc == "基本功能训练":
            loc = 'basic'
        elif loc == "功能动作训练":
            loc = 'function'
        elif loc == "空间想象训练":
            loc = 'space'
        else:
            loc = "sensorimotor"
        cv2.imshow("frame", cv2.imread(f"{config.GlobalPath}save/{loc}/{self.trainingProgramInfo[idx]['pic']}.png"))
        cv2.waitKey(0)

    def exitSystemLabelClick(self, *args):  # 主界面-退出系统
        self.close()

    def showCurrentTime(self, timeLabel):  # 显示系统时间
        # 获取系统当前时间
        time = QDateTime.currentDateTime()
        # 设置系统时间的显示格式
        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        # print(timeDisplay)
        # 状态栏显示
        timeLabel.setText(timeDisplay)

    def showTimeLabelClick(self, *args):  # 主界面-显示时间
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.showCurrentTime(self.showTimeLabel))  # 这个通过调用槽函数来刷新时间
        self.timer.start(1000)  # 每隔一秒刷新一次，这里设置为1000ms  即1s

    def initPatientInfoTable(self):
        self.patientInfoTable.setColumnCount(4)
        self.patientInfoTable.setRowCount(15)
        self.patientInfoTable.setHorizontalHeaderLabels(self.patientInfoSheetColumnsCn[1:])
        self.patientInfoTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.patientInfoTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.patientInfoTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.patientInfoTable.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.patientInfoTable.setSelectionBehavior(QHeaderView.SelectRows)
        self.patientInfoTable.setSelectionMode(QTableWidget.SingleSelection)

        self.patientInfoSheet = json.loads(
            requests.post(config.patientEasyList, data={'patient_id': self.accountId}).content.decode('utf-8'))['data']
        self.patientInfoSheetLength = len(self.patientInfoSheet)

        if self.patientInfoSheetLength % 15 == 0:
            self.patientInfoSheetMaxPages = int(self.patientInfoSheetLength // 15)
        else:
            self.patientInfoSheetMaxPages = int(self.patientInfoSheetLength // 15 + 1)

        self.patientInfoTableSetter(self.nowPage)

    def initTrainProgramTable(self):
        self.trainingProgram_tableWidget.setColumnCount(3)
        self.trainingProgram_tableWidget.setRowCount(10)
        self.trainingProgram_tableWidget.setHorizontalHeaderLabels(self.trainingProgramSheetColumnsCn[1:])
        self.trainingProgram_tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.trainingProgram_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.trainingProgram_tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.trainingProgram_tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.trainingProgram_tableWidget.setSelectionBehavior(QHeaderView.SelectRows)
        self.trainingProgram_tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.trainingProgramInfo = json.loads(requests.post(config.trainInfoListByDate).content.decode('utf-8'))['data']
        pass

    def initTrainLogTable(self):
        self.trainingLog_tableWidget.setColumnCount(4)
        self.trainingLog_tableWidget.setRowCount(10)
        self.trainingLog_tableWidget.setHorizontalHeaderLabels(self.trainingLogSheetColumnsCn)
        self.trainingLog_tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.trainingLog_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.trainingLog_tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.trainingLog_tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.trainingLog_tableWidget.setSelectionBehavior(QHeaderView.SelectRows)
        self.trainingLog_tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        pass

    def patientInfoTableClear(self):
        # 清空表格内容
        for i in range(15):
            for j in range(1, 5):
                self.patientInfoTable.setItem(i, j - 1, QTableWidgetItem(""))

    def patientInfoTableSetter(self, pages):
        self.patientInfoTableClear()
        _translate = QtCore.QCoreApplication.translate

        for i in range((pages - 1) * 15, min(pages * 15, self.patientInfoSheetLength)):
            for j in range(1, 5):
                self.patientInfoTable.setItem(i % 15, j - 1, QTableWidgetItem(
                    str(self.patientInfoSheet[i][self.patientInfoSheetColumnsEn[j]])))

        # self.pageInfoLabel.setText(
        #     _translate("Form", self.patientInfoText.format(self.nowPage, self.patientInfoSheetMaxPages)))
        ...

    def databaseSimpleQueryButtonClick(self, *args):  # 主界面-数据库-简单查询
        # 病人信息简单查询按钮
        name = self.databaseNameQueryLineEdit.text()
        self.patientInfoSheet = json.loads(requests.post(config.patientListByName, data={'name': name}).text)['data']
        self.patientInfoSheetLength = len(self.patientInfoSheet)

        if self.patientInfoSheetLength % 15 == 0:
            self.patientInfoSheetMaxPages = int(self.patientInfoSheetLength // 15)
        else:
            self.patientInfoSheetMaxPages = int(self.patientInfoSheetLength // 15 + 1)

        self.nowPage = 1

        self.patientInfoTableSetter(self.nowPage)

    def headPageButtonClick(self, *args):
        # 病人信息首页
        self.nowPage = 1
        self.patientInfoTableSetter(self.nowPage)
        ...

    def priorPageButtonClick(self, *args):
        # 病人信息前一页
        if self.nowPage - 1 == 0:
            return

        self.nowPage -= 1
        self.patientInfoTableSetter(self.nowPage)

    def nextPageButtonClick(self, *args):
        # 病人信息后一页
        if self.nowPage + 1 > self.patientInfoSheetMaxPages:
            return

        self.nowPage += 1
        self.patientInfoTableSetter(self.nowPage)

    def tailPageButtonClick(self, *args):
        # 病人信息尾页
        self.nowPage = self.patientInfoSheetMaxPages
        self.patientInfoTableSetter(self.nowPage)

    def patientInfoTableClick(self, *args):
        _translate = QtCore.QCoreApplication.translate
        selectIndex = int(self.patientInfoTable.selectedItems()[0].row())
        self.patientSelectedId = self.patientInfoSheet[(self.nowPage - 1) * 15 + selectIndex]['id']
        self.patientSelectedInfo = json.loads(
            requests.post(config.patientGetById, data={'id': self.patientSelectedId}).content.decode('utf-8'))[
            'data']

        sheet = ['脑卒中', '颅脑损伤']

        self.patientInfoNameLineEdit.setText(self.patientSelectedInfo['name'])
        self.patientInfoIdTypeComboBox.setCurrentIndex(
            self.idTypeComboboxItems.index(self.patientSelectedInfo['id_type']))
        self.patientInfoIdLineEdit.setText(self.patientSelectedInfo['id_detail'])
        self.patientInfoSexComboBox.setCurrentIndex(self.sexComboboxItems.index(self.patientSelectedInfo['sex']))
        self.patientInfoAgeLineEdit.setText(str(self.patientSelectedInfo['age']))
        self.patientInfoTelLineEdit.setText(str(self.patientSelectedInfo['tel']))
        self.patientInfoEducationCombobox.setCurrentIndex(
            self.educationComboboxItems.index(self.patientSelectedInfo['education']))
        self.patientInfoJobLineEdit.setText(self.patientSelectedInfo['job'])
        dateStr = [i for i in map(int, self.patientSelectedInfo['aid_date'].split('/'))]
        self.patientInformAidDateEdit.setDate(QDate(dateStr[0], dateStr[1], dateStr[2]))
        self.patientInfoHandedCombobox.setCurrentIndex(
            self.handComboboxItems.index(self.patientSelectedInfo['handedness']))
        self.patientInfoIllnessComboBox.setCurrentIndex(
            self.handComboboxItems.index(self.patientSelectedInfo['illness']))

        primary_etiology = self.patientSelectedInfo['primary_etiology']
        secondary_etiology = self.patientSelectedInfo['secondary_etiology']
        recognize_site = self.patientSelectedInfo['recognize_status']
        self.patientInformation_cognititveSituationComboBox.setCurrentIndex(
            self.congnizeComboboxItems.index(recognize_site))

        if primary_etiology in sheet:
            selectBox = 1
        else:
            selectBox = 0

        self.patientInformation_vasComboBox.setCurrentIndex(int(self.patientSelectedInfo['vas']) - 1)
        self.patientInformation_painfulAeraLineEdit.setText(self.patientSelectedInfo['pain_site'])
        self.patientInformation_medicalHistorySummaryTextEdit.setText(self.patientSelectedInfo['abstract'])

    def dataBase_highLevelInquireButtonClick(self, *args):  # 主界面-数据库-高级查询
        ...

    def patientBasicInformationButtonClick(self, *args):  # 主界面-病人基本信息
        self.stackedWidget.setCurrentIndex(0)

    def patientInformation_addButtonClick(self, *args):  # 主界面-病人基本信息-新增
        ...

    def patientInformation_deleteButtonClick(self, *args):  # 主界面-病人基本信息-删除
        ...

    def patientInformation_savaButtonClick(self, *args):  # 主界面-病人基本信息-保存
        ...

    # 主界面-病人基本信息-疾病类型一级选项
    def patientInformation_diseaseTypeComboBox_1Click(self, *args):
        if (self.patientInformation_diseaseTypeComboBox_1.currentIndex() == 1 or
                self.patientInformation_diseaseTypeComboBox_1.currentIndex() == 3):
            self.patientInformation_brainInjuryAreaFrame.setVisible(True)
            self.patientInformation_brainInjuryAreaFrame.setGeometry(QtCore.QRect(30, 235, 1330, 310))
            self.frame_2.setGeometry(QtCore.QRect(30, 545, 1330, 250))
            self.patientInformation_diseaseTypeFrame1_2.setVisible(False)  # 主界面-病人基本信息-疾病类型二级填写容器
            self.patientInformation_diseaseTypeFrame1.setVisible(True)  # 主界面-病人基本信息-疾病类型二级选项容器
        else:
            self.patientInformation_brainInjuryAreaFrame.setVisible(False)  # 主界面-病人基本信息-选择疾病类型一级选项出现的复选框容器
            self.frame_2.setGeometry(QtCore.QRect(30, 235, 1330, 250))  # 主界面-病人基本信息-选择疾病类型一级选项出现的复选框容器下面的容器
            self.patientInformation_diseaseTypeFrame1_2.setVisible(True)  # 主界面-病人基本信息-疾病类型二级填写容器
            self.patientInformation_diseaseTypeFrame1.setVisible(False)  # 主界面-病人基本信息-疾病类型二级选项容器
        ...

    def trainingProgramButtonClick(self, *args):  # 主界面-训练方案
        self.stackedWidget.setCurrentIndex(1)
        pass

    def trainingProgramInquireButtonClick(self, *args):  # 主界面-训练方案-查询
        ...

    def trainingProgramAddButtonClick(self, *args):  # 主界面-训练方案-新增
        ...

    def trainingLogButtonClick(self, *args):  # 主界面-训练日志
        self.stackedWidget.setCurrentIndex(2)

    def trainingLogInquireButtonClick(self, *args):  # 主界面-训练日志-查询
        begDate = ''
        endData = ''
        self.trainingLogList = json.loads(
            requests.post(config.trainInfoListByDate, data={'begate': begDate, 'endDate': endData}).content.decode(
                'utf-8'))['data']
        print(self.trainingLogList)
        self.trainingLog_tableWidget.setRowCount(max(10, len(self.trainingLogList)))
        for i in range(len(self.trainingLogList)):
            self.trainingLog_tableWidget.setItem(i, 0, QTableWidgetItem(str(self.trainingLogList[i]['train'])))
            self.trainingLog_tableWidget.setItem(i, 1, QTableWidgetItem(str(self.trainingLogList[i]['begin_time'])))
            self.trainingLog_tableWidget.setItem(i, 2, QTableWidgetItem(str(self.trainingLogList[i]['end_time'])))
            self.trainingLog_tableWidget.setItem(i, 3, QTableWidgetItem(str(self.trainingLogList[i]['detail'])))
        ...

    def trainingLog_trainingListButtonClick(self, *args):  # 主界面-训练日志-训练列表
        self.trainingLog_trainingListFrame.setVisible(True)  # 主界面-训练日志-训练列表容器
        self.trainingLog_summaryGraphFrame.setVisible(False)  # 主界面-训练日志-统计图容器
        ...

    def trainingLog_summaryGraphButtonClick(self, *args):  # 主界面-训练日志-统计图
        self.trainingLog_trainingListFrame.setVisible(False)
        self.trainingLog_summaryGraphFrame.setVisible(True)
        ...

    def evaluateButtonClick(self, *args):  # 主界面-随访评估
        self.stackedWidget.setCurrentIndex(3)

        # def evaluate_cognitiveFunctionAssessmentQMenuClick(self, *args):  #  主界面-随访评估-认知功能评定
        #     self.CognitiveFunctionAssessmentWindow=frontend.evaluate.CognitiveFunctionAssessment.cognitiveFunctionAssessment()
        #     self.CognitiveFunctionAssessmentWindow.show()
        ...

    def log_startDateEditClick(self, *args):  # 主界面-日志报表-训练开始日期
        ...

    def logButtonClick(self, *args):  # 主界面-日志报表
        self.stackedWidget.setCurrentIndex(4)

    def trainButtonClicked(self, *args):
        if self.patientSelectedId:
            self.trainingWindow = frontend.training.Training.trianging(self.patientSelectedId)
            self.trainingWindow.show()
        pass

    def setSystemButtonClicked(self, *args):
        self.setSystemWindow = frontend.setSystem.SetSystem.setSystem()
        self.setSystemWindow.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = mainInterface('123')
    gui.show()
    sys.exit(app.exec_())
