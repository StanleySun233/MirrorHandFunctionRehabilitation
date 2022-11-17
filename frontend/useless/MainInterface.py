# 主界面
import json
import sys
import threading
import time

import requests
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import config
import frontend
import tool


class Ui_Form(object):
    def setupUi(self, Form):
        Form.resize(2000, 1200)
        #         Form.setStyleSheet("background:white\n"
        # "")

        _translate = QtCore.QCoreApplication.translate

        self.background = QtWidgets.QFrame(Form)
        self.background.setGeometry(QtCore.QRect(0, 0, 2000, 150))
        self.background.setStyleSheet("background:rgb(135,206,250)")
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)

        self.systemNameCnLabel = QtWidgets.QLabel(self.background)
        self.systemNameCnLabel.setGeometry(QtCore.QRect(20, 10, 360, 40))
        self.systemNameCnLabel.setStyleSheet("color:white;\n""font:16pt")

        self.systemNameEnLabel = QtWidgets.QLabel(self.background)
        self.systemNameEnLabel.setGeometry(QtCore.QRect(20, 60, 360, 50))
        self.systemNameEnLabel.setStyleSheet("color:white;\n""font:10pt")

        self.changePassword = QtWidgets.QLabel(self.background)
        self.changePassword.setGeometry(QtCore.QRect(1250, 20, 100, 50))
        self.changePassword.setStyleSheet("color:white;font:12pt;")

        self.systemHelp = QtWidgets.QLabel(self.background)
        self.systemHelp.setGeometry(QtCore.QRect(1380, 20, 100, 50))
        self.systemHelp.setStyleSheet("color:white;font:12pt")

        self.systemExit = QtWidgets.QLabel(self.background)
        self.systemExit.setGeometry(QtCore.QRect(1510, 20, 100, 50))
        self.systemExit.setStyleSheet("color:white;font:12pt;")

        self.timeLabel = QtWidgets.QLabel(self.background)
        self.timeLabel.setGeometry(QtCore.QRect(1250, 80, 200, 50))

        self.databaseContainer = QtWidgets.QFrame(Form)
        self.databaseContainer.setGeometry(QtCore.QRect(10, 160, 600, 900))
        self.databaseContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.databaseContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.databaseContainer.setStyleSheet("background:rgb(255,255,255)")

        self.label = QtWidgets.QLabel(self.databaseContainer)
        self.label.setGeometry(QtCore.QRect(0, 0, 600, 100))
        self.label.setStyleSheet("background:rgb(135,206,250)")

        self.simpleSearchLineEditor = QtWidgets.QLineEdit(self.databaseContainer)
        self.simpleSearchLineEditor.setGeometry(QtCore.QRect(10, 30, 240, 40))

        self.simpleButton = QtWidgets.QPushButton(self.databaseContainer)
        self.simpleButton.setGeometry(QtCore.QRect(270, 30, 100, 40))

        self.advancedSearchButton = QtWidgets.QPushButton(self.databaseContainer)
        self.advancedSearchButton.setGeometry(QtCore.QRect(390, 30, 100, 40))

        self.patientInfoTable = QtWidgets.QTableWidget(self.databaseContainer)
        self.patientInfoTable.setGeometry(QtCore.QRect(0, 100, 600, 750))
        self.patientInfoTable.setStyleSheet("background:rgb(255,182,193)")

        self.headPageButton = QtWidgets.QPushButton(self.databaseContainer)
        self.headPageButton.setGeometry(QtCore.QRect(0, 850, 100, 50))

        self.priorPageButton = QtWidgets.QPushButton(self.databaseContainer)
        self.priorPageButton.setGeometry(QtCore.QRect(100, 850, 100, 50))

        self.pageInfoLabel = QtWidgets.QLabel(self.databaseContainer)
        self.pageInfoLabel.setGeometry(QtCore.QRect(200, 850, 200, 50))
        self.pageInfoLabel.setStyleSheet("background:rgb(135,206,250)")
        self.pageInfoLabel.setAlignment(Qt.AlignCenter)

        self.nextPageButton = QtWidgets.QPushButton(self.databaseContainer)
        self.nextPageButton.setGeometry(QtCore.QRect(400, 850, 100, 50))

        self.tailPageButton = QtWidgets.QPushButton(self.databaseContainer)
        self.tailPageButton.setGeometry(QtCore.QRect(500, 850, 100, 50))

        self.patientDetailInfo = QtWidgets.QFrame(Form)
        self.patientDetailInfo.setGeometry(QtCore.QRect(650, 160, 1300, 900))
        self.patientDetailInfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.patientDetailInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.patientDetailInfo.setStyleSheet("background:white")

        self.informationButton = QtWidgets.QPushButton(self.patientDetailInfo)
        self.informationButton.setGeometry(QtCore.QRect(0, 0, 275, 63))

        self.trainProgramButton = QtWidgets.QPushButton(self.patientDetailInfo)
        self.trainProgramButton.setGeometry(QtCore.QRect(275, 0, 275, 63))

        self.trainlogButton = QtWidgets.QPushButton(self.patientDetailInfo)
        self.trainlogButton.setGeometry(QtCore.QRect(550, 0, 275, 63))

        self.assessScaleButton = QtWidgets.QPushButton(self.patientDetailInfo)
        self.assessScaleButton.setGeometry(QtCore.QRect(825, 0, 275, 63))

        self.logScaleButton = QtWidgets.QPushButton(self.patientDetailInfo)
        self.logScaleButton.setGeometry(QtCore.QRect(1100, 0, 275, 63))

        self.nameLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.nameLabel.setGeometry(QtCore.QRect(20, 100, 100, 40))
        self.nameLabel.setAlignment(Qt.AlignCenter)
        self.nameLabel.setText(_translate('Form', '姓 名'))
        self.nameLabel.setStyleSheet("background:lightgray")

        self.nameLineEditor = QtWidgets.QLineEdit(self.patientDetailInfo)
        self.nameLineEditor.setGeometry(QtCore.QRect(140, 100, 200, 40))

        self.idTypeLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.idTypeLabel.setGeometry(QtCore.QRect(360, 100, 100, 40))
        self.idTypeLabel.setAlignment(Qt.AlignCenter)
        self.idTypeLabel.setText(_translate('Form', '证件类型'))
        self.idTypeLabel.setStyleSheet("background:lightgray")

        self.idTypeCombobox = QtWidgets.QComboBox(self.patientDetailInfo)
        self.idTypeCombobox.setGeometry(QtCore.QRect(480, 100, 100, 40))

        self.idDetailLineEditor = QtWidgets.QLineEdit(self.patientDetailInfo)
        self.idDetailLineEditor.setGeometry(QtCore.QRect(600, 100, 300, 40))

        self.sexLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.sexLabel.setGeometry(QtCore.QRect(20, 160, 100, 40))
        self.sexLabel.setAlignment(Qt.AlignCenter)
        self.sexLabel.setText(_translate('Form', '性 别'))
        self.sexLabel.setStyleSheet("background:lightgray")

        self.sexCombobox = QtWidgets.QComboBox(self.patientDetailInfo)
        self.sexCombobox.setGeometry(QtCore.QRect(140, 160, 200, 40))

        self.ageLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.ageLabel.setGeometry(QtCore.QRect(360, 160, 100, 40))
        self.ageLabel.setAlignment(Qt.AlignCenter)
        self.ageLabel.setText(_translate('Form', '年 龄'))
        self.ageLabel.setStyleSheet("background:lightgray")

        self.ageLineEditor = QtWidgets.QLineEdit(self.patientDetailInfo)
        self.ageLineEditor.setGeometry(QtCore.QRect(480, 160, 100, 40))

        self.telLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.telLabel.setGeometry(QtCore.QRect(600, 160, 100, 40))
        self.telLabel.setAlignment(Qt.AlignCenter)
        self.telLabel.setText(_translate('Form', '电 话'))
        self.telLabel.setStyleSheet("background:lightgray")

        self.telLineEditor = QtWidgets.QLineEdit(self.patientDetailInfo)
        self.telLineEditor.setGeometry(QtCore.QRect(720, 160, 180, 40))

        self.handednessLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.handednessLabel.setGeometry(QtCore.QRect(20, 220, 100, 40))
        self.handednessLabel.setAlignment(Qt.AlignCenter)
        self.handednessLabel.setText(_translate('Form', '利 手'))
        self.handednessLabel.setStyleSheet("background:lightgray")

        self.handednessCombobox = QtWidgets.QComboBox(self.patientDetailInfo)
        self.handednessCombobox.setGeometry(QtCore.QRect(140, 220, 100, 40))

        self.illnessLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.illnessLabel.setGeometry(QtCore.QRect(260, 220, 100, 40))
        self.illnessLabel.setAlignment(Qt.AlignCenter)
        self.illnessLabel.setText(_translate('Form', '患 手'))
        self.illnessLabel.setStyleSheet("background:lightgray")

        self.handednessCombobox = QtWidgets.QComboBox(self.patientDetailInfo)
        self.handednessCombobox.setGeometry(QtCore.QRect(140, 220, 100, 40))

        self.illnessLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.illnessLabel.setGeometry(QtCore.QRect(260, 220, 100, 40))
        self.illnessLabel.setAlignment(Qt.AlignCenter)
        self.illnessLabel.setText(_translate('Form', '患 手'))
        self.illnessLabel.setStyleSheet("background:lightgray")

        self.illnessCombobox = QtWidgets.QComboBox(self.patientDetailInfo)
        self.illnessCombobox.setGeometry(QtCore.QRect(380, 220, 100, 40))

        self.primaryEtiologyLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.primaryEtiologyLabel.setGeometry(QtCore.QRect(500, 220, 100, 40))
        self.primaryEtiologyLabel.setAlignment(Qt.AlignCenter)
        self.primaryEtiologyLabel.setText(_translate('Form', '疾病类型'))
        self.primaryEtiologyLabel.setStyleSheet("background:lightgray")

        self.primaryEtiologyCombobox = QtWidgets.QComboBox(self.patientDetailInfo)
        self.primaryEtiologyCombobox.setGeometry(QtCore.QRect(620, 220, 140, 40))

        self.secondaryEtiologyCombobox = QtWidgets.QComboBox(self.patientDetailInfo)
        self.secondaryEtiologyCombobox.setGeometry(QtCore.QRect(760, 220, 140, 40))

        self.illnessLocationCheckBox_1 = QtWidgets.QCheckBox(self.patientDetailInfo)
        self.illnessLocationCheckBox_1.setGeometry(QtCore.QRect(40, 280, 100, 20))
        self.illnessLocationCheckBox_1.setText(_translate('Form', '额叶'))
        self.illnessLocationCheckBox_1.setStyleSheet("background:lightgray")

        self.illnessLocationCheckBox_2 = QtWidgets.QCheckBox(self.patientDetailInfo)
        self.illnessLocationCheckBox_2.setGeometry(QtCore.QRect(160, 280, 100, 20))
        self.illnessLocationCheckBox_2.setText(_translate('Form', '枕叶'))
        self.illnessLocationCheckBox_2.setStyleSheet("background:lightgray")

        self.illnessLocationCheckBox_3 = QtWidgets.QCheckBox(self.patientDetailInfo)
        self.illnessLocationCheckBox_3.setGeometry(QtCore.QRect(280, 280, 100, 20))
        self.illnessLocationCheckBox_3.setText(_translate('Form', '基底节'))
        self.illnessLocationCheckBox_3.setStyleSheet("background:lightgray")

        self.illnessLocationCheckBox_4 = QtWidgets.QCheckBox(self.patientDetailInfo)
        self.illnessLocationCheckBox_4.setGeometry(QtCore.QRect(400, 280, 100, 20))
        self.illnessLocationCheckBox_4.setText(_translate('Form', '小脑'))
        self.illnessLocationCheckBox_4.setStyleSheet("background:lightgray")

        self.illnessLocationCheckBox_5 = QtWidgets.QCheckBox(self.patientDetailInfo)
        self.illnessLocationCheckBox_5.setGeometry(QtCore.QRect(40, 300, 100, 20))
        self.illnessLocationCheckBox_5.setText(_translate('Form', '顶叶'))
        self.illnessLocationCheckBox_5.setStyleSheet("background:lightgray")

        self.illnessLocationCheckBox_6 = QtWidgets.QCheckBox(self.patientDetailInfo)
        self.illnessLocationCheckBox_6.setGeometry(QtCore.QRect(160, 300, 100, 20))
        self.illnessLocationCheckBox_6.setText(_translate('Form', '内囊'))
        self.illnessLocationCheckBox_6.setStyleSheet("background:lightgray")

        self.illnessLocationCheckBox_7 = QtWidgets.QCheckBox(self.patientDetailInfo)
        self.illnessLocationCheckBox_7.setGeometry(QtCore.QRect(280, 300, 100, 20))
        self.illnessLocationCheckBox_7.setText(_translate('Form', '半卵脑区'))
        self.illnessLocationCheckBox_7.setStyleSheet("background:lightgray")

        self.illnessLocationCheckBox_8 = QtWidgets.QCheckBox(self.patientDetailInfo)
        self.illnessLocationCheckBox_8.setGeometry(QtCore.QRect(400, 300, 100, 20))
        self.illnessLocationCheckBox_8.setText(_translate('Form', '脑干'))
        self.illnessLocationCheckBox_8.setStyleSheet("background:lightgray")

        self.illnessLocationCheckBox_9 = QtWidgets.QCheckBox(self.patientDetailInfo)
        self.illnessLocationCheckBox_9.setGeometry(QtCore.QRect(40, 320, 100, 20))
        self.illnessLocationCheckBox_9.setText(_translate('Form', '什么叶'))  # TODO：这什么字
        self.illnessLocationCheckBox_9.setStyleSheet("background:lightgray")

        self.illnessLocationCheckBox_10 = QtWidgets.QCheckBox(self.patientDetailInfo)
        self.illnessLocationCheckBox_10.setGeometry(QtCore.QRect(160, 320, 100, 20))
        self.illnessLocationCheckBox_10.setText(_translate('Form', '外囊'))
        self.illnessLocationCheckBox_10.setStyleSheet("background:lightgray")

        self.illnessLocationCheckBox_11 = QtWidgets.QCheckBox(self.patientDetailInfo)
        self.illnessLocationCheckBox_11.setGeometry(QtCore.QRect(280, 320, 100, 20))
        self.illnessLocationCheckBox_11.setText(_translate('Form', '丘脑'))
        self.illnessLocationCheckBox_11.setStyleSheet("background:lightgray")

        self.courseLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.courseLabel.setGeometry(QtCore.QRect(20, 360, 100, 40))
        self.courseLabel.setAlignment(Qt.AlignCenter)
        self.courseLabel.setText(_translate('Form', '病 程'))
        self.courseLabel.setStyleSheet("background:lightgray")

        self.courseCombobox = QtWidgets.QComboBox(self.patientDetailInfo)
        self.courseCombobox.setGeometry(QtCore.QRect(140, 360, 300, 40))

        self.brunnstromLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.brunnstromLabel.setGeometry(QtCore.QRect(460, 360, 100, 40))
        self.brunnstromLabel.setAlignment(Qt.AlignCenter)
        self.brunnstromLabel.setText(_translate('Form', 'Brunnstrom分期'))
        self.brunnstromLabel.setStyleSheet("background:lightgray")

        self.brunnstromCombobox = QtWidgets.QComboBox(self.patientDetailInfo)
        self.brunnstromCombobox.setGeometry(QtCore.QRect(580, 360, 320, 40))

        self.lmtLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.lmtLabel.setGeometry(QtCore.QRect(20, 420, 100, 40))
        self.lmtLabel.setAlignment(Qt.AlignCenter)
        self.lmtLabel.setText(_translate('Form', '肌张力（屈）'))
        self.lmtLabel.setStyleSheet("background:lightgray")

        self.lmtElbowLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.lmtElbowLabel.setGeometry(QtCore.QRect(140, 420, 100, 40))
        self.lmtElbowLabel.setAlignment(Qt.AlignCenter)
        self.lmtElbowLabel.setText(_translate('Form', '肘关节'))
        self.lmtElbowLabel.setStyleSheet("background:lightgray")

        self.lmtElbowCombobox = QtWidgets.QComboBox(self.patientDetailInfo)
        self.lmtElbowCombobox.setGeometry(QtCore.QRect(260, 420, 150, 40))

        self.lmtWristLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.lmtWristLabel.setGeometry(QtCore.QRect(430, 420, 100, 40))
        self.lmtWristLabel.setAlignment(Qt.AlignCenter)
        self.lmtWristLabel.setText(_translate('Form', '腕关节'))
        self.lmtWristLabel.setStyleSheet("background:lightgray")

        self.lmtWristCombobox = QtWidgets.QComboBox(self.patientDetailInfo)
        self.lmtWristCombobox.setGeometry(QtCore.QRect(550, 420, 150, 40))

        self.lmtFingerTripLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.lmtFingerTripLabel.setGeometry(QtCore.QRect(720, 420, 100, 40))
        self.lmtFingerTripLabel.setAlignment(Qt.AlignCenter)
        self.lmtFingerTripLabel.setText(_translate('Form', '指尖关节'))
        self.lmtFingerTripLabel.setStyleSheet("background:lightgray")

        self.lmtFingerTripCombobox = QtWidgets.QComboBox(self.patientDetailInfo)
        self.lmtFingerTripCombobox.setGeometry(QtCore.QRect(840, 420, 150, 40))

        self.etLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.etLabel.setGeometry(QtCore.QRect(20, 480, 100, 40))
        self.etLabel.setAlignment(Qt.AlignCenter)
        self.etLabel.setText(_translate('Form', '肌张力（伸）'))
        self.etLabel.setStyleSheet("background:lightgray")

        self.etElbowLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.etElbowLabel.setGeometry(QtCore.QRect(140, 480, 100, 40))
        self.etElbowLabel.setAlignment(Qt.AlignCenter)
        self.etElbowLabel.setText(_translate('Form', '肘关节'))
        self.etElbowLabel.setStyleSheet("background:lightgray")

        self.etElbowCombobox = QtWidgets.QComboBox(self.patientDetailInfo)
        self.etElbowCombobox.setGeometry(QtCore.QRect(260, 480, 150, 40))

        self.etWristLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.etWristLabel.setGeometry(QtCore.QRect(430, 480, 100, 40))
        self.etWristLabel.setAlignment(Qt.AlignCenter)
        self.etWristLabel.setText(_translate('Form', '腕关节'))
        self.etWristLabel.setStyleSheet("background:lightgray")

        self.etWristCombobox = QtWidgets.QComboBox(self.patientDetailInfo)
        self.etWristCombobox.setGeometry(QtCore.QRect(550, 480, 150, 40))

        self.etFingerTripLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.etFingerTripLabel.setGeometry(QtCore.QRect(720, 480, 100, 40))
        self.etFingerTripLabel.setAlignment(Qt.AlignCenter)
        self.etFingerTripLabel.setText(_translate('Form', '指尖关节'))
        self.etFingerTripLabel.setStyleSheet("background:lightgray")

        self.etFingerTripCombobox = QtWidgets.QComboBox(self.patientDetailInfo)
        self.etFingerTripCombobox.setGeometry(QtCore.QRect(840, 480, 150, 40))

        self.vasLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.vasLabel.setGeometry(QtCore.QRect(20, 540, 100, 40))
        self.vasLabel.setAlignment(Qt.AlignCenter)
        self.vasLabel.setText(_translate('Form', 'VAS疼痛评分'))
        self.vasLabel.setStyleSheet("background:lightgray")

        self.vasCombobox = QtWidgets.QComboBox(self.patientDetailInfo)
        self.vasCombobox.setGeometry(QtCore.QRect(140, 540, 200, 40))

        self.painSiteLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.painSiteLabel.setGeometry(QtCore.QRect(360, 540, 100, 40))
        self.painSiteLabel.setAlignment(Qt.AlignCenter)
        self.painSiteLabel.setText(_translate('Form', '疼痛部位'))
        self.painSiteLabel.setStyleSheet("background:lightgray")

        self.painSiteLineEditor = QtWidgets.QLineEdit(self.patientDetailInfo)
        self.painSiteLineEditor.setGeometry(QtCore.QRect(480, 540, 400, 40))

        self.abstractLabel = QtWidgets.QLabel(self.patientDetailInfo)
        self.abstractLabel.setGeometry(QtCore.QRect(20, 600, 100, 40))
        self.abstractLabel.setAlignment(Qt.AlignCenter)
        self.abstractLabel.setText(_translate('Form', '病史摘要'))
        self.abstractLabel.setStyleSheet("background:lightgray")

        self.abstractTextEditor = QtWidgets.QTextEdit(self.patientDetailInfo)
        self.abstractTextEditor.setGeometry(QtCore.QRect(140, 600, 740, 100))

        self.addButton = QtWidgets.QPushButton(self.patientDetailInfo)
        self.addButton.setGeometry(QtCore.QRect(40, 840, 150, 40))

        self.deleteButton = QtWidgets.QPushButton(self.patientDetailInfo)
        self.deleteButton.setGeometry(QtCore.QRect(240, 840, 150, 40))

        self.saveButton = QtWidgets.QPushButton(self.patientDetailInfo)
        self.saveButton.setGeometry(QtCore.QRect(440, 840, 150, 40))

        self.patientInfoButton = QtWidgets.QPushButton(Form)
        self.patientInfoButton.setGeometry(QtCore.QRect(240, 1080, 150, 50))

        self.evaluateButton = QtWidgets.QPushButton(Form)
        self.evaluateButton.setGeometry(QtCore.QRect(460, 1080, 150, 50))

        self.trainButton = QtWidgets.QPushButton(Form)
        self.trainButton.setGeometry(QtCore.QRect(680, 1080, 150, 50))

        self.gameButton = QtWidgets.QPushButton(Form)
        self.gameButton.setGeometry(QtCore.QRect(900, 1080, 150, 50))

        self.setSystemButton = QtWidgets.QPushButton(Form)
        self.setSystemButton.setGeometry(QtCore.QRect(1120, 1080, 150, 50))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        self.idTypeComboboxItems = ['身份证', '驾驶证', '其他']
        self.sexComboboxItems = ['男', '女']
        self.handComboboxItems = ['左', '右']
        self.primaryEtiologyComboboxItems = ['脑卒中', ]  # TODO：等待具体内容
        self.secondaryEtiologyComboboxItems = [['脑梗死', ], ]  # TODO：等待具体内容
        self.courseComboboxItems = ['急性期（0-3个月）', ]  # TODO：等待具体内容
        self.brunnstromComboboxItems = ['III-IV （全指屈曲/或轻微手指伸展）']  # TODO：等待具体内容
        self.toneComboboxItems = ['0-1级', '1+ 级', '2  级', '3  级', '4  级', '5  级']
        self.vasComboboxItems = [str(i) for i in range(10)]

        self.systemNameCnLabel.setText(_translate("Form", "多模态镜像训练系统"))
        self.systemNameEnLabel.setText(_translate("Form", "Multimodel Mirror Training System"))
        self.changePassword.setText(_translate("Form", "密码修改"))
        self.systemHelp.setText(_translate("Form", "系统帮助"))
        self.systemExit.setText(_translate("Form", "系统退出"))
        self.timeLabel.setText(_translate("Form", "获取时间"))
        self.simpleButton.setText(_translate("Form", "简单查询"))
        self.advancedSearchButton.setText(_translate("Form", "高级查询"))
        self.headPageButton.setText(_translate("Form", "首页"))
        self.priorPageButton.setText(_translate("Form", "上一页"))
        self.pageInfoLabel.setText(_translate("Form", "第X页，共X页"))
        self.nextPageButton.setText(_translate("Form", "下一页"))
        self.tailPageButton.setText(_translate("Form", "尾页"))
        self.informationButton.setText(_translate("Form", "病人基本信息"))
        self.trainProgramButton.setText(_translate("Form", "训练方案"))
        self.trainlogButton.setText(_translate("Form", "训练日志"))
        self.assessScaleButton.setText(_translate("Form", "评估量表"))
        self.logScaleButton.setText(_translate("Form", "日志报表"))
        # self.patientInfoTable.setText(_translate("Form", "显示病人基本信息"))
        self.addButton.setText(_translate("Form", "新增"))
        self.deleteButton.setText(_translate("Form", "删除"))
        self.saveButton.setText(_translate("Form", "保存"))
        self.patientInfoButton.setText(_translate("Form", "病人信息"))
        self.evaluateButton.setText(_translate("Form", "评估"))
        self.trainButton.setText(_translate("Form", "训练"))
        self.gameButton.setText(_translate("Form", "游戏"))
        self.setSystemButton.setText(_translate("Form", "系统设置"))

        self.idTypeCombobox.addItems(self.idTypeComboboxItems)
        self.idTypeCombobox.setCurrentIndex(0)

        self.sexCombobox.addItems(self.sexComboboxItems)
        self.sexCombobox.setCurrentIndex(0)

        self.handednessCombobox.addItems(self.handComboboxItems)
        self.handednessCombobox.setCurrentIndex(0)

        self.illnessCombobox.addItems(self.handComboboxItems)
        self.illnessCombobox.setCurrentIndex(1)

        self.primaryEtiologyCombobox.addItems(self.primaryEtiologyComboboxItems)
        self.primaryEtiologyCombobox.setCurrentIndex(0)

        self.secondaryEtiologyCombobox.addItems(self.secondaryEtiologyComboboxItems[0])
        self.secondaryEtiologyCombobox.setCurrentIndex(0)

        self.courseCombobox.addItems(self.courseComboboxItems)
        self.courseCombobox.setCurrentIndex(0)

        self.brunnstromCombobox.addItems(self.brunnstromComboboxItems)
        self.brunnstromCombobox.setCurrentIndex(0)

        self.lmtElbowCombobox.addItems(self.toneComboboxItems)
        self.lmtElbowCombobox.setCurrentIndex(0)

        self.lmtWristCombobox.addItems(self.toneComboboxItems)
        self.lmtWristCombobox.setCurrentIndex(0)

        self.lmtFingerTripCombobox.addItems(self.toneComboboxItems)
        self.lmtFingerTripCombobox.setCurrentIndex(0)

        self.etElbowCombobox.addItems(self.toneComboboxItems)
        self.etElbowCombobox.setCurrentIndex(0)

        self.etWristCombobox.addItems(self.toneComboboxItems)
        self.etWristCombobox.setCurrentIndex(0)

        self.etFingerTripCombobox.addItems(self.toneComboboxItems)
        self.etFingerTripCombobox.setCurrentIndex(0)

        self.vasCombobox.addItems(self.vasComboboxItems)
        self.vasCombobox.setCurrentIndex(0)


class MainInterface(QtWidgets.QMainWindow, Ui_Form):
    # singal = pyqtSignal(list)
    def __init__(self, accountId):
        super(MainInterface, self).__init__()
        self.setupUi(self)

        self.accountId = accountId

        self.patientSelectedInfo = None
        self.patientInfoSheetLength = 0
        self.patientInfoSheet = None
        self.patientSelectedId = None
        self.patientInfoSheetMaxPages = None
        self.nowPage = 1

        self.patientInfoSheetColumnsCn = ['物理id', '姓名', '性别', '年龄', '患手']
        self.patientInfoSheetColumnsEn = ['id', 'name', 'sex', 'age', 'illness']
        self.patientInfoText = "第{}页，共{}页"

        self.threadHelper = tool.ThreadingHelper.ThreadingHelper()

        self.changePassword.mousePressEvent = self.changePasswordClick
        self.systemHelp.mousePressEvent = self.systemHelpClick
        self.systemExit.mousePressEvent = self.systemExitClick
        self.simpleButton.mousePressEvent = self.simpleButtonClick
        self.advancedSearchButton.mousePressEvent = self.advancedSearchButtonClick
        self.headPageButton.mousePressEvent = self.headPageButtonClick
        self.priorPageButton.mousePressEvent = self.priorPageButtonClick
        self.nextPageButton.mousePressEvent = self.nextPageButtonClick
        self.tailPageButton.mousePressEvent = self.tailPageButtonClick
        self.informationButton.mousePressEvent = self.informationButtonClick
        self.trainProgramButton.mousePressEvent = self.trainProgramButtonClick
        self.assessScaleButton.mousePressEvent = self.assessScaleButtonClick
        self.logScaleButton.mousePressEvent = self.logScaleButtonClick
        self.trainlogButton.mousePressEvent = self.trainlogButtonClick
        self.addButton.mousePressEvent = self.addButtonClick
        self.deleteButton.mousePressEvent = self.deleteButtonClick
        self.saveButton.mousePressEvent = self.saveButtonClick
        self.patientInfoButton.mousePressEvent = self.patientInfoButtonClick
        self.evaluateButton.mousePressEvent = self.evaluateButtonClick
        self.trainButton.mousePressEvent = self.trainButtonClick
        self.gameButton.mousePressEvent = self.gameButtonClick
        self.setSystemButton.mousePressEvent = self.setSystemButtonClick
        self.patientInfoTable.mouseDoubleClickEvent = self.patientInfoTableClick
        # self.confirmButton.mousePressEvent=self.confirmButtonClick
        self.illnessList = [getattr(self, 'illnessLocationCheckBox_{}'.format(i)) for i in range(1, 12)]
        self.illnessListValue = [i.text() for i in self.illnessList]

        self.timeLabelWork = threading.Thread(target=self.timeLabelSwitch)
        self.timeLabelWork.start()

        self.initPatientInfoTable()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.threadHelper.close(self.timeLabelWork)

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

    def patientInfoTableClick(self, *args):
        _translate = QtCore.QCoreApplication.translate
        selectIndex = int(self.patientInfoTable.selectedItems()[0].row())
        self.patientSelectedId = self.patientInfoSheet[(self.nowPage - 1) * 15 + selectIndex]['id']
        self.patientSelectedInfo = json.loads(
            requests.post(config.patientGetById, data={'id': self.patientSelectedId}).content.decode('utf-8'))[
            'data']
        self.nameLineEditor.setText(_translate('Form', self.patientSelectedInfo['name']))
        self.idTypeCombobox.setCurrentIndex(self.idTypeComboboxItems.index(self.patientSelectedInfo['id_type']))
        self.idDetailLineEditor.setText(_translate('Form', self.patientSelectedInfo['id_detail']))
        self.sexCombobox.setCurrentIndex(self.sexComboboxItems.index(self.patientSelectedInfo['sex']))
        self.ageLineEditor.setText(_translate('Form', str(self.patientSelectedInfo['age'])))
        self.telLineEditor.setText(_translate('Form', str(self.patientSelectedInfo['tel'])))
        self.handednessCombobox.setCurrentIndex(self.handComboboxItems.index(self.patientSelectedInfo['handedness']))
        self.illnessCombobox.setCurrentIndex(self.handComboboxItems.index(self.patientSelectedInfo['illness']))
        self.primaryEtiologyCombobox.setCurrentIndex(
            self.primaryEtiologyComboboxItems.index(self.patientSelectedInfo['primary_etiology']))
        self.secondaryEtiologyCombobox.setCurrentIndex(
            self.secondaryEtiologyComboboxItems[
                self.primaryEtiologyComboboxItems.index(self.patientSelectedInfo['primary_etiology'])].index(
                self.patientSelectedInfo['secondary_etiology'])
        )

        for i in range(11):
            self.illnessList[i].setCheckState(Qt.Unchecked)

        for i in self.patientSelectedInfo['illness_site']:
            idx = self.illnessListValue.index(i)
            self.illnessList[idx].setCheckState(Qt.Checked)

        self.courseCombobox.setCurrentIndex(self.courseComboboxItems.index(self.patientSelectedInfo['course']))
        self.brunnstromCombobox.setCurrentIndex(
            self.brunnstromComboboxItems.index(self.patientSelectedInfo['brunnstrom']))

        self.lmtElbowCombobox.setCurrentIndex(self.toneComboboxItems.index(self.patientSelectedInfo['lmt_elbow']))
        self.lmtWristCombobox.setCurrentIndex(self.toneComboboxItems.index(self.patientSelectedInfo['lmt_wrist']))
        self.lmtFingerTripCombobox.setCurrentIndex(
            self.toneComboboxItems.index(self.patientSelectedInfo['lmt_fingertip']))

        self.etElbowCombobox.setCurrentIndex(self.toneComboboxItems.index(self.patientSelectedInfo['et_elbow']))
        self.etWristCombobox.setCurrentIndex(self.toneComboboxItems.index(self.patientSelectedInfo['et_wrist']))
        self.etFingerTripCombobox.setCurrentIndex(
            self.toneComboboxItems.index(self.patientSelectedInfo['et_fingertip']))

        self.vasCombobox.setCurrentIndex(self.vasComboboxItems.index(self.patientSelectedInfo['vas']))

        self.painSiteLineEditor.setText(_translate('Form', self.patientSelectedInfo['pain_site']))

        self.abstractTextEditor.setText(_translate('Form', self.patientSelectedInfo['abstract']))

    def patientInfoTableClear(self):
        # 清空表格内容
        for i in range(15):
            for j in range(1, 5):
                self.patientInfoTable.setItem(i, j - 1, QTableWidgetItem(""))

    def patientInfoTableSetter(self, pages):
        # 根据页码设置表格内容
        _translate = QtCore.QCoreApplication.translate
        self.patientInfoTableClear()
        for i in range((pages - 1) * 15, min(pages * 15, self.patientInfoSheetLength)):
            for j in range(1, 5):
                self.patientInfoTable.setItem(i % 15, j - 1, QTableWidgetItem(
                    str(self.patientInfoSheet[i][self.patientInfoSheetColumnsEn[j]])))
        self.pageInfoLabel.setText(
            _translate("Form", self.patientInfoText.format(self.nowPage, self.patientInfoSheetMaxPages)))

    def changePasswordClick(self, *args):
        # 修改密码，可以与忘记密码页面共用
        self.forgetPasswordWindow = frontend.ForgetPassword.ForgetPassword(self.accountId)
        self.forgetPasswordWindow.show()

    def systemHelpClick(self, *args):
        # 系统帮助，后期可以改为按钮形式，或许
        ...

    def systemExitClick(self, *args):
        # 退出系统
        self.close()
        exit(0)

    def timeLabelSwitch(self, *args):
        # 获取系统时间 年/月/日/时/分/秒
        _translate = QtCore.QCoreApplication.translate
        while True:
            self.timeLabel.setText(_translate('Form', tool.Tools.getNowTime()))
            time.sleep(1)

    def simpleButtonClick(self, *args):
        # 病人信息简单查询按钮
        name = self.simpleSearchLineEditor.text()
        self.patientInfoSheet = json.loads(
            requests.post(config.patientListByName, data={'patient_id': self.accountId, 'name': name}).content.decode(
                'utf-8'))['data']
        self.patientInfoSheetLength = len(self.patientInfoSheet)

        if self.patientInfoSheetLength % 15 == 0:
            self.patientInfoSheetMaxPages = int(self.patientInfoSheetLength // 15)
        else:
            self.patientInfoSheetMaxPages = int(self.patientInfoSheetLength // 15 + 1)

        self.nowPage = 1

        self.patientInfoTableSetter(self.nowPage)

    def advancedSearchButtonClick(self, *args):
        # 病人信息高级查询按钮
        self.advancedSearchWindow = frontend.AdvancedSearch.AdvancedSearch()
        self.advancedSearchWindow.show()
        ...

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

    def informationButtonClick(self, *args):
        # 病人基本信息按钮，首页默认已用
        pass

    def trainProgramButtonClick(self, *args):
        # 病人训练方案按钮，要与当前页面显示的病人信息连接起来，即显示该病人的训练方案
        ...

    def assessScaleButtonClick(self, *args):
        # 评估量表
        ...

    def logScaleButtonClick(self, *args):
        # 日志报表
        ...

    def trainlogButtonClick(self, *args):
        # 病人训练日志
        ...

    def addButtonClick(self, *args):
        # 添加病人信息
        ...

    def deleteButtonClick(self, *args):
        # 删除病人信息
        ...

    def saveButtonClick(self, *args):
        # 保存病人信息
        ...

    def patientInfoButtonClick(self, *args):
        # 病人信息按钮
        ...

    def evaluateButtonClick(self, *args):
        # 评估按钮
        ...

    def trainButtonClick(self, *args):
        # 训练按钮
        self.basicTrainingWindow = frontend.BasicTraining.BasicTraining()
        self.basicTrainingWindow.show()

    def gameButtonClick(self, *args):
        # 游戏
        pass

    def setSystemButtonClick(self, *args):
        # 系统设置
        self.setSystemWindow = frontend.SetSystem.SetSystem()
        self.setSystemWindow.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = MainInterface(None)
    gui.show()
    sys.exit(app.exec_())
