# coding=utf-8
import json
import os
import sys
import threading
import time

import cv2
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, QTimer, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QStyle, QAction, QMenu, QToolButton, QTreeWidgetItem, QTimeEdit, \
    QDesktopWidget, QFileDialog

import config
import frontend
import tool.VideoHelper


class Ui_Form(object):
    def setupUi(self, Form):
        Form.resize(1920, 1080)  # 界面大小
        Form.setStyleSheet("background:white")

        self.topLabel = QtWidgets.QLabel(Form)
        self.topLabel.setGeometry(QtCore.QRect(0, 0, 1920, 100))
        self.topLabel.setStyleSheet("background:rgb(85, 170, 255)")

        self.label = QtWidgets.QLabel(Form)  # 手功能三维动作分析捕捉系统
        self.label.setGeometry(QtCore.QRect(10, 30, 500, 50))
        self.label.setStyleSheet("color:white;font:16pt;background:rgb(85, 170, 255)")

        self.resetPasswordLabel = QtWidgets.QLabel(Form)  # 密码修改
        self.resetPasswordLabel.setGeometry(QtCore.QRect(1600, 10, 200, 40))
        self.resetPasswordLabel.setStyleSheet("color:white;font:12pt;background:rgb(85, 170, 255)")

        self.exitSystemLabel = QtWidgets.QLabel(Form)  # 系统退出
        self.exitSystemLabel.setGeometry(QtCore.QRect(1800, 10, 200, 40))
        self.exitSystemLabel.setStyleSheet("color:white;font:12pt;background:rgb(85, 170, 255)")

        self.timeLabel = QtWidgets.QLabel(Form)  # 显示系统时间
        self.timeLabel.setGeometry(QtCore.QRect(1500, 60, 500, 40))
        self.timeLabel.setStyleSheet("font:12pt;background:rgb(85, 170, 255)")

        self.label_2 = QtWidgets.QLabel(Form)  # 姓名
        self.label_2.setGeometry(QtCore.QRect(10, 110, 120, 40))
        self.label_2.setStyleSheet("font:12pt")

        self.nameLabel = QtWidgets.QLabel(Form)  # 获取病人姓名
        self.nameLabel.setGeometry(QtCore.QRect(70, 110, 200, 40))
        self.nameLabel.setStyleSheet("font:12pt")

        self.label_3 = QtWidgets.QLabel(Form)  # 年龄
        self.label_3.setGeometry(QtCore.QRect(270, 110, 200, 40))
        self.label_3.setStyleSheet("font:12pt")

        self.ageLabel = QtWidgets.QLabel(Form)  # 获取病人年龄
        self.ageLabel.setGeometry(QtCore.QRect(330, 110, 200, 40))
        self.ageLabel.setStyleSheet("font:12pt")

        self.label_4 = QtWidgets.QLabel(Form)  # 性别
        self.label_4.setGeometry(QtCore.QRect(530, 110, 200, 40))
        self.label_4.setStyleSheet("font:12pt")

        self.sexLabel = QtWidgets.QLabel(Form)  # 获取病人性别
        self.sexLabel.setGeometry(QtCore.QRect(590, 110, 200, 40))
        self.sexLabel.setStyleSheet("font:12pt")

        self.label_5 = QtWidgets.QLabel(Form)  # 患手
        self.label_5.setGeometry(QtCore.QRect(790, 110, 200, 40))
        self.label_5.setStyleSheet("font:12pt")

        self.unhealthHandlabel = QtWidgets.QLabel(Form)  # 获取病人患疾病的手
        self.unhealthHandlabel.setGeometry(QtCore.QRect(850, 110, 200, 40))
        self.unhealthHandlabel.setStyleSheet("font:12pt")

        self.label_6 = QtWidgets.QLabel(Form)  # 疾病类型
        self.label_6.setGeometry(QtCore.QRect(1050, 110, 200, 40))
        self.label_6.setStyleSheet("font:12pt")

        self.diseaseTypeLabel_1 = QtWidgets.QLabel(Form)  # 获取一级疾病类型
        self.diseaseTypeLabel_1.setGeometry(QtCore.QRect(1160, 110, 350, 40))
        self.diseaseTypeLabel_1.setStyleSheet("font:12pt")

        self.diseaseTypeLabel_2 = QtWidgets.QLabel(Form)  # 获取二级疾病类型
        self.diseaseTypeLabel_2.setGeometry(QtCore.QRect(1300, 110, 200, 40))
        self.diseaseTypeLabel_2.setStyleSheet("font:12pt")

        self.divideLineLabel = QtWidgets.QLabel(Form)  # 蓝色横线
        self.divideLineLabel.setGeometry(QtCore.QRect(0, 150, 1920, 2))
        self.divideLineLabel.setStyleSheet("background:rgb(85, 170, 255)")

        self.spaceImaginationButton = QtWidgets.QPushButton(Form)  # 空间想象训练按钮
        self.spaceImaginationButton.setGeometry(QtCore.QRect(0, 152, 200, 50))

        self.sensorimotorButton = QtWidgets.QPushButton(Form)  # 感觉运动训练按钮
        self.sensorimotorButton.setGeometry(QtCore.QRect(200, 152, 200, 50))

        self.basicButton = QtWidgets.QPushButton(Form)  # 基本动作训练按钮
        self.basicButton.setGeometry(QtCore.QRect(400, 152, 200, 50))

        self.functionButton = QtWidgets.QPushButton(Form)  # 功能动作训练按钮
        self.functionButton.setGeometry(QtCore.QRect(600, 152, 200, 50))

        self.mirrorButton = QtWidgets.QPushButton(Form)  # 镜像训练按钮
        self.mirrorButton.setGeometry(QtCore.QRect(800, 152, 200, 50))

        self.patientinformationButton = QtWidgets.QPushButton(Form)  # 病人信息按钮
        self.patientinformationButton.setGeometry(QtCore.QRect(60, 1020, 200, 50))

        self.trainButton = QtWidgets.QPushButton(Form)
        self.trainButton.setGeometry(QtCore.QRect(300, 1020, 200, 50))

        self.setSystemButton = QtWidgets.QPushButton(Form)
        self.setSystemButton.setGeometry(QtCore.QRect(540, 1020, 200, 50))

        self.gameButton = QtWidgets.QPushButton(Form)
        self.gameButton.setGeometry(QtCore.QRect(800, 1020, 200, 50))
        self.gameButton.setVisible(False)

        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 210, 1920, 780))

        self.page = QtWidgets.QWidget()  # 空间想象训练堆叠窗口

        pix = QtGui.QPixmap(config.GlobalPath + "src/fig/welcome_use.jpg")
        self.picturLabel = QtWidgets.QLabel(self.page)  # 空间想象训练图片显示
        self.picturLabel.setGeometry(QtCore.QRect(1100, 30, 800, 740))
        self.picturLabel.setPixmap(pix)
        self.picturLabel.setScaledContents(True)
        self.picturLabel.setStyleSheet("border-width: 1px;border-style: solid;border-color:black")

        self.spaceImaginationFrame = QtWidgets.QFrame(self.page)  # 空间想象训练容器布局
        self.spaceImaginationFrame.setGeometry(QtCore.QRect(20, 220, 1000, 575))
        self.spaceImaginationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spaceImaginationFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.label_11 = QtWidgets.QLabel(self.spaceImaginationFrame)  # 训练情况
        self.label_11.setGeometry(QtCore.QRect(10, 10, 250, 40))
        self.label_11.setStyleSheet("font:14pt;color:#00BFFF")

        self.label_12 = QtWidgets.QLabel(self.spaceImaginationFrame)  # 总共（张）
        self.label_12.setGeometry(QtCore.QRect(10, 70, 200, 70))
        self.label_12.setStyleSheet("font:12pt;")

        self.spaceImageTrainingPictureTotalNumber = QtWidgets.QLabel(self.spaceImaginationFrame)  # 显示图片训练的总张数
        self.spaceImageTrainingPictureTotalNumber.setGeometry(QtCore.QRect(160, 70, 200, 70))
        self.spaceImageTrainingPictureTotalNumber.setStyleSheet("font:12pt;")

        self.label_13 = QtWidgets.QLabel(self.spaceImaginationFrame)  # 当前张
        self.label_13.setGeometry(QtCore.QRect(280, 70, 230, 70))
        self.label_13.setStyleSheet("font:12pt;")

        self.currentPictureNumLabel = QtWidgets.QLabel(self.spaceImaginationFrame)  # 显示当前图片训练张数
        self.currentPictureNumLabel.setGeometry(QtCore.QRect(430, 70, 200, 70))
        self.currentPictureNumLabel.setStyleSheet("font:12pt;")

        self.label_14 = QtWidgets.QLabel(self.spaceImaginationFrame)  # 剩余张
        self.label_14.setGeometry(QtCore.QRect(570, 70, 200, 70))
        self.label_14.setStyleSheet("font:12pt;")

        self.remainPictureNumLabel = QtWidgets.QLabel(self.spaceImaginationFrame)  # 显示图片训练剩余张数
        self.remainPictureNumLabel.setGeometry(QtCore.QRect(740, 70, 200, 70))
        self.remainPictureNumLabel.setStyleSheet("font:12pt;")

        self.label_15 = QtWidgets.QLabel(self.spaceImaginationFrame)  # 正确张数
        self.label_15.setGeometry(QtCore.QRect(10, 170, 200, 70))
        self.label_15.setStyleSheet("font:12pt;")

        self.correctNumLabel = QtWidgets.QLabel(self.spaceImaginationFrame)  # 获取总的选择的正确数量
        self.correctNumLabel.setGeometry(QtCore.QRect(160, 170, 200, 70))
        self.correctNumLabel.setStyleSheet("font:12pt;")

        self.label_16 = QtWidgets.QLabel(self.spaceImaginationFrame)  # 左手正确数量
        self.label_16.setGeometry(QtCore.QRect(280, 170, 200, 70))
        self.label_16.setStyleSheet("font:12pt;")

        self.leftCorrectNumLabel = QtWidgets.QLabel(self.spaceImaginationFrame)  # 选择左手图片判断正确的数量
        self.leftCorrectNumLabel.setGeometry(QtCore.QRect(480, 170, 200, 70))
        self.leftCorrectNumLabel.setStyleSheet("font:12pt;")

        self.label_17 = QtWidgets.QLabel(self.spaceImaginationFrame)  # 右手正确数量
        self.label_17.setGeometry(QtCore.QRect(570, 170, 200, 70))
        self.label_17.setStyleSheet("font:12pt;")

        self.rightCorrectNumLabel = QtWidgets.QLabel(self.spaceImaginationFrame)  # 选择右手图片判断正确的数量
        self.rightCorrectNumLabel.setGeometry(QtCore.QRect(780, 170, 200, 70))
        self.rightCorrectNumLabel.setStyleSheet("font:12pt;")

        self.label_18 = QtWidgets.QLabel(self.spaceImaginationFrame)  # 正确率
        self.label_18.setGeometry(QtCore.QRect(10, 270, 200, 70))
        self.label_18.setStyleSheet("font:12pt;")

        self.correctRateLabel = QtWidgets.QLabel(self.spaceImaginationFrame)  # 获取正确率
        self.correctRateLabel.setGeometry(QtCore.QRect(170, 270, 200, 70))
        self.correctRateLabel.setStyleSheet("font:12pt;")

        self.label_19 = QtWidgets.QLabel(self.spaceImaginationFrame)  # 左手正确率
        self.label_19.setGeometry(QtCore.QRect(280, 270, 200, 70))
        self.label_19.setStyleSheet("font:12pt;")

        self.leftCorrectRateLabel = QtWidgets.QLabel(self.spaceImaginationFrame)  # 选择左手图片判断正确的几率
        self.leftCorrectRateLabel.setGeometry(QtCore.QRect(480, 270, 200, 70))
        self.leftCorrectRateLabel.setStyleSheet("font:12pt;")

        self.label_20 = QtWidgets.QLabel(self.spaceImaginationFrame)  # 右手正确率
        self.label_20.setGeometry(QtCore.QRect(570, 270, 200, 70))
        self.label_20.setStyleSheet("font:12pt;")

        self.rightCorrectRateLabel = QtWidgets.QLabel(self.spaceImaginationFrame)  # 选择右手图片判断正确的几率
        self.rightCorrectRateLabel.setGeometry(QtCore.QRect(780, 270, 200, 70))
        self.rightCorrectRateLabel.setStyleSheet("font:12pt;")

        self.label_21 = QtWidgets.QLabel(self.spaceImaginationFrame)  # 平均用时
        self.label_21.setGeometry(QtCore.QRect(10, 370, 200, 70))
        self.label_21.setStyleSheet("font:12pt;")

        self.averageTimeLabel = QtWidgets.QLabel(self.spaceImaginationFrame)  # 获取平均用时
        self.averageTimeLabel.setGeometry(QtCore.QRect(200, 370, 200, 70))
        self.averageTimeLabel.setStyleSheet("font:12pt;")

        self.label_22 = QtWidgets.QLabel(self.spaceImaginationFrame)  # 左手平均用时
        self.label_22.setGeometry(QtCore.QRect(280, 370, 200, 70))
        self.label_22.setStyleSheet("font:12pt;")

        self.leftAverageTimeLabel = QtWidgets.QLabel(self.spaceImaginationFrame)  # 获取左手平均用时
        self.leftAverageTimeLabel.setGeometry(QtCore.QRect(480, 370, 200, 70))
        self.leftAverageTimeLabel.setStyleSheet("font:12pt;")

        self.label_23 = QtWidgets.QLabel(self.spaceImaginationFrame)  # 右手平均用时
        self.label_23.setGeometry(QtCore.QRect(570, 370, 200, 70))
        self.label_23.setStyleSheet("font:12pt;")

        self.rightAverageTimeLabel = QtWidgets.QLabel(self.spaceImaginationFrame)  # 获取右手平均用时
        self.rightAverageTimeLabel.setGeometry(QtCore.QRect(780, 370, 200, 70))
        self.rightAverageTimeLabel.setStyleSheet("font:12pt;")

        self.label_118 = QtWidgets.QLabel(self.spaceImaginationFrame)  # 训练时长
        self.label_118.setGeometry(QtCore.QRect(10, 470, 200, 70))
        self.label_118.setStyleSheet("font:14pt;")

        self.trainingTimeLabel = QtWidgets.QLabel(self.spaceImaginationFrame)  # 获取空间想象训练时长
        self.trainingTimeLabel.setGeometry(QtCore.QRect(170, 470, 200, 70))
        self.trainingTimeLabel.setStyleSheet("font:12pt;")

        self.label_7 = QtWidgets.QLabel(self.page)  # 训练参数设置
        self.label_7.setGeometry(QtCore.QRect(20, 70, 200, 40))
        self.label_7.setStyleSheet("font:14pt;color:#1E90FF")

        self.trainProgramFrame = QtWidgets.QFrame(self.page)  # 训练方案容器
        self.trainProgramFrame.setGeometry(QtCore.QRect(10, 0, 600, 60))
        self.trainProgramFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.trainProgramFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.trainProgramLabel = QtWidgets.QLabel(self.trainProgramFrame)  # 训练方案
        self.trainProgramLabel.setGeometry(QtCore.QRect(10, 10, 200, 40))
        self.trainProgramLabel.setStyleSheet("font:14pt;color:#1E90FF")

        self.trainProgramComboBox = QtWidgets.QComboBox(self.trainProgramFrame)  # 训练方案选择
        self.trainProgramComboBox.setGeometry(QtCore.QRect(140, 10, 300, 40))
        self.trainProgramComboBox.setObjectName("trainProgramComboBox")
        self.trainProgramFrame.setVisible(False)

        self.label_8 = QtWidgets.QLabel(self.page)  # 图片总数
        self.label_8.setGeometry(QtCore.QRect(20, 120, 200, 40))
        self.label_8.setStyleSheet("font:12pt;")

        self.pictureNumComboBox = QtWidgets.QComboBox(self.page)  # 图片总数选择
        self.pictureNumComboBox.setGeometry(QtCore.QRect(200, 120, 150, 40))
        self.pictureNumComboBox.addItems(['', '10', '20', '30', '40', '50', '60'])
        self.pictureNumComboBox.setStyleSheet("font:12pt;")

        self.label_9 = QtWidgets.QLabel(self.page)  # 播放速率
        self.label_9.setGeometry(QtCore.QRect(360, 120, 200, 40))
        self.label_9.setStyleSheet("font:12pt;")

        self.playSpeedCombobox = QtWidgets.QComboBox(self.page)  # 空间想象播放速率选择
        self.playSpeedCombobox.setGeometry(QtCore.QRect(540, 120, 150, 40))
        self.playSpeedCombobox.addItems(['', '3', '5', '7', '8', '9', '10'])
        self.playSpeedCombobox.setStyleSheet("font:12pt;")

        self.label_10 = QtWidgets.QLabel(self.page)  # 辨别难度
        self.label_10.setGeometry(QtCore.QRect(710, 120, 200, 40))
        self.label_10.setStyleSheet("font:12pt;")

        self.discriminationDifficultyComboBox = QtWidgets.QComboBox(self.page)  # 辨别难度选择
        self.discriminationDifficultyComboBox.setGeometry(QtCore.QRect(840, 120, 200, 40))
        self.discriminationDifficultyComboBox.addItems(['', '低难度', '中难度', '高难度'])
        self.discriminationDifficultyComboBox.setStyleSheet("font:12pt;")

        # 播放状态记录变量
        self.is_playing = True

        self.space_startButton = QtWidgets.QPushButton(self.page)  # 空间想象开始训练按钮
        self.space_startButton.setGeometry(QtCore.QRect(650, 175, 150, 40))

        self.stopButtonFrame = QtWidgets.QFrame(self.page)  # 空间想象停止训练容器
        self.stopButtonFrame.setGeometry(QtCore.QRect(830, 175, 150, 40))
        self.stopButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stopButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.stopButton = QtWidgets.QPushButton(self.stopButtonFrame)  # 空间想象停止按钮
        self.stopButton.setGeometry(QtCore.QRect(0, 0, 175, 40))
        self.stopButtonFrame.setVisible(False)

        self.page_2 = QtWidgets.QWidget()

        self.basic_selectTrainingFrame = QtWidgets.QFrame(self.page_2)  # 基本动作训练容器
        self.basic_selectTrainingFrame.setGeometry(QtCore.QRect(10, 10, 700, 600))
        self.basic_selectTrainingFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.basic_selectTrainingFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.basic_scrollArea = QtWidgets.QScrollArea(self.basic_selectTrainingFrame)  # 基本动作训练滑动窗口
        self.basic_scrollArea.setGeometry(QtCore.QRect(0, 0, 700, 600))
        self.basic_scrollArea.setWidgetResizable(True)

        self.basic_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.basic_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 700, 600))
        self.basic_scrollAreaWidgetContents.setMinimumHeight(3000)
        self.basic_scrollArea.setWidget(self.basic_scrollAreaWidgetContents)

        self.basic_leftTree = QtWidgets.QTreeWidget(self.basic_scrollAreaWidgetContents)
        self.basic_leftTree.setGeometry(QtCore.QRect(0, 0, 700, 10000))
        self.basic_leftTree.setStyleSheet('font:14pt')
        # 为树控件指定列数
        self.basic_leftTree.setColumnCount(1)
        # 指定列标签
        self.basic_leftTree.setHeaderLabels(['基本训练动作_左'])
        # 根节点
        self.basic_trainingLeftActionRoot_1 = QTreeWidgetItem(self.basic_leftTree)  # 基本动作训练-训练动作1根节点
        self.basic_trainingLeftActionRoot_1.setText(0, '拇指运动')  # 0代表第一列，即Key列
        self.basic_leftTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.basic_trainingLeftActionRoot_1.setCheckState(0, Qt.Unchecked)

        # 添加子节点1
        self.basic_trainingLeftAction1Child_1 = QTreeWidgetItem(
            self.basic_trainingLeftActionRoot_1)  # 基本动作训练-训练动作1的孩子节点1
        self.basic_trainingLeftAction1Child_1.setText(0, '拇指对食指')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.basic_trainingLeftAction1Child_1.setCheckState(0, Qt.Unchecked)
        self.basic_trainingLeftAction1Child_2 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_1)
        self.basic_trainingLeftAction1Child_2.setText(0, '拇指对小指指根')
        self.basic_trainingLeftAction1Child_2.setCheckState(0, Qt.Unchecked)
        self.basic_trainingLeftAction1Child_3 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_1)
        self.basic_trainingLeftAction1Child_3.setText(0, '拇指环转')
        self.basic_trainingLeftAction1Child_3.setCheckState(0, Qt.Unchecked)
        self.basic_trainingLeftAction1Child_4 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_1)
        self.basic_trainingLeftAction1Child_4.setText(0, '拇指屈伸')
        self.basic_trainingLeftAction1Child_4.setCheckState(0, Qt.Unchecked)
        self.basic_trainingLeftAction1Child_5 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_1)
        self.basic_trainingLeftAction1Child_5.setText(0, '拇指外展')
        self.basic_trainingLeftAction1Child_5.setCheckState(0, Qt.Unchecked)
        self.basic_trainingLeftAction1Child_6 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_1)
        self.basic_trainingLeftAction1Child_6.setText(0, '拇指对四指')
        self.basic_trainingLeftAction1Child_6.setCheckState(0, Qt.Unchecked)
        self.basic_trainingLeftAction1Child_7 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_1)
        self.basic_trainingLeftAction1Child_7.setText(0, '拇指对掌')
        self.basic_trainingLeftAction1Child_7.setCheckState(0, Qt.Unchecked)
        self.basic_trainingLeftAction1Child_8 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_1)
        self.basic_trainingLeftAction1Child_8.setText(0, '拇指伸展')
        self.basic_trainingLeftAction1Child_8.setCheckState(0, Qt.Unchecked)

        self.basic_trainingLeftActionRoot_2 = QTreeWidgetItem(self.basic_leftTree)  # 基本动作训练-训练动作2根节点
        self.basic_trainingLeftActionRoot_2.setText(0, '精细灵活性运动')  # 0代表第一列，即Key列
        self.basic_leftTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.basic_trainingLeftActionRoot_2.setCheckState(0, Qt.Unchecked)
        # 添加子节点1
        self.basic_trainingLeftAction2Child_1 = QTreeWidgetItem(
            self.basic_trainingLeftActionRoot_2)  # 基本动作训练-训练动作1的孩子节点1
        self.basic_trainingLeftAction2Child_1.setText(0, '比OK')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.basic_trainingLeftAction2Child_1.setCheckState(0, Qt.Unchecked)
        # 添加子节点2
        self.basic_trainingLeftAction2Child_2 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_2)
        self.basic_trainingLeftAction2Child_2.setText(0, '比数字')
        self.basic_trainingLeftAction2Child_2.setCheckState(0, Qt.Unchecked)
        self.basic_trainingLeftAction2Child_3 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_2)
        self.basic_trainingLeftAction2Child_3.setText(0, '侧捏')
        self.basic_trainingLeftAction2Child_3.setCheckState(0, Qt.Unchecked)

        # 根节点
        self.basic_trainingLeftActionRoot_3 = QTreeWidgetItem(self.basic_leftTree)  # 基本动作训练-训练动作2根节点
        self.basic_trainingLeftActionRoot_3.setText(0, '抓握运动')  # 0代表第一列，即Key列
        self.basic_leftTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.basic_trainingLeftActionRoot_3.setCheckState(0, Qt.Unchecked)
        # 添加子节点1
        self.basic_trainingLeftAction3Child_1 = QTreeWidgetItem(
            self.basic_trainingLeftActionRoot_3)  # 基本动作训练-训练动作1的孩子节点1
        self.basic_trainingLeftAction3Child_1.setText(0, '钩状抓握')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.basic_trainingLeftAction3Child_1.setCheckState(0, Qt.Unchecked)
        # 添加子节点2
        self.basic_trainingLeftAction3Child_2 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_3)
        self.basic_trainingLeftAction3Child_2.setText(0, '球状抓握')
        self.basic_trainingLeftAction3Child_2.setCheckState(0, Qt.Unchecked)
        self.basic_trainingLeftAction3Child_3 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_3)
        self.basic_trainingLeftAction3Child_3.setText(0, '握拳')
        self.basic_trainingLeftAction3Child_3.setCheckState(0, Qt.Unchecked)
        self.basic_trainingLeftAction3Child_4 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_3)
        self.basic_trainingLeftAction3Child_4.setText(0, '直拳')
        self.basic_trainingLeftAction3Child_4.setCheckState(0, Qt.Unchecked)
        self.basic_trainingLeftAction3Child_5 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_3)
        self.basic_trainingLeftAction3Child_5.setText(0, '柱状抓握')
        self.basic_trainingLeftAction3Child_5.setCheckState(0, Qt.Unchecked)

        self.basic_trainingLeftActionRoot_4 = QTreeWidgetItem(self.basic_leftTree)  # 基本动作训练-训练动作2根节点
        self.basic_trainingLeftActionRoot_4.setText(0, '手指动作')  # 0代表第一列，即Key列
        self.basic_leftTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.basic_trainingLeftActionRoot_4.setCheckState(0, Qt.Unchecked)
        # 添加子节点1
        self.basic_trainingLeftAction4Child_1 = QTreeWidgetItem(
            self.basic_trainingLeftActionRoot_4)  # 基本动作训练-训练动作1的孩子节点1
        self.basic_trainingLeftAction4Child_1.setText(0, '手指内收外展')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.basic_trainingLeftAction4Child_1.setCheckState(0, Qt.Unchecked)
        # 添加子节点2
        self.basic_trainingLeftAction4Child_2 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_4)
        self.basic_trainingLeftAction4Child_2.setText(0, '四指单独屈伸')
        self.basic_trainingLeftAction4Child_2.setCheckState(0, Qt.Unchecked)
        self.basic_trainingLeftAction4Child_3 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_4)
        self.basic_trainingLeftAction4Child_3.setText(0, '四指屈曲')
        self.basic_trainingLeftAction4Child_3.setCheckState(0, Qt.Unchecked)
        self.basic_trainingLeftAction4Child_4 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_4)
        self.basic_trainingLeftAction4Child_4.setText(0, '四指伸展')
        self.basic_trainingLeftAction4Child_4.setCheckState(0, Qt.Unchecked)
        self.basic_trainingLeftAction4Child_5 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_4)
        self.basic_trainingLeftAction4Child_5.setText(0, '掌指关节屈曲')
        self.basic_trainingLeftAction4Child_5.setCheckState(0, Qt.Unchecked)
        self.basic_trainingLeftAction4Child_6 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_4)
        self.basic_trainingLeftAction4Child_6.setText(0, '指尖关节伸展')
        self.basic_trainingLeftAction4Child_6.setCheckState(0, Qt.Unchecked)

        self.basic_trainingLeftActionRoot_5 = QTreeWidgetItem(self.basic_leftTree)  # 基本动作训练-训练动作2根节点
        self.basic_trainingLeftActionRoot_5.setText(0, '腕部运动')  # 0代表第一列，即Key列
        self.basic_leftTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.basic_trainingLeftActionRoot_5.setCheckState(0, Qt.Unchecked)
        # 添加子节点1
        self.basic_trainingLeftAction5Child_1 = QTreeWidgetItem(
            self.basic_trainingLeftActionRoot_5)  # 基本动作训练-训练动作1的孩子节点1
        self.basic_trainingLeftAction5Child_1.setText(0, '尺偏')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.basic_trainingLeftAction5Child_1.setCheckState(0, Qt.Unchecked)
        # 添加子节点2
        self.basic_trainingLeftAction5Child_2 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_5)
        self.basic_trainingLeftAction5Child_2.setText(0, '桡偏')
        self.basic_trainingLeftAction5Child_2.setCheckState(0, Qt.Unchecked)
        self.basic_trainingLeftAction5Child_3 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_5)
        self.basic_trainingLeftAction5Child_3.setText(0, '前臂中立位腕背伸')
        self.basic_trainingLeftAction5Child_3.setCheckState(0, Qt.Unchecked)
        self.basic_trainingLeftAction5Child_4 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_5)
        self.basic_trainingLeftAction5Child_4.setText(0, '前臂旋前位腕背伸')
        self.basic_trainingLeftAction5Child_4.setCheckState(0, Qt.Unchecked)

        self.basic_trainingLeftActionRoot_6 = QTreeWidgetItem(self.basic_leftTree)  # 基本动作训练-训练动作2根节点
        self.basic_trainingLeftActionRoot_6.setText(0, '前臂旋转')  # 0代表第一列，即Key列
        self.basic_leftTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.basic_trainingLeftActionRoot_6.setCheckState(0, Qt.Unchecked)
        # 添加子节点1
        self.basic_trainingLeftAction6Child_1 = QTreeWidgetItem(
            self.basic_trainingLeftActionRoot_6)  # 基本动作训练-训练动作1的孩子节点1
        self.basic_trainingLeftAction6Child_1.setText(0, '前臂旋前')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.basic_trainingLeftAction6Child_1.setCheckState(0, Qt.Unchecked)
        # 添加子节点2
        self.basic_trainingLeftAction6Child_2 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_6)
        self.basic_trainingLeftAction6Child_2.setText(0, '前臂旋后')
        self.basic_trainingLeftAction6Child_2.setCheckState(0, Qt.Unchecked)
        self.basic_trainingLeftAction6Child_3 = QTreeWidgetItem(self.basic_trainingLeftActionRoot_6)
        self.basic_trainingLeftAction6Child_3.setText(0, '前臂旋前旋后')
        self.basic_trainingLeftAction6Child_3.setCheckState(0, Qt.Unchecked)

        self.basic_rightTree = QtWidgets.QTreeWidget(self.basic_scrollAreaWidgetContents)
        self.basic_rightTree.setGeometry(QtCore.QRect(0, 0, 700, 10000))
        self.basic_rightTree.setStyleSheet('font:14pt')
        self.basic_rightTree.setVisible(False)
        # 为树控件指定列数
        self.basic_rightTree.setColumnCount(1)
        # 指定列标签
        self.basic_rightTree.setHeaderLabels(['基本训练动作_右'])
        # 根节点
        self.basic_trainingrightActionRoot_1 = QTreeWidgetItem(self.basic_rightTree)  # 基本动作训练-训练动作1根节点
        self.basic_trainingrightActionRoot_1.setText(0, '拇指运动')  # 0代表第一列，即Key列
        self.basic_rightTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.basic_trainingrightActionRoot_1.setCheckState(0, Qt.Unchecked)

        # 添加子节点1
        self.basic_trainingrightAction1Child_1 = QTreeWidgetItem(
            self.basic_trainingrightActionRoot_1)  # 基本动作训练-训练动作1的孩子节点1
        self.basic_trainingrightAction1Child_1.setText(0, '拇指对食指')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.basic_trainingrightAction1Child_1.setCheckState(0, Qt.Unchecked)
        self.basic_trainingrightAction1Child_2 = QTreeWidgetItem(self.basic_trainingrightActionRoot_1)
        self.basic_trainingrightAction1Child_2.setText(0, '拇指对小指指根')
        self.basic_trainingrightAction1Child_2.setCheckState(0, Qt.Unchecked)
        self.basic_trainingrightAction1Child_3 = QTreeWidgetItem(self.basic_trainingrightActionRoot_1)
        self.basic_trainingrightAction1Child_3.setText(0, '拇指环转')
        self.basic_trainingrightAction1Child_3.setCheckState(0, Qt.Unchecked)
        self.basic_trainingrightAction1Child_4 = QTreeWidgetItem(self.basic_trainingrightActionRoot_1)
        self.basic_trainingrightAction1Child_4.setText(0, '拇指屈伸')
        self.basic_trainingrightAction1Child_4.setCheckState(0, Qt.Unchecked)
        self.basic_trainingrightAction1Child_5 = QTreeWidgetItem(self.basic_trainingrightActionRoot_1)
        self.basic_trainingrightAction1Child_5.setText(0, '拇指外展')
        self.basic_trainingrightAction1Child_5.setCheckState(0, Qt.Unchecked)
        self.basic_trainingrightAction1Child_6 = QTreeWidgetItem(self.basic_trainingrightActionRoot_1)
        self.basic_trainingrightAction1Child_6.setText(0, '拇指对四指')
        self.basic_trainingrightAction1Child_6.setCheckState(0, Qt.Unchecked)
        self.basic_trainingrightAction1Child_7 = QTreeWidgetItem(self.basic_trainingrightActionRoot_1)
        self.basic_trainingrightAction1Child_7.setText(0, '拇指对掌')
        self.basic_trainingrightAction1Child_7.setCheckState(0, Qt.Unchecked)
        self.basic_trainingrightAction1Child_8 = QTreeWidgetItem(self.basic_trainingrightActionRoot_1)
        self.basic_trainingrightAction1Child_8.setText(0, '拇指伸展')
        self.basic_trainingrightAction1Child_8.setCheckState(0, Qt.Unchecked)

        self.basic_trainingrightActionRoot_2 = QTreeWidgetItem(self.basic_rightTree)  # 基本动作训练-训练动作2根节点
        self.basic_trainingrightActionRoot_2.setText(0, '精细灵活性运动')  # 0代表第一列，即Key列
        self.basic_rightTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.basic_trainingrightActionRoot_2.setCheckState(0, Qt.Unchecked)
        # 添加子节点1
        self.basic_trainingrightAction2Child_1 = QTreeWidgetItem(
            self.basic_trainingrightActionRoot_2)  # 基本动作训练-训练动作1的孩子节点1
        self.basic_trainingrightAction2Child_1.setText(0, '比OK')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.basic_trainingrightAction2Child_1.setCheckState(0, Qt.Unchecked)
        # 添加子节点2
        self.basic_trainingrightAction2Child_2 = QTreeWidgetItem(self.basic_trainingrightActionRoot_2)
        self.basic_trainingrightAction2Child_2.setText(0, '比数字')
        self.basic_trainingrightAction2Child_2.setCheckState(0, Qt.Unchecked)
        self.basic_trainingrightAction2Child_3 = QTreeWidgetItem(self.basic_trainingrightActionRoot_2)
        self.basic_trainingrightAction2Child_3.setText(0, '侧捏')
        self.basic_trainingrightAction2Child_3.setCheckState(0, Qt.Unchecked)

        # 根节点
        self.basic_trainingrightActionRoot_3 = QTreeWidgetItem(self.basic_rightTree)  # 基本动作训练-训练动作2根节点
        self.basic_trainingrightActionRoot_3.setText(0, '抓握运动')  # 0代表第一列，即Key列
        self.basic_rightTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.basic_trainingrightActionRoot_3.setCheckState(0, Qt.Unchecked)
        # 添加子节点1
        self.basic_trainingrightAction3Child_1 = QTreeWidgetItem(
            self.basic_trainingrightActionRoot_3)  # 基本动作训练-训练动作1的孩子节点1
        self.basic_trainingrightAction3Child_1.setText(0, '钩状抓握')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.basic_trainingrightAction3Child_1.setCheckState(0, Qt.Unchecked)
        # 添加子节点2
        self.basic_trainingrightAction3Child_2 = QTreeWidgetItem(self.basic_trainingrightActionRoot_3)
        self.basic_trainingrightAction3Child_2.setText(0, '球状抓握')
        self.basic_trainingrightAction3Child_2.setCheckState(0, Qt.Unchecked)
        self.basic_trainingrightAction3Child_3 = QTreeWidgetItem(self.basic_trainingrightActionRoot_3)
        self.basic_trainingrightAction3Child_3.setText(0, '握拳')
        self.basic_trainingrightAction3Child_3.setCheckState(0, Qt.Unchecked)
        self.basic_trainingrightAction3Child_4 = QTreeWidgetItem(self.basic_trainingrightActionRoot_3)
        self.basic_trainingrightAction3Child_4.setText(0, '直拳')
        self.basic_trainingrightAction3Child_4.setCheckState(0, Qt.Unchecked)
        self.basic_trainingrightAction3Child_5 = QTreeWidgetItem(self.basic_trainingrightActionRoot_3)
        self.basic_trainingrightAction3Child_5.setText(0, '柱状抓握')
        self.basic_trainingrightAction3Child_5.setCheckState(0, Qt.Unchecked)

        self.basic_trainingrightActionRoot_4 = QTreeWidgetItem(self.basic_rightTree)  # 基本动作训练-训练动作2根节点
        self.basic_trainingrightActionRoot_4.setText(0, '手指动作')  # 0代表第一列，即Key列
        self.basic_leftTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.basic_trainingrightActionRoot_4.setCheckState(0, Qt.Unchecked)
        # 添加子节点1
        self.basic_trainingrightAction4Child_1 = QTreeWidgetItem(
            self.basic_trainingrightActionRoot_4)  # 基本动作训练-训练动作1的孩子节点1
        self.basic_trainingrightAction4Child_1.setText(0, '手指内收外展')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.basic_trainingrightAction4Child_1.setCheckState(0, Qt.Unchecked)
        # 添加子节点2
        self.basic_trainingrightAction4Child_2 = QTreeWidgetItem(self.basic_trainingrightActionRoot_4)
        self.basic_trainingrightAction4Child_2.setText(0, '四指单独屈伸')
        self.basic_trainingrightAction4Child_2.setCheckState(0, Qt.Unchecked)
        self.basic_trainingrightAction4Child_3 = QTreeWidgetItem(self.basic_trainingrightActionRoot_4)
        self.basic_trainingrightAction4Child_3.setText(0, '四指屈曲')
        self.basic_trainingrightAction4Child_3.setCheckState(0, Qt.Unchecked)
        self.basic_trainingrightAction4Child_4 = QTreeWidgetItem(self.basic_trainingrightActionRoot_4)
        self.basic_trainingrightAction4Child_4.setText(0, '四指伸展')
        self.basic_trainingrightAction4Child_4.setCheckState(0, Qt.Unchecked)
        self.basic_trainingrightAction4Child_5 = QTreeWidgetItem(self.basic_trainingrightActionRoot_4)
        self.basic_trainingrightAction4Child_5.setText(0, '掌指关节屈曲')
        self.basic_trainingrightAction4Child_5.setCheckState(0, Qt.Unchecked)
        self.basic_trainingrightAction4Child_6 = QTreeWidgetItem(self.basic_trainingrightActionRoot_4)
        self.basic_trainingrightAction4Child_6.setText(0, '指尖关节伸展')
        self.basic_trainingrightAction4Child_6.setCheckState(0, Qt.Unchecked)

        self.basic_trainingrightActionRoot_5 = QTreeWidgetItem(self.basic_rightTree)  # 基本动作训练-训练动作2根节点
        self.basic_trainingrightActionRoot_5.setText(0, '腕部运动')  # 0代表第一列，即Key列
        self.basic_leftTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.basic_trainingrightActionRoot_5.setCheckState(0, Qt.Unchecked)
        # 添加子节点1
        self.basic_trainingrightAction5Child_1 = QTreeWidgetItem(
            self.basic_trainingLeftActionRoot_5)  # 基本动作训练-训练动作1的孩子节点1
        self.basic_trainingrightAction5Child_1.setText(0, '尺偏')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.basic_trainingrightAction5Child_1.setCheckState(0, Qt.Unchecked)
        # 添加子节点2
        self.basic_trainingrightAction5Child_2 = QTreeWidgetItem(self.basic_trainingrightActionRoot_5)
        self.basic_trainingrightAction5Child_2.setText(0, '桡偏')
        self.basic_trainingrightAction5Child_2.setCheckState(0, Qt.Unchecked)
        self.basic_trainingrightAction5Child_3 = QTreeWidgetItem(self.basic_trainingrightActionRoot_5)
        self.basic_trainingrightAction5Child_3.setText(0, '前臂中立位腕背伸')
        self.basic_trainingrightAction5Child_3.setCheckState(0, Qt.Unchecked)
        self.basic_trainingrightAction5Child_4 = QTreeWidgetItem(self.basic_trainingrightActionRoot_5)
        self.basic_trainingrightAction5Child_4.setText(0, '前臂旋前位腕背伸')
        self.basic_trainingrightAction5Child_4.setCheckState(0, Qt.Unchecked)

        self.basic_trainingrightActionRoot_6 = QTreeWidgetItem(self.basic_rightTree)  # 基本动作训练-训练动作2根节点
        self.basic_trainingrightActionRoot_6.setText(0, '前臂旋转')  # 0代表第一列，即Key列
        self.basic_rightTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.basic_trainingrightActionRoot_6.setCheckState(0, Qt.Unchecked)
        # 添加子节点1
        self.basic_trainingrightAction6Child_1 = QTreeWidgetItem(
            self.basic_trainingrightActionRoot_6)  # 基本动作训练-训练动作1的孩子节点1
        self.basic_trainingrightAction6Child_1.setText(0, '前臂旋前')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.basic_trainingrightAction6Child_1.setCheckState(0, Qt.Unchecked)
        # 添加子节点2
        self.basic_trainingrightAction6Child_2 = QTreeWidgetItem(self.basic_trainingrightActionRoot_6)
        self.basic_trainingrightAction6Child_2.setText(0, '前臂旋后')
        self.basic_trainingrightAction6Child_2.setCheckState(0, Qt.Unchecked)
        self.basic_trainingrightAction6Child_3 = QTreeWidgetItem(self.basic_trainingrightActionRoot_6)
        self.basic_trainingrightAction6Child_3.setText(0, '前臂旋前旋后')
        self.basic_trainingrightAction6Child_3.setCheckState(0, Qt.Unchecked)

        self.basic_leftCameraLabel = QtWidgets.QLabel(self.page_2)  # 基本动作训练-左边摄像显示界面
        self.basic_leftCameraLabel.setGeometry(QtCore.QRect(740, 80, 550, 520))
        self.basic_leftCameraLabel.setStyleSheet("border-width: 1px;border-style: solid;border-color:black")
        self.basic_leftCameraLabel.setPixmap(QPixmap("./src/fig/empty_camera.png"))

        self.basic_rightCameraLabel = QtWidgets.QLabel(self.page_2)  # 基本动作训练-右边摄像显示界面
        self.basic_rightCameraLabel.setGeometry(QtCore.QRect(1340, 80, 550, 520))
        self.basic_rightCameraLabel.setStyleSheet("border-width: 1px;border-style: solid;border-color:black")
        self.basic_rightCameraLabel.setPixmap(QPixmap("./src/fig/empty_camera.png"))

        self.label_119 = QtWidgets.QLabel(self.page_2)
        self.label_119.setGeometry(QtCore.QRect(745, 30, 120, 40))
        self.label_119.setText("左手")
        self.label_119.setStyleSheet("font:14pt;color:#1E90FF")

        self.basic_leftIsPlaying = True
        self.basic_leftMirrrorButton = QtWidgets.QPushButton(self.page_2)  # 基本动作训练-左手镜像
        self.basic_leftMirrrorButton.setGeometry(QtCore.QRect(820, 35, 100, 40))
        self.basic_leftMirrrorButton.setStyleSheet("font:12pt")

        self.basic_leftCopyButton = QtWidgets.QPushButton(self.page_2)  # 基本动作训练-左手复制
        self.basic_leftCopyButton.setGeometry(QtCore.QRect(960, 35, 100, 40))
        self.basic_leftCopyButton.setStyleSheet("font:12pt")

        self.basic_leftMaskButton = QtWidgets.QPushButton(self.page_2)  # 基本动作训练-左手遮罩
        self.basic_leftMaskButton.setGeometry(QtCore.QRect(1100, 35, 100, 40))
        self.basic_leftMaskButton.setStyleSheet("font:12pt")

        self.basic_leftPlayButton = QtWidgets.QPushButton(self.page_2)  # 基本动作训练-左手播放
        self.basic_leftPlayButton.setGeometry(QtCore.QRect(745, 620, 120, 40))
        self.basic_leftPlayButton.setStyleSheet("font:12pt")

        self.basic_leftStopButton = QtWidgets.QPushButton(self.page_2)  # 基本动作训练-左手重新开始
        self.basic_leftStopButton.setGeometry(QtCore.QRect(905, 620, 120, 40))
        self.basic_leftStopButton.setStyleSheet("font:12pt")

        self.basic_LeftRecoderButton = QtWidgets.QToolButton(self.page_2)  # 基本动作训练-左手录制
        self.basic_LeftRecoderButton.setGeometry(QtCore.QRect(1065, 620, 120, 40))
        self.basic_LeftRecoderButton.setStyleSheet("font:12pt")

        self.basic_leftScreenRecording = QAction(self.page_2)  # 基本动作训练-左手录屏
        self.basic_leftScreenRecording.setText('录屏')

        self.basic_leftPopup_menu = QMenu(self.page_2)
        self.basic_leftPopup_menu.addAction(self.basic_leftScreenRecording)

        self.basic_LeftRecoderButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.basic_LeftRecoderButton.setAutoRaise(True)
        self.basic_LeftRecoderButton.setMenu(self.basic_leftPopup_menu)

        self.label_120 = QtWidgets.QLabel(self.page_2)
        self.label_120.setGeometry(QtCore.QRect(1350, 30, 120, 40))
        self.label_120.setText("右手")
        self.label_120.setStyleSheet("font:14pt;color:#1E90FF")

        self.basic_rightMirrrorButton = QtWidgets.QPushButton(self.page_2)  # 基本动作训练-右手镜像
        self.basic_rightMirrrorButton.setGeometry(QtCore.QRect(1420, 35, 100, 40))
        self.basic_rightMirrrorButton.setStyleSheet("font:12pt")

        self.basic_rightCopyButton = QtWidgets.QPushButton(self.page_2)  # 基本动作训练-右手复制
        self.basic_rightCopyButton.setGeometry(QtCore.QRect(1560, 35, 100, 40))
        self.basic_rightCopyButton.setStyleSheet("font:12pt")

        self.basic_rightMaskButton = QtWidgets.QPushButton(self.page_2)  # 基本动作训练-右手遮罩
        self.basic_rightMaskButton.setGeometry(QtCore.QRect(1700, 35, 100, 40))
        self.basic_rightMaskButton.setStyleSheet("font:12pt")

        self.basic_rightIsPlaying = True
        self.basic_rightPlayButton = QtWidgets.QPushButton(self.page_2)  # 基本动作训练-右手播放
        self.basic_rightPlayButton.setGeometry(QtCore.QRect(1350, 620, 120, 40))
        self.basic_rightPlayButton.setStyleSheet("font:12pt")

        self.basic_rightStopButton = QtWidgets.QPushButton(self.page_2)  # 基本动作训练-右手重新开始
        self.basic_rightStopButton.setGeometry(QtCore.QRect(1510, 620, 120, 40))
        self.basic_rightStopButton.setStyleSheet("font:12pt")

        self.basic_rightRecoderButton = QtWidgets.QToolButton(self.page_2)  # 基本动作训练-右手录制
        self.basic_rightRecoderButton.setGeometry(QtCore.QRect(1670, 620, 120, 40))
        self.basic_rightRecoderButton.setStyleSheet("font:12pt")

        self.basic_rightScreenRecording = QAction(self.page_2)  # 基本动作训练-右手录屏
        self.basic_rightScreenRecording.setText('录屏')

        self.basic_rightPopup_menu = QMenu(self.page_2)
        self.basic_rightPopup_menu.addAction(self.basic_rightScreenRecording)

        self.basic_rightRecoderButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.basic_rightRecoderButton.setAutoRaise(True)
        self.basic_rightRecoderButton.setMenu(self.basic_rightPopup_menu)

        self.basic_cancelButton = QtWidgets.QPushButton(self.page_2)  # 基本动作训练-全部取消
        self.basic_cancelButton.setGeometry(QtCore.QRect(10, 620, 120, 40))
        self.basic_cancelButton.setStyleSheet("font:12pt")

        self.basic_selectAllButton = QtWidgets.QPushButton(self.page_2)  # 基本动作训练-全部选择
        self.basic_selectAllButton.setGeometry(QtCore.QRect(140, 620, 120, 40))
        self.basic_selectAllButton.setStyleSheet("font:12pt")

        self.label_24 = QtWidgets.QLabel(self.page_2)  # 组数
        self.label_24.setGeometry(QtCore.QRect(270, 620, 120, 40))
        self.label_24.setStyleSheet("font:12pt")

        self.basic_trainingGroupNumLineEdit = QtWidgets.QLineEdit(self.page_2)  # 基本动作训练-获取训练组数
        self.basic_trainingGroupNumLineEdit.setGeometry(QtCore.QRect(330, 620, 120, 40))
        self.basic_trainingGroupNumLineEdit.setStyleSheet("font:12pt")

        self.label_25 = QtWidgets.QLabel(self.page_2)  # 训练方式
        self.label_25.setGeometry(QtCore.QRect(470, 620, 120, 40))
        self.label_25.setStyleSheet("font:12pt")

        self.basic_trainingWayComboBox = QtWidgets.QComboBox(self.page_2)  # 基本动作训练-获取训练方式
        self.basic_trainingWayComboBox.setGeometry(QtCore.QRect(540, 620, 120, 40))
        self.basic_trainingWayComboBox.addItems(['', 'AABB', 'ABAB'])
        self.basic_trainingWayComboBox.setStyleSheet("font:12pt")

        self.label_26 = QtWidgets.QLabel(self.page_2)  # 训练次数
        self.label_26.setGeometry(QtCore.QRect(10, 680, 120, 40))
        self.label_26.setStyleSheet("font:12pt")

        self.basic_trainingNumLineEdit = QtWidgets.QLineEdit(self.page_2)  # 基本动作训练-获取每组训练次数
        self.basic_trainingNumLineEdit.setGeometry(QtCore.QRect(120, 680, 120, 40))
        self.basic_trainingNumLineEdit.setStyleSheet("font:12pt")

        self.label_27 = QtWidgets.QLabel(self.page_2)  # 播放次数
        self.label_27.setGeometry(QtCore.QRect(250, 680, 120, 40))
        self.label_27.setStyleSheet("font:12pt")

        self.basic_playNumLineEdit = QtWidgets.QLineEdit(self.page_2)  # 基本动作训练-获取每组视频播放次数
        self.basic_playNumLineEdit.setGeometry(QtCore.QRect(360, 680, 120, 40))
        self.basic_playNumLineEdit.setStyleSheet("font:12pt")

        self.label_54 = QtWidgets.QLabel(self.page_2)  # 播放速率
        self.label_54.setGeometry(QtCore.QRect(500, 680, 120, 40))
        self.label_54.setText('播放速率')
        self.label_54.setStyleSheet("font:12pt")

        self.basic_playSpeedComBox = QtWidgets.QComboBox(self.page_2)  # 基本动作训练-获取视频播放速率
        self.basic_playSpeedComBox.setGeometry(QtCore.QRect(600, 680, 120, 40))
        self.basic_playSpeedComBox.addItems(['', '0.5', '1', '1.25', '1.5', '2'])
        self.basic_playSpeedComBox.setStyleSheet("font:12pt")

        self.basic_recommendButton = QtWidgets.QPushButton(self.page_2)  # 基本动作训练-获取该病人预先设置好的训练方案
        self.basic_recommendButton.setGeometry(QtCore.QRect(10, 730, 120, 40))
        self.basic_recommendButton.setStyleSheet("font:12pt")

        self.basic_isPlaying = True

        self.basic_startButton = QtWidgets.QPushButton(self.page_2)  # 基本动作训练-开始训练
        self.basic_startButton.setGeometry(QtCore.QRect(140, 730, 120, 40))
        self.basic_startButton.setStyleSheet("font:12pt")

        self.label_52 = QtWidgets.QLabel(self.page_2)
        self.label_52.setGeometry(QtCore.QRect(400, 730, 120, 40))
        self.label_52.setText("训练时长:")
        self.label_52.setStyleSheet("font:12pt")

        self.basic_timeEdit = QTimeEdit(self.page_2)  # 基本动作训练-时间计时器
        self.basic_timeEdit.setDisplayFormat('HH:mm:ss')
        self.basic_timeEdit.setGeometry(QtCore.QRect(520, 730, 120, 40))

        self.basic_traingSituationFrame = QtWidgets.QFrame(self.page_2)  # 基本动作训练情况显示窗口
        self.basic_traingSituationFrame.setGeometry(QtCore.QRect(10, 10, 700, 710))
        self.basic_traingSituationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.basic_traingSituationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.basic_traingSituationFrame.setVisible(False)

        self.label_61 = QtWidgets.QLabel(self.basic_traingSituationFrame)  # 训练情况
        self.label_61.setGeometry(QtCore.QRect(20, 10, 120, 40))
        self.label_61.setStyleSheet("font:14pt;color:#1E90FF")

        self.label_62 = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.label_62.setGeometry(QtCore.QRect(20, 60, 200, 40))
        self.label_62.setStyleSheet("font:10pt")

        self.basic_trainingModeLabel = QtWidgets.QLabel(self.basic_traingSituationFrame)  # 基本动作训练训练情况-获取训练模式
        self.basic_trainingModeLabel.setGeometry(QtCore.QRect(140, 60, 200, 40))
        self.basic_trainingModeLabel.setStyleSheet("font:10pt")

        self.label_63 = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.label_63.setGeometry(QtCore.QRect(200, 60, 220, 40))
        self.label_63.setStyleSheet("font:10pt")

        self.basic_trianingGroupsLabel = QtWidgets.QLabel(self.basic_traingSituationFrame)  # 基本动作训练训练情况-获取训练组数
        self.basic_trianingGroupsLabel.setGeometry(QtCore.QRect(330, 60, 220, 40))
        self.basic_trianingGroupsLabel.setStyleSheet("font:10pt")

        self.label_65 = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.label_65.setGeometry(QtCore.QRect(360, 60, 220, 40))
        self.label_65.setStyleSheet("font:10pt")

        self.basic_triangNumLabel = QtWidgets.QLabel(self.basic_traingSituationFrame)  # 基本动作训练训练情况-获取训练动作个数
        self.basic_triangNumLabel.setGeometry(QtCore.QRect(470, 60, 220, 40))
        self.basic_triangNumLabel.setStyleSheet("font:10pt")

        self.label_66 = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.label_66.setGeometry(QtCore.QRect(500, 60, 220, 40))
        self.label_66.setStyleSheet("font:10pt")

        self.label_121 = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.label_121.setGeometry(QtCore.QRect(40, 100, 220, 40))
        self.label_121.setText("总共(组):")
        self.label_121.setStyleSheet("font:10pt")

        self.basic_trainingTotalNumLabel = QtWidgets.QLabel(self.basic_traingSituationFrame)  # 基本动作训练训练情况-获取训练动作组数
        self.basic_trainingTotalNumLabel.setGeometry(QtCore.QRect(150, 100, 220, 40))
        self.basic_trainingTotalNumLabel.setText("--")
        self.basic_trainingTotalNumLabel.setStyleSheet("font:10pt")

        self.label_122 = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.label_122.setGeometry(QtCore.QRect(200, 100, 220, 40))
        self.label_122.setText("当前(组):")
        self.label_122.setStyleSheet("font:10pt")

        self.basic_trainingCurrentNumLabel = QtWidgets.QLabel(self.basic_traingSituationFrame)  # 基本动作训练训练情况-获取当前训练动作组数
        self.basic_trainingCurrentNumLabel.setGeometry(QtCore.QRect(300, 100, 220, 40))
        self.basic_trainingCurrentNumLabel.setText("--")
        self.basic_trainingCurrentNumLabel.setStyleSheet("font:10pt")

        self.label_123 = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.label_123.setGeometry(QtCore.QRect(350, 100, 220, 40))
        self.label_123.setText("剩余(组):")
        self.label_123.setStyleSheet("font:10pt")

        self.basic_trainingRemainNumLabel = QtWidgets.QLabel(self.basic_traingSituationFrame)  # 基本动作训练训练情况-获取剩余训练动作组数
        self.basic_trainingRemainNumLabel.setGeometry(QtCore.QRect(450, 100, 220, 40))
        self.basic_trainingRemainNumLabel.setText("--")
        self.basic_trainingRemainNumLabel.setStyleSheet("font:10pt")

        self.label_64 = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.label_64.setGeometry(QtCore.QRect(20, 140, 250, 40))
        self.label_64.setStyleSheet("font:10pt")

        self.basic_trainingNameLabel = QtWidgets.QLabel(self.basic_traingSituationFrame)  # 基本动作训练训练情况-获取训练动作名称
        self.basic_trainingNameLabel.setGeometry(QtCore.QRect(210, 140, 500, 40))
        self.basic_trainingNameLabel.setStyleSheet("font:10pt")

        self.label_67 = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.label_67.setGeometry(QtCore.QRect(20, 180, 200, 40))
        self.label_67.setStyleSheet("font:10pt")

        self.label_68 = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.label_68.setGeometry(QtCore.QRect(40, 220, 200, 40))
        self.label_68.setStyleSheet("font:10pt")

        # 基本动作训练情况-获取跟视频训练总次数
        self.basic_trianingTotalNumPlayVideoLabel = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.basic_trianingTotalNumPlayVideoLabel.setGeometry(QtCore.QRect(160, 220, 200, 40))
        self.basic_trianingTotalNumPlayVideoLabel.setStyleSheet("font:10pt")

        self.label_69 = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.label_69.setGeometry(QtCore.QRect(200, 220, 200, 40))
        self.label_69.setStyleSheet("font:10pt")

        # 基本动作训练情况-获取跟视频训练当前次数
        self.basic_currentPlayVideoLabel = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.basic_currentPlayVideoLabel.setGeometry(QtCore.QRect(320, 220, 200, 40))
        self.basic_currentPlayVideoLabel.setStyleSheet("font:10pt")

        self.label_70 = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.label_70.setGeometry(QtCore.QRect(370, 220, 200, 40))
        self.label_70.setStyleSheet("font:10pt")

        # 基本动作训练情况-获取跟视频训练剩余次数
        self.basic_remainingPlayVideoLabel = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.basic_remainingPlayVideoLabel.setGeometry(QtCore.QRect(480, 220, 200, 40))
        self.basic_remainingPlayVideoLabel.setStyleSheet("font:10pt")

        self.label_71 = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.label_71.setGeometry(QtCore.QRect(20, 260, 200, 40))
        self.label_71.setStyleSheet("font:10pt")

        self.label_72 = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.label_72.setGeometry(QtCore.QRect(40, 300, 200, 40))
        self.label_72.setStyleSheet("font:10pt")

        # 基本动作训练情况-获取自行训练总次数
        self.basic_autonomousTrianingTotalNumLabel = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.basic_autonomousTrianingTotalNumLabel.setGeometry(QtCore.QRect(160, 300, 200, 40))
        self.basic_autonomousTrianingTotalNumLabel.setStyleSheet("font:10pt")

        self.label_73 = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.label_73.setGeometry(QtCore.QRect(200, 300, 200, 40))
        self.label_73.setStyleSheet("font:10pt")

        # 基本动作训练情况-获取自行训练当前次数
        self.basic_autonomousCurrentLabel = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.basic_autonomousCurrentLabel.setGeometry(QtCore.QRect(320, 300, 200, 40))
        self.basic_autonomousCurrentLabel.setStyleSheet("font:10pt")

        self.label_74 = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.label_74.setGeometry(QtCore.QRect(370, 300, 200, 40))
        self.label_74.setStyleSheet("font:10pt")

        # 基本动作训练情况-获取自行训练剩余次数
        self.basic_autonomousRemainingLabel = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.basic_autonomousRemainingLabel.setGeometry(QtCore.QRect(480, 300, 200, 40))
        self.basic_autonomousRemainingLabel.setStyleSheet("font:10pt")

        # 基本动作训练情况-显示当前播放的视频
        self.basic_showVideoLabel = QtWidgets.QLabel(self.basic_traingSituationFrame)
        self.basic_showVideoLabel.setGeometry(QtCore.QRect(10, 340, 680, 350))
        self.basic_showVideoLabel.setStyleSheet("border-width: 1px;border-style: solid;border-color:black")

        self.basic_historyRecordButton = QtWidgets.QPushButton(self.page_2)  # 基本动作训练——显示视频历史记录
        self.basic_historyRecordButton.setGeometry(QtCore.QRect(270, 730, 120, 40))
        self.basic_historyRecordButton.setText('历史记录')
        self.basic_historyRecordButton.setStyleSheet("font:12pt")

        self.page_3 = QtWidgets.QWidget()

        self.function_selectTrainingFrame = QtWidgets.QFrame(self.page_3)  # 功能动作训练容器
        self.function_selectTrainingFrame.setGeometry(QtCore.QRect(10, 10, 700, 600))
        self.function_selectTrainingFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.function_selectTrainingFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.function_scrollArea = QtWidgets.QScrollArea(self.function_selectTrainingFrame)  # 功能动作训练滑动窗口
        self.function_scrollArea.setGeometry(QtCore.QRect(0, 0, 700, 600))
        self.function_scrollArea.setWidgetResizable(True)

        self.function_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.function_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 700, 600))
        self.function_scrollAreaWidgetContents.setMinimumHeight(3000)
        self.function_scrollArea.setWidget(self.function_scrollAreaWidgetContents)

        self.function_leftTree = QtWidgets.QTreeWidget(self.function_scrollAreaWidgetContents)
        self.function_leftTree.setGeometry(QtCore.QRect(0, 0, 700, 10000))
        self.function_leftTree.setStyleSheet('font:14pt')
        # 为树控件指定列数
        self.function_leftTree.setColumnCount(1)
        # 指定列标签
        self.function_leftTree.setHeaderLabels(['功能训练动作_左'])
        # 根节点
        self.function_trainingLeftActionRoot_1 = QTreeWidgetItem(self.function_leftTree)  # 功能动作训练-训练动作1根节点
        self.function_trainingLeftActionRoot_1.setText(0, '精细动作')  # 0代表第一列，即Key列
        self.function_leftTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.function_trainingLeftActionRoot_1.setCheckState(0, Qt.Unchecked)
        # 添加子节点1
        self.function_trainingLeftAction1Child_1 = QTreeWidgetItem(
            self.function_trainingLeftActionRoot_1)  # 功能动作训练-训练动作1的孩子节点1
        self.function_trainingLeftAction1Child_1.setText(0, '侧捏夹子')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.function_trainingLeftAction1Child_1.setCheckState(0, Qt.Unchecked)
        # 功能动作训练-训练动作1的孩子节点2
        self.function_trainingLeftAction1Child_2 = QTreeWidgetItem(self.function_trainingLeftActionRoot_1)
        self.function_trainingLeftAction1Child_2.setText(0, '对指翻书页')
        self.function_trainingLeftAction1Child_2.setCheckState(0, Qt.Unchecked)
        self.function_trainingLeftAction1Child_3 = QTreeWidgetItem(self.function_trainingLeftActionRoot_1)
        self.function_trainingLeftAction1Child_3.setText(0, '对指捏夹子')
        self.function_trainingLeftAction1Child_3.setCheckState(0, Qt.Unchecked)
        self.function_trainingLeftAction1Child_4 = QTreeWidgetItem(self.function_trainingLeftActionRoot_1)
        self.function_trainingLeftAction1Child_4.setText(0, '拿玻璃球')
        self.function_trainingLeftAction1Child_4.setCheckState(0, Qt.Unchecked)
        self.function_trainingLeftAction1Child_5 = QTreeWidgetItem(self.function_trainingLeftActionRoot_1)
        self.function_trainingLeftAction1Child_5.setText(0, '拿回形针')
        self.function_trainingLeftAction1Child_5.setCheckState(0, Qt.Unchecked)
        self.function_trainingLeftAction1Child_6 = QTreeWidgetItem(self.function_trainingLeftActionRoot_1)
        self.function_trainingLeftAction1Child_6.setText(0, '拿木块两指捏')
        self.function_trainingLeftAction1Child_6.setCheckState(0, Qt.Unchecked)
        self.function_trainingLeftAction1Child_7 = QTreeWidgetItem(self.function_trainingLeftActionRoot_1)
        self.function_trainingLeftAction1Child_7.setText(0, '拿木块三指捏')
        self.function_trainingLeftAction1Child_7.setCheckState(0, Qt.Unchecked)
        self.function_trainingLeftAction1Child_8 = QTreeWidgetItem(self.function_trainingLeftActionRoot_1)
        self.function_trainingLeftAction1Child_8.setText(0, '拿小木块两指捏')
        self.function_trainingLeftAction1Child_8.setCheckState(0, Qt.Unchecked)
        self.function_trainingLeftAction1Child_9 = QTreeWidgetItem(self.function_trainingLeftActionRoot_1)
        self.function_trainingLeftAction1Child_9.setText(0, '拿小木块三指捏')
        self.function_trainingLeftAction1Child_9.setCheckState(0, Qt.Unchecked)
        self.function_trainingLeftAction1Child_10 = QTreeWidgetItem(self.function_trainingLeftActionRoot_1)
        self.function_trainingLeftAction1Child_10.setText(0, '拿钥匙')
        self.function_trainingLeftAction1Child_10.setCheckState(0, Qt.Unchecked)

        # 根节点
        self.function_trainingLeftActionRoot_2 = QTreeWidgetItem(self.function_leftTree)  # 功能动作训练-训练动作2根节点
        self.function_trainingLeftActionRoot_2.setText(0, '复合旋转运动')  # 0代表第一列，即Key列
        self.function_leftTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.function_trainingLeftActionRoot_2.setCheckState(0, Qt.Unchecked)

        # 添加子节点1
        self.function_trainingLeftAction2Child_1 = QTreeWidgetItem(
            self.function_trainingLeftActionRoot_2)  # 功能动作训练-训练动作2的孩子节点1
        self.function_trainingLeftAction2Child_1.setText(0, '翻卡片')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.function_trainingLeftAction2Child_1.setCheckState(0, Qt.Unchecked)
        # 功能动作训练-训练动作2的孩子节点2
        self.function_trainingLeftAction2Child_2 = QTreeWidgetItem(self.function_trainingLeftActionRoot_2)
        self.function_trainingLeftAction2Child_2.setText(0, '翻木板')
        self.function_trainingLeftAction2Child_2.setCheckState(0, Qt.Unchecked)
        self.function_trainingLeftAction2Child_3 = QTreeWidgetItem(self.function_trainingLeftActionRoot_2)
        self.function_trainingLeftAction2Child_3.setText(0, '翻日历')
        self.function_trainingLeftAction2Child_3.setCheckState(0, Qt.Unchecked)
        self.function_trainingLeftAction2Child_4 = QTreeWidgetItem(self.function_trainingLeftActionRoot_2)
        self.function_trainingLeftAction2Child_4.setText(0, '翻书页')
        self.function_trainingLeftAction2Child_4.setCheckState(0, Qt.Unchecked)
        self.function_trainingLeftAction2Child_5 = QTreeWidgetItem(self.function_trainingLeftActionRoot_2)
        self.function_trainingLeftAction2Child_5.setText(0, '前臂旋前套杯子')
        self.function_trainingLeftAction2Child_5.setCheckState(0, Qt.Unchecked)
        self.function_trainingLeftAction2Child_6 = QTreeWidgetItem(self.function_trainingLeftActionRoot_2)
        self.function_trainingLeftAction2Child_6.setText(0, '套杯子')
        self.function_trainingLeftAction2Child_6.setCheckState(0, Qt.Unchecked)

        self.function_trainingLeftActionRoot_3 = QTreeWidgetItem(self.function_leftTree)  # 功能动作训练-训练动作2根节点
        self.function_trainingLeftActionRoot_3.setText(0, '抓握运动')  # 0代表第一列，即Key列
        self.function_leftTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.function_trainingLeftActionRoot_3.setCheckState(0, Qt.Unchecked)

        # 添加子节点1
        self.function_trainingLeftAction3Child_1 = QTreeWidgetItem(
            self.function_trainingLeftActionRoot_3)  # 功能动作训练-训练动作2的孩子节点1
        self.function_trainingLeftAction3Child_1.setText(0, '木棒抓握')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.function_trainingLeftAction3Child_1.setCheckState(0, Qt.Unchecked)
        # 功能动作训练-训练动作2的孩子节点2
        self.function_trainingLeftAction3Child_2 = QTreeWidgetItem(self.function_trainingLeftActionRoot_3)
        self.function_trainingLeftAction3Child_2.setText(0, '拿玻璃杯')
        self.function_trainingLeftAction3Child_2.setCheckState(0, Qt.Unchecked)
        self.function_trainingLeftAction3Child_3 = QTreeWidgetItem(self.function_trainingLeftActionRoot_3)
        self.function_trainingLeftAction3Child_3.setText(0, '拿矿泉水瓶')
        self.function_trainingLeftAction3Child_3.setCheckState(0, Qt.Unchecked)
        self.function_trainingLeftAction3Child_4 = QTreeWidgetItem(self.function_trainingLeftActionRoot_3)
        self.function_trainingLeftAction3Child_4.setText(0, '捏弹力球')
        self.function_trainingLeftAction3Child_4.setCheckState(0, Qt.Unchecked)

        self.function_trainingLeftActionRoot_4 = QTreeWidgetItem(self.function_leftTree)  # 功能动作训练-训练动作2根节点
        self.function_trainingLeftActionRoot_4.setText(0, 'ADL活动')  # 0代表第一列，即Key列
        self.function_leftTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.function_trainingLeftActionRoot_4.setCheckState(0, Qt.Unchecked)

        # 添加子节点1
        self.function_trainingLeftAction4Child_1 = QTreeWidgetItem(
            self.function_trainingLeftActionRoot_4)  # 功能动作训练-训练动作2的孩子节点1
        self.function_trainingLeftAction4Child_1.setText(0, '写字')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.function_trainingLeftAction4Child_1.setCheckState(0, Qt.Unchecked)
        # 功能动作训练-训练动作2的孩子节点2
        self.function_trainingLeftAction4Child_2 = QTreeWidgetItem(self.function_trainingLeftActionRoot_4)
        self.function_trainingLeftAction4Child_2.setText(0, '旋转铅笔')
        self.function_trainingLeftAction4Child_2.setCheckState(0, Qt.Unchecked)
        self.function_trainingLeftAction4Child_3 = QTreeWidgetItem(self.function_trainingLeftActionRoot_4)
        self.function_trainingLeftAction4Child_3.setText(0, '旋转钥匙')
        self.function_trainingLeftAction4Child_3.setCheckState(0, Qt.Unchecked)
        self.function_trainingLeftAction4Child_4 = QTreeWidgetItem(self.function_trainingLeftActionRoot_4)
        self.function_trainingLeftAction4Child_4.setText(0, '用勺子舀珠子')
        self.function_trainingLeftAction4Child_4.setCheckState(0, Qt.Unchecked)
        self.function_trainingLeftAction4Child_5 = QTreeWidgetItem(self.function_trainingLeftActionRoot_4)
        self.function_trainingLeftAction4Child_5.setText(0, '抓放网球')
        self.function_trainingLeftAction4Child_5.setCheckState(0, Qt.Unchecked)

        self.function_trainingLeftActionRoot_5 = QTreeWidgetItem(self.function_leftTree)  # 功能动作训练-训练动作2根节点
        self.function_trainingLeftActionRoot_5.setText(0, '双手联合运动')  # 0代表第一列，即Key列
        self.function_leftTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.function_trainingLeftActionRoot_5.setCheckState(0, Qt.Unchecked)

        # 添加子节点1
        self.function_trainingLeftAction5Child_1 = QTreeWidgetItem(
            self.function_trainingLeftActionRoot_5)  # 功能动作训练-训练动作2的孩子节点1
        self.function_trainingLeftAction5Child_1.setText(0, '双手滚训练棒')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.function_trainingLeftAction5Child_1.setCheckState(0, Qt.Unchecked)
        # 功能动作训练-训练动作2的孩子节点2
        self.function_trainingLeftAction5Child_2 = QTreeWidgetItem(self.function_trainingLeftActionRoot_5)
        self.function_trainingLeftAction5Child_2.setText(0, '双手用力弯曲训练棒')
        self.function_trainingLeftAction5Child_2.setCheckState(0, Qt.Unchecked)

        self.function_rightTree = QtWidgets.QTreeWidget(self.function_scrollAreaWidgetContents)
        self.function_rightTree.setGeometry(QtCore.QRect(0, 0, 700, 10000))
        self.function_rightTree.setStyleSheet('font:14pt')
        # 为树控件指定列数
        self.function_rightTree.setColumnCount(1)
        # 指定列标签
        self.function_rightTree.setHeaderLabels(['功能训练动作_右'])
        self.function_rightTree.setVisible(False)
        # 根节点
        self.function_trainingRightActionRoot_1 = QTreeWidgetItem(self.function_rightTree)  # 功能动作训练-训练动作1根节点
        self.function_trainingRightActionRoot_1.setText(0, '精细动作')  # 0代表第一列，即Key列
        self.function_rightTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.function_trainingRightActionRoot_1.setCheckState(0, Qt.Unchecked)

        # 添加子节点1
        self.function_trainingRightAction1Child_1 = QTreeWidgetItem(
            self.function_trainingRightActionRoot_1)  # 功能动作训练-训练动作1的孩子节点1
        self.function_trainingRightAction1Child_1.setText(0, '侧捏夹子')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.function_trainingRightAction1Child_1.setCheckState(0, Qt.Unchecked)
        self.function_trainingRightAction1Child_2 = QTreeWidgetItem(self.function_trainingRightActionRoot_1)
        self.function_trainingRightAction1Child_2.setText(0, '对指翻书页')
        self.function_trainingRightAction1Child_2.setCheckState(0, Qt.Unchecked)

        self.function_trainingRightAction1Child_3 = QTreeWidgetItem(self.function_trainingRightActionRoot_1)
        self.function_trainingRightAction1Child_3.setText(0, '对指捏夹子')
        self.function_trainingRightAction1Child_3.setCheckState(0, Qt.Unchecked)
        self.function_trainingRightAction1Child_4 = QTreeWidgetItem(self.function_trainingRightActionRoot_1)
        self.function_trainingRightAction1Child_4.setText(0, '拿玻璃球')
        self.function_trainingRightAction1Child_4.setCheckState(0, Qt.Unchecked)
        self.function_trainingRightAction1Child_5 = QTreeWidgetItem(self.function_trainingLeftActionRoot_1)
        self.function_trainingRightAction1Child_5.setText(0, '拿回形针')
        self.function_trainingRightAction1Child_5.setCheckState(0, Qt.Unchecked)
        self.function_trainingRightAction1Child_6 = QTreeWidgetItem(self.function_trainingLeftActionRoot_1)
        self.function_trainingRightAction1Child_6.setText(0, '拿木块两指捏')
        self.function_trainingRightAction1Child_6.setCheckState(0, Qt.Unchecked)
        self.function_trainingRightAction1Child_7 = QTreeWidgetItem(self.function_trainingRightActionRoot_1)
        self.function_trainingRightAction1Child_7.setText(0, '拿木块三指捏')
        self.function_trainingRightAction1Child_7.setCheckState(0, Qt.Unchecked)
        self.function_trainingRightAction1Child_8 = QTreeWidgetItem(self.function_trainingRightActionRoot_1)
        self.function_trainingRightAction1Child_8.setText(0, '拿小木块两指捏')
        self.function_trainingRightAction1Child_8.setCheckState(0, Qt.Unchecked)
        self.function_trainingRightAction1Child_9 = QTreeWidgetItem(self.function_trainingRightActionRoot_1)
        self.function_trainingRightAction1Child_9.setText(0, '拿小木块三指捏')
        self.function_trainingRightAction1Child_9.setCheckState(0, Qt.Unchecked)
        self.function_trainingRightAction1Child_10 = QTreeWidgetItem(self.function_trainingRightActionRoot_1)
        self.function_trainingRightAction1Child_10.setText(0, '拿钥匙')
        self.function_trainingRightAction1Child_10.setCheckState(0, Qt.Unchecked)

        # 根节点
        self.function_trainingRightActionRoot_2 = QTreeWidgetItem(self.function_rightTree)  # 功能动作训练-训练动作2根节点
        self.function_trainingRightActionRoot_2.setText(0, '复合旋转运动')  # 0代表第一列，即Key列
        self.function_rightTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.function_trainingRightActionRoot_2.setCheckState(0, Qt.Unchecked)

        # 添加子节点1
        self.function_trainingRightAction2Child_1 = QTreeWidgetItem(
            self.function_trainingRightActionRoot_2)  # 功能动作训练-训练动作2的孩子节点1
        self.function_trainingRightAction2Child_1.setText(0, '翻卡片')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.function_trainingRightAction2Child_1.setCheckState(0, Qt.Unchecked)
        # 功能动作训练-训练动作2的孩子节点2
        self.function_trainingRightAction2Child_2 = QTreeWidgetItem(self.function_trainingRightActionRoot_2)
        self.function_trainingRightAction2Child_2.setText(0, '翻木板')
        self.function_trainingRightAction2Child_2.setCheckState(0, Qt.Unchecked)
        self.function_trainingRightAction2Child_3 = QTreeWidgetItem(self.function_trainingRightActionRoot_2)
        self.function_trainingRightAction2Child_3.setText(0, '翻日历')
        self.function_trainingRightAction2Child_3.setCheckState(0, Qt.Unchecked)
        self.function_trainingRightAction2Child_4 = QTreeWidgetItem(self.function_trainingRightActionRoot_2)
        self.function_trainingRightAction2Child_4.setText(0, '翻书页')
        self.function_trainingRightAction2Child_4.setCheckState(0, Qt.Unchecked)
        self.function_trainingRightAction2Child_5 = QTreeWidgetItem(self.function_trainingRightActionRoot_2)
        self.function_trainingRightAction2Child_5.setText(0, '前臂旋前套杯子')
        self.function_trainingRightAction2Child_5.setCheckState(0, Qt.Unchecked)
        self.function_trainingRightAction2Child_6 = QTreeWidgetItem(self.function_trainingRightActionRoot_2)
        self.function_trainingRightAction2Child_6.setText(0, '套杯子')
        self.function_trainingRightAction2Child_6.setCheckState(0, Qt.Unchecked)

        self.function_trainingRightActionRoot_3 = QTreeWidgetItem(self.function_rightTree)  # 功能动作训练-训练动作2根节点
        self.function_trainingRightActionRoot_3.setText(0, '抓握运动')  # 0代表第一列，即Key列
        self.function_rightTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.function_trainingRightActionRoot_3.setCheckState(0, Qt.Unchecked)

        # 添加子节点1
        self.function_trainingRightAction3Child_1 = QTreeWidgetItem(
            self.function_trainingRightActionRoot_3)  # 功能动作训练-训练动作2的孩子节点1
        self.function_trainingRightAction3Child_1.setText(0, '木棒抓握')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.function_trainingRightAction3Child_1.setCheckState(0, Qt.Unchecked)
        # 功能动作训练-训练动作2的孩子节点2
        self.function_trainingRightAction3Child_2 = QTreeWidgetItem(self.function_trainingRightActionRoot_3)
        self.function_trainingRightAction3Child_2.setText(0, '拿玻璃杯')
        self.function_trainingRightAction3Child_2.setCheckState(0, Qt.Unchecked)
        self.function_trainingRightAction3Child_3 = QTreeWidgetItem(self.function_trainingRightActionRoot_3)
        self.function_trainingRightAction3Child_3.setText(0, '拿矿泉水瓶')
        self.function_trainingRightAction3Child_3.setCheckState(0, Qt.Unchecked)
        self.function_trainingRightAction3Child_4 = QTreeWidgetItem(self.function_trainingRightActionRoot_3)
        self.function_trainingRightAction3Child_4.setText(0, '捏弹力球')
        self.function_trainingRightAction3Child_4.setCheckState(0, Qt.Unchecked)

        self.function_trainingRightActionRoot_4 = QTreeWidgetItem(self.function_rightTree)  # 功能动作训练-训练动作2根节点
        self.function_trainingRightActionRoot_4.setText(0, 'ADL活动')  # 0代表第一列，即Key列
        self.function_rightTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.function_trainingRightActionRoot_4.setCheckState(0, Qt.Unchecked)

        # 添加子节点1
        self.function_trainingRightAction4Child_1 = QTreeWidgetItem(
            self.function_trainingRightActionRoot_4)  # 功能动作训练-训练动作2的孩子节点1
        self.function_trainingRightAction4Child_1.setText(0, '写字')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.function_trainingRightAction4Child_1.setCheckState(0, Qt.Unchecked)
        # 功能动作训练-训练动作2的孩子节点2
        self.function_trainingRightAction4Child_2 = QTreeWidgetItem(self.function_trainingRightActionRoot_4)
        self.function_trainingRightAction4Child_2.setText(0, '旋转铅笔')
        self.function_trainingRightAction4Child_2.setCheckState(0, Qt.Unchecked)
        self.function_trainingRightAction4Child_3 = QTreeWidgetItem(self.function_trainingRightActionRoot_4)
        self.function_trainingRightAction4Child_3.setText(0, '旋转钥匙')
        self.function_trainingRightAction4Child_3.setCheckState(0, Qt.Unchecked)
        self.function_trainingRightAction4Child_4 = QTreeWidgetItem(self.function_trainingRightActionRoot_4)
        self.function_trainingRightAction4Child_4.setText(0, '用勺子舀珠子')
        self.function_trainingRightAction4Child_4.setCheckState(0, Qt.Unchecked)
        self.function_trainingRightAction4Child_5 = QTreeWidgetItem(self.function_trainingRightActionRoot_4)
        self.function_trainingRightAction4Child_5.setText(0, '抓放网球')
        self.function_trainingRightAction4Child_5.setCheckState(0, Qt.Unchecked)

        self.function_trainingRightActionRoot_5 = QTreeWidgetItem(self.function_rightTree)  # 功能动作训练-训练动作2根节点
        self.function_trainingRightActionRoot_5.setText(0, '双手联合运动')  # 0代表第一列，即Key列
        self.function_rightTree.setColumnWidth(0, 200)  # 第一列列宽设为200
        # 开启复选框状态
        self.function_trainingRightActionRoot_5.setCheckState(0, Qt.Unchecked)

        # 添加子节点1
        self.function_trainingRightAction5Child_1 = QTreeWidgetItem(
            self.function_trainingRightActionRoot_5)  # 功能动作训练-训练动作2的孩子节点1
        self.function_trainingRightAction5Child_1.setText(0, '双手滚训练棒')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.function_trainingRightAction5Child_1.setCheckState(0, Qt.Unchecked)
        # 功能动作训练-训练动作2的孩子节点2
        self.function_trainingRightAction5Child_2 = QTreeWidgetItem(self.function_trainingRightActionRoot_5)
        self.function_trainingRightAction5Child_2.setText(0, '双手用力弯曲训练棒')
        self.function_trainingRightAction5Child_2.setCheckState(0, Qt.Unchecked)

        self.function_leftCameraLabel = QtWidgets.QLabel(self.page_3)  # 功能动作训练-左边摄像显示界面
        self.function_leftCameraLabel.setGeometry(QtCore.QRect(740, 80, 550, 520))
        self.function_leftCameraLabel.setStyleSheet("border-width: 1px;border-style: solid;border-color:black")
        self.function_leftCameraLabel.setPixmap(QPixmap("./src/fig/empty_camera.png"))

        self.function_rightCameraLabel = QtWidgets.QLabel(self.page_3)  # 功能动作训练-右边摄像显示界面
        self.function_rightCameraLabel.setGeometry(QtCore.QRect(1340, 80, 550, 520))
        self.function_rightCameraLabel.setStyleSheet("border-width: 1px;border-style: solid;border-color:black")
        self.function_rightCameraLabel.setPixmap(QPixmap("./src/fig/empty_camera.png"))

        self.label_124 = QtWidgets.QLabel(self.page_3)
        self.label_124.setGeometry(QtCore.QRect(745, 30, 120, 40))
        self.label_124.setText("左手")
        self.label_124.setStyleSheet("font:14pt;color:#1E90FF")

        self.function_leftMirrrorButton = QtWidgets.QPushButton(self.page_3)  # 功能动作训练-左手镜像
        self.function_leftMirrrorButton.setGeometry(QtCore.QRect(820, 35, 100, 40))
        self.function_leftMirrrorButton.setStyleSheet("font:12pt")

        self.function_leftCopyButton = QtWidgets.QPushButton(self.page_3)  # 功能动作训练-左手复制
        self.function_leftCopyButton.setGeometry(QtCore.QRect(960, 35, 100, 40))
        self.function_leftCopyButton.setStyleSheet("font:12pt")

        self.function_leftMaskButton = QtWidgets.QPushButton(self.page_3)  # 功能动作训练-左手遮罩
        self.function_leftMaskButton.setGeometry(QtCore.QRect(1100, 35, 100, 40))
        self.function_leftMaskButton.setStyleSheet("font:12pt")

        self.function_leftPlayButton = QtWidgets.QPushButton(self.page_3)  # 功能动作训练-左手播放
        self.function_leftPlayButton.setGeometry(QtCore.QRect(745, 620, 120, 40))
        self.function_leftPlayButton.setStyleSheet("font:12pt")

        self.function_leftStopButton = QtWidgets.QPushButton(self.page_3)  # 功能动作训练-左手重新开始
        self.function_leftStopButton.setGeometry(QtCore.QRect(905, 620, 120, 40))
        self.function_leftStopButton.setStyleSheet("font:12pt")

        self.function_LeftRecoderButton = QtWidgets.QToolButton(self.page_3)  # 功能动作训练-左手录制
        self.function_LeftRecoderButton.setGeometry(QtCore.QRect(1065, 620, 120, 40))
        self.function_LeftRecoderButton.setStyleSheet("font:12pt")

        self.function_leftScreenRecording = QAction(self.page_3)  # 功能动作训练-左手录屏
        self.function_leftScreenRecording.setText('录屏')

        self.function_isPlaying = True
        self.function_leftIsPlaying = True
        self.function_rightIsPlaying = True

        self.function_leftPopup_menu = QMenu(self.page_3)
        self.function_leftPopup_menu.addAction(self.function_leftScreenRecording)

        self.function_LeftRecoderButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.function_LeftRecoderButton.setAutoRaise(True)
        self.function_LeftRecoderButton.setMenu(self.function_leftPopup_menu)

        self.label_125 = QtWidgets.QLabel(self.page_3)
        self.label_125.setGeometry(QtCore.QRect(1350, 30, 120, 40))
        self.label_125.setText("右手")
        self.label_125.setStyleSheet("font:14pt;color:#1E90FF")

        self.function_rightMirrrorButton = QtWidgets.QPushButton(self.page_3)  # 功能动作训练-右手镜像
        self.function_rightMirrrorButton.setGeometry(QtCore.QRect(1420, 35, 100, 40))
        self.function_rightMirrrorButton.setStyleSheet("font:12pt")

        self.function_rightCopyButton = QtWidgets.QPushButton(self.page_3)  # 功能动作训练-右手复制
        self.function_rightCopyButton.setGeometry(QtCore.QRect(1560, 35, 100, 40))
        self.function_rightCopyButton.setStyleSheet("font:12pt")

        self.function_rightMaskButton = QtWidgets.QPushButton(self.page_3)  # 功能动作训练-右手遮罩
        self.function_rightMaskButton.setGeometry(QtCore.QRect(1700, 35, 100, 40))
        self.function_rightMaskButton.setStyleSheet("font:12pt")

        self.function_rightPlayButton = QtWidgets.QPushButton(self.page_3)  # 功能动作训练-右手播放
        self.function_rightPlayButton.setGeometry(QtCore.QRect(1350, 620, 120, 40))
        self.function_rightPlayButton.setStyleSheet("font:12pt")

        self.function_rightStopButton = QtWidgets.QPushButton(self.page_3)  # 功能动作训练-右手重新开始
        self.function_rightStopButton.setGeometry(QtCore.QRect(1510, 620, 120, 40))
        self.function_rightStopButton.setStyleSheet("font:12pt")

        self.function_rightRecoderButton = QtWidgets.QToolButton(self.page_3)  # 功能动作训练-右手录制
        self.function_rightRecoderButton.setGeometry(QtCore.QRect(1670, 620, 120, 40))
        self.function_rightRecoderButton.setStyleSheet("font:12pt")

        self.function_rightScreenRecording = QAction(self.page_3)  # 功能动作训练-右手录屏
        self.function_rightScreenRecording.setText('录屏')

        self.function_rightPopup_menu = QMenu(self.page_3)
        self.function_rightPopup_menu.addAction(self.function_rightScreenRecording)

        self.function_rightRecoderButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.function_rightRecoderButton.setAutoRaise(True)
        self.function_rightRecoderButton.setMenu(self.function_rightPopup_menu)

        self.function_cancelButton = QtWidgets.QPushButton(self.page_3)  # 功能动作训练-全部取消
        self.function_cancelButton.setGeometry(QtCore.QRect(10, 620, 120, 40))
        self.function_cancelButton.setStyleSheet("font:12pt")

        self.function_selectAllButton = QtWidgets.QPushButton(self.page_3)  # 功能动作训练-全部选择
        self.function_selectAllButton.setGeometry(QtCore.QRect(140, 620, 120, 40))
        self.function_selectAllButton.setStyleSheet("font:12pt")

        self.label_29 = QtWidgets.QLabel(self.page_3)  # 组数
        self.label_29.setGeometry(QtCore.QRect(270, 620, 120, 40))
        self.label_29.setStyleSheet("font:12pt")

        self.function_trainingGroupNumLineEdit = QtWidgets.QLineEdit(self.page_3)  # 功能动作训练-获取训练组数
        self.function_trainingGroupNumLineEdit.setGeometry(QtCore.QRect(330, 620, 120, 40))
        self.function_trainingGroupNumLineEdit.setStyleSheet("font:12pt")

        self.label_28 = QtWidgets.QLabel(self.page_3)  # 方式
        self.label_28.setGeometry(QtCore.QRect(470, 620, 120, 40))
        self.label_28.setStyleSheet("font:12pt")

        self.function_trainingWayComboBox = QtWidgets.QComboBox(self.page_3)  # 功能动作训练-获取训练方式
        self.function_trainingWayComboBox.setGeometry(QtCore.QRect(540, 620, 120, 40))
        self.function_trainingWayComboBox.addItems(['', 'AABB', 'ABAB'])
        self.function_trainingWayComboBox.setStyleSheet("font:12pt")

        self.label_30 = QtWidgets.QLabel(self.page_3)  # 训练次数
        self.label_30.setGeometry(QtCore.QRect(10, 680, 120, 40))
        self.label_30.setStyleSheet("font:12pt")

        self.function_trainingNumLineEdit = QtWidgets.QLineEdit(self.page_3)  # 功能动作训练-获取训练次数
        self.function_trainingNumLineEdit.setGeometry(QtCore.QRect(120, 680, 120, 40))
        self.function_trainingNumLineEdit.setStyleSheet("font:12pt")

        self.label_31 = QtWidgets.QLabel(self.page_3)  # 播放次数
        self.label_31.setGeometry(QtCore.QRect(250, 680, 120, 40))
        self.label_31.setStyleSheet("font:12pt")

        self.function_playNumLineEdit = QtWidgets.QLineEdit(self.page_3)  # 功能动作训练-获取每组视频播放次数
        self.function_playNumLineEdit.setGeometry(QtCore.QRect(360, 680, 120, 40))
        self.function_playNumLineEdit.setStyleSheet("font:12pt")

        self.label_51 = QtWidgets.QLabel(self.page_3)  # 播放速率
        self.label_51.setGeometry(QtCore.QRect(500, 680, 120, 40))
        self.label_51.setText('播放速率')
        self.label_51.setStyleSheet("font:12pt")

        self.function_playSpeedComBox = QtWidgets.QComboBox(self.page_3)  # 功能动作训练-获取视频播放速率
        self.function_playSpeedComBox.setGeometry(QtCore.QRect(600, 680, 120, 40))
        self.function_playSpeedComBox.addItems(['', '0.5', '1', '1.25', '1.5', '2'])
        self.function_playSpeedComBox.setStyleSheet("font:12pt")

        self.function_recommendButton = QtWidgets.QPushButton(self.page_3)  # 功能动作训练-获取该病人预先设置好的训练方案
        self.function_recommendButton.setGeometry(QtCore.QRect(10, 730, 120, 40))
        self.function_recommendButton.setStyleSheet("font:12pt")

        self.function_startButton = QtWidgets.QPushButton(self.page_3)  # 推荐动作训练-开始训练
        self.function_startButton.setGeometry(QtCore.QRect(140, 730, 120, 40))
        self.function_startButton.setStyleSheet("font:12pt")

        self.function_historyRecordButton = QtWidgets.QPushButton(self.page_3)  # 功能动作训练——显示视频历史记录
        self.function_historyRecordButton.setGeometry(QtCore.QRect(270, 730, 120, 40))
        self.function_historyRecordButton.setText('历史记录')
        self.function_historyRecordButton.setStyleSheet("font:12pt")

        self.label_55 = QtWidgets.QLabel(self.page_3)
        self.label_55.setGeometry(QtCore.QRect(400, 730, 120, 40))
        self.label_55.setText("训练时长:")
        self.label_55.setStyleSheet("font:12pt")

        self.function_timeEdit = QTimeEdit(self.page_3)  # 功能训练-时间计时器
        self.function_timeEdit.setDisplayFormat('HH:mm:ss')
        self.function_timeEdit.setGeometry(QtCore.QRect(520, 730, 120, 40))

        self.function_traingSituationFrame = QtWidgets.QFrame(self.page_3)  # 功能动作训练情况显示窗口
        self.function_traingSituationFrame.setGeometry(QtCore.QRect(10, 10, 700, 710))
        self.function_traingSituationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.function_traingSituationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.function_traingSituationFrame.setVisible(False)

        self.label_75 = QtWidgets.QLabel(self.function_traingSituationFrame)  # 训练情况
        self.label_75.setGeometry(QtCore.QRect(20, 10, 120, 40))
        self.label_75.setStyleSheet("font:14pt;color:#1E90FF")

        self.label_76 = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.label_76.setGeometry(QtCore.QRect(20, 60, 200, 40))
        self.label_76.setStyleSheet("font:10pt")

        # 功能动作训练训练情况-获取训练模式
        self.function_trainingModeLabel = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.function_trainingModeLabel.setGeometry(QtCore.QRect(140, 60, 200, 40))
        self.function_trainingModeLabel.setStyleSheet("font:10pt")

        self.label_77 = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.label_77.setGeometry(QtCore.QRect(200, 60, 220, 40))
        self.label_77.setStyleSheet("font:10pt")

        # 功能动作训练训练情况-获取训练组数
        self.function_trianingGroupsLabel = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.function_trianingGroupsLabel.setGeometry(QtCore.QRect(330, 60, 220, 40))
        self.function_trianingGroupsLabel.setStyleSheet("font:10pt")

        self.label_78 = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.label_78.setGeometry(QtCore.QRect(360, 60, 220, 40))
        self.label_78.setStyleSheet("font:10pt")

        # 功能动作训练训练情况-获取训练动作个数
        self.function_triangNumLabel = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.function_triangNumLabel.setGeometry(QtCore.QRect(470, 60, 220, 40))
        self.function_triangNumLabel.setStyleSheet("font:10pt")

        self.label_79 = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.label_79.setGeometry(QtCore.QRect(500, 60, 220, 40))
        self.label_79.setStyleSheet("font:10pt")

        self.label_126 = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.label_126.setGeometry(QtCore.QRect(40, 100, 220, 40))
        self.label_126.setText("总共(组):")
        self.label_126.setStyleSheet("font:10pt")

        # 功能动作训练训练情况-获取训练动作组数
        self.function_trainingTotalNumLabel = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.function_trainingTotalNumLabel.setGeometry(QtCore.QRect(150, 100, 220, 40))
        self.function_trainingTotalNumLabel.setText("--")
        self.function_trainingTotalNumLabel.setStyleSheet("font:10pt")

        self.label_127 = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.label_127.setGeometry(QtCore.QRect(200, 100, 220, 40))
        self.label_127.setText("当前(组):")
        self.label_127.setStyleSheet("font:10pt")

        # 功能动作训练训练情况-获取当前训练动作组数
        self.function_trainingCurrentNumLabel = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.function_trainingCurrentNumLabel.setGeometry(QtCore.QRect(300, 100, 220, 40))
        self.function_trainingCurrentNumLabel.setText("--")
        self.function_trainingCurrentNumLabel.setStyleSheet("font:10pt")

        self.label_128 = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.label_128.setGeometry(QtCore.QRect(350, 100, 220, 40))
        self.label_128.setText("剩余(组):")
        self.label_128.setStyleSheet("font:10pt")

        # 功能动作训练训练情况-获取剩余训练动作组数
        self.function_trainingRemainNumLabel = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.function_trainingRemainNumLabel.setGeometry(QtCore.QRect(450, 100, 220, 40))
        self.function_trainingRemainNumLabel.setText("--")
        self.function_trainingRemainNumLabel.setStyleSheet("font:10pt")

        self.label_80 = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.label_80.setGeometry(QtCore.QRect(20, 140, 250, 40))
        self.label_80.setStyleSheet("font:10pt")

        # 功能动作训练训练情况-获取训练动作名称
        self.function_trainingNameLabel = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.function_trainingNameLabel.setGeometry(QtCore.QRect(210, 140, 500, 40))
        self.function_trainingNameLabel.setStyleSheet("font:10pt")

        self.label_81 = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.label_81.setGeometry(QtCore.QRect(20, 180, 200, 40))
        self.label_81.setStyleSheet("font:10pt")

        self.label_82 = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.label_82.setGeometry(QtCore.QRect(40, 220, 200, 40))
        self.label_82.setStyleSheet("font:10pt")

        # 功能动作训练情况-获取跟视频训练总次数
        self.function_trianingTotalNumPlayVideoLabel = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.function_trianingTotalNumPlayVideoLabel.setGeometry(QtCore.QRect(160, 220, 200, 40))
        self.function_trianingTotalNumPlayVideoLabel.setStyleSheet("font:10pt")

        self.label_83 = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.label_83.setGeometry(QtCore.QRect(200, 220, 200, 40))
        self.label_83.setStyleSheet("font:10pt")

        # 功能动作训练情况-获取跟视频训练当前次数
        self.function_currentPlayVideoLabel = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.function_currentPlayVideoLabel.setGeometry(QtCore.QRect(320, 220, 200, 40))
        self.function_currentPlayVideoLabel.setStyleSheet("font:10pt")

        self.label_84 = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.label_84.setGeometry(QtCore.QRect(370, 220, 200, 40))
        self.label_84.setStyleSheet("font:10pt")

        # 功能动作训练情况-获取跟视频训练剩余次数
        self.function_remainingPlayVideoLabel = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.function_remainingPlayVideoLabel.setGeometry(QtCore.QRect(480, 220, 200, 40))
        self.function_remainingPlayVideoLabel.setStyleSheet("font:10pt")

        self.label_85 = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.label_85.setGeometry(QtCore.QRect(20, 260, 200, 40))
        self.label_85.setStyleSheet("font:10pt")

        self.label_86 = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.label_86.setGeometry(QtCore.QRect(40, 300, 200, 40))
        self.label_86.setStyleSheet("font:10pt")

        # 功能动作训练情况-获取自行训练总次数
        self.function_autonomousTrianingTotalNumLabel = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.function_autonomousTrianingTotalNumLabel.setGeometry(QtCore.QRect(160, 300, 200, 40))
        self.function_autonomousTrianingTotalNumLabel.setStyleSheet("font:10pt")

        self.label_87 = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.label_87.setGeometry(QtCore.QRect(200, 300, 200, 40))
        self.label_87.setStyleSheet("font:10pt")

        # 功能动作训练情况-获取自行训练当前次数
        self.function_autonomousCurrentLabel = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.function_autonomousCurrentLabel.setGeometry(QtCore.QRect(320, 300, 200, 40))
        self.function_autonomousCurrentLabel.setStyleSheet("font:10pt")

        self.label_88 = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.label_88.setGeometry(QtCore.QRect(370, 300, 200, 40))
        self.label_88.setStyleSheet("font:10pt")

        # 功能动作训练情况-获取自行训练剩余次数
        self.function_autonomousRemainingLabel = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.function_autonomousRemainingLabel.setGeometry(QtCore.QRect(480, 300, 200, 40))
        self.function_autonomousRemainingLabel.setStyleSheet("font:10pt")

        # 功能动作训练情况-显示当前播放的视频
        self.function_showVideoLabel = QtWidgets.QLabel(self.function_traingSituationFrame)
        self.function_showVideoLabel.setGeometry(QtCore.QRect(10, 340, 680, 350))
        self.function_showVideoLabel.setStyleSheet("border-width: 1px;border-style: solid;border-color:black")

        self.page_4 = QtWidgets.QWidget()

        self.mirror_lefCameraLabel = QtWidgets.QLabel(self.page_4)  # 镜像训练-左手摄像头显示界面
        self.mirror_lefCameraLabel.setGeometry(QtCore.QRect(30, 65, 900, 650))
        self.mirror_lefCameraLabel.setStyleSheet("border-width: 1px;border-style: solid;border-color:black")
        self.mirror_lefCameraLabel.setPixmap(QPixmap('./src/fig/empty_camera.png'))
        self.mirror_lefCameraLabel.setAlignment(Qt.AlignCenter)

        self.mirror_rightCameraLabel = QtWidgets.QLabel(self.page_4)  # 镜像训练-右手摄像头显示界面
        self.mirror_rightCameraLabel.setGeometry(QtCore.QRect(970, 65, 900, 650))
        self.mirror_rightCameraLabel.setStyleSheet("border-width: 1px;border-style: solid;border-color:black")
        self.mirror_rightCameraLabel.setPixmap(QPixmap('./src/fig/empty_camera.png'))
        self.mirror_rightCameraLabel.setAlignment(Qt.AlignCenter)

        self.label_129 = QtWidgets.QLabel(self.page_4)
        self.label_129.setGeometry(QtCore.QRect(30, 20, 120, 40))
        self.label_129.setText("左手")
        self.label_129.setStyleSheet("font:14pt;color:#1E90FF")

        self.mirror_leftMirrorButton = QtWidgets.QPushButton(self.page_4)  # 镜像训练-左手镜像
        self.mirror_leftMirrorButton.setGeometry(QtCore.QRect(100, 20, 100, 40))
        self.mirror_leftMirrorButton.setStyleSheet("font:12pt;")

        self.mirror_leftCopyButton = QtWidgets.QPushButton(self.page_4)  # 镜像训练-左手复制
        self.mirror_leftCopyButton.setGeometry(QtCore.QRect(240, 20, 100, 40))
        self.mirror_leftCopyButton.setStyleSheet("font:12pt;")

        self.mirror_leftMaskButton = QtWidgets.QPushButton(self.page_4)  # 镜像训练-左手遮罩
        self.mirror_leftMaskButton.setGeometry(QtCore.QRect(380, 20, 100, 40))
        self.mirror_leftMaskButton.setStyleSheet("font:12pt;")

        self.mirror_leftPlayButton = QtWidgets.QPushButton(self.page_4)  # 镜像训练-左手播放
        self.mirror_leftPlayButton.setGeometry(QtCore.QRect(100, 725, 100, 40))
        self.mirror_leftPlayButton.setStyleSheet("font:12pt;")

        self.mirror_leftRecoderButton = QtWidgets.QToolButton(self.page_4)  # 镜像训练-左手录制
        self.mirror_leftRecoderButton.setGeometry(QtCore.QRect(240, 725, 100, 40))
        self.mirror_leftRecoderButton.setStyleSheet("font:12pt;")

        self.mirror_leftScreenRecording = QAction(self.page_4)  # 镜像训练-左手录屏
        self.mirror_leftScreenRecording.setText('录屏')

        self.mirror_leftPopup_menu = QMenu(self.page_4)
        self.mirror_leftPopup_menu.addAction(self.mirror_leftScreenRecording)

        self.mirror_leftRecoderButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.mirror_leftRecoderButton.setAutoRaise(True)
        self.mirror_leftRecoderButton.setMenu(self.mirror_leftPopup_menu)

        self.mirror_historyRecordButton = QtWidgets.QPushButton(self.page_4)  # 镜像训练——显示视频历史记录
        self.mirror_historyRecordButton.setGeometry(QtCore.QRect(380, 725, 100, 40))
        self.mirror_historyRecordButton.setText('历史记录')
        self.mirror_historyRecordButton.setStyleSheet("font:12pt")

        self.label_56 = QtWidgets.QLabel(self.page_4)
        self.label_56.setGeometry(QtCore.QRect(520, 725, 150, 40))
        self.label_56.setText("训练时长:")
        self.label_56.setStyleSheet("font:12pt")

        self.mirror_timeEdit = QTimeEdit(self.page_4)  # 镜像训练-时间计时器
        self.mirror_timeEdit.setDisplayFormat('HH:mm:ss')
        self.mirror_timeEdit.setGeometry(QtCore.QRect(640, 725, 150, 40))

        self.label_130 = QtWidgets.QLabel(self.page_4)
        self.label_130.setGeometry(QtCore.QRect(970, 20, 120, 40))
        self.label_130.setText("右手")
        self.label_130.setStyleSheet("font:14pt;color:#1E90FF")

        self.mirror_rightMirrorButton = QtWidgets.QPushButton(self.page_4)  # 镜像训练-右手镜像
        self.mirror_rightMirrorButton.setGeometry(QtCore.QRect(1040, 20, 100, 40))
        self.mirror_rightMirrorButton.setStyleSheet("font:12pt;")

        self.mirror_rightCopyButton = QtWidgets.QPushButton(self.page_4)  # 镜像训练-右手复制
        self.mirror_rightCopyButton.setGeometry(QtCore.QRect(1180, 20, 100, 40))
        self.mirror_rightCopyButton.setStyleSheet("font:12pt;")

        self.mirror_rightMaskButton = QtWidgets.QPushButton(self.page_4)  # 镜像训练-右手遮罩
        self.mirror_rightMaskButton.setGeometry(QtCore.QRect(1320, 20, 100, 40))
        self.mirror_rightMaskButton.setStyleSheet("font:12pt;")

        self.mirror_rightPlayButton = QtWidgets.QPushButton(self.page_4)  # 镜像训练-右手播放
        self.mirror_rightPlayButton.setGeometry(QtCore.QRect(1040, 725, 100, 40))
        self.mirror_rightPlayButton.setStyleSheet("font:12pt;")

        self.mirror_rightRecoderButton = QtWidgets.QToolButton(self.page_4)  # 镜像训练-右手录制
        self.mirror_rightRecoderButton.setGeometry(QtCore.QRect(1180, 725, 100, 40))
        self.mirror_rightRecoderButton.setStyleSheet("font:12pt;")

        self.mirror_rightScreenRecording = QAction(self.page_4)  # 镜像训练-右手录屏
        self.mirror_rightScreenRecording.setText('录屏')

        self.mirror_startButton = QtWidgets.QPushButton(self.page_4)  # 镜像训练-右手播放
        self.mirror_startButton.setGeometry(QtCore.QRect(840, 725, 100, 40))
        self.mirror_startButton.setText('开始训练')
        self.mirror_startButton.setStyleSheet("font:12pt;")

        self.mirror_rightPopup_menu = QMenu(self.page_4)
        self.mirror_rightPopup_menu.addAction(self.mirror_rightScreenRecording)

        self.mirror_rightRecoderButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.mirror_rightRecoderButton.setAutoRaise(True)
        self.mirror_rightRecoderButton.setMenu(self.mirror_rightPopup_menu)

        self.mirror_leftIsPlaying = True
        self.mirror_rightIsPlaying = True
        self.mirror_isPlaying = True

        self.page_9 = QtWidgets.QWidget()

        self.label_57 = QtWidgets.QLabel(self.page_9)
        self.label_57.setGeometry(QtCore.QRect(10, 240, 54, 12))
        self.label_57.setObjectName("label_57")

        self.sensorimotor_leftIsPlaying = True
        self.sensorimotor_rightIsPlaying = True

        self.sensorimotor_selectTrainingFrame = QtWidgets.QFrame(self.page_9)  # 感觉运动训练容器
        self.sensorimotor_selectTrainingFrame.setGeometry(QtCore.QRect(10, 10, 700, 600))
        self.sensorimotor_selectTrainingFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sensorimotor_selectTrainingFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.sensorimotor_scrollArea = QtWidgets.QScrollArea(self.sensorimotor_selectTrainingFrame)  # 感觉运动训练滑动窗口
        self.sensorimotor_scrollArea.setGeometry(QtCore.QRect(0, 0, 700, 600))
        self.sensorimotor_scrollArea.setWidgetResizable(True)

        self.sensorimotor_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.sensorimotor_scrollAreaWidgetContents.setMinimumHeight(3000)
        self.sensorimotor_scrollArea.setWidget(self.sensorimotor_scrollAreaWidgetContents)

        # 感觉运动训练-训练动作左根节点
        self.sensorimotor_leftTree = QtWidgets.QTreeWidget(self.sensorimotor_scrollAreaWidgetContents)
        self.sensorimotor_leftTree.setGeometry(QtCore.QRect(0, 0, 700, 10000))
        self.sensorimotor_leftTree.setStyleSheet('font:14pt')
        # 为树控件指定列数
        self.sensorimotor_leftTree.setColumnCount(1)

        # 指定列标签
        self.sensorimotor_leftTree.setHeaderLabels(['感觉运动观察训练_左'])

        # 感觉运动训练-训练动作左1根节点
        self.sensorimotor_trainingLeftActionRoot_1 = QTreeWidgetItem(self.sensorimotor_leftTree)
        self.sensorimotor_trainingLeftActionRoot_1.setText(0, '浅感觉')  # 0代表第一列，即Key列
        self.sensorimotor_leftTree.setColumnWidth(0, 350)

        # 开启复选框状态
        self.sensorimotor_trainingLeftActionRoot_1.setCheckState(0, Qt.Unchecked)

        # 感觉运动训练-训练动作1的孩子节点1
        self.sensorimotor_trainingLeftAction1Child_1 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_1)
        self.sensorimotor_trainingLeftAction1Child_1.setText(0, '触摸布')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.sensorimotor_trainingLeftAction1Child_1.setCheckState(0, Qt.Unchecked)

        # 感觉运动训练-训练动作1的孩子节点2
        self.sensorimotor_trainingLeftAction1Child_2 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_1)
        self.sensorimotor_trainingLeftAction1Child_2.setText(0, '触摸指压板')
        self.sensorimotor_trainingLeftAction1Child_2.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction1Child_3 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_1)
        self.sensorimotor_trainingLeftAction1Child_3.setText(0, '触摸竹简')
        self.sensorimotor_trainingLeftAction1Child_3.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction1Child_4 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_1)
        self.sensorimotor_trainingLeftAction1Child_4.setText(0, '触摸桌垫')
        self.sensorimotor_trainingLeftAction1Child_4.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction1Child_5 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_1)
        self.sensorimotor_trainingLeftAction1Child_5.setText(0, '单丝触觉—食指远端指腹')
        self.sensorimotor_trainingLeftAction1Child_5.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction1Child_6 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_1)
        self.sensorimotor_trainingLeftAction1Child_6.setText(0, '单丝触觉—手背虎口')
        self.sensorimotor_trainingLeftAction1Child_6.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction1Child_7 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_1)
        self.sensorimotor_trainingLeftAction1Child_7.setText(0, '单丝触觉—远端指背')
        self.sensorimotor_trainingLeftAction1Child_7.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction1Child_8 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_1)
        self.sensorimotor_trainingLeftAction1Child_8.setText(0, '棉签轻触觉—食指背侧')
        self.sensorimotor_trainingLeftAction1Child_8.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction1Child_9 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_1)
        self.sensorimotor_trainingLeftAction1Child_9.setText(0, '棉签轻触觉—食指指腹')
        self.sensorimotor_trainingLeftAction1Child_9.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction1Child_10 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_1)
        self.sensorimotor_trainingLeftAction1Child_10.setText(0, '刷擦1—手背')
        self.sensorimotor_trainingLeftAction1Child_10.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction1Child_11 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_1)
        self.sensorimotor_trainingLeftAction1Child_11.setText(0, '刷擦1—手掌')
        self.sensorimotor_trainingLeftAction1Child_11.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction1Child_12 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_1)
        self.sensorimotor_trainingLeftAction1Child_12.setText(0, '纸板触觉—手背')
        self.sensorimotor_trainingLeftAction1Child_12.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction1Child_13 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_1)
        self.sensorimotor_trainingLeftAction1Child_13.setText(0, '纸板触觉—手掌')
        self.sensorimotor_trainingLeftAction1Child_13.setCheckState(0, Qt.Unchecked)

        # 感觉运动训练-训练动作2根节点
        self.sensorimotor_trainingLeftActionRoot_2 = QTreeWidgetItem(self.sensorimotor_leftTree)
        self.sensorimotor_trainingLeftActionRoot_2.setText(0, '深感觉')  # 0代表第一列，即Key列
        self.sensorimotor_leftTree.setColumnWidth(0, 350)  # 第一列列宽设为200
        # 开启复选框状态
        self.sensorimotor_trainingLeftActionRoot_2.setCheckState(0, Qt.Unchecked)

        # 感觉运动训练-训练动作2的孩子节点1
        self.sensorimotor_trainingLeftAction2Child_1 = QTreeWidgetItem(
            self.sensorimotor_trainingLeftActionRoot_2)  # 基本动作训练-训练动作1的孩子节点1
        self.sensorimotor_trainingLeftAction2Child_1.setText(0, '运动觉')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.sensorimotor_trainingLeftAction2Child_1.setCheckState(0, Qt.Unchecked)

        # 感觉运动训练-训练动作2的孩子节点2
        self.sensorimotor_trainingLeftAction2Child_2 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_2)
        self.sensorimotor_trainingLeftAction2Child_2.setText(0, '震动觉1')
        self.sensorimotor_trainingLeftAction2Child_2.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction2Child_3 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_2)
        self.sensorimotor_trainingLeftAction2Child_3.setText(0, '震动觉2')
        self.sensorimotor_trainingLeftAction2Child_3.setCheckState(0, Qt.Unchecked)

        self.sensorimotor_trainingLeftActionRoot_3 = QTreeWidgetItem(self.sensorimotor_leftTree)
        self.sensorimotor_trainingLeftActionRoot_3.setText(0, '复合感觉')  # 0代表第一列，即Key列
        self.sensorimotor_leftTree.setColumnWidth(0, 350)  # 第一列列宽设为200
        # 开启复选框状态
        self.sensorimotor_trainingLeftActionRoot_3.setCheckState(0, Qt.Unchecked)

        # 感觉运动训练-训练动作3的孩子节点1
        self.sensorimotor_trainingLeftAction3Child_1 = QTreeWidgetItem(
            self.sensorimotor_trainingLeftActionRoot_3)  # 基本动作训练-训练动作1的孩子节点1
        self.sensorimotor_trainingLeftAction3Child_1.setText(0, '皮肤定位觉')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.sensorimotor_trainingLeftAction3Child_1.setCheckState(0, Qt.Unchecked)

        # 感觉运动训练-训练动作2的孩子节点2
        self.sensorimotor_trainingLeftAction3Child_2 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_3)
        self.sensorimotor_trainingLeftAction3Child_2.setText(0, '抓木块1')
        self.sensorimotor_trainingLeftAction3Child_2.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction3Child_3 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_3)
        self.sensorimotor_trainingLeftAction3Child_3.setText(0, '抓木块2')
        self.sensorimotor_trainingLeftAction3Child_3.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction3Child_4 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_3)
        self.sensorimotor_trainingLeftAction3Child_4.setText(0, '抓木块3')
        self.sensorimotor_trainingLeftAction3Child_4.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction3Child_5 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_3)
        self.sensorimotor_trainingLeftAction3Child_5.setText(0, '抓木块4')
        self.sensorimotor_trainingLeftAction3Child_5.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction3Child_6 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_3)
        self.sensorimotor_trainingLeftAction3Child_6.setText(0, '抓球1')
        self.sensorimotor_trainingLeftAction3Child_6.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction3Child_7 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_3)
        self.sensorimotor_trainingLeftAction3Child_7.setText(0, '抓球2')
        self.sensorimotor_trainingLeftAction3Child_7.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction3Child_8 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_3)
        self.sensorimotor_trainingLeftAction3Child_8.setText(0, '抓球3')
        self.sensorimotor_trainingLeftAction3Child_8.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction3Child_9 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_3)
        self.sensorimotor_trainingLeftAction3Child_9.setText(0, '抓球4')
        self.sensorimotor_trainingLeftAction3Child_9.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction3Child_10 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_3)
        self.sensorimotor_trainingLeftAction3Child_10.setText(0, '抓圆柱1')
        self.sensorimotor_trainingLeftAction3Child_10.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction3Child_11 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_3)
        self.sensorimotor_trainingLeftAction3Child_11.setText(0, '抓圆柱2')
        self.sensorimotor_trainingLeftAction3Child_11.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction3Child_12 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_3)
        self.sensorimotor_trainingLeftAction3Child_12.setText(0, '抓圆柱3')
        self.sensorimotor_trainingLeftAction3Child_12.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction3Child_13 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_3)
        self.sensorimotor_trainingLeftAction3Child_13.setText(0, '抓圆柱4')
        self.sensorimotor_trainingLeftAction3Child_13.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingLeftAction3Child_15 = QTreeWidgetItem(self.sensorimotor_trainingLeftActionRoot_3)
        self.sensorimotor_trainingLeftAction3Child_15.setText(0, '抓圆柱5')
        self.sensorimotor_trainingLeftAction3Child_15.setCheckState(0, Qt.Unchecked)

        self.sensorimotor_rightTree = QtWidgets.QTreeWidget(self.sensorimotor_scrollAreaWidgetContents)
        self.sensorimotor_rightTree.setGeometry(QtCore.QRect(0, 0, 700, 10000))
        self.sensorimotor_rightTree.setStyleSheet('font:14pt')
        # 为树控件指定列数
        self.sensorimotor_rightTree.setColumnCount(1)
        # 指定列标签
        self.sensorimotor_rightTree.setHeaderLabels(['感觉运动观察训练_右'])
        self.sensorimotor_rightTree.setVisible(False)

        # 感觉运动训练-训练动作1根节点
        self.sensorimotor_trainingRightActionRoot_1 = QTreeWidgetItem(self.sensorimotor_rightTree)
        self.sensorimotor_trainingRightActionRoot_1.setText(0, '浅感觉')  # 0代表第一列，即Key列
        self.sensorimotor_rightTree.setColumnWidth(0, 350)  # 第一列列宽设为200
        # 开启复选框状态
        self.sensorimotor_trainingRightActionRoot_1.setCheckState(0, Qt.Unchecked)

        # 感觉运动训练-训练动作1的孩子节点1
        self.sensorimotor_trainingRighAction1Child_1 = QTreeWidgetItem(self.sensorimotor_trainingRightActionRoot_1)
        self.sensorimotor_trainingRighAction1Child_1.setText(0, '触摸布')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.sensorimotor_trainingRighAction1Child_1.setCheckState(0, Qt.Unchecked)

        # 感觉运动训练-训练动作1的孩子节点2
        self.sensorimotor_trainingRightAction1Child_2 = QTreeWidgetItem(self.sensorimotor_trainingRightActionRoot_1)
        self.sensorimotor_trainingRightAction1Child_2.setText(0, '触摸指压板')
        self.sensorimotor_trainingRightAction1Child_2.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction1Child_3 = QTreeWidgetItem(self.sensorimotor_trainingRightActionRoot_1)
        self.sensorimotor_trainingRightAction1Child_3.setText(0, '触摸竹简')
        self.sensorimotor_trainingRightAction1Child_3.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction1Child_4 = QTreeWidgetItem(self.sensorimotor_trainingRightActionRoot_1)
        self.sensorimotor_trainingRightAction1Child_4.setText(0, '触摸桌垫')
        self.sensorimotor_trainingRightAction1Child_4.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction1Child_5 = QTreeWidgetItem(self.sensorimotor_trainingRightActionRoot_1)
        self.sensorimotor_trainingRightAction1Child_5.setText(0, '单丝触觉—食指远端指腹')
        self.sensorimotor_trainingRightAction1Child_5.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction1Child_6 = QTreeWidgetItem(self.sensorimotor_trainingRightActionRoot_1)
        self.sensorimotor_trainingRightAction1Child_6.setText(0, '单丝触觉—手背虎口')
        self.sensorimotor_trainingRightAction1Child_6.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction1Child_7 = QTreeWidgetItem(self.sensorimotor_trainingRightActionRoot_1)
        self.sensorimotor_trainingRightAction1Child_7.setText(0, '单丝触觉—远端指背')
        self.sensorimotor_trainingRightAction1Child_7.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction1Child_8 = QTreeWidgetItem(self.sensorimotor_trainingRightActionRoot_1)
        self.sensorimotor_trainingRightAction1Child_8.setText(0, '棉签轻触觉—食指背侧')
        self.sensorimotor_trainingRightAction1Child_8.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction1Child_9 = QTreeWidgetItem(self.sensorimotor_trainingRightActionRoot_1)
        self.sensorimotor_trainingRightAction1Child_9.setText(0, '棉签轻触觉—食指指腹')
        self.sensorimotor_trainingRightAction1Child_9.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction1Child_10 = QTreeWidgetItem(self.sensorimotor_trainingRightActionRoot_1)
        self.sensorimotor_trainingRightAction1Child_10.setText(0, '刷擦1—手背')
        self.sensorimotor_trainingRightAction1Child_10.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction1Child_11 = QTreeWidgetItem(self.sensorimotor_trainingRightActionRoot_1)
        self.sensorimotor_trainingRightAction1Child_11.setText(0, '刷擦1—手掌')
        self.sensorimotor_trainingRightAction1Child_11.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction1Child_12 = QTreeWidgetItem(self.sensorimotor_trainingRightActionRoot_1)
        self.sensorimotor_trainingRightAction1Child_12.setText(0, '纸板触觉—手背')
        self.sensorimotor_trainingRightAction1Child_12.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction1Child_13 = QTreeWidgetItem(self.sensorimotor_trainingRightActionRoot_1)
        self.sensorimotor_trainingRightAction1Child_13.setText(0, '纸板触觉—手掌')
        self.sensorimotor_trainingRightAction1Child_13.setCheckState(0, Qt.Unchecked)

        # 感觉运动训练-训练动作2根节点
        self.sensorimotor_trainingRightActionRoot_2 = QTreeWidgetItem(self.sensorimotor_rightTree)
        self.sensorimotor_trainingRightActionRoot_2.setText(0, '深感觉')  # 0代表第一列，即Key列
        self.sensorimotor_rightTree.setColumnWidth(0, 350)  # 第一列列宽设为200
        # 开启复选框状态
        self.sensorimotor_trainingRightActionRoot_2.setCheckState(0, Qt.Unchecked)

        # 感觉运动训练-训练动作2的孩子节点1
        self.sensorimotor_trainingRightAction2Child_1 = QTreeWidgetItem(
            self.sensorimotor_trainingRightActionRoot_2)  # 基本动作训练-训练动作1的孩子节点1
        self.sensorimotor_trainingRightAction2Child_1.setText(0, '运动觉')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.sensorimotor_trainingRightAction2Child_1.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction2Child_2 = QTreeWidgetItem(
            self.sensorimotor_trainingRightActionRoot_2)  # 基本动作训练-训练动作1的孩子节点1
        self.sensorimotor_trainingRightAction2Child_2.setText(0, '震动觉1')  # 第一列Key为 子节点1
        self.sensorimotor_trainingRightAction2Child_2.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction2Child_3 = QTreeWidgetItem(
            self.sensorimotor_trainingRightActionRoot_2)  # 基本动作训练-训练动作1的孩子节点1
        self.sensorimotor_trainingRightAction2Child_3.setText(0, '震动觉2')  # 第一列Key为 子节点1
        self.sensorimotor_trainingRightAction2Child_3.setCheckState(0, Qt.Unchecked)

        self.sensorimotor_trainingRightActionRoot_3 = QTreeWidgetItem(self.sensorimotor_rightTree)
        self.sensorimotor_trainingRightActionRoot_3.setText(0, '复合感觉')  # 0代表第一列，即Key列
        self.sensorimotor_rightTree.setColumnWidth(0, 350)  # 第一列列宽设为200
        # 开启复选框状态
        self.sensorimotor_trainingRightActionRoot_3.setCheckState(0, Qt.Unchecked)

        # 感觉运动训练-训练动作3的孩子节点1
        self.sensorimotor_trainingRightAction3Child_1 = QTreeWidgetItem(
            self.sensorimotor_trainingRightActionRoot_3)  # 基本动作训练-训练动作1的孩子节点1
        self.sensorimotor_trainingRightAction3Child_1.setText(0, '皮肤定位觉')  # 第一列Key为 子节点1
        # 设置子节点1开启复选框状态
        self.sensorimotor_trainingRightAction3Child_1.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction3Child_2 = QTreeWidgetItem(
            self.sensorimotor_trainingRightActionRoot_3)  # 基本动作训练-训练动作1的孩子节点1
        self.sensorimotor_trainingRightAction3Child_2.setText(0, '抓木块1')
        self.sensorimotor_trainingRightAction3Child_2.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction3Child_3 = QTreeWidgetItem(
            self.sensorimotor_trainingRightActionRoot_3)  # 基本动作训练-训练动作1的孩子节点1
        self.sensorimotor_trainingRightAction3Child_3.setText(0, '抓木块2')
        self.sensorimotor_trainingRightAction3Child_3.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction3Child_4 = QTreeWidgetItem(
            self.sensorimotor_trainingRightActionRoot_3)  # 基本动作训练-训练动作1的孩子节点1
        self.sensorimotor_trainingRightAction3Child_4.setText(0, '抓木块3')
        self.sensorimotor_trainingRightAction3Child_4.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction3Child_5 = QTreeWidgetItem(
            self.sensorimotor_trainingRightActionRoot_3)  # 基本动作训练-训练动作1的孩子节点1
        self.sensorimotor_trainingRightAction3Child_5.setText(0, '抓木块4')
        self.sensorimotor_trainingRightAction3Child_5.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction3Child_6 = QTreeWidgetItem(
            self.sensorimotor_trainingRightActionRoot_3)  # 基本动作训练-训练动作1的孩子节点1
        self.sensorimotor_trainingRightAction3Child_6.setText(0, '抓球1')
        self.sensorimotor_trainingRightAction3Child_6.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction3Child_7 = QTreeWidgetItem(
            self.sensorimotor_trainingRightActionRoot_3)  # 基本动作训练-训练动作1的孩子节点1
        self.sensorimotor_trainingRightAction3Child_7.setText(0, '抓球2')
        self.sensorimotor_trainingRightAction3Child_7.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction3Child_8 = QTreeWidgetItem(
            self.sensorimotor_trainingRightActionRoot_3)  # 基本动作训练-训练动作1的孩子节点1
        self.sensorimotor_trainingRightAction3Child_8.setText(0, '抓球3')
        self.sensorimotor_trainingRightAction3Child_8.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction3Child_9 = QTreeWidgetItem(
            self.sensorimotor_trainingRightActionRoot_3)  # 基本动作训练-训练动作1的孩子节点1
        self.sensorimotor_trainingRightAction3Child_9.setText(0, '抓球4')
        self.sensorimotor_trainingRightAction3Child_9.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction3Child_10 = QTreeWidgetItem(
            self.sensorimotor_trainingRightActionRoot_3)  # 基本动作训练-训练动作1的孩子节点1
        self.sensorimotor_trainingRightAction3Child_10.setText(0, '抓圆柱1')
        self.sensorimotor_trainingRightAction3Child_10.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction3Child_11 = QTreeWidgetItem(
            self.sensorimotor_trainingRightActionRoot_3)  # 基本动作训练-训练动作1的孩子节点1
        self.sensorimotor_trainingRightAction3Child_11.setText(0, '抓圆柱2')
        self.sensorimotor_trainingRightAction3Child_11.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction3Child_12 = QTreeWidgetItem(
            self.sensorimotor_trainingRightActionRoot_3)  # 基本动作训练-训练动作1的孩子节点1
        self.sensorimotor_trainingRightAction3Child_12.setText(0, '抓圆柱3')
        self.sensorimotor_trainingRightAction3Child_12.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction3Child_13 = QTreeWidgetItem(
            self.sensorimotor_trainingRightActionRoot_3)  # 基本动作训练-训练动作1的孩子节点1
        self.sensorimotor_trainingRightAction3Child_13.setText(0, '抓圆柱4')
        self.sensorimotor_trainingRightAction3Child_13.setCheckState(0, Qt.Unchecked)
        self.sensorimotor_trainingRightAction3Child_14 = QTreeWidgetItem(
            self.sensorimotor_trainingRightActionRoot_3)  # 基本动作训练-训练动作1的孩子节点1
        self.sensorimotor_trainingRightAction3Child_14.setText(0, '抓圆柱5')
        self.sensorimotor_trainingRightAction3Child_14.setCheckState(0, Qt.Unchecked)

        self.sensorimotor_leftCameraLabel = QtWidgets.QLabel(self.page_9)  # 感觉运动训练-左边摄像显示界面
        self.sensorimotor_leftCameraLabel.setGeometry(QtCore.QRect(740, 80, 550, 520))
        self.sensorimotor_leftCameraLabel.setStyleSheet("border-width: 1px;border-style: solid;border-color:black")
        self.sensorimotor_leftCameraLabel.setPixmap(QPixmap("./src/fig/empty_camera.png"))

        self.sensorimotor_rightCameraLabel = QtWidgets.QLabel(self.page_9)  # 感觉运动训练-右边摄像显示界面
        self.sensorimotor_rightCameraLabel.setGeometry(QtCore.QRect(1340, 80, 550, 520))
        self.sensorimotor_rightCameraLabel.setStyleSheet("border-width: 1px;border-style: solid;border-color:black")
        self.sensorimotor_rightCameraLabel.setPixmap(QPixmap("./src/fig/empty_camera.png"))

        self.label_53 = QtWidgets.QLabel(self.page_9)
        self.label_53.setGeometry(QtCore.QRect(745, 30, 120, 40))
        self.label_53.setText("左手")
        self.label_53.setStyleSheet("font:14pt;color:#1E90FF")

        self.sensorimotor_leftMirrrorButton = QtWidgets.QPushButton(self.page_9)  # 感觉运动训练-左手镜像
        self.sensorimotor_leftMirrrorButton.setGeometry(QtCore.QRect(820, 35, 100, 40))
        self.sensorimotor_leftMirrrorButton.setStyleSheet("font:12pt")

        self.sensorimotor_leftCopyButton = QtWidgets.QPushButton(self.page_9)  # 感觉运动训练-左手复制
        self.sensorimotor_leftCopyButton.setGeometry(QtCore.QRect(960, 35, 100, 40))
        self.sensorimotor_leftCopyButton.setStyleSheet("font:12pt")

        self.sensorimotor_leftMaskButton = QtWidgets.QPushButton(self.page_9)  # 感觉运动训练-左手遮罩
        self.sensorimotor_leftMaskButton.setGeometry(QtCore.QRect(1100, 35, 100, 40))
        self.sensorimotor_leftMaskButton.setStyleSheet("font:12pt")

        self.sensorimotor_leftPlayButton = QtWidgets.QPushButton(self.page_9)  # 感觉运动训练-左手播放
        self.sensorimotor_leftPlayButton.setGeometry(QtCore.QRect(745, 620, 120, 40))
        self.sensorimotor_leftPlayButton.setStyleSheet("font:12pt")

        self.sensorimotor_leftStopButton = QtWidgets.QPushButton(self.page_9)  # 感觉运动训练-左手重新开始
        self.sensorimotor_leftStopButton.setGeometry(QtCore.QRect(905, 620, 120, 40))
        self.sensorimotor_leftStopButton.setStyleSheet("font:12pt")

        self.sensorimotor_LeftRecorderButton = QtWidgets.QToolButton(self.page_9)  # 感觉运动训练-左手录制
        self.sensorimotor_LeftRecorderButton.setGeometry(QtCore.QRect(1065, 620, 120, 40))
        self.sensorimotor_LeftRecorderButton.setStyleSheet("font:12pt")

        self.sensorimotor_leftScreenRecording = QAction(self.page_9)  # 感觉运动训练-左手录屏
        self.sensorimotor_leftScreenRecording.setText('录屏')

        self.sensorimotor_leftPopup_menu = QMenu(self.page_9)
        self.sensorimotor_leftPopup_menu.addAction(self.sensorimotor_leftScreenRecording)

        self.sensorimotor_LeftRecorderButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.sensorimotor_LeftRecorderButton.setAutoRaise(True)
        self.sensorimotor_LeftRecorderButton.setMenu(self.sensorimotor_leftPopup_menu)

        self.label_52 = QtWidgets.QLabel(self.page_9)
        self.label_52.setGeometry(QtCore.QRect(1350, 30, 120, 40))
        self.label_52.setText("右手")
        self.label_52.setStyleSheet("font:14pt;color:#1E90FF")

        self.sensorimotor_rightMirrrorButton = QtWidgets.QPushButton(self.page_9)  # 感觉运动训练-右手镜像
        self.sensorimotor_rightMirrrorButton.setGeometry(QtCore.QRect(1420, 35, 100, 40))
        self.sensorimotor_rightMirrrorButton.setStyleSheet("font:12pt")

        self.sensorimotor_rightCopyButton = QtWidgets.QPushButton(self.page_9)  # 感觉运动训练-右手复制
        self.sensorimotor_rightCopyButton.setGeometry(QtCore.QRect(1560, 35, 100, 40))
        self.sensorimotor_rightCopyButton.setStyleSheet("font:12pt")

        self.sensorimotor_rightMaskButton = QtWidgets.QPushButton(self.page_9)  # 感觉运动训练-右手遮罩
        self.sensorimotor_rightMaskButton.setGeometry(QtCore.QRect(1700, 35, 100, 40))
        self.sensorimotor_rightMaskButton.setStyleSheet("font:12pt")

        self.sensorimotor_rightPlayButton = QtWidgets.QPushButton(self.page_9)  # 感觉运动训练-右手播放
        self.sensorimotor_rightPlayButton.setGeometry(QtCore.QRect(1350, 620, 120, 40))
        self.sensorimotor_rightPlayButton.setStyleSheet("font:12pt")

        self.sensorimotor_rightStopButton = QtWidgets.QPushButton(self.page_9)  # 感觉运动训练-右手重新开始
        self.sensorimotor_rightStopButton.setGeometry(QtCore.QRect(1510, 620, 120, 40))
        self.sensorimotor_rightStopButton.setStyleSheet("font:12pt")

        self.sensorimotor_oneDelayButton = QtWidgets.QToolButton(self.page_9)  # 感觉运动训练-延迟镜像
        self.sensorimotor_oneDelayButton.setGeometry(QtCore.QRect(1510, 680, 150, 40))
        self.sensorimotor_oneDelayButton.setText('单侧延迟')
        self.sensorimotor_oneDelayButton.setStyleSheet("font:12pt")

        self.sensorimotor_twoDelayAction = QAction(self.page_9)
        self.sensorimotor_twoDelayAction.setText('双侧延迟')
        self.sensorimotor_oneTwoDelayAction = QAction(self.page_9)
        self.sensorimotor_oneTwoDelayAction.setText('单双侧延迟')

        self.sensorimotor_delayPopup_menu = QMenu(self.page_9)
        self.sensorimotor_delayPopup_menu.addAction(self.sensorimotor_twoDelayAction)
        self.sensorimotor_delayPopup_menu.addAction(self.sensorimotor_oneTwoDelayAction)

        self.sensorimotor_oneDelayButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.sensorimotor_oneDelayButton.setAutoRaise(True)
        self.sensorimotor_oneDelayButton.setMenu(self.sensorimotor_delayPopup_menu)

        self.sensorimotor_rightRecorderButton = QtWidgets.QToolButton(self.page_9)  # 感觉运动训练-右手录制
        self.sensorimotor_rightRecorderButton.setGeometry(QtCore.QRect(1670, 620, 120, 40))
        self.sensorimotor_rightRecorderButton.setStyleSheet("font:12pt")

        self.sensorimotor_rightScreenRecording = QAction(self.page_9)  # 感觉运动训练-右手录屏
        self.sensorimotor_rightScreenRecording.setText('录屏')

        self.sensorimotor_rightPopup_menu = QMenu(self.page_9)
        self.sensorimotor_rightPopup_menu.addAction(self.sensorimotor_rightScreenRecording)

        self.sensorimotor_rightRecorderButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.sensorimotor_rightRecorderButton.setAutoRaise(True)
        self.sensorimotor_rightRecorderButton.setMenu(self.sensorimotor_rightPopup_menu)

        self.sensorimotor_cancelButton = QtWidgets.QPushButton(self.page_9)  # 感觉运动训练-全部取消
        self.sensorimotor_cancelButton.setGeometry(QtCore.QRect(10, 620, 120, 40))
        self.sensorimotor_cancelButton.setStyleSheet("font:12pt")

        self.sensorimotor_selectAllButton = QtWidgets.QPushButton(self.page_9)  # 感觉运动训练-全选
        self.sensorimotor_selectAllButton.setGeometry(QtCore.QRect(140, 620, 120, 40))
        self.sensorimotor_selectAllButton.setStyleSheet("font:12pt")

        self.label_50 = QtWidgets.QLabel(self.page_9)
        self.label_50.setGeometry(QtCore.QRect(270, 620, 120, 40))
        self.label_50.setText('模式')
        self.label_50.setStyleSheet("font:12pt")

        self.sensorimotor_trainingModeComboBox = QtWidgets.QComboBox(self.page_9)  # 感觉运动训练-获取训练模式
        self.sensorimotor_trainingModeComboBox.setGeometry(QtCore.QRect(330, 620, 150, 40))
        self.sensorimotor_trainingModeComboBox.addItems(['', '单侧训练', '双侧训练', '单双侧训练'])
        self.sensorimotor_trainingModeComboBox.setStyleSheet("font:12pt")

        self.label_60 = QtWidgets.QLabel(self.page_9)
        self.label_60.setGeometry(QtCore.QRect(500, 620, 120, 40))
        self.label_60.setStyleSheet("font:12pt")

        self.sensorimotor_trainingWayComboBox = QtWidgets.QComboBox(self.page_9)  # 感觉运动训练-获取训练方式
        self.sensorimotor_trainingWayComboBox.setGeometry(QtCore.QRect(570, 620, 120, 40))
        self.sensorimotor_trainingWayComboBox.addItems(['', 'AABB', 'ABAB'])
        self.sensorimotor_trainingWayComboBox.setStyleSheet("font:12pt")

        self.label_32 = QtWidgets.QLabel(self.page_9)
        self.label_32.setGeometry(QtCore.QRect(10, 680, 120, 40))
        self.label_32.setText('组数')
        self.label_32.setStyleSheet("font:12pt")

        self.sensorimotor_trainingGroupNumLineEdit = QtWidgets.QLineEdit(self.page_9)  # 感觉运动训练-获取训练组数
        self.sensorimotor_trainingGroupNumLineEdit.setGeometry(QtCore.QRect(70, 680, 120, 40))
        self.sensorimotor_trainingGroupNumLineEdit.setStyleSheet("font:12pt")

        self.label_59 = QtWidgets.QLabel(self.page_9)
        self.label_59.setGeometry(QtCore.QRect(200, 680, 120, 40))
        self.label_59.setStyleSheet("font:12pt")

        self.sensorimotor_trainingNumLineEdit = QtWidgets.QLineEdit(self.page_9)  # 感觉运动训练-获取每组动作训练次数
        self.sensorimotor_trainingNumLineEdit.setGeometry(QtCore.QRect(300, 680, 120, 40))
        self.sensorimotor_trainingNumLineEdit.setStyleSheet("font:12pt")

        self.label_58 = QtWidgets.QLabel(self.page_9)  # 播放次数
        self.label_58.setGeometry(QtCore.QRect(430, 680, 120, 40))
        self.label_58.setStyleSheet("font:12pt")

        self.sensorimotor_playNumLineEdit = QtWidgets.QLineEdit(self.page_9)  # 感觉运动训练-获取每组视频播放次数
        self.sensorimotor_playNumLineEdit.setGeometry(QtCore.QRect(530, 680, 120, 40))
        self.sensorimotor_playNumLineEdit.setStyleSheet("font:12pt")

        self.label_39 = QtWidgets.QLabel(self.page_9)  # 播放次数
        self.label_39.setGeometry(QtCore.QRect(660, 680, 120, 40))
        self.label_39.setText('播放速率')
        self.label_39.setStyleSheet("font:12pt")

        self.sensorimotor_playSppedComBox = QtWidgets.QComboBox(self.page_9)  # 感觉运动训练-播放速率
        self.sensorimotor_playSppedComBox.setGeometry(QtCore.QRect(760, 680, 120, 40))
        self.sensorimotor_playSppedComBox.addItems(['', '0.5', '1', '1.25', '1.5', '2'])
        self.sensorimotor_playSppedComBox.setStyleSheet("font:12pt")

        self.sensorimotor_setOneDelayPlayVideoFrame = QtWidgets.QFrame(self.page_9)  # 设置单侧延时镜像视频播放次数容器
        self.sensorimotor_setOneDelayPlayVideoFrame.setGeometry(QtCore.QRect(890, 680, 270, 40))
        self.sensorimotor_setOneDelayPlayVideoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sensorimotor_setOneDelayPlayVideoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sensorimotor_setOneDelayPlayVideoFrame.setVisible(False)

        self.label_34 = QtWidgets.QLabel(self.sensorimotor_setOneDelayPlayVideoFrame)  # 播放次数
        self.label_34.setGeometry(QtCore.QRect(0, 0, 200, 40))
        self.label_34.setText('延迟播放次数')
        self.label_34.setStyleSheet("font:12pt")

        self.sensorimotor_oneDelayPlayNumLineEdit = QtWidgets.QLineEdit(
            self.sensorimotor_setOneDelayPlayVideoFrame)  # 感觉运动训练-单侧延迟播放次数
        self.sensorimotor_oneDelayPlayNumLineEdit.setGeometry(QtCore.QRect(150, 0, 120, 40))
        self.sensorimotor_oneDelayPlayNumLineEdit.setStyleSheet("font:12pt")

        self.sensorimotor_setTwoDelayPlayVideoFrame = QtWidgets.QFrame(self.page_9)  # 设置双侧延时镜像视频播放次数容器
        self.sensorimotor_setTwoDelayPlayVideoFrame.setGeometry(QtCore.QRect(890, 680, 270, 40))
        self.sensorimotor_setTwoDelayPlayVideoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sensorimotor_setTwoDelayPlayVideoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sensorimotor_setTwoDelayPlayVideoFrame.setVisible(False)

        self.label_35 = QtWidgets.QLabel(self.sensorimotor_setTwoDelayPlayVideoFrame)
        self.label_35.setGeometry(QtCore.QRect(0, 0, 200, 40))
        self.label_35.setText('延迟播放次数')
        self.label_35.setStyleSheet("font:12pt")

        self.sensorimotor_twoDelayPlayNumLineEdit = QtWidgets.QLineEdit(
            self.sensorimotor_setTwoDelayPlayVideoFrame)  # 感觉运动训练-双侧延迟播放次数
        self.sensorimotor_twoDelayPlayNumLineEdit.setGeometry(QtCore.QRect(150, 0, 120, 40))
        self.sensorimotor_twoDelayPlayNumLineEdit.setStyleSheet("font:12pt")

        self.sensorimotor_setOneTwoDelayPlayVideoFrame = QtWidgets.QFrame(self.page_9)  # 设置单双侧延时镜像视频播放次数容器
        self.sensorimotor_setOneTwoDelayPlayVideoFrame.setGeometry(QtCore.QRect(890, 680, 400, 40))
        self.sensorimotor_setOneTwoDelayPlayVideoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sensorimotor_setOneTwoDelayPlayVideoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sensorimotor_setOneTwoDelayPlayVideoFrame.setVisible(False)

        self.label_35 = QtWidgets.QLabel(self.sensorimotor_setOneTwoDelayPlayVideoFrame)
        self.label_35.setGeometry(QtCore.QRect(0, 0, 200, 40))
        self.label_35.setText('延迟播放次数')
        self.label_35.setStyleSheet("font:12pt")

        self.sensorimotor_OneTwoDelayPlayNumLineEdit_1 = QtWidgets.QLineEdit(
            self.sensorimotor_setOneTwoDelayPlayVideoFrame)  # 感觉运动训练-单双侧-单侧延迟播放次数
        self.sensorimotor_OneTwoDelayPlayNumLineEdit_1.setGeometry(QtCore.QRect(150, 0, 120, 40))
        self.sensorimotor_OneTwoDelayPlayNumLineEdit_1.setStyleSheet("font:12pt")

        self.sensorimotor_OneTwoDelayPlayNumLineEdit_2 = QtWidgets.QLineEdit(
            self.sensorimotor_setOneTwoDelayPlayVideoFrame)  # 感觉运动训练-单双侧-双侧延迟播放次数
        self.sensorimotor_OneTwoDelayPlayNumLineEdit_2.setGeometry(QtCore.QRect(280, 0, 120, 40))
        self.sensorimotor_OneTwoDelayPlayNumLineEdit_2.setStyleSheet("font:12pt")

        self.sensorimotor_recommendButton = QtWidgets.QPushButton(self.page_9)  # 感觉运动训练-获取该病人预先设置好的训练方案
        self.sensorimotor_recommendButton.setGeometry(QtCore.QRect(10, 730, 120, 40))
        self.sensorimotor_recommendButton.setStyleSheet("font:12pt")

        self.sensorimotor_startButton = QtWidgets.QPushButton(self.page_9)  # 感觉运动训练-开始训练
        self.sensorimotor_startButton.setGeometry(QtCore.QRect(140, 730, 120, 40))
        self.sensorimotor_startButton.setStyleSheet("font:12pt")

        self.sensorimotor_historyRecordButton = QtWidgets.QPushButton(self.page_9)  # 功能动作训练——显示视频历史记录
        self.sensorimotor_historyRecordButton.setGeometry(QtCore.QRect(270, 730, 120, 40))
        self.sensorimotor_historyRecordButton.setText('历史记录')
        self.sensorimotor_historyRecordButton.setStyleSheet("font:12pt")

        self.label_33 = QtWidgets.QLabel(self.page_9)
        self.label_33.setGeometry(QtCore.QRect(400, 730, 120, 40))
        self.label_33.setText("训练时长:")
        self.label_33.setStyleSheet("font:12pt")

        self.sensorimotor_timeEdit = QTimeEdit(self.page_9)  # 功能训练-时间计时器
        self.sensorimotor_timeEdit.setDisplayFormat('HH:mm:ss')
        self.sensorimotor_timeEdit.setGeometry(QtCore.QRect(520, 730, 120, 40))

        self.sensorimotor_traingSituationFrame = QtWidgets.QFrame(self.page_9)  # 感觉运动训练情况显示窗口
        self.sensorimotor_traingSituationFrame.setGeometry(QtCore.QRect(10, 10, 700, 710))
        self.sensorimotor_traingSituationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sensorimotor_traingSituationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sensorimotor_traingSituationFrame.setVisible(False)

        self.label_104 = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.label_104.setGeometry(QtCore.QRect(20, 10, 120, 40))
        self.label_104.setStyleSheet("font:14pt;color:#1E90FF")

        self.label_105 = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.label_105.setGeometry(QtCore.QRect(20, 60, 200, 40))
        self.label_105.setStyleSheet("font:10pt")

        # 感觉运动训练训练情况-获取训练模式
        self.sensorimotor_trainingModeLabel1 = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.sensorimotor_trainingModeLabel1.setGeometry(QtCore.QRect(140, 60, 200, 40))
        self.sensorimotor_trainingModeLabel1.setStyleSheet("font:10pt")

        self.sensorimotor_trainingModeLabel2 = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.sensorimotor_trainingModeLabel2.setGeometry(QtCore.QRect(240, 60, 200, 40))
        self.sensorimotor_trainingModeLabel2.setStyleSheet("font:10pt")

        self.label_106 = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.label_106.setGeometry(QtCore.QRect(300, 60, 200, 40))
        self.label_106.setStyleSheet("font:10pt")

        # 感觉运动训练训练情况-获取组数
        self.sensorimotor_trianingGroupsLabel = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.sensorimotor_trianingGroupsLabel.setGeometry(QtCore.QRect(430, 60, 200, 40))
        self.sensorimotor_trianingGroupsLabel.setStyleSheet("font:10pt")

        self.label_107 = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.label_107.setGeometry(QtCore.QRect(460, 60, 200, 40))
        self.label_107.setStyleSheet("font:10pt")

        # 感觉运动训练训练情况-获取训练动作个数
        self.sensorimotor_triangNumLabel = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.sensorimotor_triangNumLabel.setGeometry(QtCore.QRect(560, 60, 200, 40))
        self.sensorimotor_triangNumLabel.setStyleSheet("font:10pt")

        self.label_108 = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.label_108.setGeometry(QtCore.QRect(580, 60, 200, 40))
        self.label_108.setStyleSheet("font:10pt")

        self.label_36 = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.label_36.setGeometry(QtCore.QRect(40, 100, 220, 40))
        self.label_36.setText("总共(组):")
        self.label_36.setStyleSheet("font:10pt")

        # 感觉运动训练训练情况获取训练动作组数
        self.sensorimotor_trainingTotalNumLabel = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.sensorimotor_trainingTotalNumLabel.setGeometry(QtCore.QRect(150, 100, 220, 40))
        self.sensorimotor_trainingTotalNumLabel.setText("--")
        self.sensorimotor_trainingTotalNumLabel.setStyleSheet("font:10pt")

        self.label_37 = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.label_37.setGeometry(QtCore.QRect(200, 100, 250, 40))
        self.label_37.setText("当前(组):")
        self.label_37.setStyleSheet("font:10pt")

        # 感觉运动训练训练情况-获取当前训练动作组数
        self.sensorimotor_trainingCurrentNumLabel = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.sensorimotor_trainingCurrentNumLabel.setGeometry(QtCore.QRect(300, 100, 220, 40))
        self.sensorimotor_trainingCurrentNumLabel.setText("--")
        self.sensorimotor_trainingCurrentNumLabel.setStyleSheet("font:10pt")

        self.label_38 = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.label_38.setGeometry(QtCore.QRect(350, 100, 220, 40))
        self.label_38.setText("剩余(组):")
        self.label_38.setStyleSheet("font:10pt")

        # 感觉运动训练训练情况--获取剩余训练动作组数
        self.sensorimotor_trainingRemainNumLabel = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.sensorimotor_trainingRemainNumLabel.setGeometry(QtCore.QRect(450, 100, 220, 40))
        self.sensorimotor_trainingRemainNumLabel.setText("--")
        self.sensorimotor_trainingRemainNumLabel.setStyleSheet("font:10pt")

        self.label_109 = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.label_109.setGeometry(QtCore.QRect(20, 140, 250, 40))
        self.label_109.setStyleSheet("font:10pt")

        # 感觉运动训练训练情况-获取训练动作名称
        self.sensorimotor_trainingNameLabel = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.sensorimotor_trainingNameLabel.setGeometry(QtCore.QRect(210, 140, 500, 40))
        self.sensorimotor_trainingNameLabel.setStyleSheet("font:10pt")

        self.label_110 = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.label_110.setGeometry(QtCore.QRect(20, 180, 200, 40))
        self.label_110.setStyleSheet("font:10pt")

        self.label_111 = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.label_111.setGeometry(QtCore.QRect(40, 220, 200, 40))
        self.label_111.setStyleSheet("font:10pt")

        # 感觉运动训练训练情况-获取训练总次数
        self.sensorimotor_trianingTotalNumPlayVideoLabel = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.sensorimotor_trianingTotalNumPlayVideoLabel.setGeometry(QtCore.QRect(160, 220, 200, 40))
        self.sensorimotor_trianingTotalNumPlayVideoLabel.setStyleSheet("font:10pt")

        self.label_112 = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.label_112.setGeometry(QtCore.QRect(200, 220, 200, 40))
        self.label_112.setStyleSheet("font:10pt")

        # 感觉运动训练训练情况-获取跟视频训练当前次数
        self.sensorimotor_currentPlayVideoLabel = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.sensorimotor_currentPlayVideoLabel.setGeometry(QtCore.QRect(320, 220, 200, 40))
        self.sensorimotor_currentPlayVideoLabel.setStyleSheet("font:10pt")

        self.label_113 = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.label_113.setGeometry(QtCore.QRect(370, 220, 200, 40))
        self.label_113.setStyleSheet("font:10pt")

        # 感觉运动训练训练情况-获取跟视频训练剩余次数
        self.sensorimotor_remainingPlayVideoLabel = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.sensorimotor_remainingPlayVideoLabel.setGeometry(QtCore.QRect(480, 220, 200, 40))
        self.sensorimotor_remainingPlayVideoLabel.setStyleSheet("font:10pt")

        self.label_114 = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.label_114.setGeometry(QtCore.QRect(20, 260, 200, 40))
        self.label_114.setStyleSheet("font:10pt")

        self.label_115 = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.label_115.setGeometry(QtCore.QRect(40, 300, 200, 40))
        self.label_115.setStyleSheet("font:10pt")

        # 感觉运动训练训练情况-获取自行训练总次数
        self.sensorimotor_autonomousTrianingTotalNumLabel = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.sensorimotor_autonomousTrianingTotalNumLabel.setGeometry(QtCore.QRect(160, 300, 200, 40))
        self.sensorimotor_autonomousTrianingTotalNumLabel.setStyleSheet("font:10pt")

        self.label_116 = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.label_116.setGeometry(QtCore.QRect(200, 300, 200, 40))
        self.label_116.setStyleSheet("font:10pt")

        # 感觉运动训练训练情况-获取自行训练当前次数
        self.sensorimotor_autonomousCurrentLabel = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.sensorimotor_autonomousCurrentLabel.setGeometry(QtCore.QRect(320, 300, 200, 40))
        self.sensorimotor_autonomousCurrentLabel.setStyleSheet("font:10pt")

        self.label_117 = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.label_117.setGeometry(QtCore.QRect(370, 300, 200, 40))
        self.label_117.setStyleSheet("font:10pt")

        # 感觉运动训练训练情况-获取自行训练剩余次数
        self.sensorimotor_autonomousRemainingLabel = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.sensorimotor_autonomousRemainingLabel.setGeometry(QtCore.QRect(480, 300, 200, 40))
        self.sensorimotor_autonomousRemainingLabel.setStyleSheet("font:10pt")

        # 感觉运动训练训练情况-显示当前播放的视频
        self.sensorimotor_showVideoLabel = QtWidgets.QLabel(self.sensorimotor_traingSituationFrame)
        self.sensorimotor_showVideoLabel.setGeometry(QtCore.QRect(10, 340, 680, 350))
        self.sensorimotor_showVideoLabel.setStyleSheet("border-width: 1px;border-style: solid;border-color:black")

        self.sensorimotor_isPlaying = True

        self.stackedWidget.addWidget(self.page)  # 空间想象
        self.stackedWidget.addWidget(self.page_9)  # 感觉运动
        self.stackedWidget.addWidget(self.page_2)  # 基本动作
        self.stackedWidget.addWidget(self.page_3)  # 功能动作
        self.stackedWidget.addWidget(self.page_4)  # 镜像

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)  # 默认显示空间想象训练页面
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "智能多模态镜像评估与训练系统"))
        self.resetPasswordLabel.setText(_translate("Form", "密码修改"))
        self.exitSystemLabel.setText(_translate("Form", "系统退出"))
        self.label_2.setText(_translate("Form", "姓名"))
        self.nameLabel.setText(_translate("Form", "TextLabel"))
        self.label_3.setText(_translate("Form", "年龄"))
        self.ageLabel.setText(_translate("Form", "TextLabel"))
        self.label_4.setText(_translate("Form", "性别"))
        self.sexLabel.setText(_translate("Form", "TextLabel"))
        self.label_5.setText(_translate("Form", "患手"))
        self.unhealthHandlabel.setText(_translate("Form", "TextLabel"))
        self.label_6.setText(_translate("Form", "疾病类型"))
        self.diseaseTypeLabel_1.setText(_translate("Form", "TextLabel"))
        self.diseaseTypeLabel_2.setText(_translate("Form", "TextLabel"))
        self.spaceImaginationButton.setText(_translate("Form", "空间想象训练"))
        self.basicButton.setText(_translate("Form", "基本动作训练"))
        self.functionButton.setText(_translate("Form", "功能动作训练"))
        self.mirrorButton.setText(_translate("Form", "自主镜像训练"))
        self.sensorimotorButton.setText(_translate("Form", "感觉运动观察训练"))
        self.label_11.setText(_translate("Form", "训练情况"))
        self.label_12.setText(_translate("Form", "总共（张）："))
        self.spaceImageTrainingPictureTotalNumber.setText(_translate("Form", "--"))
        self.label_13.setText(_translate("Form", "当前（张）"))
        self.currentPictureNumLabel.setText(_translate("Form", "--"))
        self.label_14.setText(_translate("Form", "剩余（张）："))
        self.remainPictureNumLabel.setText(_translate("Form", "--"))
        self.label_15.setText(_translate("Form", "正确（张）："))
        self.correctNumLabel.setText(_translate("Form", "--"))
        self.label_16.setText(_translate("Form", "左手正确（张）："))
        self.leftCorrectNumLabel.setText(_translate("Form", "--"))
        self.label_17.setText(_translate("Form", "右手正确（张）："))
        self.rightCorrectNumLabel.setText(_translate("Form", "--"))
        self.label_18.setText(_translate("Form", "正确率（%）："))
        self.correctRateLabel.setText(_translate("Form", "--"))
        self.label_19.setText(_translate("Form", "左手正确率（%）："))
        self.leftCorrectRateLabel.setText(_translate("Form", "--"))
        self.label_20.setText(_translate("Form", "右手正确率（%）："))
        self.rightCorrectRateLabel.setText(_translate("Form", "--"))
        self.label_21.setText(_translate("Form", "平均用时（秒）： "))
        self.averageTimeLabel.setText(_translate("Form", "--"))
        self.label_22.setText(_translate("Form", "左手平均（秒）："))
        self.leftAverageTimeLabel.setText(_translate("Form", "--"))
        self.label_23.setText(_translate("Form", "右手平均（秒）："))
        self.rightAverageTimeLabel.setText(_translate("Form", "--"))
        self.label_118.setText(_translate("Form", "训练时长："))
        self.trainingTimeLabel.setText(_translate("Form", "--"))
        self.label_7.setText(_translate("Form", "训练参数设置"))
        self.trainProgramLabel.setText(_translate("Form", "训练方案"))
        self.label_8.setText(_translate("Form", "图片总数（张）："))
        self.label_9.setText(_translate("Form", "播放速率（秒）："))
        self.label_10.setText(_translate("Form", "辨别难度："))
        self.space_startButton.setText(_translate("Form", "开始训练"))
        self.stopButton.setText(_translate("Form", "停止训练"))
        self.basic_leftMirrrorButton.setText(_translate("Form", "镜像"))
        self.basic_leftCopyButton.setText(_translate("Form", "复制"))
        self.basic_leftMaskButton.setText(_translate("Form", "遮罩"))
        self.basic_leftPlayButton.setText(_translate("Form", "播放"))
        self.basic_leftStopButton.setText(_translate("Form", "重新开始"))
        self.basic_LeftRecoderButton.setText(_translate("Form", "录制"))
        self.basic_rightMirrrorButton.setText(_translate("Form", "镜像"))
        self.basic_rightCopyButton.setText(_translate("Form", "复制"))
        self.basic_rightMaskButton.setText(_translate("Form", "遮罩"))
        self.basic_rightStopButton.setText(_translate("Form", "重新开始"))
        self.basic_rightPlayButton.setText(_translate("Form", "播放"))
        self.basic_rightRecoderButton.setText(_translate("Form", "录制"))
        self.basic_cancelButton.setText(_translate("Form", "全部取消"))
        self.label_24.setText(_translate("Form", "组数"))
        self.label_25.setText(_translate("Form", "方式"))
        self.label_26.setText(_translate("Form", "训练次数"))
        self.label_27.setText(_translate("Form", "播放次数"))
        self.basic_selectAllButton.setText(_translate("Form", "全部"))
        self.basic_recommendButton.setText(_translate("Form", "推荐"))
        self.basic_startButton.setText(_translate("Form", "开始训练"))
        self.label_61.setText(_translate("Form", "训练情况"))
        self.label_62.setText(_translate("Form", "本次训练使用"))
        self.basic_trainingModeLabel.setText(_translate("Form", "----"))
        self.label_63.setText(_translate("Form", "模式，共训练"))
        self.basic_trianingGroupsLabel.setText(_translate("Form", "--"))
        self.label_65.setText(_translate("Form", "组，（包含"))
        self.basic_triangNumLabel.setText(_translate("Form", "--"))
        self.label_66.setText(_translate("Form", "个训练动作）"))
        self.label_64.setText(_translate("Form", "当前训练动作名称："))
        self.basic_trainingNameLabel.setText(_translate("Form", "--"))
        self.label_67.setText(_translate("Form", "跟图训练"))
        self.label_68.setText(_translate("Form", "总共（次）："))
        self.basic_trianingTotalNumPlayVideoLabel.setText(_translate("Form", "--"))
        self.label_69.setText(_translate("Form", "当前（次）："))
        self.basic_currentPlayVideoLabel.setText(_translate("Form", "--"))
        self.label_70.setText(_translate("Form", "剩余（次）："))
        self.basic_remainingPlayVideoLabel.setText(_translate("Form", "--"))
        self.label_71.setText(_translate("Form", "自行训练"))
        self.label_72.setText(_translate("Form", "总共（次）："))
        self.basic_autonomousTrianingTotalNumLabel.setText(_translate("Form", "--"))
        self.label_73.setText(_translate("Form", "当前（次）："))
        self.basic_autonomousCurrentLabel.setText(_translate("Form", "--"))
        self.label_74.setText(_translate("Form", "剩余（次）："))
        self.basic_autonomousRemainingLabel.setText(_translate("Form", "--"))
        self.function_rightMirrrorButton.setText(_translate("Form", "镜像"))
        self.function_selectAllButton.setText(_translate("Form", "全部"))
        self.function_startButton.setText(_translate("Form", "开始训练"))
        self.function_rightMaskButton.setText(_translate("Form", "遮罩"))
        self.label_28.setText(_translate("Form", "方式"))
        self.label_29.setText(_translate("Form", "组数"))
        self.function_rightStopButton.setText(_translate("Form", "重新开始"))
        self.function_leftPlayButton.setText(_translate("Form", "播放"))
        self.label_30.setText(_translate("Form", "训练次数"))
        self.function_rightRecoderButton.setText(_translate("Form", "录制"))
        self.function_LeftRecoderButton.setText(_translate("Form", "录制"))
        self.label_31.setText(_translate("Form", "播放次数"))
        self.function_leftMaskButton.setText(_translate("Form", "遮罩"))
        self.function_rightPlayButton.setText(_translate("Form", "播放"))
        self.function_leftCopyButton.setText(_translate("Form", "复制"))
        self.function_rightCopyButton.setText(_translate("Form", "复制"))
        self.function_leftStopButton.setText(_translate("Form", "重新开始"))
        self.function_leftMirrrorButton.setText(_translate("Form", "镜像"))
        self.function_cancelButton.setText(_translate("Form", "全部取消"))
        self.function_recommendButton.setText(_translate("Form", "推荐"))
        self.label_75.setText(_translate("Form", "训练情况"))
        self.label_76.setText(_translate("Form", "本次训练使用"))
        self.function_trainingModeLabel.setText(_translate("Form", "--"))
        self.label_77.setText(_translate("Form", "模式，共训练"))
        self.function_trianingGroupsLabel.setText(_translate("Form", "--"))
        self.label_78.setText(_translate("Form", "组，（包含"))
        self.function_triangNumLabel.setText(_translate("Form", "--"))
        self.label_79.setText(_translate("Form", "个训练动作）"))
        self.label_80.setText(_translate("Form", "当前训练动作名称："))
        self.function_trainingNameLabel.setText(_translate("Form", "--"))
        self.label_81.setText(_translate("Form", "跟图训练"))
        self.label_82.setText(_translate("Form", "总共（次）："))
        self.function_trianingTotalNumPlayVideoLabel.setText(_translate("Form", "--"))
        self.label_83.setText(_translate("Form", "当前（次）："))
        self.function_currentPlayVideoLabel.setText(_translate("Form", "--"))
        self.label_84.setText(_translate("Form", "剩余（次）："))
        self.function_remainingPlayVideoLabel.setText(_translate("Form", "--"))
        self.label_85.setText(_translate("Form", "自行训练"))
        self.label_86.setText(_translate("Form", "总共（次）："))
        self.function_autonomousTrianingTotalNumLabel.setText(_translate("Form", "--"))
        self.label_87.setText(_translate("Form", "当前（次）："))
        self.function_autonomousCurrentLabel.setText(_translate("Form", "--"))
        self.label_88.setText(_translate("Form", "剩余（次）："))
        self.function_autonomousRemainingLabel.setText(_translate("Form", "--"))
        self.mirror_leftMirrorButton.setText(_translate("Form", "镜像"))
        self.mirror_leftCopyButton.setText(_translate("Form", "复制"))
        self.mirror_leftMaskButton.setText(_translate("Form", "遮罩"))
        self.mirror_leftPlayButton.setText(_translate("Form", "播放"))
        self.mirror_leftRecoderButton.setText(_translate("Form", "录制"))
        self.mirror_rightMirrorButton.setText(_translate("Form", "镜像"))
        self.mirror_rightPlayButton.setText(_translate("Form", "播放"))
        self.mirror_rightRecoderButton.setText(_translate("Form", "录制"))
        self.mirror_rightMaskButton.setText(_translate("Form", "遮罩"))
        self.mirror_rightCopyButton.setText(_translate("Form", "复制"))
        self.label_57.setText(_translate("Form", "组数"))
        self.sensorimotor_leftStopButton.setText(_translate("Form", "重新开始"))
        self.sensorimotor_rightPlayButton.setText(_translate("Form", "播放"))
        self.label_58.setText(_translate("Form", "播放次数"))
        self.sensorimotor_leftPlayButton.setText(_translate("Form", "播放"))
        self.sensorimotor_cancelButton.setText(_translate("Form", "全部取消"))
        self.label_59.setText(_translate("Form", "训练次数"))
        self.label_60.setText(_translate("Form", "方式"))
        self.sensorimotor_rightCopyButton.setText(_translate("Form", "复制"))
        self.sensorimotor_rightStopButton.setText(_translate("Form", "重新开始"))
        self.sensorimotor_rightMirrrorButton.setText(_translate("Form", "镜像"))
        self.sensorimotor_LeftRecorderButton.setText(_translate("Form", "录制"))
        self.sensorimotor_startButton.setText(_translate("Form", "开始训练"))
        self.sensorimotor_rightRecorderButton.setText(_translate("Form", "录制"))
        self.sensorimotor_recommendButton.setText(_translate("Form", "推荐"))
        self.sensorimotor_leftMirrrorButton.setText(_translate("Form", "镜像"))
        self.sensorimotor_leftCopyButton.setText(_translate("Form", "复制"))
        self.sensorimotor_leftMaskButton.setText(_translate("Form", "遮罩"))
        self.sensorimotor_selectAllButton.setText(_translate("Form", "全部"))
        self.sensorimotor_rightMaskButton.setText(_translate("Form", "遮罩"))
        self.label_104.setText(_translate("Form", "训练情况"))
        self.label_105.setText(_translate("Form", "本次训练使用"))
        self.sensorimotor_trainingModeLabel1.setText(_translate("Form", "--"))
        self.sensorimotor_trainingModeLabel2.setText(_translate("Form", "--"))
        self.label_106.setText(_translate("Form", "模式，共训练"))
        self.sensorimotor_trianingGroupsLabel.setText(_translate("Form", "--"))
        self.label_107.setText(_translate("Form", "组，（包含"))
        self.sensorimotor_triangNumLabel.setText(_translate("Form", "--"))
        self.label_108.setText(_translate("Form", "个训练动作）"))
        self.label_109.setText(_translate("Form", "当前训练动作名称："))
        self.sensorimotor_trainingNameLabel.setText(_translate("Form", "--"))
        self.label_110.setText(_translate("Form", "跟图训练"))
        self.label_111.setText(_translate("Form", "总共（次）："))
        self.sensorimotor_trianingTotalNumPlayVideoLabel.setText(_translate("Form", "--"))
        self.label_112.setText(_translate("Form", "当前（次）："))
        self.sensorimotor_currentPlayVideoLabel.setText(_translate("Form", "--"))
        self.label_113.setText(_translate("Form", "剩余（次）："))
        self.sensorimotor_remainingPlayVideoLabel.setText(_translate("Form", "--"))
        self.label_114.setText(_translate("Form", "自行训练"))
        self.label_115.setText(_translate("Form", "总共（次）："))
        self.sensorimotor_autonomousTrianingTotalNumLabel.setText(_translate("Form", "--"))
        self.label_116.setText(_translate("Form", "当前（次）："))
        self.sensorimotor_autonomousCurrentLabel.setText(_translate("Form", "--"))
        self.label_117.setText(_translate("Form", "剩余（次）："))
        self.sensorimotor_autonomousRemainingLabel.setText(_translate("Form", "--"))
        self.sensorimotor_showVideoLabel.setText(_translate("Form", "TextLabel"))
        self.patientinformationButton.setText(_translate("Form", "病人信息"))
        self.trainButton.setText(_translate("Form", "训练"))
        self.gameButton.setText(_translate("Form", "游戏"))
        self.setSystemButton.setText(_translate("Form", "系统设置"))


class trianging(QtWidgets.QMainWindow, Ui_Form):
    # singal = pyqtSignal(list)
    def __init__(self, patient_id):
        self.patient_id = patient_id
        super(trianging, self).__init__()
        self.setupUi(self)

        self.patientInfo = \
            json.loads(requests.post(config.patientGetById, data={'id': self.patient_id}).content.decode('utf-8'))[
                'data']

        self.nameLabel.setText(self.patientInfo['name'])
        self.ageLabel.setText(str(self.patientInfo['age']))
        self.sexLabel.setText(self.patientInfo['sex'])
        self.unhealthHandlabel.setText(self.patientInfo['illness'])
        self.diseaseTypeLabel_1.setText(self.patientInfo['primary_etiology'])
        self.diseaseTypeLabel_2.setText(self.patientInfo['secondary_etiology'])
        self.emptyCamera = QPixmap(config.GlobalPath + "src/fig/empty_camera.png")

        self.illness = self.patientInfo['illness']

        if self.illness == '左':
            self.function_leftTree.show()
            self.basic_leftTree.show()
            self.sensorimotor_leftTree.show()

            self.function_rightTree.hide()
            self.basic_rightTree.hide()
            self.sensorimotor_rightTree.hide()

        else:
            self.function_leftTree.hide()
            self.basic_leftTree.hide()
            self.sensorimotor_leftTree.hide()

            self.function_rightTree.show()
            self.basic_rightTree.show()
            self.sensorimotor_rightTree.show()

        self.functionDictionary = {'PinchClipSideways_right': '侧捏夹子_右', '侧捏夹子_右': 'PinchClipSideways_right',
                                   'PinchClipSideways_left': '侧捏夹子_左', '侧捏夹子_左': 'PinchClipSideways_left',
                                   'FlipPagesBook_right': '对指翻书页_右', '对指翻书页_右': 'FlipPagesBook_right',
                                   'FlipPagesBook_left': '对指翻书页_左', '对指翻书页_左': 'FlipPagesBook_left',
                                   'PinchClampFingers_right': '对指捏夹子_右',
                                   '对指捏夹子_右': 'PinchClampFingers_right',
                                   'PinchClampFingers_left': '对指捏夹子_左', '对指捏夹子_左': 'PinchClampFingers_left',
                                   'FlipCcards_right': '翻卡片_右', '翻卡片_右': 'FlipCcards_right',
                                   'FlipCcards_left': '翻卡片_左', '翻卡片_左': 'FlipCcards_left',
                                   'FlipPlanks_right': '翻木板_右', '翻木板_右': 'FlipPlanks_right',
                                   'FlipPlanks_left': '翻木板_左', '翻木板_左': 'FlipPlanks_left',
                                   'TurnThroughCalendar_right': '翻日历_右', '翻日历_右': 'TurnThroughCalendar_right',
                                   'TurnThroughCalendar_left': '翻日历_左', '翻日历_左': 'TurnThroughCalendar_left',
                                   'TurnPages_right': '翻书页_右', '翻书页_右': 'TurnPages_right',
                                   'TurnPages_left': '翻书页_左', '翻书页_左': 'TurnPages_left',
                                   'WoodenStickGrip_right': '木棒抓握_右', '木棒抓握_右': 'WoodenStickGrip_right',
                                   'WoodenStickGrip_left': '木棒抓握_左', '木棒抓握_左': 'WoodenStickGrip_left',
                                   'TakeGlass_right': '拿玻璃杯_右', '拿玻璃杯_右': 'TakeGlass_right',
                                   'TakeGlass_left': '拿玻璃杯_左', '拿玻璃杯_左': 'TakeGlass_left',
                                   'TakeGlassBall_right': '拿玻璃球_右', '拿玻璃球_右': 'TakeGlassBall_right',
                                   'TakeGlassBall_left': '拿玻璃球__左', '拿玻璃球__左': 'TakeGlassBall_left',
                                   'TakePaperClip_right': '拿回形针_右', '拿回形针_右': 'TakePaperClip_right',
                                   'TakePaperClip_left': '拿回形针_左', '拿回形针_左': 'TakePaperClip_left',
                                   'TakeMineralWaterBottle_right': '拿矿泉水瓶_右',
                                   '拿矿泉水瓶_右': 'TakeMineralWaterBottle_right',
                                   'TakeMineralWaterBottle_left': '拿矿泉水瓶_左',
                                   '拿矿泉水瓶_左': 'TakeMineralWaterBottle_left',
                                   'TakeWoodenBlockPinchTwoFingers_right': '拿木块两指捏_右',
                                   '拿木块两指捏_右': 'TakeWoodenBlockPinchTwoFingers_right',
                                   'TakeWoodenBlockPinchTwoFingers_left': '拿木块两指捏_左',
                                   '拿木块两指捏_左': 'TakeWoodenBlockPinchTwoFingers_left',
                                   'TakeWoodenBlockPinchThreeFingers_right': '拿木块三指捏_右',
                                   '拿木块三指捏_右': 'TakeWoodenBlockPinchThreeFingers_right',
                                   'TakeWoodenBlockPinchThreeFingers_left': '拿木块三指捏_左',
                                   '拿木块三指捏_左': 'TakeWoodenBlockPinchThreeFingers_left',
                                   'TakeSmallWoodenBlockPinchTwoFingers_right': '拿小木块两指捏_右',
                                   '拿小木块两指捏_右': 'TakeSmallWoodenBlockPinchTwoFingers_right',
                                   'TakeSmallWoodenBlockPinchTwoFingers_left': '拿小木块两指捏_左',
                                   '拿小木块两指捏_左': 'TakeSmallWoodenBlockPinchTwoFingers_left',
                                   'TakeSmallWoodenBlockPinchThreeFingers_right': '拿小木块三指捏_右',
                                   '拿小木块三指捏_右': 'TakeSmallWoodenBlockPinchThreeFingers_right',
                                   'TakeSmallWoodenBlockPinchThreeFingers_left': '拿小木块三指捏_左',
                                   '拿小木块三指捏_左': 'TakeSmallWoodenBlockPinchThreeFingers_left',
                                   'TakeKeys_right': '拿钥匙_右', '拿钥匙_右': 'TakeKeys_right',
                                   'TakeKeys_left': '拿钥匙__左', '拿钥匙__左': 'TakeKeys_left',
                                   'PinchBbouncyBall_right': '捏弹力球_右', '捏弹力球_右': 'PinchBbouncyBall_right',
                                   'PinchBbouncyBall_left': '捏弹力球_左', '捏弹力球_左': 'PinchBbouncyBall_left',
                                   'ForearmPronatorSetCupl_right': '前臂旋前套杯子_右',
                                   '前臂旋前套杯子_右': 'ForearmPronatorSetCupl_right',
                                   'ForearmPronatorSetCup_left': '前臂旋前套杯子_左',
                                   '前臂旋前套杯子_左': 'ForearmPronatorSetCup_left',
                                   'RollTrainingStick': '双手滚训练棒', '双手滚训练棒': 'RollTrainingStick',
                                   'BendStickFirmly': '双手用力弯训练棒', '双手用力弯训练棒': 'BendStickFirmly',
                                   'SetCups_right': '套杯子_右', '套杯子_右': 'SetCups_right',
                                   'SetCups_left': '套杯子_左', '套杯子_左': 'SetCups_left', 'Write_right': '写字_右',
                                   '写字_右': 'Write_right', 'Write_left': '写字_左', '写字_左': 'Write_left',
                                   'RotatePencil_right': '旋转铅笔_右', '旋转铅笔_右': 'RotatePencil_right',
                                   'RotatePencil_left': '旋转铅笔_左', '旋转铅笔_左': 'RotatePencil_left',
                                   'RotateKey_right': '旋转钥匙_右', '旋转钥匙_右': 'RotateKey_right',
                                   'RotateKey_left': '旋转钥匙_左', '旋转钥匙_左': 'RotateKey_left',
                                   'TakeSpoonBeads_right': '拿勺子舀珠子_右', '拿勺子舀珠子_右': 'TakeSpoonBeads_right',
                                   'TakeSpoonBeads_left': '拿勺子舀珠子_左', '拿勺子舀珠子_左': 'TakeSpoonBeads_left',
                                   'GrabReleaseTennisBalls_right': '抓放网球_右',
                                   '抓放网球_右': 'GrabReleaseTennisBalls_right',
                                   'GrabReleaseTennisBalls_left': '抓放网球_左',
                                   '抓放网球_左': 'GrabReleaseTennisBalls_left'}

        self.basicDictionary = {'ThanOK_right': '比ok_右', '比ok_右': 'ThanOK_right', 'ThanOK_left': '比ok_左',
                                '比ok_左': 'ThanOK_left',
                                'ThanNumbers_right': '比数字_右', '比数字_右': 'ThanNumbers_right',
                                'ThanNumbers_left': '比数字_左',
                                '比数字_左': 'ThanNumbers_left', 'SidePinch_right': '侧捏_右',
                                '侧捏_右': 'SidePinch_right',
                                'SidePinch_left': '侧捏_左', '侧捏_左': 'SidePinch_left',
                                'RulerDeviation_right': '尺偏_右',
                                '尺偏_右': 'RulerDeviation_right', 'RulerDeviation_left': '尺偏_左',
                                '尺偏_左': 'RulerDeviation_left',
                                'HookLikeGrip_right': '钩状抓握_右', '钩状抓握_右': 'HookLikeGrip_right',
                                'HookLikeGrip_left': '钩状抓握_左',
                                '钩状抓握_左': 'HookLikeGrip_left', 'TTIndexF_right': '拇指对食指_右',
                                '拇指对食指_右': 'TTIndexF_right',
                                'TTIndexF_left': '拇指对食指_左', '拇指对食指_左': 'TTIndexF_left',
                                'TTFourF_right': '拇指对四指_右',
                                '拇指对四指_右': 'TTFourF_right', 'TTFourF_left': '拇指对四指_左',
                                '拇指对四指_左': 'TTFourF_left',
                                'TTLittleF_right': '拇指对小指_右', '拇指对小指_右': 'TTLittleF_right',
                                'TTLittleF_left': '拇指对小指_左',
                                '拇指对小指_左': 'TTLittleF_left', 'TTPalm_right': '拇指对掌_右',
                                '拇指对掌_右': 'TTPalm_right',
                                'TTPalm_left': '拇指对掌_左', '拇指对掌_左': 'TTPalm_left',
                                'TLoopTurn_right': '拇指环转_右',
                                '拇指环转_右': 'TLoopTurn_right', 'TLoopTurn_left': '拇指环转_左',
                                '拇指环转_左': 'TLoopTurn_left',
                                'TFAExtension_right': '拇指屈伸_右', '拇指屈伸_右': 'TFAExtension_right',
                                'TFAExtension_left': '拇指屈伸_左',
                                '拇指屈伸_左': 'TFAExtension_left', 'TExtension_right': '拇指伸展_右',
                                '拇指伸展_右': 'TExtension_right',
                                'TExtension_left': '拇指伸展_左', '拇指伸展_左': 'TExtension_left',
                                'TAbduction_right': '拇指外展_右',
                                '拇指外展_右': 'TAbduction_right', 'TAbduction_left': '拇指外展_左',
                                '拇指外展_左': 'TAbduction_left',
                                'Forsupination_right': '前臂旋后_右', '前臂旋后_右': 'Forsupination_right',
                                'Forsupination_left': '前臂旋后_左', '前臂旋后_左': 'Forsupination_left',
                                'ForEarmProPost_right': '前臂旋前旋后_右', '前臂旋前旋后_右': 'ForEarmProPost_right',
                                'ForEarmProPost_left': '前臂旋前旋后_左', '前臂旋前旋后_左': 'ForEarmProPost_left',
                                'ForPronation_right': '前臂旋前_右', '前臂旋前_右': 'ForPronation_right',
                                'ForPronation_left': '前臂旋前_左',
                                '前臂旋前_左': 'ForPronation_left', 'BallGrip_right': '球状抓握_右',
                                '球状抓握_右': 'BallGrip_right',
                                'BallGrip_left': '球状抓握_左', '球状抓握_左': 'BallGrip_left',
                                'RadialDeviation_right': '桡偏_右',
                                '桡偏_右': 'RadialDeviation_right', 'RadialDeviation_left': '桡偏_左',
                                '桡偏_左': 'RadialDeviation_left',
                                'FInsideOut_right': '手指内外收展_右', '手指内外收展_右': 'FInsideOut_right',
                                'FInsideOut_left': '手指内外收展_左', '手指内外收展_左': 'FInsideOut_left',
                                'FFFExtendedSeparately_right': '四指单独屈伸_右',
                                '四指单独屈伸_右': 'FFFExtendedSeparately_right',
                                'FFFExtendedSeparately_left': '四指单独屈伸_左',
                                '四指单独屈伸_左': 'FFFExtendedSeparately_left',
                                'FFFlexion_right': '四指屈曲_右', '四指屈曲_右': 'FFFlexion_right',
                                'FFFlexion_left': '四指屈曲_左',
                                '四指屈曲_左': 'FFFlexion_left', 'FFExtended_right': '四指伸展_右',
                                '四指伸展_右': 'FFExtended_right',
                                'FFExtended_left': '四指伸展_左', '四指伸展_左': 'FFExtended_left',
                                'WristPalmCurl_right': '腕掌曲_右',
                                '腕掌曲_右': 'WristPalmCurl_right', 'WristPalmCurl_left': '腕掌曲_左',
                                '腕掌曲_左': 'WristPalmCurl_left',
                                'Fist_right': '握拳_右', '握拳_右': 'Fist_right', 'Fist_left': '握拳_左',
                                '握拳_左': 'Fist_left',
                                'ProWristDorsalExtension_right': '旋前腕背伸_右',
                                '旋前腕背伸_右': 'ProWristDorsalExtension_right',
                                'ProWristDorsalExtension_left': '旋前腕背伸_左',
                                '旋前腕背伸_左': 'ProWristDorsalExtension_left',
                                'TMJFIJExtended_right': '掌指关节屈曲，指间关节伸展_右',
                                '掌指关节屈曲，指间关节伸展_右': 'TMJFIJExtended_right',
                                'TMJFIJExtended_left': '掌指关节屈曲，指间关节伸展_左',
                                '掌指关节屈曲，指间关节伸展_左': 'TMJFIJExtended_left',
                                'StraightPunch_right': '直拳_右', '直拳_右': 'StraightPunch_right',
                                'StraightPunch_left': '直拳_左',
                                '直拳_左': 'StraightPunch_left', 'NeutralWristExtension_right': '中立位腕背伸_右',
                                '中立位腕背伸_右': 'NeutralWristExtension_right',
                                'NeutralWristExtension_left': '中立位腕背伸_左',
                                '中立位腕背伸_左': 'NeutralWristExtension_left', 'ColumnarGrip_right': '柱状抓握_右',
                                '柱状抓握_右': 'ColumnarGrip_right', 'ColumnarGrip_left': '柱状抓握_左',
                                '柱状抓握_左': 'ColumnarGrip_left'}

        self.leftCameraImage = [None, None]
        self.rightCameraImage = [None, None]
        self.basicVideoImage = None
        self.leftCameraFlip = 1
        self.rightCameraFlip = 1
        self.recordFlag = 0
        self.recordSheet = []

        self.leftCameraBlank = 0
        self.rightCameraBlank = 0

        self.statusShowTime()  # 显示系统时间
        self.spaceImaginationButton.clicked.connect(self.spaceImaginationButtonClick)  # 空间想象训练
        self.basicButton.clicked.connect(self.basicButtonClick)  # 基本动作训练
        self.functionButton.clicked.connect(self.functionButtonClick)  # 功能动作训练按钮
        self.mirrorButton.clicked.connect(self.mirrorButtonClick)  # 镜像训练按钮
        self.sensorimotorButton.clicked.connect(self.sensorimotorButtonClick)  # 感觉运动训练按钮
        self.resetPasswordLabel.mousePressEvent = self.resetPasswordLabelClick  # 密码修改
        self.exitSystemLabel.mousePressEvent = self.exitSystemLabelClick  # 系统退出
        self.space_startButton.clicked.connect(self.space_startButtonClick)  # 空间想象开始训练按钮
        self.basic_startButton.clicked.connect(self.basic_startButtonClick)  # 基本动作训练-开始训练
        self.basic_leftMirrrorButton.clicked.connect(self.basic_leftMirrorButtonClick)  # 基本动作训练-左手镜像
        self.basic_leftCopyButton.clicked.connect(self.basic_leftCopyButtonClick)  # 基本动作训练-左手复制
        self.basic_leftMaskButton.clicked.connect(self.basic_leftMaskButtonClick)  # 基本动作训练-左手遮罩
        self.basic_leftPlayButton.clicked.connect(self.basic_leftPlayButtonClick)  # 基本动作训练-左手播放
        self.basic_leftStopButton.clicked.connect(self.basic_leftStopButtonClick)  # 基本动作训练-左手重新开始
        self.basic_LeftRecoderButton.clicked.connect(self.basic_LeftRecoderButtonClick)  # 基本动作训练-左手录制
        self.basic_rightMirrrorButton.clicked.connect(self.basic_rightMirrorButtonClick)  # 基本动作训练-右手镜像
        self.basic_rightCopyButton.clicked.connect(self.basic_rightCopyButtonClick)  # 基本动作训练-右手复制
        self.basic_rightMaskButton.clicked.connect(self.basic_rightMaskButtonClick)  # 基本动作训练-右手遮罩
        self.basic_rightPlayButton.clicked.connect(self.basic_rightPlayButtonClick)  # 基本动作训练-右手播放
        self.basic_rightStopButton.clicked.connect(self.basic_rightStopButtonClick)  # 基本动作训练-右手重新开始
        self.basic_rightRecoderButton.clicked.connect(self.basic_rightRecoderButtonClick)  # 基本动作训练-右手录制
        self.basic_cancelButton.clicked.connect(self.basic_cancelButtonClick)  # 基本动作训练-全部取消
        self.basic_selectAllButton.clicked.connect(self.basic_selectAllButtonClick)  # 基本动作训练-全部选择
        self.function_startButton.clicked.connect(self.function_startButtonClick)  # 功能动作训练-开始训练
        self.function_leftMirrrorButton.clicked.connect(self.function_leftMirrrorButtonClick)  # 功能动作训练-左手镜像
        self.function_leftCopyButton.clicked.connect(self.function_leftCopyButtonClick)  # 功能动作训练-左手复制
        self.function_leftMaskButton.clicked.connect(self.function_leftMaskButtonClick)  # 功能动作训练-左手遮罩
        self.function_leftPlayButton.clicked.connect(self.function_leftPlayButtonClick)  # 功能动作训练-左手播放
        self.function_leftStopButton.clicked.connect(self.function_leftStopButtonClick)  # 功能动作训练-左手重新开始
        self.function_LeftRecoderButton.clicked.connect(self.function_LeftRecoderButtonClick)  # 功能动作训练-左手录制
        self.function_rightMirrrorButton.clicked.connect(self.function_rightMirrrorButtonClick)  # 功能动作训练-右手镜像
        self.function_rightCopyButton.clicked.connect(self.function_rightCopyButtonClick)  # 功能动作训练-右手复制
        self.function_rightMaskButton.clicked.connect(self.function_rightMaskButtonClick)  # 功能动作训练-右手遮罩
        self.function_rightPlayButton.clicked.connect(self.function_rightPlayButtonClick)  # 功能动作训练-右手播放
        self.function_rightStopButton.clicked.connect(self.function_rightStopButtonClick)  # 功能动作训练-右手重新开始
        self.function_rightRecoderButton.clicked.connect(self.function_rightRecoderButtonClick)  # 功能动作训练-右手录制
        self.function_cancelButton.clicked.connect(self.function_cancelButtonClick)  # 功能动作训练-全部取消
        self.function_selectAllButton.clicked.connect(self.function_selectAllButtonClick)  # 功能动作训练-全部选择
        self.mirror_leftMirrorButton.clicked.connect(self.mirror_leftMirrorButtonClick)  # 镜像训练-左手镜像
        self.mirror_leftCopyButton.clicked.connect(self.mirror_leftCopyButtonClick)  # 镜像训练-左手复制
        self.mirror_leftMaskButton.clicked.connect(self.mirror_leftMaskButtonClick)  # 镜像训练-左手遮罩
        self.mirror_leftPlayButton.clicked.connect(self.mirror_leftPlayButtonClick)  # 镜像训练-左手播放
        self.mirror_leftRecoderButton.clicked.connect(self.mirror_leftRecoderButtonClick)  # 镜像训练-左手录制
        self.mirror_rightMirrorButton.clicked.connect(self.mirror_rightMirrorButtonClick)  # 镜像训练-右手镜像
        self.mirror_rightCopyButton.clicked.connect(self.mirror_rightCopyButtonClick)  # 镜像训练-右手复制
        self.mirror_rightMaskButton.clicked.connect(self.mirror_rightMaskButtonClick)  # 镜像训练-右手遮罩
        self.mirror_rightPlayButton.clicked.connect(self.mirror_rightPlayButtonClick)  # 镜像训练-右手播放
        self.mirror_rightRecoderButton.clicked.connect(self.mirror_rightRecoderButtonClick)  # 镜像训练-右手录制
        self.mirror_historyRecordButton.clicked.connect(self.mirror_historyRecordButtonClick)  # 镜像训练——显示视频历史记录
        self.sensorimotor_leftMirrrorButton.clicked.connect(self.sensorimotor_leftMirrrorButtonClick)  # 感觉运动训练-左手镜像
        self.sensorimotor_leftCopyButton.clicked.connect(self.sensorimotor_leftCopyButtonClick)  # 感觉运动训练-左手复制
        self.sensorimotor_leftMaskButton.clicked.connect(self.sensorimotor_leftMaskButtonClick)  # 感觉运动训练-左手遮罩
        self.sensorimotor_leftPlayButton.clicked.connect(self.sensorimotor_leftPlayButtonClick)  # 感觉运动训练-左手播放
        self.sensorimotor_leftStopButton.clicked.connect(self.sensorimotor_leftStopButtonClick)  # 感觉运动训练-左手重新开始
        self.sensorimotor_LeftRecorderButton.clicked.connect(self.sensorimotor_leftRecoderButtonClick)  # 感觉运动训练-左手录制
        self.sensorimotor_rightMirrrorButton.clicked.connect(self.sensorimotor_rightMirrorButtonClick)  # 感觉运动训练-右手镜像
        self.sensorimotor_rightCopyButton.clicked.connect(self.sensorimotor_rightCopyButtonClick)  # 感觉运动训练-右手复制
        self.sensorimotor_rightMaskButton.clicked.connect(self.sensorimotor_rightMaskButtonClick)  # 感觉运动训练-右手遮罩
        self.sensorimotor_rightPlayButton.clicked.connect(self.sensorimotor_rightPlayButtonClick)  # 感觉运动训练-右手播放
        self.sensorimotor_rightStopButton.clicked.connect(self.sensorimotor_rightStopButtonClick)  # 感觉运动训练-右手重新开始
        self.sensorimotor_rightRecorderButton.clicked.connect(self.sensorimotor_rightRecoderButtonClick)  # 感觉运动训练-右手录制
        self.sensorimotor_cancelButton.clicked.connect(self.sensorimotor_cancelButtonClick)  # 感觉运动训练-全部取消
        self.sensorimotor_selectAllButton.clicked.connect(self.sensorimotor_selectAllButtonClick)  # 感觉运动训练-全选
        self.sensorimotor_historyRecordButton.clicked.connect(
            self.sensorimotor_historyRecordButtonClick)  # 感觉运动训练-显示历史视频记录
        self.sensorimotor_startButton.clicked.connect(self.sensorimotor_startButtonClick)  # 感觉运动训练-开始训练
        self.sensorimotor_trainingModeComboBox.currentIndexChanged.connect(
            self.sensorimotor_trainingModeComboBoxClick)  # 感觉运动训练-获取训练模式（单、双、单双）
        self.mirror_startButton.clicked.connect(self.mirror_startButtonClick)

        self.spaceImageWindow = frontend.training.SpaceTrainingPatient.SpaceTrainingPatient()
        self.monitor = QDesktopWidget().screenGeometry(1)
        self.spaceImageWindow.move(self.monitor.left(), self.monitor.top())
        self.spaceImageWindow.showFullScreen()
        self.spaceImageWindow.show()

        self.sensorWindow = frontend.training.SensorimotorPatient.sensorimotor_Patient()
        self.sensorWindow.move(self.monitor.left(), self.monitor.top())
        self.sensorWindow.showFullScreen()
        self.sensorWindow.hide()

        self.basicTrainingWindow = frontend.training.BasicTrainingPatient.BasicTrainingPatient()
        self.basicTrainingWindow.move(self.monitor.left(), self.monitor.top())
        self.basicTrainingWindow.showFullScreen()
        self.basicTrainingWindow.hide()

        self.mirrorWindow = frontend.training.MirrorPatient.mirrorPatient()
        self.mirrorWindow.move(self.monitor.left(), self.monitor.top())
        self.mirrorWindow.showFullScreen()
        self.mirrorWindow.hide()

        self.functionWindow = frontend.training.FunctionTrianingPatient.functionTrianingPatient()
        self.functionWindow.move(self.monitor.left(), self.monitor.top())
        self.functionWindow.showFullScreen()
        self.functionWindow.hide()

        self.leftCamera = tool.VideoHelper.CameraReader(config.LeftCaptureId)
        # self.rightCamera = tool.VideoHelper.CameraReader(config.RightCaptureId)
        self.rightCamera = self.leftCamera

        self.cameraWorker = threading.Thread(target=self.cameraRead)
        self.cameraWorker.start()

    def cameraRead(self):
        while True:
            if self.leftCameraFlip == 1:
                self.leftCameraImage = self.leftCamera.readCamera(picSize=(960, 1080))
            else:
                self.leftCameraImage = self.leftCamera.readCamera(picSize=(960, 1080), flip=False)
            if self.rightCameraFlip == 1:
                self.rightCameraImage = self.rightCamera.readCamera(picSize=(960, 1080))
            else:
                self.rightCameraImage = self.rightCamera.readCamera(picSize=(960, 1080), flip=False)
            if self.leftCameraBlank == 1:
                self.leftCameraImage = [self.emptyCamera.toImage(), self.emptyCamera]
            if self.rightCameraBlank == 1:
                self.rightCameraImage = [self.emptyCamera.toImage(), self.emptyCamera]

            index = self.stackedWidget.currentIndex()
            if index == 0:
                pass
            elif index == 1:
                self.sensorWindow.showLeftPictureByPicture(self.leftCameraImage[1])
                self.sensorWindow.showRightPictureByPicture(self.rightCameraImage[1])
                self.sensorimotor_leftCameraLabel.setPixmap(
                    self.leftCameraImage[1].scaled(550, 520, transformMode=QtCore.Qt.SmoothTransformation))
                self.sensorimotor_rightCameraLabel.setPixmap(
                    self.rightCameraImage[1].scaled(550, 520, transformMode=QtCore.Qt.SmoothTransformation))
            elif index == 2:
                self.basicTrainingWindow.showLeftPictureByPicture(self.leftCameraImage[1])
                self.basicTrainingWindow.showRightPictureByPicture(self.rightCameraImage[1])
                self.basic_leftCameraLabel.setPixmap(
                    self.leftCameraImage[1].scaled(550, 520, transformMode=QtCore.Qt.SmoothTransformation))
                self.basic_rightCameraLabel.setPixmap(
                    self.rightCameraImage[1].scaled(550, 520, transformMode=QtCore.Qt.SmoothTransformation))
            elif index == 3:
                self.functionWindow.showLeftPictureByPicture(self.leftCameraImage[1])
                self.functionWindow.showRightPictureByPicture(self.rightCameraImage[1])
                self.function_leftCameraLabel.setPixmap(
                    self.leftCameraImage[1].scaled(550, 520, transformMode=QtCore.Qt.SmoothTransformation))
                self.function_rightCameraLabel.setPixmap(
                    self.rightCameraImage[1].scaled(550, 520, transformMode=QtCore.Qt.SmoothTransformation))
            else:
                self.mirrorWindow.showLeftPictureByPicture(self.leftCameraImage[1])
                self.mirrorWindow.showRightPictureByPicture(self.rightCameraImage[1])
                self.mirror_lefCameraLabel.setPixmap(
                    self.leftCameraImage[1].scaled(900, 650, transformMode=QtCore.Qt.SmoothTransformation))
                self.mirror_rightCameraLabel.setPixmap(
                    self.rightCameraImage[1].scaled(900, 650, transformMode=QtCore.Qt.SmoothTransformation))

            if self.recordFlag == 1:
                self.recordSheet.append(self.leftCameraImage[0])
            elif self.recordFlag == 2:
                self.recordSheet.append(self.rightCameraImage[0])

    def cameraStatusReset(self):
        self.leftCameraFlip = 1
        self.rightCameraFlip = 1
        self.leftCameraBlank = 0
        self.rightCameraBlank = 0

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        threadingHelper = tool.ThreadingHelper.ThreadingHelper()
        threadingHelper.close(self.cameraWorker)
        self.leftCamera.release()
        self.rightCamera.release()

        self.spaceImageWindow.destroy()
        self.sensorWindow.destroy()
        self.basicTrainingWindow.destroy()
        self.mirrorWindow.destroy()
        self.functionWindow.destroy()
        self.destroy()
        sys.exit(app.exec_())

    def showCurrentTime(self, timeLabel):  # 显示系统时间
        # 获取系统当前时间
        dt = QDateTime.currentDateTime()
        # 设置系统时间的显示格式
        timeDisplay = dt.toString('yyyy-MM-dd hh:mm:ss dddd')
        # print(timeDisplay)
        # 状态栏显示
        timeLabel.setText(timeDisplay)

    def statusShowTime(self):  # 实时显示系统时间
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.showCurrentTime(self.timeLabel))  # 这个通过调用槽函数来刷新时间
        self.timer.start(1000)  # 每隔一秒刷新一次，这里设置为1000ms  即1s

    def spaceImaginationButtonClick(self, *args):  # 空间想象训练
        self.stackedWidget.setCurrentIndex(0)
        self.spaceImageWindow.show()
        self.sensorWindow.close()
        self.basicTrainingWindow.close()
        self.mirrorWindow.close()
        self.functionWindow.close()
        self.cameraStatusReset()
        self.resetVideoRecorder()

    def sensorimotorButtonClick(self, *args):  # 感觉运动训练
        self.stackedWidget.setCurrentIndex(1)
        self.spaceImageWindow.close()
        self.sensorWindow.show()
        self.basicTrainingWindow.close()
        self.mirrorWindow.close()
        self.cameraStatusReset()
        self.resetVideoRecorder()

    def basicButtonClick(self, *args):  # 基本动作训练按钮
        self.stackedWidget.setCurrentIndex(2)
        self.spaceImageWindow.close()
        self.sensorWindow.close()
        self.basicTrainingWindow.show()
        self.mirrorWindow.close()
        self.functionWindow.close()
        self.cameraStatusReset()
        self.resetVideoRecorder()

    def functionButtonClick(self, *args):  # 功能动作训练按钮
        self.stackedWidget.setCurrentIndex(3)
        self.spaceImageWindow.close()
        self.sensorWindow.close()
        self.basicTrainingWindow.close()
        self.mirrorWindow.close()
        self.functionWindow.show()
        self.cameraStatusReset()
        self.resetVideoRecorder()

    def mirrorButtonClick(self, *args):  # 镜像动作训练按钮
        self.stackedWidget.setCurrentIndex(4)
        self.spaceImageWindow.close()
        self.sensorWindow.close()
        self.basicTrainingWindow.close()
        self.mirrorWindow.show()
        self.functionWindow.close()
        self.cameraStatusReset()
        self.resetVideoRecorder()

    def resetVideoRecorder(self):
        self.recordFlag = 0
        self.recordSheet = []

    def resetPasswordLabelClick(self, *args):  # 密码修改
        ...

    def exitSystemLabelClick(self, *args):  # 系统退出
        self.close()

    def space_startButtonClick(self, *args):  # 空间想象训练开始训练按钮
        _translate = QtCore.QCoreApplication.translate
        self.stopButtonFrame.setVisible(True)
        if self.is_playing:
            self.space_startButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaStop))
            self.space_startButton.setText("暂停")
            self.spaceImageTrainingPictureInfo = \
                json.loads(requests.post(config.spaceImageConfigGetPic,
                                         data={
                                             'difficult': self.discriminationDifficultyComboBox.currentText(),
                                             'pic_number': self.pictureNumComboBox.currentText()}).content.decode(
                    'utf-8'))['data']
            self.spaceImageTrainingPictureTotalNumber.setText(
                _translate("Form", str(len(self.spaceImageTrainingPictureInfo))))
            self.startImagePlayerThread = threading.Thread(target=self.startImagePlayer)
            self.startImagePlayerThread.start()
            self.is_playing = False

        else:
            self.space_startButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaPlay))
            self.space_startButton.setText("开始训练")
            self.is_playing = True
            self.threadHelper = tool.ThreadingHelper.ThreadingHelper()
            self.threadHelper.close(self.startImagePlayerThread)
            self.picturLabel.setPixmap(QPixmap(f"{config.GlobalPath}src/fig/welcome_use.jpg"))
        ...

    def startImagePlayer(self):
        self.beginTime = tool.Tools.getNowTime()
        trans = {"左": "left", "右": "right", "低难度": "easy", "中难度": "mid", "高难度": "hard"}
        _translate = QtCore.QCoreApplication.translate
        cnt = 1
        left_correct = 0
        right_correct = 0
        left_count = 0
        right_count = 0
        left_cnt = 0
        right_cnt = 0
        left_time = 0
        right_time = 0

        for i in self.spaceImageTrainingPictureInfo:
            if i['type'] == '左':
                left_count += 1
            else:
                right_count += 1

        for i in self.spaceImageTrainingPictureInfo:
            _diff = trans[i["difficult"]]
            _type = trans[i["type"]]
            name = i["pic_id"]
            img_small = QPixmap(f"{config.GlobalPath}src/train/{_diff}/{_type}/{name}")
            img_large = QPixmap(f"{config.GlobalPath}src/train/{_diff}/{_type}/{name}")
            img_large = img_large.scaled(1300, 1100)
            self.picturLabel.setPixmap(img_small)
            self.spaceImageWindow.replacePicture(img_large)
            self.spaceImageWindow.nowSelection = None
            self.spaceImageWindow.timeSelected = time.time()
            self.currentPictureNumLabel.setText(_translate("Form", str(cnt)))
            self.remainPictureNumLabel.setText(_translate("Form", str(len(self.spaceImageTrainingPictureInfo) - cnt)))

            time.sleep(int(self.playSpeedCombobox.currentText()))

            if i['type'] == '左':
                left_cnt += 1
            else:
                right_cnt += 1

            if self.spaceImageWindow.nowSelection == i['type'] and i['type'] == '左':
                left_correct += 1
            elif self.spaceImageWindow.nowSelection == i['type'] and i['type'] == '右':
                right_correct += 1

            time_consume = min(int(self.playSpeedCombobox.currentText()),
                               time.time() - self.spaceImageWindow.timeSelected)

            if i['type'] == '左':
                left_time += time_consume
            else:
                right_time += time_consume

            self.trainingTimeLabel.setText(_translate("From", str(int(self.playSpeedCombobox.currentText()) * len(
                self.spaceImageTrainingPictureInfo))))
            self.averageTimeLabel.setText(_translate("From", str(round(((left_time + right_time) / cnt), 2))))

            self.correctNumLabel.setText(_translate("Form", str(left_correct + right_correct)))
            self.leftCorrectNumLabel.setText(_translate("Form", str(left_correct)))
            self.rightCorrectNumLabel.setText(_translate("Form", str(right_correct)))
            self.correctRateLabel.setText(
                _translate("Form", str(round(((left_correct + right_correct) / cnt) * 100, 2))))
            if left_cnt == 0:
                self.leftCorrectRateLabel.setText(_translate("Form", "100.0"))
                self.leftAverageTimeLabel.setText(_translate("From", "0"))
            else:
                self.leftCorrectRateLabel.setText(
                    _translate("Form", str(round((left_correct / left_cnt) * 100, 2))))
                self.leftAverageTimeLabel.setText(_translate("From", str(round((left_time / left_cnt), 2))))

            if right_cnt == 0:
                self.rightCorrectRateLabel.setText(_translate("Form", "100.0"))
                self.rightAverageTimeLabel.setText(_translate("From", "0"))
            else:
                self.rightCorrectRateLabel.setText(
                    _translate("Form", str(round((right_correct / right_cnt) * 100, 2))))
                self.rightAverageTimeLabel.setText(_translate("From", str(round((right_time / right_cnt), 2))))

            cnt += 1

        self.space_startButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaPlay))
        self.space_startButton.setText("开始训练")
        self.is_playing = True

        pic = self.grab()
        pic_id = tool.Tools.getTimeStamp()
        print(f"{config.GlobalPath}save/space/{pic_id}.png")
        pic.save(f"{config.GlobalPath}save/space/{pic_id}.png")
        result = {"id": self.patient_id,
                  'end_time': tool.Tools.getNowTime(),
                  'train': "空间想象训练",
                  'status': "已完成",
                  'pic': pic_id,
                  'begin_time': self.beginTime,
                  'detail': 'None'}
        requests.post(config.trainInfoInsert, data=result)
        self.picturLabel.setPixmap(QPixmap(f"{config.GlobalPath}src/fig/welcome_use.jpg"))
        self.spaceImageWindow.replacePicture(QPixmap(f"{config.GlobalPath}src/fig/welcome_use.jpg"))

    def basic_startTask(self):
        self.beginTime = tool.Tools.getTimeStamp()
        _translate = QtCore.QCoreApplication.translate
        if self.basic_type == "AABB":
            for trainTime in range(self.basicTrainTime):
                for i in self.basicVideoSheet:
                    for groupTime in range(self.basicGroupTime):
                        self.basic_trainingNameLabel.setText(_translate("Form", i))
                        for playTime in range(self.basicPlayTime):
                            cap = cv2.VideoCapture(config.GlobalPath + "src/video/basic/" + i)
                            print(i)
                            while True:
                                ret, frame = cap.read()
                                if not ret:
                                    break
                                cv2.imwrite('temp.png', cv2.resize(frame, (680, 350)))
                                self.basicVideoImage = QPixmap('temp.png')
                                self.basic_showVideoLabel.setPixmap(self.basicVideoImage)
                            cap.release()
                        try:
                            os.remove('temp.png')
                        except:
                            pass
        else:
            for groupTime in range(self.basicGroupTime):
                for playTime in range(self.basicPlayTime):
                    for i in self.basicVideoSheet:
                        self.basic_trainingNameLabel.setText(_translate("Form", i))
                        for trainTime in range(self.basicTrainTime):
                            cap = cv2.VideoCapture(config.GlobalPath + "src/video/basic/" + i)
                            print(i)
                            while True:
                                ret, frame = cap.read()
                                if not ret:
                                    break
                                cv2.imwrite('temp.png', cv2.resize(frame, (680, 350)))
                                self.basicVideoImage = QPixmap('temp.png')
                                self.basic_showVideoLabel.setPixmap(self.basicVideoImage)
                            cap.release()
                        try:
                            os.remove('temp.png')
                        except:
                            pass
        pic = self.grab()
        pic_id = tool.Tools.getTimeStamp()
        print(f"{config.GlobalPath}save/basic/{pic_id}.png")
        pic.save(f"{config.GlobalPath}save/basic/{pic_id}.png")
        result = {"id": self.patient_id,
                  'end_time': tool.Tools.getNowTime(),
                  'train': "基本功能训练",
                  'status': "已完成",
                  'pic': pic_id,
                  'begin_time': self.beginTime,
                  'detail': self.trainDetailSheet}
        requests.post(config.trainInfoInsert, data=result)

        self.basic_startButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaPlay))
        self.basic_startButton.setText("开始训练")
        self.basic_selectTrainingFrame.setVisible(True)  # 基本动作训练容器
        self.basic_traingSituationFrame.setVisible(False)
        self.basic_isPlaying = True

    def basic_startButtonClick(self, *args):  # 基本动作训练开始训练按钮
        _translate = QtCore.QCoreApplication.translate
        self.basic_selectTrainingFrame.setVisible(False)
        self.basic_traingSituationFrame.setVisible(True)
        if self.basic_isPlaying:
            self.basic_startButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaStop))
            self.basic_startButton.setText("停止训练")
            self.basic_selectTrainingFrame.setVisible(False)  # 基本动作训练容器
            self.basic_traingSituationFrame.setVisible(True)
            self.basic_isPlaying = False

            checked_text_list = []
            items = self.basic_leftTree.findItems('', Qt.MatchContains | Qt.MatchRecursive, 0)
            for item in items:
                if item.parent() and not item.childCount() and item.checkState(0) == 2:
                    checked_text_list.append(item.text(0))

            items = self.basic_rightTree.findItems('', Qt.MatchContains | Qt.MatchRecursive, 0)
            for item in items:
                if item.parent() and not item.childCount() and item.checkState(0) == 2:
                    checked_text_list.append(item.text(0))

            self.trainDetailSheet = ','.join(checked_text_list)
            print(self.trainDetailSheet)

            for i in range(len(checked_text_list)):
                checked_text_list[i] = checked_text_list[i] + "_" + self.patientInfo['illness']

            self.basicPlaySpeed: int = self.basic_playSpeedComBox.currentText()
            if self.basicPlaySpeed == '':
                self.basicPlaySpeed = 1
            else:
                self.basicPlaySpeed = float(self.basicPlaySpeed)

            self.basicVideoSheet = []

            for i in checked_text_list:
                try:
                    en_hand_speed = f"{self.basicDictionary[i]}_{self.basicPlaySpeed}.mp4"
                    self.basicVideoSheet.append(en_hand_speed)
                except Exception as e:
                    print(i,e)

            print(self.basicVideoSheet)

            self.basic_type = self.basic_trainingWayComboBox.currentText()
            if self.basic_type == '':
                self.basic_type = 'AABB'

            self.basicGroupTime: int = self.basic_trainingGroupNumLineEdit.text()
            if self.basicGroupTime == '':
                self.basicGroupTime = 1
            else:
                try:
                    self.basicGroupTime = int(self.basicGroupTime)
                except:
                    self.basicGroupTime = 1

            self.basicTrainTime: int = self.basic_trainingNumLineEdit.text()
            if self.basicTrainTime == '':
                self.basicTrainTime = 1
            else:
                try:
                    self.basicTrainTime = int(self.basicTrainTime)
                except:
                    self.basicTrainTime = 1

            self.basicPlayTime: int = self.basic_playNumLineEdit.text()
            if self.basicPlayTime == '':
                self.basicPlayTime = 1
            else:
                try:
                    self.basicPlayTime = int(self.basicPlayTime)
                except:
                    self.basicPlayTime = 1

            self.basicPlaySpeed = self.basic_playSpeedComBox.currentText()
            if self.basicPlaySpeed == '':
                self.basicPlaySpeed = 1

            self.basic_trainingModeLabel.setText(_translate("Form", self.basic_type))
            self.basic_trainingTotalNumLabel.setText(_translate("Form", str(self.basicGroupTime)))
            self.basic_trainingCurrentNumLabel.setText(_translate("Form", str(self.basicTrainTime)))

            self.basicStartTask = threading.Thread(target=self.basic_startTask)
            self.basicStartTask.start()

        else:
            self.basic_startButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaPlay))
            self.basic_startButton.setText("开始训练")
            self.basic_selectTrainingFrame.setVisible(True)  # 基本动作训练容器
            self.basic_traingSituationFrame.setVisible(False)
            self.basic_isPlaying = True

            self.threadHelper = tool.ThreadingHelper.ThreadingHelper()
            self.threadHelper.close(self.basicStartTask)

    def basic_reset(self):
        _translate = QtCore.QCoreApplication.translate
        self.basic_trainingModeLabel.setText(_translate("Form", "----"))
        self.basic_trainingTotalNumLabel.setText(_translate("Form", "----"))
        self.basic_trainingNameLabel.setText(_translate("Form", "--"))
        self.basic_trainingGroupNumLineEdit.setText(_translate("Form", "--"))

    def basic_leftMirrorButtonClick(self, *args):  # 基本动作训练-左手镜像
        self.leftCameraFlip ^= 1
        ...

    def basic_leftCopyButtonClick(self, *args):  # 基本动作训练-左手复制
        ...

    def basic_leftMaskButtonClick(self, *args):  # 基本动作训练-左手遮罩
        self.leftCameraBlank ^= 1
        ...

    def basic_leftPlayButtonClick(self, *args):  # 基本动作训练-左手播放
        if self.basic_leftIsPlaying:
            self.basic_leftPlayButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaStop))
            self.basic_leftPlayButton.setText("停止")
            self.basic_leftIsPlaying = False

        else:
            self.basic_leftPlayButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaPlay))
            self.basic_leftPlayButton.setText("播放")
            self.basic_leftIsPlaying = True
        ...

    def basic_leftStopButtonClick(self, *args):  # 基本动作训练-左手重新开
        ...

    def basic_LeftRecoderButtonClick(self, *args):  # 基本动作训练-左手录制
        if self.recordFlag != 0:  # 1-left 2-right
            self.recordFlag = 0
            path = QFileDialog.getExistingDirectory()
            if path != '':
                savePath = f"{path}/{tool.Tools.getNowTime()}_basic_left.mp4".replace("//", "/")
                recorder = tool.VideoHelper.VideoWriter(savePath, 'mp4', 24, (550, 520))
                for i in self.recordSheet:
                    recorder.saveFigByImg(i)
                recorder.save()
                self.recordSheet = []
            else:
                return
        else:
            self.recordFlag = 1

        ...

    def basic_rightMirrorButtonClick(self, *args):  # 基本动作训练-右手镜像
        self.rightCameraFlip ^= 1
        ...

    def basic_rightCopyButtonClick(self, *args):  # 基本动作训练-右手复制
        ...

    def basic_rightMaskButtonClick(self, *args):  # 基本动作训练-右手遮罩
        self.rightCameraBlank ^= 1
        ...

    def basic_rightPlayButtonClick(self, *args):  # 基本动作训练-右手播放
        if self.basic_rightIsPlaying:
            self.basic_rightPlayButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaStop))
            self.basic_rightPlayButton.setText("停止")
            self.basic_rightIsPlaying = False

        else:
            self.basic_rightPlayButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaPlay))
            self.basic_rightPlayButton.setText("播放")
            self.basic_rightIsPlaying = True
        ...

    def basic_rightStopButtonClick(self, *args):  # 基本动作训练-右手重新开始
        ...

    def basic_rightRecoderButtonClick(self, *args):  # 基本动作训练-右手录制
        if self.recordFlag != 0:  # 1-left 2-right
            self.recordFlag = 0
            path = QFileDialog.getExistingDirectory()
            if path != '':
                savePath = f"{path}/{tool.Tools.getNowTime()}_basic_right.mp4".replace(
                    "//", "/")
                recorder = tool.VideoHelper.VideoWriter(savePath, 'mp4', 24, (550, 520))
                for i in self.recordSheet:
                    recorder.saveFigByImg(i)
                recorder.save()
                self.recordSheet = []
            else:
                return
        else:
            self.recordFlag = 2
        ...

    def basic_cancelButtonClick(self, *args):  # 基本动作训练-全部取消
        ...

    def basic_selectAllButtonClick(self, *args):  # 基本动作训练-全部选择
        ...

    def function_startButtonClick(self, *args):  # 功能动作训练-开始训练按钮

        _translate = QtCore.QCoreApplication.translate
        self.function_selectTrainingFrame.setVisible(False)  # 功能动作训练容器
        self.function_traingSituationFrame.setVisible(True)  # 功能动作-训练情况显示窗口
        if self.function_isPlaying:
            self.function_startButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaStop))
            self.function_startButton.setText("停止训练")
            self.function_selectTrainingFrame.setVisible(False)  # 功能动作训练容器
            self.function_traingSituationFrame.setVisible(True)
            self.function_isPlaying = False

            checked_text_list = []
            items = self.function_leftTree.findItems('', Qt.MatchContains | Qt.MatchRecursive, 0)
            for item in items:
                if item.parent() and not item.childCount() and item.checkState(0) == 2:
                    checked_text_list.append(item.text(0))

            items = self.function_rightTree.findItems('', Qt.MatchContains | Qt.MatchRecursive, 0)
            for item in items:
                if item.parent() and not item.childCount() and item.checkState(0) == 2:
                    checked_text_list.append(item.text(0))

            for i in range(len(checked_text_list)):
                checked_text_list[i] = checked_text_list[i] + "_" + self.patientInfo['illness']

            self.trainDetailSheet = ','.join(checked_text_list)
            print(self.trainDetailSheet)

            self.functionPlaySpeed: int = self.function_playSpeedComBox.currentText()
            if self.functionPlaySpeed == '':
                self.functionPlaySpeed = 1
            else:
                self.functionPlaySpeed = float(self.functionPlaySpeed)

            self.functionVideoSheet = []

            for i in checked_text_list:
                en_hand_speed = f"{self.functionDictionary[i]}_{self.functionPlaySpeed}.mp4"
                self.functionVideoSheet.append(en_hand_speed)

            print(self.functionVideoSheet)

            self.function_type = self.function_trainingWayComboBox.currentText()
            if self.function_type == '':
                self.function_type = 'AABB'

            self.functionGroupTime: int = self.function_trainingGroupNumLineEdit.text()
            if self.functionGroupTime == '':
                self.functionGroupTime = 1
            else:
                try:
                    self.functionGroupTime = int(self.functionGroupTime)
                except:
                    self.functionGroupTime = 1

            self.functionTrainTime: int = self.function_trainingNumLineEdit.text()
            if self.functionTrainTime == '':
                self.functionTrainTime = 1
            else:
                try:
                    self.functionTrainTime = int(self.functionTrainTime)
                except:
                    self.functionTrainTime = 1

            self.functionPlayTime: int = self.function_playNumLineEdit.text()

            if self.functionPlayTime == '':
                self.functionPlayTime = 1
            else:
                try:
                    self.functionPlayTime = int(self.functionPlayTime)
                except:
                    self.functionPlayTime = 1

            self.functionPlaySpeed = self.function_playSpeedComBox.currentText()
            if self.functionPlaySpeed == '':
                self.functionPlaySpeed = 1

            self.function_trainingModeLabel.setText(_translate("Form", self.function_type))
            self.function_trainingTotalNumLabel.setText(_translate("Form", str(self.functionGroupTime)))
            self.function_trainingCurrentNumLabel.setText(_translate("Form", str(self.functionTrainTime)))

            self.functionStartTask = threading.Thread(target=self.function_startTask)
            self.functionStartTask.start()

        else:
            self.function_startButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaPlay))
            self.function_startButton.setText("开始训练")
            self.function_selectTrainingFrame.setVisible(True)  # 功能动作训练容器
            self.function_traingSituationFrame.setVisible(False)
            self.function_isPlaying = True
            self.threadHelper = tool.ThreadingHelper.ThreadingHelper()
            self.threadHelper.close(self.functionStartTask)

    def function_startTask(self):
        self.beginTime = tool.Tools.getNowTime()
        _translate = QtCore.QCoreApplication.translate
        if self.function_type == "AABB":
            for trainTime in range(self.functionTrainTime):  # 训练次数
                for i in self.functionVideoSheet:  # 训练视频
                    for groupTime in range(self.functionGroupTime):  # 训练组数
                        self.function_trainingNameLabel.setText(_translate("Form", i))
                        for playTime in range(self.functionPlayTime):  # 播放次数
                            cap = cv2.VideoCapture(config.GlobalPath + "src/video/function/" + i)
                            while True:
                                ret, frame = cap.read()
                                if not ret:
                                    break
                                cv2.imwrite('temp.png', cv2.resize(frame, (680, 350)))
                                self.functionVideoImage = QPixmap('temp.png')
                                self.function_showVideoLabel.setPixmap(self.functionVideoImage)
                                self.functionWindow.showMiddlePicture(self.functionVideoImage)
                            cap.release()
                        try:
                            os.remove('temp.png')
                        except:
                            pass
        else:  # ABAB
            for groupTime in range(self.functionGroupTime):
                for playTime in range(self.functionPlayTime):  # 播放次数
                    for i in self.functionVideoSheet:
                        self.function_trainingNameLabel.setText(_translate("Form", i))
                        for trainTime in range(self.functionTrainTime):
                            cap = cv2.VideoCapture(config.GlobalPath + "src/video/function/" + i)
                            while True:
                                ret, frame = cap.read()
                                if not ret:
                                    break
                                cv2.imwrite('temp.png', cv2.resize(frame, (680, 350)))
                                self.functionVideoImage = QPixmap('temp.png')
                                self.function_showVideoLabel.setPixmap(self.functionVideoImage)
                                self.functionWindow.showMiddlePicture(self.functionVideoImage)
                            cap.release()
                            try:
                                os.remove('temp.png')
                            except:
                                pass
        pic = self.grab()
        pic_id = tool.Tools.getTimeStamp()
        pic.save(f"{config.GlobalPath}save/function/{pic_id}.png")
        result = {"id": self.patient_id,
                  'end_time': tool.Tools.getNowTime(),
                  'train': "功能动作训练",
                  'status': "已完成",
                  'pic': pic_id,
                  'begin_time': self.beginTime,
                  'detail': self.trainDetailSheet}
        requests.post(config.trainInfoInsert, data=result)

        self.function_startButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaPlay))
        self.function_startButton.setText("开始训练")
        self.function_selectTrainingFrame.setVisible(True)  # 功能动作训练容器
        self.function_traingSituationFrame.setVisible(False)
        self.function_isPlaying = True

    def function_leftMirrrorButtonClick(self, *args):  # 功能动作训练-左手镜像
        self.leftCameraFlip ^= 1
        ...

    def function_leftCopyButtonClick(self, *args):  # 功能动作训练-左手复制
        ...

    def function_leftMaskButtonClick(self, *args):  # 功能动作训练-左手遮罩
        self.leftCameraBlank ^= 1
        ...

    def function_leftPlayButtonClick(self, *args):  # 功能动作训练-左手播放
        if self.function_leftIsPlaying:
            self.function_leftPlayButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaStop))
            self.function_leftPlayButton.setText("停止")
            self.function_leftIsPlaying = False

        else:
            self.function_leftPlayButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaPlay))
            self.function_leftPlayButton.setText("播放")
            self.function_leftIsPlaying = True
        ...

    def function_leftStopButtonClick(self, *args):  # 功能动作训练-左手重新开始
        ...

    def function_LeftRecoderButtonClick(self, *args):  # 功能动作训练-左手录制
        if self.recordFlag != 0:  # 1-left 2-right
            self.recordFlag = 0
            path = QFileDialog.getExistingDirectory()
            if path != '':
                savePath = f"{path}/{tool.Tools.getNowTime()}_function_left.mp4".replace("//", "/")
                recorder = tool.VideoHelper.VideoWriter(savePath, 'mp4', 24, (550, 520))
                for i in self.recordSheet:
                    recorder.saveFigByImg(i)
                recorder.save()
                self.recordSheet = []
            else:
                return
        else:
            self.recordFlag = 1
        ...

    def function_rightMirrrorButtonClick(self, *args):  # 功能动作训练-右手镜像
        self.rightCameraFlip ^= 1
        ...

    def function_rightCopyButtonClick(self, *args):  # 功能动作训练-右手复制
        ...

    def function_rightMaskButtonClick(self, *args):  # 功能动作训练-右手遮罩
        self.rightCameraBlank ^= 1
        ...

    def function_rightPlayButtonClick(self, *args):  # 功能动作训练-右手播放
        if self.function_rightIsPlaying:
            self.function_rightPlayButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaStop))
            self.function_rightPlayButton.setText("停止")
            self.function_rightIsPlaying = False

        else:
            self.function_rightPlayButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaPlay))
            self.function_rightPlayButton.setText("播放")
            self.function_rightIsPlaying = True
        ...

    def function_rightStopButtonClick(self, *args):  # 功能动作训练-右手重新开始
        ...

    def function_rightRecoderButtonClick(self, *args):  # 功能动作训练-右手录制
        if self.recordFlag != 0:  # 1-left 2-right
            self.recordFlag = 0
            path = QFileDialog.getExistingDirectory()
            if path != '':
                savePath = f"{path}/{tool.Tools.getNowTime()}_function_right.mp4".replace(
                    "//", "/")
                recorder = tool.VideoHelper.VideoWriter(savePath, 'mp4', 24, (550, 520))
                for i in self.recordSheet:
                    recorder.saveFigByImg(i)
                recorder.save()
                self.recordSheet = []
            else:
                return
        else:
            self.recordFlag = 2
        ...

    def function_cancelButtonClick(self, *args):  # 功能动作训练-全部取消
        ...

    def function_selectAllButtonClick(self, *args):  # 功能动作训练-全部选择
        ...

    def mirror_leftMirrorButtonClick(self, *args):  # 镜像训练-左手镜像
        self.leftCameraFlip ^= 1
        ...

    def mirror_leftCopyButtonClick(self, *args):  # 镜像训练-左手复制
        ...

    def mirror_leftMaskButtonClick(self, *args):  # 镜像训练-左手遮罩
        self.leftCameraBlank ^= 1
        ...

    def mirror_leftPlayButtonClick(self, *args):  # 镜像训练-左手播放
        if self.mirror_leftIsPlaying:
            self.mirror_leftPlayButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaStop))
            self.mirror_leftPlayButton.setText("停止")
            self.mirror_leftIsPlaying = False

        else:
            self.mirror_leftPlayButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaPlay))
            self.mirror_leftPlayButton.setText("播放")
            self.mirror_leftIsPlaying = True
        ...

    def mirror_startButtonClick(self,*args):
        if self.mirror_isPlaying:
            self.mirror_startButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaStop))
            self.mirror_startButton.setText("停止训练")
            self.mirror_isPlaying = False

        else:
            self.mirror_startButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaPlay))
            self.mirror_startButton.setText("开始训练")
            self.mirror_isPlaying = True


    def mirror_leftRecoderButtonClick(self, *args):  # 镜像训练-左手录制
        if self.recordFlag != 0:  # 1-left 2-right
            self.recordFlag = 0
            path = QFileDialog.getExistingDirectory()
            if path != '':
                savePath = f"{path}/{tool.Tools.getNowTime()}_mirror_left.mp4".replace("//", "/")
                recorder = tool.VideoHelper.VideoWriter(savePath, 'mp4', 24, (550, 520))
                for i in self.recordSheet:
                    recorder.saveFigByImg(i)
                recorder.save()
                self.recordSheet = []
            else:
                return
        else:
            self.recordFlag = 1
        ...

    def mirror_rightMirrorButtonClick(self, *args):  # 镜像训练-右手镜像
        self.rightCameraFlip ^= 1
        ...

    def mirror_rightCopyButtonClick(self, *args):  # 镜像训练-右手复制
        ...

    def mirror_rightMaskButtonClick(self, *args):  # 镜像训练-右手遮罩
        self.rightCameraBlank ^= 1
        ...

    def mirror_rightPlayButtonClick(self, *args):  # 镜像训练-右手播放
        if self.mirror_rightIsPlaying:
            self.mirror_rightPlayButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaStop))
            self.mirror_rightPlayButton.setText("停止")
            self.mirror_rightIsPlaying = False
            self.beginTime = tool.Tools.getNowTime()

        else:
            self.mirror_rightPlayButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaPlay))
            self.mirror_rightPlayButton.setText("播放")
            self.mirror_rightIsPlaying = True
            pic = self.grab()
            pic_id = tool.Tools.getTimeStamp()
            pic.save(f"{config.GlobalPath}save/mirror/{pic_id}.png")
            result = {"id": self.patient_id,
                      'end_time': tool.Tools.getNowTime(),
                      'train': "自主镜像训练",
                      'status': "已完成",
                      'pic': pic_id,
                      'begin_time': self.beginTime,
                      'detail': self.trainDetailSheet}
            requests.post(config.trainInfoInsert, data=result)
        ...

    def mirror_rightRecoderButtonClick(self, *args):  # 镜像训练-右手录制
        if self.recordFlag != 0:  # 1-left 2-right
            self.recordFlag = 0
            path = QFileDialog.getExistingDirectory()
            if path != '':
                savePath = f"{path}/{tool.Tools.getNowTime()}_mirror_right.mp4".replace("//", "/")
                recorder = tool.VideoHelper.VideoWriter(savePath, 'mp4', 24, (550, 520))
                for i in self.recordSheet:
                    recorder.saveFigByImg(i)
                recorder.save()
                self.recordSheet = []
            else:
                return
        else:
            self.recordFlag = 1
        ...
        ...

    def mirror_historyRecordButtonClick(self, *args):  # 镜像训练——显示视频历史记录
        ...

    def sensorimotor_leftMirrrorButtonClick(self, *args):  # 感觉运动训练-左手镜像
        self.leftCameraFlip ^= 1
        ...

    def sensorimotor_leftCopyButtonClick(self, *args):  # 感觉运动训练-左手复制
        ...

    def sensorimotor_leftMaskButtonClick(self, *args):  # 感觉运动训练-左手遮罩
        self.leftCameraBlank ^= 1
        ...

    def sensorimotor_leftPlayButtonClick(self, *args):  # 感觉运动训练-左手播放
        if self.sensorimotor_leftIsPlaying:
            self.sensorimotor_leftPlayButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaStop))
            self.sensorimotor_leftPlayButton.setText("停止")
            self.sensorimotor_leftIsPlaying = False
        else:
            self.sensorimotor_leftPlayButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaPlay))
            self.sensorimotor_leftPlayButton.setText("播放")
            self.sensorimotor_leftIsPlaying = True
        ...

    def sensorimotor_leftRecoderButtonClick(self, *args):  # 感觉运动训练-左手录制
        if self.recordFlag != 0:  # 1-left 2-right
            self.recordFlag = 0
            path = QFileDialog.getExistingDirectory()
            if path != '':
                savePath = f"{path}/{tool.Tools.getNowTime()}_sensorimotor_left.mp4".replace(
                    "//", "/")
                print(savePath)
                print(len(self.recordSheet))
                recorder = tool.VideoHelper.VideoWriter(savePath, 'mp4', 24, (550, 520))
                for i in self.recordSheet:
                    recorder.saveFigByImg(i)
                recorder.save()
                self.recordSheet = []
            else:
                return
        else:
            self.recordFlag = 1

    def sensorimotor_rightMirrorButtonClick(self, *args):  # 感觉运动训练-右手镜像
        self.rightCameraFlip ^= 1
        ...

    def sensorimotor_rightCopyButtonClick(self, *args):  # 感觉运动训练-右手复制
        ...

    def sensorimotor_rightMaskButtonClick(self, *args):  # 感觉运动训练-右手遮罩
        self.rightCameraBlank ^= 1
        ...

    def sensorimotor_rightPlayButtonClick(self, *args):  # 感觉运动训练-右手播放
        if self.sensorimotor_rightIsPlaying:
            self.sensorimotor_rightPlayButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaStop))
            self.sensorimotor_rightPlayButton.setText("停止")
            self.sensorimotor_rightIsPlaying = False


        else:
            self.sensorimotor_rightPlayButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaPlay))
            self.sensorimotor_rightPlayButton.setText("播放")
            self.sensorimotor_rightIsPlaying = True
        ...

    def sensorimotor_rightRecoderButtonClick(self, *args):  # 感觉运动训练-右手录制
        if self.recordFlag != 0:  # 1-left 2-right
            self.recordFlag = 0
            path = QFileDialog.getExistingDirectory()
            if path != '':
                savePath = f"{path}/{tool.Tools.getNowTime()}_sensorimotor_right.mp4".replace(
                    "//", "/")
                recorder = tool.VideoHelper.VideoWriter(savePath, 'mp4', 24, (550, 520))
                for i in self.recordSheet:
                    recorder.saveFigByImg(i)
                recorder.save()
                self.recordSheet = []
            else:
                return
        else:
            self.recordFlag = 2

    def sensorimotor_historyRecordButtonClick(self, *args):  # 感觉运动训练-显示视频历史记录
        ...

    def sensorimotor_leftStopButtonClick(self, *args):  # 感觉运动训练-左手重新开始
        ...

    def sensorimotor_rightStopButtonClick(self, *args):  # 感觉运动训练-右手重新开始
        ...

    def sensorimotor_cancelButtonClick(self, *args):  # 感觉运动训练-全部取消
        ...

    def sensorimotor_selectAllButtonClick(self, *args):  # 感觉运动训练-全选
        ...

    def sensorimotor_startButtonClick(self, *args):  # 感觉运动训练-开始训练
        _translate = QtCore.QCoreApplication.translate
        self.sensorimotor_selectTrainingFrame.setVisible(False)  # 功能动作训练容器
        self.sensorimotor_traingSituationFrame.setVisible(True)  # 功能动作-训练情况显示窗口
        if self.sensorimotor_isPlaying:
            self.sensorimotor_startButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaStop))
            self.sensorimotor_startButton.setText("停止训练")
            self.sensorimotor_selectTrainingFrame.setVisible(False)  # 功能动作训练容器
            self.sensorimotor_traingSituationFrame.setVisible(True)
            self.sensorimotor_isPlaying = False

            self.sensorimotorVideoSheet = ["straight_left_1.mp4", "straight_right_1.mp4"]  #

            self.sensorimotor_type = self.sensorimotor_trainingWayComboBox.currentText()
            if self.sensorimotor_type == '':
                self.sensorimotor_type = 'AABB'

            self.sensorimotorTrainTime: int = self.sensorimotor_trainingGroupNumLineEdit.text()
            if self.sensorimotorTrainTime == '':
                self.sensorimotorTrainTime = 1
            else:
                try:
                    self.sensorimotorTrainTime = int(self.sensorimotorTrainTime)
                except:
                    self.sensorimotorTrainTime = 1

            self.sensorimotorShowTime: int = self.sensorimotor_trainingNumLineEdit.text()
            if self.sensorimotorShowTime == '':
                self.sensorimotorShowTime = 1
            else:
                try:
                    self.sensorimotorShowTime = int(self.sensorimotorShowTime)
                except:
                    self.sensorimotorShowTime = 1

            self.sensorimotorPlaySpeed = self.sensorimotor_playSppedComBox.currentText()
            if self.sensorimotorPlaySpeed == '':
                self.sensorimotorPlaySpeed = 1

            # self.sensorimotor_trainingMode.setText(_translate("Form", self.sensorimotor_type))
            # self.sensorimotor_trainingTotalNumLabel.setText(_translate("Form", str(self.sensorimotorTrainTime)))
            # self.sensorimotor_trainingCurrentNumLabel.setText(_translate("Form", str(self.sensorimotorShowTime)))

            self.sensorimotorTask = threading.Thread(target=self.sensorimotor_startTask)
            self.sensorimotorTask.start()


        else:
            self.sensorimotor_startButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaPlay))
            self.sensorimotor_startButton.setText("开始训练")
            self.sensorimotor_selectTrainingFrame.setVisible(True)  # 功能动作训练容器
            self.sensorimotor_traingSituationFrame.setVisible(False)
            self.sensorimotor_isPlaying = True
            self.threadHelper = tool.ThreadingHelper.ThreadingHelper()
            self.threadHelper.close(self.sensorimotorTask)
        ...

    def sensorimotor_startTask(self):
        _translate = QtCore.QCoreApplication.translate
        if self.sensorimotor_type == "AABB":
            for i in self.sensorimotorVideoSheet:
                for trainTime in range(self.sensorimotorTrainTime):
                    self.sensorimotor_trainingNameLabel.setText(_translate("Form", i))
                    for runTime in range(self.sensorimotorShowTime):
                        cap = cv2.VideoCapture(config.GlobalPath + "src/video/basic/" + i)
                        print(i)
                        while True:
                            ret, frame = cap.read()
                            if not ret:
                                break
                            cv2.imwrite('temp.png', cv2.resize(frame, (680, 350)))
                            self.sensorimotorVideoImage = QPixmap('temp.png')
                            self.sensorimotor_showVideoLabel.setPixmap(self.sensorimotorVideoImage)
                        cap.release()
                    try:
                        os.remove('temp.png')
                    except:
                        pass
        else:  # ABAB
            for trainTime in range(self.sensorimotorTrainTime):
                for i in self.sensorimotorVideoSheet:
                    self.sensorimotor_trainingNameLabel.setText(_translate("Form", i))
                    for runTime in range(self.sensorimotorShowTime):
                        cap = cv2.VideoCapture(config.GlobalPath + "src/video/basic/" + i)
                        print(i)
                        while True:
                            ret, frame = cap.read()
                            if not ret:
                                break
                            cv2.imwrite('temp.png', cv2.resize(frame, (680, 350)))
                            self.sensorimotorVideoImage = QPixmap('temp.png')
                            self.sensorimotor_showVideoLabel.setPixmap(self.sensorimotorVideoImage)
                        cap.release()
                    try:
                        os.remove('temp.png')
                    except:
                        pass
        pic = self.grab()
        pic_id = tool.Tools.getTimeStamp()
        print(f"{config.GlobalPath}save/sensorimotor/{pic_id}.png")
        pic.save(f"{config.GlobalPath}save/sensorimotor/{pic_id}.png")
        result = {"id": self.patient_id,
                  'end_time': tool.Tools.getNowTime(),
                  'train': "感觉运动训练",
                  'status': "已完成",
                  'pic': pic_id,
                  'begin_time': self.beginTime,
                  'detail': self.trainDetailSheet}
        requests.post(config.trainInfoInsert, data=result)

        self.sensorimotor_startButton.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaPlay))
        self.sensorimotor_startButton.setText("开始训练")
        self.sensorimotor_selectTrainingFrame.setVisible(True)  # 功能动作训练容器
        self.sensorimotor_traingSituationFrame.setVisible(False)
        self.sensorimotor_isPlaying = True

    def sensorimotor_trainingModeComboBoxClick(self, *args):  # 感觉运动训练-选择训练模式
        if self.sensorimotor_trainingModeComboBox.currentIndex() == 1:  # 单侧模式视频延迟播放次数
            self.sensorimotor_setOneDelayPlayVideoFrame.setVisible(True)
            self.sensorimotor_setTwoDelayPlayVideoFrame.setVisible(False)
            self.sensorimotor_setOneTwoDelayPlayVideoFrame.setVisible(False)
        elif self.sensorimotor_trainingModeComboBox.currentIndex() == 2:
            self.sensorimotor_setTwoDelayPlayVideoFrame.setVisible(True)
            self.sensorimotor_setOneDelayPlayVideoFrame.setVisible(False)
            self.sensorimotor_setOneTwoDelayPlayVideoFrame.setVisible(False)
        else:
            self.sensorimotor_setOneTwoDelayPlayVideoFrame.setVisible(True)
            self.sensorimotor_setOneDelayPlayVideoFrame.setVisible(False)
            self.sensorimotor_setTwoDelayPlayVideoFrame.setVisible(False)
        ...


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = trianging('1')
    gui.show()
    sys.exit(app.exec_())
