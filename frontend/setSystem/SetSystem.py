import json
import os
import sys

import cv2
import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem

import config
import frontend


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.setSystemSpaceImageAddButtonInterfaceWindow = frontend.setSystem.SetSystemSpaceImageAddButtonInterface.setSystemSpaceImageAddButtonInterface()  # 空间想象上传图片界面
        self.setSystemSpaceImageEditDataInterfaceWindow = frontend.setSystem.SetSystemSpaceImageEditDataInterface.setSystemSpaceImageEditDataInterface()  # 点击表格中数据跳出来的页面
        self.setSystemSpaceImageDeleteButtonInterfaceWindow = frontend.setSystem.SetSystemSpaceImageDeleteButtonInterface.setSystemSpaceImageDeleteButtonInterface()

        self.body_frame = QtWidgets.QFrame(self.centralwidget)  # 主界面背景色
        self.body_frame.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.body_frame.setStyleSheet("QFrame{background-color:rgb(242,249,255)}")
        self.body_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.menu_frame = QtWidgets.QFrame(self.body_frame)  # 按钮位置背景色
        self.menu_frame.setGeometry(QtCore.QRect(60, 40, 371, 930))
        self.menu_frame.setMaximumSize(QtCore.QSize(531, 930))
        self.menu_frame.setStyleSheet("QFrame{background-color:rgb(255, 255, 255)}")
        self.menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.label = QtWidgets.QLabel(self.menu_frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 371, 60))
        self.label.setText('系统设置')
        self.label.setStyleSheet("font:14pt;color:white;background:rgb(0,138,200)")

        # 系统设置-空间想象训练参数设置按钮
        self.space_training_parameter_setting_button = QtWidgets.QPushButton(self.menu_frame)
        self.space_training_parameter_setting_button.setGeometry(QtCore.QRect(0, 60, 371, 60))

        # 系统设置-感觉运动观察训练参数设置按钮
        self.sensorimotor_observation_setting_button = QtWidgets.QPushButton(self.menu_frame)
        self.sensorimotor_observation_setting_button.setGeometry(QtCore.QRect(0, 120, 371, 60))

        # 系统设置-基本动作训练参数设置按钮
        self.basic_parameter_setting_button = QtWidgets.QPushButton(self.menu_frame)
        self.basic_parameter_setting_button.setText('基本动作训练参数设置')
        self.basic_parameter_setting_button.setGeometry(QtCore.QRect(0, 180, 371, 60))

        # 系统设置- 功能动作训练参数设置按钮
        self.function_parameter_setting_button = QtWidgets.QPushButton(self.menu_frame)
        self.function_parameter_setting_button.setGeometry(QtCore.QRect(0, 240, 371, 60))

        self.main_widget = QtWidgets.QStackedWidget(self.body_frame)  # 堆叠窗口
        self.main_widget.setGeometry(QtCore.QRect(540, 40, 1231, 930))
        self.main_widget.setMaximumSize(QtCore.QSize(16777215, 930))
        self.main_widget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.main_widget.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.space_training_parameter_setting_widget = QtWidgets.QWidget()  # 空间想象训练窗口
        self.space_training_parameter_setting_widget.setStyleSheet("background-color: rgb(241,250,255);")

        self.space_training_discrimination_difficulty_text = QtWidgets.QTextEdit(
            self.space_training_parameter_setting_widget)  # 辨别难度
        self.space_training_discrimination_difficulty_text.setGeometry(QtCore.QRect(20, 120, 171, 41))
        self.space_training_discrimination_difficulty_text.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.space_training_discrimination_difficulty_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.space_training_discrimination_difficulty_text.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)

        self.space_training_picture_type_text = QtWidgets.QTextEdit(
            self.space_training_parameter_setting_widget)  # 图片类型
        self.space_training_picture_type_text.setGeometry(QtCore.QRect(370, 120, 161, 41))
        self.space_training_picture_type_text.setFrameShape(QtWidgets.QFrame.NoFrame)

        # 系统设置-空间想象训练参数设置-难度选择
        self.space_training_discrimination_difficulty_comboBox = QtWidgets.QComboBox(
            self.space_training_parameter_setting_widget)
        self.space_training_discrimination_difficulty_comboBox.setGeometry(QtCore.QRect(160, 120, 161, 31))
        self.space_training_discrimination_difficulty_comboBox.addItems(['', '低难度', '中难度', '高难度'])
        self.space_training_discrimination_difficulty_comboBox.setStyleSheet('background:white;font:12pt')

        self.space_training_parameter_setting = QtWidgets.QLabel(self.space_training_parameter_setting_widget)
        self.space_training_parameter_setting.setGeometry(QtCore.QRect(10, 0, 500, 71))
        self.space_training_parameter_setting.setText('空间想象训练参数设置')
        self.space_training_parameter_setting.setAlignment(Qt.AlignCenter)
        self.space_training_parameter_setting.setStyleSheet(
            "color: rgb(255, 255, 255);background-color: rgb(0,138,200);font:16pt")

        # 系统设置-空间想象训练参数设置-图片类型选择
        self.space_training_picture_type_comboBox = QtWidgets.QComboBox(self.space_training_parameter_setting_widget)
        self.space_training_picture_type_comboBox.setGeometry(QtCore.QRect(500, 120, 161, 31))
        self.space_training_picture_type_comboBox.addItems(['', '左', '右'])
        self.space_training_picture_type_comboBox.setStyleSheet('background:white;font:12pt')

        # 系统设置-空间想象训练参数设置-查询按钮
        self.space_training_query_button = QtWidgets.QPushButton(self.space_training_parameter_setting_widget)
        self.space_training_query_button.setGeometry(QtCore.QRect(730, 120, 111, 41))
        self.space_training_query_button.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(0,138,200);")

        # 系统设置-空间想象训练参数设置-增加按钮
        self.space_training_add_button = QtWidgets.QPushButton(self.space_training_parameter_setting_widget)
        self.space_training_add_button.setGeometry(QtCore.QRect(890, 120, 111, 41))
        self.space_training_add_button.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(0,138,200);")

        # 系统设置-空间想象训练参数设置-批量删除按钮
        self.space_training_delet_button = QtWidgets.QPushButton(self.space_training_parameter_setting_widget)
        self.space_training_delet_button.setGeometry(QtCore.QRect(1050, 120, 111, 41))
        self.space_training_delet_button.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(0,138,200);")

        # 系统设置-空间想象训练参数设置-显示参数表格
        self.space_training_table = QtWidgets.QTableWidget(self.space_training_parameter_setting_widget)
        self.space_training_table.setGeometry(QtCore.QRect(40, 260, 1161, 550))
        self.space_training_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.space_training_table.setStyleSheet('background:white;font:14pt')
        self.space_training_table.setColumnCount(3)
        self.space_training_table.setRowCount(20)
        self.space_training_table.horizontalHeader().setDefaultSectionSize(200)
        self.space_training_table.horizontalHeader().setMinimumSectionSize(50)
        self.space_training_table.horizontalHeader().setStretchLastSection(True)
        self.space_training_table.verticalHeader().setDefaultSectionSize(40)
        self.space_training_table.verticalHeader().setMinimumSectionSize(40)
        self.space_training_table.verticalHeader().setSortIndicatorShown(False)
        self.space_training_table.verticalHeader().setStretchLastSection(False)
        self.space_training_table.setHorizontalHeaderLabels(['名称', '辨别难度', '图片类型'])
        self.space_training_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.space_training_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.space_training_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.space_training_table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.space_training_table.setSelectionBehavior(QHeaderView.SelectRows)
        self.space_training_table.setSelectionMode(QTableWidget.SingleSelection)
        self.main_widget.addWidget(self.space_training_parameter_setting_widget)

        self.sensorimotor_observation_setting_widget = QtWidgets.QWidget()  # 感觉运动观察训练堆叠窗口
        self.sensorimotor_observation_setting_widget.setStyleSheet("background-color: rgb(241,250,255);")

        # 系统设置-感觉运动观察训练参数设置-查询按钮
        self.sensorimotor_observation_query_button = QtWidgets.QPushButton(self.sensorimotor_observation_setting_widget)
        self.sensorimotor_observation_query_button.setGeometry(QtCore.QRect(940, 130, 111, 41))
        self.sensorimotor_observation_query_button.setStyleSheet(
            "color: rgb(255, 255, 255);background-color: rgb(0,138,200);")

        self.label_1 = QtWidgets.QLabel(self.sensorimotor_observation_setting_widget)
        self.label_1.setGeometry(QtCore.QRect(10, 130, 200, 31))
        self.label_1.setText('动作名称:')
        self.label_1.setStyleSheet("font:12pt;")

        # 系统设置-感觉运动观察训练参数设置-动作名称
        self.sensorimotor_observation_active_name_lineEdit = QtWidgets.QLineEdit(
            self.sensorimotor_observation_setting_widget)
        self.sensorimotor_observation_active_name_lineEdit.setGeometry(QtCore.QRect(120, 130, 200, 31))
        self.sensorimotor_observation_active_name_lineEdit.setStyleSheet('background:white;font:12pt')

        self.sensorimotor_observation_table = QtWidgets.QTableWidget(self.sensorimotor_observation_setting_widget)
        self.sensorimotor_observation_table.setGeometry(QtCore.QRect(30, 270, 1161, 550))
        self.sensorimotor_observation_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sensorimotor_observation_table.setStyleSheet('background:white;font:14pt')
        self.sensorimotor_observation_table.setColumnCount(3)
        self.sensorimotor_observation_table.setRowCount(20)
        self.sensorimotor_observation_table.horizontalHeader().setStretchLastSection(True)
        self.sensorimotor_observation_table.verticalHeader().setStretchLastSection(False)
        self.sensorimotor_observation_table.setHorizontalHeaderLabels(['名称', '动作类型', '功能类型'])
        self.sensorimotor_observation_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sensorimotor_observation_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.sensorimotor_observation_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.sensorimotor_observation_table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.sensorimotor_observation_table.setSelectionBehavior(QHeaderView.SelectRows)
        self.sensorimotor_observation_table.setSelectionMode(QTableWidget.SingleSelection)

        self.sensorimotor_observation_setting = QtWidgets.QLabel(self.sensorimotor_observation_setting_widget)
        self.sensorimotor_observation_setting.setGeometry(QtCore.QRect(0, 10, 500, 71))
        self.sensorimotor_observation_setting.setAlignment(Qt.AlignCenter)
        self.sensorimotor_observation_setting.setStyleSheet(
            "color: rgb(255, 255, 255);background-color: rgb(0,138,200);font:16pt")
        self.sensorimotor_observation_setting.setText('感觉运动观察训练参数设置')

        self.sensorimotor_observation_add_button = QtWidgets.QPushButton(self.sensorimotor_observation_setting_widget)
        self.sensorimotor_observation_add_button.setGeometry(QtCore.QRect(1080, 130, 111, 41))
        self.sensorimotor_observation_add_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                               "background-color: rgb(0,138,200);")

        self.sensorimotor_observation_home_page = QtWidgets.QPushButton(self.sensorimotor_observation_setting_widget)
        self.sensorimotor_observation_home_page.setGeometry(QtCore.QRect(80, 850, 120, 40))
        self.sensorimotor_observation_home_page.setStyleSheet("background-color: rgb(255, 255, 255);font:12pt")

        self.sensorimotor_observation_previous_page = QtWidgets.QPushButton(
            self.sensorimotor_observation_setting_widget)
        self.sensorimotor_observation_previous_page.setGeometry(QtCore.QRect(220, 850, 120, 40))
        self.sensorimotor_observation_previous_page.setStyleSheet("background-color: rgb(255, 255, 255);font:12pt")

        self.sensorimotor_observation_next_page = QtWidgets.QPushButton(self.sensorimotor_observation_setting_widget)
        self.sensorimotor_observation_next_page.setGeometry(QtCore.QRect(360, 850, 120, 40))
        self.sensorimotor_observation_next_page.setStyleSheet("background-color: rgb(255, 255, 255);font:12pt")

        self.sensorimotor_observation_lastpage = QtWidgets.QPushButton(self.sensorimotor_observation_setting_widget)
        self.sensorimotor_observation_lastpage.setGeometry(QtCore.QRect(500, 850, 120, 40))
        self.sensorimotor_observation_lastpage.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.sensorimotor_observation_lastpage.setStyleSheet("background-color: rgb(255, 255, 255);font:12pt")

        self.active_typeLabel = QtWidgets.QLabel(self.sensorimotor_observation_setting_widget)
        self.active_typeLabel.setGeometry(QtCore.QRect(330, 130, 161, 41))
        self.active_typeLabel.setText('动作类型:')
        self.active_typeLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.active_typeLabel.setStyleSheet("font:12pt;")

        # 系统设置-感觉运动观察训练参数设置-动作类型
        self.sensorimotor_observation_active_type_comboBox = QtWidgets.QComboBox(
            self.sensorimotor_observation_setting_widget)
        self.sensorimotor_observation_active_type_comboBox.setGeometry(QtCore.QRect(440, 130, 200, 31))
        self.sensorimotor_observation_active_type_comboBox.addItems(['', '浅感觉', '深感觉', '复合感觉'])
        self.sensorimotor_observation_active_type_comboBox.setStyleSheet('background:white;font:12pt')

        self.label_2 = QtWidgets.QLabel(self.sensorimotor_observation_setting_widget)
        self.label_2.setGeometry(QtCore.QRect(650, 130, 200, 31))
        self.label_2.setText('功能类型:')
        self.label_2.setStyleSheet("font:12pt;")

        self.sensorimotor_observation_active_specification_comboBox = QtWidgets.QComboBox(
            self.sensorimotor_observation_setting_widget)
        self.sensorimotor_observation_active_specification_comboBox.setGeometry(QtCore.QRect(760, 130, 150, 31))
        self.sensorimotor_observation_active_specification_comboBox.setStyleSheet('font:12pt')
        self.sensorimotor_observation_active_specification_comboBox.addItems(['', '左', '右'])
        self.sensorimotor_observation_active_specification_comboBox.setStyleSheet('background:white;font:12pt')
        self.main_widget.addWidget(self.sensorimotor_observation_setting_widget)

        self.basic_parameter_setting_widget = QtWidgets.QWidget()
        self.basic_parameter_setting_widget.setStyleSheet("background-color: rgb(241,250,255);")

        self.basic_parameter_setting = QtWidgets.QLabel(self.basic_parameter_setting_widget)
        self.basic_parameter_setting.setGeometry(QtCore.QRect(10, 10, 500, 71))
        self.basic_parameter_setting.setText('基本动作训练参数设置')
        self.basic_parameter_setting.setAlignment(Qt.AlignCenter)
        self.basic_parameter_setting.setStyleSheet(
            "color: rgb(255, 255, 255);background-color: rgb(0,138,200);font:16pt")

        self.label_4 = QtWidgets.QLabel(self.basic_parameter_setting_widget)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 171, 41))
        self.label_4.setText('动作名称:')
        self.label_4.setStyleSheet('font:14pt')

        self.basic_activeNameQLineEdit = QtWidgets.QLineEdit(self.basic_parameter_setting_widget)
        self.basic_activeNameQLineEdit.setGeometry(QtCore.QRect(160, 130, 161, 35))
        self.basic_activeNameQLineEdit.setStyleSheet('font:12pt;background:white')

        self.label_3 = QtWidgets.QLabel(self.basic_parameter_setting_widget)
        self.label_3.setGeometry(QtCore.QRect(330, 130, 161, 41))
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setText('动作类型:')
        self.label_3.setStyleSheet('font:14pt')

        self.basic_active_type_comboBox = QtWidgets.QComboBox(self.basic_parameter_setting_widget)
        self.basic_active_type_comboBox.setGeometry(QtCore.QRect(460, 130, 200, 35))
        self.basic_active_type_comboBox.addItems(
            ['', '拇指运动', '精细灵活性运动', '抓握运动', '手指动作', '腕部运动', '前臂旋转'])
        self.basic_active_type_comboBox.setStyleSheet('background:white;font:12pt')

        self.label_5 = QtWidgets.QLabel(self.basic_parameter_setting_widget)
        self.label_5.setGeometry(QtCore.QRect(670, 130, 161, 41))
        self.label_5.setText('功能类型:')
        self.label_5.setStyleSheet('font:14pt')

        self.basic_active_specification_comboBox = QtWidgets.QComboBox(self.basic_parameter_setting_widget)
        self.basic_active_specification_comboBox.setGeometry(QtCore.QRect(800, 130, 161, 35))
        self.basic_active_specification_comboBox.addItems(['', '左', '右'])
        self.basic_active_specification_comboBox.setStyleSheet('background:white;font:12pt')

        self.basic_query_button = QtWidgets.QPushButton(self.basic_parameter_setting_widget)
        self.basic_query_button.setGeometry(QtCore.QRect(970, 130, 111, 41))
        self.basic_query_button.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(0,138,200);font:12pt")
        self.basic_query_button.setText('查询')

        self.basic_add_button = QtWidgets.QPushButton(self.basic_parameter_setting_widget)
        self.basic_add_button.setGeometry(QtCore.QRect(1090, 130, 120, 40))
        self.basic_add_button.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(0,138,200);font:12pt")
        self.basic_add_button.setText('增加')

        self.basic_table = QtWidgets.QTableWidget(self.basic_parameter_setting_widget)
        self.basic_table.setGeometry(QtCore.QRect(40, 270, 1161, 550))
        self.basic_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.basic_table.setStyleSheet('background:white;font:14pt')
        self.basic_table.setColumnCount(3)
        self.basic_table.setRowCount(20)
        self.basic_table.horizontalHeader().setDefaultSectionSize(200)
        self.basic_table.horizontalHeader().setMinimumSectionSize(50)
        self.basic_table.horizontalHeader().setStretchLastSection(True)
        self.basic_table.verticalHeader().setDefaultSectionSize(40)
        self.basic_table.verticalHeader().setMinimumSectionSize(40)
        self.basic_table.verticalHeader().setSortIndicatorShown(False)
        self.basic_table.verticalHeader().setStretchLastSection(False)
        self.basic_table.setHorizontalHeaderLabels(['名称', '动作类型', '功能类型'])
        self.basic_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.basic_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.basic_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.basic_table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.basic_table.setSelectionBehavior(QHeaderView.SelectRows)
        self.basic_table.setSelectionMode(QTableWidget.SingleSelection)

        self.basic_home_page = QtWidgets.QPushButton(self.basic_parameter_setting_widget)
        self.basic_home_page.setGeometry(QtCore.QRect(90, 850, 120, 40))
        self.basic_home_page.setStyleSheet("background-color: rgb(255, 255, 255);font:12pt")
        self.basic_home_page.setText('首页')

        self.basic_previous_page = QtWidgets.QPushButton(self.basic_parameter_setting_widget)
        self.basic_previous_page.setGeometry(QtCore.QRect(250, 850, 120, 40))
        self.basic_previous_page.setStyleSheet("background-color: rgb(255, 255, 255);font:12pt")
        self.basic_previous_page.setText('上一页')

        self.basic_next_page = QtWidgets.QPushButton(self.basic_parameter_setting_widget)
        self.basic_next_page.setGeometry(QtCore.QRect(410, 850, 120, 40))
        self.basic_next_page.setText('下一页')
        self.basic_next_page.setStyleSheet("background-color: rgb(255, 255, 255);font:12pt")

        self.basic_lastpage = QtWidgets.QPushButton(self.basic_parameter_setting_widget)
        self.basic_lastpage.setGeometry(QtCore.QRect(570, 850, 120, 40))
        self.basic_lastpage.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.basic_lastpage.setStyleSheet("background-color: rgb(255, 255, 255);font:12pt")
        self.basic_lastpage.setText('尾页')

        self.main_widget.addWidget(self.basic_parameter_setting_widget)

        self.function_parameter_setting_widget = QtWidgets.QWidget()
        self.function_parameter_setting_widget.setStyleSheet("background-color: rgb(241,250,255);")
        self.function_parameter_setting = QtWidgets.QLabel(self.function_parameter_setting_widget)
        self.function_parameter_setting.setGeometry(QtCore.QRect(10, 10, 500, 71))
        self.function_parameter_setting.setAlignment(Qt.AlignCenter)
        self.function_parameter_setting.setText('功能动作训练参数设置')
        self.function_parameter_setting.setStyleSheet(
            "color: rgb(255, 255, 255);background-color: rgb(0,138,200);font:16pt")

        self.label_6 = QtWidgets.QLabel(self.function_parameter_setting_widget)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 161, 41))
        self.label_6.setText('动作名称:')
        self.label_6.setStyleSheet('font:14pt')

        self.function_activeNameQLineEdit = QtWidgets.QLineEdit(self.function_parameter_setting_widget)
        self.function_activeNameQLineEdit.setGeometry(QtCore.QRect(140, 130, 170, 35))
        self.function_activeNameQLineEdit.setStyleSheet('background:white;font:12pt')

        self.label_7 = QtWidgets.QLabel(self.function_parameter_setting_widget)
        self.label_7.setGeometry(QtCore.QRect(320, 130, 161, 41))
        self.label_7.setText('动作类型:')
        self.label_7.setStyleSheet('font:14pt')

        self.function_active_type_comboBox = QtWidgets.QComboBox(self.function_parameter_setting_widget)
        self.function_active_type_comboBox.setGeometry(QtCore.QRect(450, 130, 200, 35))
        self.function_active_type_comboBox.addItems(
            ['', '精细动作', '复合旋转运动', '抓握运动', 'ADL活动', '双手联合运动'])
        self.function_active_type_comboBox.setStyleSheet('background:white;font:12pt')

        self.label_8 = QtWidgets.QLabel(self.function_parameter_setting_widget)
        self.label_8.setGeometry(QtCore.QRect(660, 130, 161, 41))
        self.label_8.setText('功能类型:')
        self.label_8.setStyleSheet('font:14pt')

        self.function_active_specification_comboBox = QtWidgets.QComboBox(self.function_parameter_setting_widget)
        self.function_active_specification_comboBox.setGeometry(QtCore.QRect(790, 130, 120, 35))
        self.function_active_specification_comboBox.addItems(['', '左', '右'])
        self.function_active_specification_comboBox.setStyleSheet('background:white;font:12pt')

        self.function_query_button = QtWidgets.QPushButton(self.function_parameter_setting_widget)
        self.function_query_button.setGeometry(QtCore.QRect(950, 130, 111, 41))
        self.function_query_button.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(0,138,200);font:12pt")

        self.function_add_button = QtWidgets.QPushButton(self.function_parameter_setting_widget)
        self.function_add_button.setGeometry(QtCore.QRect(1090, 130, 111, 41))
        self.function_add_button.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(0,138,200);font:12pt")

        self.function_table = QtWidgets.QTableWidget(self.function_parameter_setting_widget)
        self.function_table.setGeometry(QtCore.QRect(40, 270, 1161, 550))
        self.function_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.function_table.setStyleSheet('background:white;font:14pt')
        self.function_table.setColumnCount(3)
        self.function_table.setRowCount(20)
        self.function_table.horizontalHeader().setDefaultSectionSize(200)
        self.function_table.horizontalHeader().setMinimumSectionSize(50)
        self.function_table.horizontalHeader().setStretchLastSection(True)
        self.function_table.verticalHeader().setDefaultSectionSize(40)
        self.function_table.verticalHeader().setMinimumSectionSize(40)
        self.function_table.verticalHeader().setSortIndicatorShown(False)
        self.function_table.verticalHeader().setStretchLastSection(False)
        self.function_table.setHorizontalHeaderLabels(['名称', '动作类型', '功能类型'])
        self.function_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.function_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.function_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.function_table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.function_table.setSelectionBehavior(QHeaderView.SelectRows)
        self.function_table.setSelectionMode(QTableWidget.SingleSelection)

        self.function_home_page = QtWidgets.QPushButton(self.function_parameter_setting_widget)
        self.function_home_page.setGeometry(QtCore.QRect(90, 850, 120, 40))
        self.function_home_page.setStyleSheet("background-color: rgb(255, 255, 255);font:12pt")

        self.function_previous_page = QtWidgets.QPushButton(self.function_parameter_setting_widget)
        self.function_previous_page.setGeometry(QtCore.QRect(250, 850, 120, 40))
        self.function_previous_page.setStyleSheet("background-color: rgb(255, 255, 255);font:12pt")

        self.function_next_page = QtWidgets.QPushButton(self.function_parameter_setting_widget)
        self.function_next_page.setGeometry(QtCore.QRect(410, 850, 120, 40))
        self.function_next_page.setStyleSheet("background-color: rgb(255, 255, 255);font:12pt")

        self.function_lastpage = QtWidgets.QPushButton(self.function_parameter_setting_widget)
        self.function_lastpage.setGeometry(QtCore.QRect(570, 850, 120, 40))
        self.function_lastpage.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.function_lastpage.setStyleSheet("background-color: rgb(255, 255, 255);font:12pt")

        self.main_widget.addWidget(self.function_parameter_setting_widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.main_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.space_training_parameter_setting_button, self.function_parameter_setting_button)

        self.refreshButton = QtWidgets.QPushButton(self.body_frame)
        self.refreshButton.setGeometry(QtCore.QRect(1600, 0, 200, 60))
        self.refreshButton.setText("刷新")
        self.refreshButton.setStyleSheet("font:14pt;color:white;background:rgb(0,138,200)")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.space_training_parameter_setting_button.setText(_translate("MainWindow", "空间想象训练参数设置"))
        self.sensorimotor_observation_setting_button.setText(_translate("MainWindow", "感觉运动观察训练参数设置"))
        self.function_parameter_setting_button.setText(_translate("MainWindow", "功能动作训练参数设置"))
        self.space_training_discrimination_difficulty_text.setHtml(_translate("MainWindow",
                                                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD "
                                                                              "HTML 4.0//EN\" "
                                                                              "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                              "p, li { white-space: pre-wrap; }\n"
                                                                              "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">辨别难度：</span></p></body></html>"))
        self.space_training_picture_type_text.setHtml(_translate("MainWindow",
                                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                 "p, li { white-space: pre-wrap; }\n"
                                                                 "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">图片类型：</span></p></body></html>"))
        self.space_training_query_button.setText(_translate("MainWindow", "查询"))
        self.space_training_add_button.setText(_translate("MainWindow", "新增"))
        self.space_training_delet_button.setText(_translate("MainWindow", "批量删除"))
        self.sensorimotor_observation_query_button.setText(_translate("MainWindow", "查询"))
        self.sensorimotor_observation_lastpage.setText(_translate("MainWindow", "尾页"))
        self.sensorimotor_observation_add_button.setText(_translate("MainWindow", "新增"))
        self.sensorimotor_observation_next_page.setText(_translate("MainWindow", "下一页"))
        self.sensorimotor_observation_home_page.setText(_translate("MainWindow", "首页"))
        self.sensorimotor_observation_previous_page.setText(_translate("MainWindow", "上一页"))
        self.function_query_button.setText(_translate("MainWindow", "查询"))
        self.function_previous_page.setText(_translate("MainWindow", "上一页"))
        self.function_home_page.setText(_translate("MainWindow", "首页"))
        self.function_lastpage.setText(_translate("MainWindow", "尾页"))
        self.function_add_button.setText(_translate("MainWindow", "新增"))
        self.function_next_page.setText(_translate("MainWindow", "下一页"))


class setSystem(QtWidgets.QMainWindow, Ui_MainWindow):  # 基本功能动作训练
    def __init__(self):
        super(setSystem, self).__init__()
        self.setupUi(self)
        self.space_training_parameter_setting_button.clicked.connect(self.spaceTraining_parameterSettingButtonClick)
        self.space_training_add_button.clicked.connect(self.space_training_add_buttonClick)  # 系统设置-空间想象训练参数设置-增加按钮
        self.space_training_delet_button.clicked.connect(
            self.space_training_delete_buttonClick)  # 系统设置-空间想象训练参数设置-批量删除按钮
        self.sensorimotor_observation_setting_button.clicked.connect(self.sensorimotor_observationSettingButtonClick)
        self.basic_parameter_setting_button.clicked.connect(self.basic_parameter_setting_buttonClick)
        self.function_parameter_setting_button.clicked.connect(
            self.function_parameter_setting_buttonClick)  # 系统设置- 功能动作训练参数设置按钮
        self.space_training_table.doubleClicked.connect(self.space_training_click)
        self.refreshButton.clicked.connect(self.initForSearch)
        self.initForSearch()

    def spaceTraining_parameterSettingButtonClick(self, *args):  # 系统设置-空间想象训练参数设置按钮
        self.main_widget.setCurrentIndex(0)
        ...

    def space_training_click(self, *args):
        trans = {"左": "left", "右": "right", "低难度": "easy", "中难度": "mid", "高难度": "hard"}
        try:
            idx = int(self.space_training_table.selectedItems()[0].row())
        except:
            return
        diff = trans[self.spaceImageConfigList[idx]['difficult']]
        _type = trans[self.spaceImageConfigList[idx]['type']]
        pic_id = self.spaceImageConfigList[idx]['pic_id']
        img = cv2.imread(f"{config.GlobalPath}src/train/{diff}/{_type}/{pic_id}")
        cv2.imshow(self.spaceImageConfigList[idx]['name'], img)
        cv2.waitKey(0)
        ...

    def space_training_add_buttonClick(self, *args):  # 系统设置-空间想象训练参数设置按钮
        self.setSystemSpaceImageAddButtonInterfaceWindow.show()
        ...

    def space_training_delete_buttonClick(self, *args):  # 系统设置-空间想象训练参数设置-增加按钮
        self.setSystemSpaceImageDeleteButtonInterfaceWindow.show()
        ...

    def sensorimotor_observationSettingButtonClick(self, *args):  # 系统设置-空间想象训练参数设置-批量删除按钮
        self.main_widget.setCurrentIndex(1)
        ...

    def basic_parameter_setting_buttonClick(self, *args):  # 系统设置-基本动作训练参数设置按钮
        self.main_widget.setCurrentIndex(2)
        ...

    def function_parameter_setting_buttonClick(self, *args):  # 系统设置- 功能动作训练参数设置按钮
        self.main_widget.setCurrentIndex(3)
        ...

    def initForSearch(self):
        self.spaceImageConfigList = json.loads(requests.post(config.spaceImageConfigList).content.decode('utf-8'))[
            'data']
        self.space_training_table.setRowCount(max(len(self.spaceImageConfigList), 10))
        for i in range(len(self.spaceImageConfigList)):
            self.space_training_table.setItem(i, 0, QTableWidgetItem(self.spaceImageConfigList[i]['name']))
            self.space_training_table.setItem(i, 1, QTableWidgetItem(self.spaceImageConfigList[i]['difficult']))
            self.space_training_table.setItem(i, 2, QTableWidgetItem(self.spaceImageConfigList[i]['type']))
        self.sensorimotorObservationConfigList = None
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = setSystem()
    gui.show()
    sys.exit(app.exec_())
