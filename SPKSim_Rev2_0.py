# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import PyQt5,os
import ctypes
import sys,csv
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QShortcut
from PyQt5.QtGui import QKeySequence
from numpy import pi
import numpy as np
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
c = 343 # speed of sound at 20 C.
lo = 1.21


 # set the mainwindow can be disp_layed correctly in different DPI monitors (start)
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
 # set the mainwindow can be disp_lyed correctly in different DPI monitors (end)

def Params_Init(fc_num, sp_shape):
    Parameter_common = {"bc_v": 1,
                       "fv_v":0.03}
    Parameter_sp_c = {"sp_n": 3,
                      "sp_l": 0.8,
                      "sp_d": 1.3,
                      "Rmesh": 32}
    Parameter_sp_r = {"sp_n": 1,
                      "sp_l": 0.8,
                      "sp_w": 5,
                      "sp_h": 1.3,
                      "Rmesh": 32}
    Parameter_FC1 = {"fc1_l": 8,
                    "fc1_w": 6,
                    "fc1_h": 1.5}
    Parameter_FC2 = {"fc2_l": 4,
                    "fc2_w": 6,
                    "fc2_h": 1.5}
    Parameter_tn = {"tn_l": 1,
                    "tn_w": 6,
                    "tn_h": 4}
    Parameter_FC3 = {"fc3_l": 4,
                    "fc3_w": 6,
                    "fc3_h": 1.5}
    Parameter = Parameter_common
    if fc_num =="1x" and sp_shape =="Circular":
        Parameter.update(Parameter_sp_c)
        Parameter.update(Parameter_FC1)
    elif fc_num =="1x" and sp_shape =="Rectangular":
        Parameter.update(Parameter_sp_r)
        Parameter.update(Parameter_FC1)
    elif fc_num =="2x" and sp_shape =="Circular":
        Parameter.update(Parameter_sp_c)
        Parameter.update(Parameter_FC1)
        Parameter.update(Parameter_FC2)
    elif fc_num =="2x" and sp_shape =="Rectangular":
        Parameter.update(Parameter_sp_r)
        Parameter.update(Parameter_FC1)
        Parameter.update(Parameter_FC2)
    elif fc_num =="3x" and sp_shape =="Circular":
        Parameter.update(Parameter_sp_c)
        Parameter.update(Parameter_FC1)
        Parameter.update(Parameter_FC2)
        Parameter.update(Parameter_tn)
        Parameter.update(Parameter_FC3)
    elif fc_num =="3x" and sp_shape =="Rectangular":
        Parameter.update(Parameter_sp_r)
        Parameter.update(Parameter_FC1)
        Parameter.update(Parameter_FC2)
        Parameter.update(Parameter_tn)
        Parameter.update(Parameter_FC3)
    else:
        print("Not Selected")

    return Parameter


def Params_Init_Setup(fc_num, sp_shape):
    ID_1C = ["D01","D02","D03-1","D03-2","D03-3","D04","D05-1","D05-2","D05-3"]
    ID_1R = ["D01","D02","D03-1","D03-2","D03-3","D03-4","D04","D05-1","D05-2","D05-3"]
    ID_2C = ["D01","D02","D03-1","D03-2","D03-3","D04","D05-1","D05-2","D05-3","D06-1","D06-2","D06-3"]
    ID_2R = ["D01","D02","D03-1","D03-2","D03-3","D03-4","D04","D05-1","D05-2","D05-3","D06-1","D06-2","D06-3"]
    ID_3C = ["D01","D02","D03-1","D03-2","D03-3","D04","D05-1","D05-2","D05-3","D06-1","D06-2","D06-3",
             "D07-1","D07-2","D07-3","D08-1","D08-2","D08-3"]
    ID_3R = ["D01","D02","D03-1","D03-2","D03-3","D03-4","D04","D05-1","D05-2","D05-3","D06-1","D06-2","D06-3",
             "D07-1","D07-2","D07-3","D08-1","D08-2","D08-3"]

    Name_Parameters_1C = ["Back Chamber Volume (c.c.)","Front Space Volume (c.c.)",
                       "Sound Port Number","Sound Port Length (mm)",
                       "Sound Port Diameter (mm)","Mesh Rayl (Ohm)",
                       "Front Chamber (1) Length (mm)","Front Chamber (1) Width (mm)","Front Chamber (1) Height (mm)"]

    Name_Parameters_1R = ["Back Chamber Volume (c.c.)","Front Space Volume (c.c.)",
                       "Sound Port Number","Sound Port Length (mm)",
                       "Sound Port Width (mm)","Sound Port Height (mm)","Mesh Rayl (Ohm)",
                       "Front Chamber (1) Length (mm)","Front Chamber (1) Width (mm)","Front Chamber (1) Height (mm)"]

    Name_Parameters_2C = ["Back Chamber Volume (c.c.)","Front Space Volume (c.c.)",
                       "Sound Port Number","Sound Port Length (mm)",
                       "Sound Port Diameter (mm)","Mesh Rayl (Ohm)",
                       "Front Chamber (1) Length (mm)","Front Chamber (1) Width (mm)","Front Chamber (1) Height (mm)",
                       "Front Chamber (2) Length (mm)","Front Chamber (2) Width (mm)","Front Chamber (2) Height (mm)"]

    Name_Parameters_2R = ["Back Chamber Volume (c.c.)","Front Space Volume (c.c.)",
                       "Sound Port Number","Sound Port Length (mm)",
                       "Sound Port Width (mm)","Sound Port Height (mm)","Mesh Rayl (Ohm)",
                       "Front Chamber (1) Length (mm)","Front Chamber (1) Width (mm)","Front Chamber (1) Height (mm)",
                       "Front Chamber (2) Length (mm)","Front Chamber (2) Width (mm)","Front Chamber (2) Height (mm)"]

    Name_Parameters_3C = ["Back Chamber Volume (c.c.)","Front Space Volume (c.c.)",
                       "Sound Port Number","Sound Port Length (mm)",
                       "Sound Port Diameter (mm)","Mesh Rayl (Ohm)",
                       "Front Chamber (1) Length (mm)","Front Chamber (1) Width (mm)","Front Chamber (1) Height (mm)",
                       "Front Chamber (2) Length (mm)","Front Chamber (2) Width (mm)","Front Chamber (2) Height (mm)",
                       "Tunnel Length (mm)","Tunnel Width (mm)","Tunnel Height (mm)",
                       "Front Chamber (3) Length (mm)","Front Chamber (3) Width (mm)","Front Chamber (3) Height (mm)"]

    Name_Parameters_3R = ["Back Chamber Volume (c.c.)","Front Space Volume (c.c.)",
                       "Sound Port Number","Sound Port Length (mm)",
                       "Sound Port Width (mm)","Sound Port Height (mm)","Mesh Rayl (Ohm)",
                       "Front Chamber (1) Length (mm)","Front Chamber (1) Width (mm)","Front Chamber (1) Height (mm)",
                       "Front Chamber (2) Length (mm)","Front Chamber (2) Width (mm)","Front Chamber (2) Height (mm)",
                       "Tunnel Length (mm)","Tunnel Width (mm)","Tunnel Height (mm)",
                       "Front Chamber (3) Length (mm)","Front Chamber (3) Width (mm)","Front Chamber (3) Height (mm)"]

    if fc_num=="1x" and sp_shape=="Circular":
        #print("{} is selected".format(Name_Parameters_1C))
        return ID_1C, Name_Parameters_1C
    elif fc_num=="1x" and sp_shape=="Rectangular":
        #print("{} is selected".format(Name_Parameters_1R))
        return ID_1R, Name_Parameters_1R
    elif fc_num=="2x" and sp_shape=="Circular":
        return ID_2C, Name_Parameters_2C
    elif fc_num=="2x" and sp_shape=="Rectangular":
        return ID_2R, Name_Parameters_2R
    elif fc_num=="3x" and sp_shape=="Circular":
        return ID_3C, Name_Parameters_3C
    elif fc_num=="3x" and sp_shape=="Rectangular":
        return ID_3R, Name_Parameters_3R
    else:
        pass

class Ui_MainWindow(object):

    def __init__(self):
        self.PM =Params_Init("3x","Circular")
        self.TS_Init = {"SD" : 1.04, "BL" : 0.837, "Re" : 8, "Le" : 0.045, "Cmm" : 1.8, "Mmm" : 0.06, "Rmm" : 0.203}
        self.spid ="Circular"
        self.fcid = "1x"
        #print(len(self.PM))
        self.sp_l = self.PM["sp_l"]
        self.sp_w = 1
        self.sp_n = self.PM["sp_n"]
        self.sp_d = self.PM["sp_d"]
        self.sp_h = 1
        self.rayl = self.PM["Rmesh"]
        self.fc1_l =self.PM["fc1_l"]
        self.fc1_w =self.PM["fc1_w"]
        self.fc1_h =self.PM["fc1_h"]
        self.fc2_l =self.PM["fc2_l"]
        self.fc2_w =self.PM["fc2_w"]
        self.fc2_h =self.PM["fc2_h"]
        self.fc3_l =self.PM["fc3_l"]
        self.fc3_w =self.PM["fc3_w"]
        self.fc3_h =self.PM["fc3_h"]
        self.tn_l = self.PM["tn_l"]
        self.tn_w = self.PM["tn_w"]
        self.tn_h = self.PM["tn_h"]
        self.bc_v = self.PM["bc_v"]
        self.fv_v = self.PM["fv_v"]
        self.BL = self.TS_Init["BL"]
        self.Re = self.TS_Init["Re"]
        self.Le = self.TS_Init["Le"]
        self.Cmm = self.TS_Init["Cmm"]
        self.Mmm = self.TS_Init["Mmm"]
        self.Rmm = self.TS_Init["Rmm"]
        self.SD = self.TS_Init["SD"]
        #print(self.fc3_l)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Speaker Enclosure FR Simulation Rev2.0")
       #MainWindow.resize(1400, 950)
        MainWindow.setGeometry(QtCore.QRect(100, 50, 1300, 900))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1300, 900))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 20, 500, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 450, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame_TSPara = QtWidgets.QFrame(self.centralwidget)
        self.frame_TSPara.setGeometry(QtCore.QRect(30, 90, 220, 280))
        self.frame_TSPara.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_TSPara.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_TSPara.setObjectName("frame_TSPara")
        self.TS_Parameters = QtWidgets.QLabel(self.frame_TSPara)
        self.TS_Parameters.setGeometry(QtCore.QRect(10, 0, 120, 16))
        self.TS_Parameters.setObjectName("TS_Parameters")
#######################################################################################3
        self.frame_Test = QtWidgets.QFrame(self.centralwidget)
        self.frame_Test.setGeometry(QtCore.QRect(205, 90, 240, 270))
        self.frame_Test.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Test.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Test.setObjectName("frame_Test")
        self.frame_integration = QtWidgets.QFrame(self.centralwidget)
        self.frame_integration.setGeometry(QtCore.QRect(30, 380, 400, 500))
        self.frame_integration.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_integration.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_integration.setObjectName("frame_integration")
#######################################################################################3
        self.frame_intChart = QtWidgets.QFrame(self.centralwidget)
        self.frame_intChart.setGeometry(QtCore.QRect(500, 480, 750, 500))
        self.frame_intChart.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_intChart.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_intChart.setObjectName("frame_intChart")
        self.label_drawing = QtWidgets.QLabel(self.frame_intChart)
        self.label_drawing.setGeometry(QtCore.QRect(0, 0, 440, 25))
        self.label_drawing.setObjectName("label_drawing")
        self.SPK_Drawing = QtWidgets.QLabel(self.frame_intChart)
        self.SPK_Drawing.setGeometry(QtCore.QRect(0, 30, 600, 300))
        self.SPK_Drawing.setText("")
        self.SPK_Drawing.setPixmap(QtGui.QPixmap("Images/1FC_C.png"))
        self.SPK_Drawing.setScaledContents(True)
        self.SPK_Drawing.setObjectName("SPK_Drawing")

        self.RC_Statement = QtWidgets.QLabel(self.frame_intChart)
        self.RC_Statement.setGeometry(QtCore.QRect(620, 300, 100, 25))
        self.RC_Statement.setText("- Raymond Cheng")
        self.RC_Statement.setScaledContents(True)
        self.RC_Statement.setObjectName("RC_Statement")
        font = QtGui.QFont()
        font.setPointSize(8)
        self.button_Calculation = QtWidgets.QPushButton(self.frame_intChart)
        self.button_Calculation.setGeometry(QtCore.QRect(610,30,60,30))
        self.button_Calculation.setObjectName("Calculate")
        self.button_Calculation.setText("Calculate")
        self.button_Calculation.clicked.connect(self.Plot1)
        self.button_Calculation.setFont(font)
#######################################################################################3
        self.frame_SPL = QtWidgets.QFrame(self.centralwidget)
        self.frame_SPL.setGeometry(QtCore.QRect(500, 50, 670, 420))
        self.frame_SPL.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_SPL.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_SPL.setObjectName("frame_SPL")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame_SPL)
        self.graphicsView.setEnabled(True)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 670, 420))
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setObjectName("graphicsView")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.tableWidget = QtWidgets.QTableWidget(self.frame_TSPara)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 160, 245))
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setLineWidth(2)
        self.tableWidget.setMidLineWidth(1)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(7)
        for n in range(7):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(n,item)
            
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        for n in range(7):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.tableWidget.setItem(n,0,item)

        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(40)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
## Test Setup
        font = QtGui.QFont()
        font.setPointSize(8)
        font1 = QtGui.QFont()
        font1.setPointSize(12)
        self.frame_Test.setFont(font)
        self.label_test=QtWidgets.QLabel(self.frame_Test)
        self.label_test.setGeometry(QtCore.QRect(10,0,100,20))
        self.label_test.setText("Test Setup")
        self.label_test.setFont(font1)

        self.Driven_Volt = QtWidgets.QDoubleSpinBox(self.frame_Test)
        self.Driven_Volt.setGeometry(QtCore.QRect(130, 140, 60, 19))
        self.Driven_Volt.setMaximum(10000000)
        self.Driven_Volt.setSingleStep(0.01)
        self.Driven_Volt.setProperty("value", 2)
        self.Driven_Volt.setObjectName("Driven_Volt")
        self.label_vdrv = QtWidgets.QLabel(self.frame_Test)
        self.label_vdrv.setGeometry(QtCore.QRect(10, 140, 99, 16))
        self.label_vdrv.setMaximumSize(QtCore.QSize(100, 20))
        # self.label_vdrv.setObjectName("label_vdrv")
        self.label_vdrv.setText("Driven Voltage (V)")

        self.label_pdrv = QtWidgets.QLabel(self.frame_Test)
        # self.label_pdrv.setEnabled(True)
        self.label_pdrv.setGeometry(QtCore.QRect(10, 170, 52, 16))
        self.label_pdrv.setMaximumSize(QtCore.QSize(100, 20))
        self.label_pdrv.setText("Power (W)")
        # self.label_pdrv.setObjectName("label_pdrv")
        self.Driven_Power = QtWidgets.QDoubleSpinBox(self.frame_Test)
        self.Driven_Power.setGeometry(QtCore.QRect(130, 170, 60, 20))
        self.Driven_Power.setMaximum(10000000)
        self.Driven_Power.setSingleStep(0.01)
        self.Driven_Power.setProperty("value", 0.5)
        self.Driven_Power.setObjectName("Driven_Power")
        self.label_testDist = QtWidgets.QLabel(self.frame_Test)
        self.label_testDist.setEnabled(True)
        self.label_testDist.setGeometry(QtCore.QRect(10, 200, 100, 20))
        self.label_testDist.setMaximumSize(QtCore.QSize(100, 20))
        self.label_testDist.setObjectName("label_testDist")
        self.lineEdit_testDist = QtWidgets.QLineEdit(self.frame_Test)
        self.lineEdit_testDist.setGeometry(QtCore.QRect(130, 200, 61, 20))
        self.lineEdit_testDist.setObjectName("lineEdit_testDist")
        self.lineEdit_testDist.setText("0.1")
        self.label_TestDistChart = QtWidgets.QLabel(self.frame_Test)
        self.label_TestDistChart.setGeometry(QtCore.QRect(10, 30, 221, 80))
        self.label_TestDistChart.setText("")
        self.label_TestDistChart.setPixmap(QtGui.QPixmap("Images/Test_Distance.png"))
        self.label_TestDistChart.setScaledContents(True)
        self.label_TestDistChart.setObjectName("label_TestDistChart")
        self.label_DUT = QtWidgets.QLabel(self.frame_Test)
        self.label_DUT.setGeometry(QtCore.QRect(20, 90, 101, 16))
        self.label_DUT.setText("DUT")
        self.label_Dist = QtWidgets.QLabel(self.frame_Test)
        self.label_Dist.setGeometry(QtCore.QRect(90, 30, 101, 16))
        self.label_Dist.setText("Test Distance")
        self.label_Mic = QtWidgets.QLabel(self.frame_Test)
        self.label_Mic.setGeometry(QtCore.QRect(160, 90, 101, 16))
        self.label_Mic.setText("Ref. Mic")
    ## Setup Frequency Range
        self.label_freqRange = QtWidgets.QLabel(self.frame_Test)
        self.label_freqRange.setGeometry(QtCore.QRect(10,230,100,20))
        self.label_freqRange.setText("Frequency Range:")
        self.lineEdit_freqStart = QtWidgets.QLineEdit(self.frame_Test)
        self.lineEdit_freqStart.setGeometry(QtCore.QRect(120,230,40,20))
        self.lineEdit_freqStart.setText("100")
        self.label_wave = QtWidgets.QLabel(self.frame_Test)
        self.label_wave.setGeometry(QtCore.QRect(160,230,10,20))
        self.label_wave.setText(" ~ ")
        self.lineEdit_freqEnd = QtWidgets.QLineEdit(self.frame_Test)
        self.lineEdit_freqEnd.setGeometry(QtCore.QRect(180,230,40,20))
        self.lineEdit_freqEnd.setText("20000")


        font = QtGui.QFont()
        font.setPointSize(8)
        self.frame_integration.setFont(font)
        self.label_integration = QtWidgets.QLabel(self.frame_integration)
        self.label_integration.setObjectName("label_integration")
        self.label_integration.setGeometry(QtCore.QRect(10,10,240,20))

        # Setup radio buttons (Start)
        self.widget = QtWidgets.QWidget(self.frame_integration)
        self.widget.setGeometry(QtCore.QRect(10, 50, 240, 20))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_SP_Shape = QtWidgets.QLabel(self.widget)
        self.label_SP_Shape.setObjectName("label_SP_Shape")
        self.horizontalLayout.addWidget(self.label_SP_Shape)
        self.radioButton_SP_C = QtWidgets.QRadioButton(self.widget)
        self.radioButton_SP_C.setObjectName("radioButton_SP_C")
        self.radioButton_SP_C.setChecked(True)
        self.radioButton_SP_C.toggled.connect(self.btn_event)
        self.horizontalLayout.addWidget(self.radioButton_SP_C)
        self.radioButton_SP_R = QtWidgets.QRadioButton(self.widget)
        self.radioButton_SP_R.setObjectName("radioButton_SP_R")
        self.radioButton_SP_R.toggled.connect(self.btn_event)
        self.horizontalLayout.addWidget(self.radioButton_SP_R)
        self.widget1 = QtWidgets.QWidget(self.frame_integration)
        self.widget1.setGeometry(QtCore.QRect(10, 80, 244, 20))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_FC_Num = QtWidgets.QLabel(self.widget1)
        self.label_FC_Num.setObjectName("label_FC_Num")
        self.horizontalLayout_2.addWidget(self.label_FC_Num)
        self.radioButton_FC1 = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_FC1.setObjectName("radioButton_FC1")
        self.radioButton_FC1.setChecked(True)
        self.radioButton_FC1.toggled.connect(self.btn_event)
        self.horizontalLayout_2.addWidget(self.radioButton_FC1)
        self.radioButton_FC2 = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_FC2.setObjectName("radioButton_FC2")
        self.radioButton_FC2.toggled.connect(self.btn_event)
        self.horizontalLayout_2.addWidget(self.radioButton_FC2)
        self.radioButton_FC3 = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_FC3.setObjectName("radioButton_FC3")
        self.radioButton_FC3.toggled.connect(self.btn_event)
        self.horizontalLayout_2.addWidget(self.radioButton_FC3)
        # Setup radio buttons (End)
        self.dv = self.Driven_Volt
        self.dp = self.Driven_Power
        self.dv.setDecimals(4)
        self.dv.setDecimals(2)
        self.dv.valueChanged.connect(self.volt_pow_cal)
        self.dp.valueChanged.connect(self.volt_pow_cal)
        self.vdrv = self.dv.value()
        self.pdrv = self.dp.value()
        self.Re = 8


        # self.tableWidget.setSortingEnabled(__sortingEnabled)
        # self.label_vdrv.setText(_translate("MainWindow", "Driven Voltage (V)"))
        self.label_testDist.setText("Test Distance (m)")
        # self.label_pdrv.setText(_translate("MainWindow", "Power (W)"))
        font.setPointSize(12)
        self.label_drawing.setText("1 Front Chamber x Side-Firing x Round Sound Ports")
        self.label_drawing.setFont(font)
        self.label_integration.setText("Integration Parameters")
        self.label_integration.setFont(font)
        self.label_SP_Shape.setText("Sound Port Shape:")
        self.radioButton_SP_C.setText("Circular")
        self.radioButton_SP_R.setText("Rectangular")
        self.label_FC_Num.setText("Front Chamber Number:")
        self.radioButton_FC1.setText("1x")
        self.radioButton_FC2.setText("2x")
        self.radioButton_FC3.setText("3x")
        self.label.setText("Miniature Speaker Enclosure FR Simulation")
        self.TS_Parameters.setText("TS Parameters")

## Setup Menu Bar
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        # self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        #self.menuHelp = QtWidgets.QMenu(self.menubar)
        #self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionManual = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionSave.setObjectName("actionSave")
        self.actionExit.setObjectName("actionExit")
        self.actionManual.setObjectName("actionManual")
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        #self.menuHelp.addAction(self.actionManual)
        self.menubar.addAction(self.menuFile.menuAction())
        #self.menubar.addAction(self.menuHelp.menuAction())
        self.actionSave.triggered.connect(lambda: self.save())
        self.actionImport.triggered.connect(lambda: self.importData())
        self.actionExit.triggered.connect(lambda: sys.exit())
        self.actionManual.triggered.connect(lambda: self.manual())
        self.menuFile.setTitle("File")
        #self.menuHelp.setTitle("Help")
        self.actionImport.setText("Import Parameters")
        self.actionSave.setText("Save Data")
        self.actionExit.setText("Exit")
        self.actionManual.setText("Manual")
        self.actionImport.setShortcut("Ctrl+I")
        self.actionSave.setShortcut("Ctrl+S")
        self.actionExit.setShortcut("Ctrl+Q")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

##
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_integration)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 110, 360, 310))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy) 
        self.tableWidget_2.setMaximumSize(QtCore.QSize(360, 16777215))
        self.tableWidget_2.setAutoFillBackground(True)
        self.tableWidget_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_2.setAutoScrollMargin(10)
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 10))
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_2.verticalHeader().setStretchLastSection(True)
        ##### Set Design Parameter Table Width (Start)
        header = self.tableWidget_2.horizontalHeader()
        column = 0
        width = 200
        header.setSectionResizeMode(column, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(column, QtWidgets.QHeaderView.Interactive)
        header.resizeSection(column, width)
        column = 1
        width = 50
        header.setSectionResizeMode(column, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(column, QtWidgets.QHeaderView.Interactive)
        header.resizeSection(column, width)
##
        self.TSParameters()
        # Default setup: 1x FC, round soundport
        self.setupUi_Params_Init("1x","Circular")
        self.retranslateParams_Init("1x","Circular")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def TSParameters(self):

        TS = {"BL": self.BL,
              "Re (Ohm)": self.Re,
              "Le (mH)": self.Le,
              "Cmm (mm/N)": self.Cmm,
              "Mmm (g)": self.Mmm,
              "Rmm(ohm)": self.Rmm,
              "SD (cm^2)":self.SD,
              }
        TSNameList = list(TS.keys())
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TS_Parameters.setFont(font)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Value")
        font = QtGui.QFont()
        font.setPointSize(8)
        for n in range(len(TS)):

            item = self.tableWidget.verticalHeaderItem(n)
            item.setText(TSNameList[n])
            item.setFont(font)
            item = self.tableWidget.item(n,0)
            item.setText(str(TS[TSNameList[n]]))
            item.setFont(font)
    def save(self):
        csvpath, ok = QFileDialog.getSaveFileName(None,
                                                  caption= "Save CSV File",
                                                  directory="",
                                                  filter="CSV (*.csv)")

        try:
            ofile = open(csvpath,'w',newline = '')
        except:
            return ctypes.windll.user32.MessageBoxW(0, "Not selected or file is open", "Save warning", 1)
        writer = csv.writer(ofile,dialect='excel')
        SPL_Main.__init__(self)
        params = SPL_Main.ParametersUpdate(self,self.fcid, self.spid)
        SimData = SPLPlot()
        writer.writerow(["Sound Port Shape:", self.spid])
        writer.writerow(["Front Chamber Type:", self.fcid])
        writer.writerow(["Driven Voltage", self.dv.value()])
        writer.writerow(["Driven Power", self.dp.value()])
        writer.writerow(["Test Distance",self.dist])
        writer.writerow(["Parameter", "Value"])
        for k, v in params.items():
            writer.writerow([k, v])

        if not SimData.x ==[]:
            writer.writerow(["Frequency","dBSPL"])
            for f,spl in zip(SimData.x,SimData.y):
                writer.writerow([f, spl])
        ofile.close()
    def importData(self):
        csvpath, ok = QFileDialog.getOpenFileName(None,
                                                  caption="",
                                                  filter = "CSV (*.csv)")
        try:
            ofile = open(csvpath, 'r',newline = '')
            d0 = csv.reader(ofile)
            d1 = pd.DataFrame(data = d0)
            d2 = d1.values
            d2[0][1]
            d3 = {d2[0][0]:d2[0][1]}
            for n in range(len(d2)-1):
                n+=1
                d3.update({d2[n][0]:d2[n][1]})
            #SPL_Main()

            self.BL = d3["BL"]
            self.Re = d3["Re"]
            self.Le = d3["Le"]
            self.Cmm = d3["Cmm"]
            self.Mmm = d3["Mmm"]
            self.Rmm = d3["Rmm"]
            self.SD = d3["SD"]
            self.TSParameters()
            self.spid = d3["Sound Port Shape:"]
            self.bc_v = d3["bc_v"]

            self.fv_v = d3["fv_v"]
            self.sp_n = d3["sp_n"]
            self.sp_l = d3["sp_l"]
            self.rayl = d3["Rmesh"]
            self.vdrv = d3["Driven Voltage"]
            self.pdrv = d3["Driven Power"]
            self.dist = d3["Test Distance"]

            if self.spid == "Circular":
                self.sp_d = d3["sp_d"]
                self.radioButton_SP_C.setChecked(True)
            else:
                self.sp_w = d3["sp_w"]
                self.sp_h = d3["sp_h"]
                self.radioButton_SP_R.setChecked(True)
            self.fc1_l = d3["fc1_l"]
            self.fc1_w = d3["fc1_w"]
            self.fc1_h = d3["fc1_h"]
            self.fcid = d3["Front Chamber Type:"]
            if self.fcid == "1x":
                self.radioButton_FC1.setChecked(True)
            self.fcid = d3["Front Chamber Type:"]
            if self.fcid == "2x":
                self.radioButton_FC2.setChecked(True)
                self.fc2_l = d3["fc2_l"]
                self.fc2_w = d3["fc2_w"]
                self.fc2_h = d3["fc2_h"]
            self.fcid = d3["Front Chamber Type:"]
            if self.fcid == "3x":
                self.radioButton_FC3.setChecked(True)
                self.fc2_l = d3["fc2_l"]
                self.fc2_w = d3["fc2_w"]
                self.fc3_l = d3["fc3_l"]
                self.fc3_w = d3["fc3_w"]
                self.fc3_h = d3["fc3_h"]
            self.dv.setValue(float(self.vdrv))
            self.dp.setValue(float(self.pdrv))
            self.lineEdit_testDist.setText(str(self.dist))

            #SPL_Main.ParametersUpdate(self, self.fcid,self.spid)
            SPL_Main.retranslateParams(self,self.fcid,self.spid)
            #SPL_Main.__init__(self)
            self.Plot1()
        except:
            return ctypes.windll.user32.MessageBoxW(0, "Note selected or bad format", "Import warning", 1)
        print(self.vdrv)

    def exitTool(self):
        quit()

    def manual(self):
        file = "SPK Simulation Tool Introduction.pdf"
        if os.path.exists(file):
            print("file exists")
        else:
            print("file is not there")
        try:
            file = "SPK Simulation Tool Introduction.pdf"
            if os.path.exists(file):
                subprocess.Popen([file],shell=True)
                print("manual exists")
        except:
            return ctypes.windll.user32.MessageBoxW(0, "Manual File is not found", "Manual warning", 1)
    def Plot1(self):
        ax = SPLPlot(self.graphicsView, width = 7, height = 4.2, dpi = 100)
        ax.show()




    def setupUi_Params_Init(self,fc_num,sp_shape):

        # Design Parameters
        #self.Parameters = Params_Init_Setup(fc_num,sp_shape)
        Parameters_ID, Parameters_Name = Params_Init_Setup(fc_num,sp_shape)
        len_Parameters = len(Parameters_ID)
        self.tableWidget_2.setRowCount(len_Parameters)
        for n in range(len_Parameters):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setVerticalHeaderItem(n, item)

        #print("UItable is updated")
        ##### Set Design Parameter Table Width (End)
        for n in range(len_Parameters):
            #print(n)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setItem(n, 0, item)
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.tableWidget_2.setItem(n, 1, item)


    def retranslateParams_Init(self,fc_num,sp_shape):
        # Setup DParameter Table (Start)
        self.Parameters = Params_Init(fc_num,sp_shape)
        Parameters_ID, Parameters_Name = Params_Init_Setup(fc_num,sp_shape)
        #print(Parameters_ID,Parameters_Name)

        n = 0
        for ID in Parameters_ID:
            #print(n, ID)
            item = self.tableWidget_2.verticalHeaderItem(n)
            item.setText(ID)
            n+=1

        item = self.tableWidget_2.horizontalHeaderItem(0).setText("Parameters")
        item = self.tableWidget_2.horizontalHeaderItem(1).setText("Value")
        #__sortingEnabled = self.tableWidget_2.isSortingEnabled()
        #self.tableWidget_2.setSortingEnabled(False)
        n = 0
        #print("Parameter length is {}".format(len(Parameters_Name)))
        for name in Parameters_Name:
            item = self.tableWidget_2.item(n, 0)
            item.setText(name)
            n+=1
        n = 0
        for k,v in self.Parameters.items():
            item = self.tableWidget_2.item(n, 1)
            item.setText(str(v))

            #print(n,v)
            n+=1

        #print("Parameter Table is updated")
        # Setup DParameter Table (End)
       # item.setText(_translate("MainWindow", "0"))
        #self.tableWidget_2.setSortingEnabled(__sortingEnabled)
    def volt_pow_cal(self):
        spinbox = self.dv.sender()
        spinbox = self.dp.sender()
        print("driven voltage = {}".format(self.dv))
        self.Re = float(self.tableWidget.item(1,0).text())
        #self.Re = 8
        print("Re value = {}".format(self.Re))
        if spinbox is self.dv:
            self.dp.setValue((pow(self.dv.value(),2)/self.Re))
        if spinbox is self.dp:
            self.dv.setValue(pow(self.dp.value()*self.Re,0.5))
    def btn_event(self, value):
        #rbtn = self.widget.sender()
        #print(rbtn.isChecked(),rbtn.text())
        #print(len(rbtn.text()))
        #print("FC1 checked: {}".format(self.radioButton_FC1.isChecked()))
        #print("FC2 checked: {}".format(self.radioButton_FC2.isChecked()))
        #print("FC3 checked: {}".format(self.radioButton_FC3.isChecked()))
        rbtnfc1 = self.radioButton_FC1
        rbtnfc2 = self.radioButton_FC2
        rbtnfc3 = self.radioButton_FC3
        rbtnspc = self.radioButton_SP_C
        rbtnspr = self.radioButton_SP_R
        if rbtnfc1.isChecked():
            self.fcid =rbtnfc1.text()
        if rbtnfc2.isChecked():
            self.fcid =rbtnfc2.text()
        if rbtnfc3.isChecked():
            self.fcid =rbtnfc3.text()
        if rbtnspc.isChecked():
            self.spid =rbtnspc.text()
        if rbtnspr.isChecked():
            self.spid =rbtnspr.text()

        self.setupUi_Params_Init(self.fcid,self.spid)
        self.retranslateParams_Init(self.fcid, self.spid)
        sp_text = lambda x: "Round" if x =="Circular" else x


        self.label_drawing.setText("{} Front Chamber x Side-Firing x {} Sound Ports".format(self.fcid,sp_text(self.spid)))
        if self.spid == "Circular" and self.fcid =="1x":
            self.SPK_Drawing.setPixmap(QtGui.QPixmap("Images/1FC_C.png"))
        if self.spid == "Circular" and self.fcid =="2x":
            self.SPK_Drawing.setPixmap(QtGui.QPixmap("Images/2FC_C.png"))
        if self.spid == "Circular" and self.fcid =="3x":
            self.SPK_Drawing.setPixmap(QtGui.QPixmap("Images/3FC_C.png"))
        if self.spid == "Rectangular" and self.fcid =="1x":
            self.SPK_Drawing.setPixmap(QtGui.QPixmap("Images/1FC_R.png"))
        if self.spid == "Rectangular" and self.fcid =="2x":
            self.SPK_Drawing.setPixmap(QtGui.QPixmap("Images/2FC_R.png"))
        if self.spid == "Rectangular" and self.fcid =="3x":
            self.SPK_Drawing.setPixmap(QtGui.QPixmap("Images/3FC_R.png"))


        return

class SPL_Main:
    def __init__(self):
        params = ui.tableWidget_2
        TS = ui.tableWidget
        self.MainWindow = MainWindow
        self.ui = Ui_MainWindow()
        self.dv = ui.Driven_Volt
        self.dp = ui.Driven_Power
        self.dv.setDecimals(4)
        self.dv.setDecimals(2)
        # self.dv.valueChanged.connect(self.volt_pow_cal)
        # self.dp.valueChanged.connect(self.volt_pow_cal)
        self.x = []
        self.y = []
        self.vdrv = self.dv.value()
        self.pdrv = self.dp.value()
        self.spid = ui.spid
        self.fcid = ui.fcid
        self.bc_v = float(params.item(0,1).text())
        self.fv_v = float(params.item(1,1).text())
        self.sp_n = float(params.item(2,1).text())
        self.sp_l = float(params.item(3,1).text())
        self.sp_d = float(params.item(4,1).text())
        self.sp_w = float(params.item(4,1).text())
        if self.spid == "Circular":
            n = 5
        else:
            n = 6
            self.sp_h = float(params.item(5,1).text())
        #print("SP id = {}".format(self.spid))
        self.rayl = float(params.item(n,1).text())
        self.fc1_l = float(params.item(n+1,1).text())
        self.fc1_w = float(params.item(n+2,1).text())
        self.fc1_h = float(params.item(n+3,1).text())
        if self.fcid =="2x":
            self.fc2_l = float(params.item(n+4,1).text())
            self.fc2_w = float(params.item(n+5,1).text())
            self.fc2_h = float(params.item(n+6,1).text())
        if self.fcid == "3x":
            self.fc2_l = float(params.item(n+4,1).text())
            self.fc2_w = float(params.item(n+5,1).text())
            self.fc2_h = float(params.item(n+6,1).text())
            self.tn_l = float(params.item(n+7,1).text())
            self.tn_w = float(params.item(n+8,1).text())
            self.tn_h = float(params.item(n+9,1).text())
            self.fc3_l = float(params.item(n+10,1).text())
            self.fc3_w = float(params.item(n+11,1).text())
            self.fc3_h = float(params.item(n+12,1).text())
        self.dist = float(ui.lineEdit_testDist.text())
        self.freqStart = float(ui.lineEdit_freqStart.text())
        self.freqEnd = float(ui.lineEdit_freqEnd.text())
        #print("fc1_h = {}".format(self.fc1_h))

        self.BL = float(TS.item(0,0).text())
        self.Re = float(TS.item(1,0).text())
        self.Le = float(TS.item(2,0).text())
        self.Cmm = float(TS.item(3,0).text())
        self.Mmm = float(TS.item(4,0).text())
        self.Rmm = float(TS.item(5,0).text())
        self.SD = float(TS.item(6,0).text())
        #a = self.test()

    def ParametersUpdate(self,fcid, spid):
        if spid == "Circular":
            Parameter = {"BL": self.BL, "Re": self.Re, "Le": self.Le, "Cmm": self.Cmm,
                         "Mmm": self.Mmm, "Rmm": self.Rmm,"SD": self.SD,
                         "bc_v": self.bc_v,"fv_v": self.fv_v,
                         "sp_n": self.sp_n, "sp_l": self.sp_l, "sp_d": self.sp_d,"Rmesh": self.rayl,
                         "fc1_l": self.fc1_l, "fc1_w": self.fc1_w, "fc1_h": self.fc1_h}

            if fcid == "2x":
                Parameter.update({"fc2_l": self.fc2_l, "fc2_w": self.fc2_w, "fc2_h": self.fc2_h})
            if fcid == "3x":
                Parameter.update({"fc2_l": self.fc2_l, "fc2_w": self.fc2_w, "fc2_h": self.fc2_h,
                                  "tn_l": self.tn_l, "tn_w": self.tn_w, "tn_h": self.tn_h,
                                  "fc3_l": self.fc3_l, "fc3_w": self.fc3_w, "fc3_h": self.fc3_h})
        if spid == "Rectangular":
            Parameter = {"BL": self.BL, "Re": self.Re, "Le": self.Le, "Cmm": self.Cmm,
                         "Mmm": self.Mmm, "Rmm": self.Rmm,"SD": self.SD,
                         "bc_v": self.bc_v,"fv_v": self.fv_v,
                         "sp_n": self.sp_n, "sp_l": self.sp_l, "sp_w": self.sp_w, "sp_h": self.sp_h, "Rmesh": self.rayl,
                         "fc1_l": self.fc1_l, "fc1_w": self.fc1_w, "fc1_h": self.fc1_h}

            if fcid == "2x":
                Parameter.update({"fc2_l": self.fc2_l, "fc2_w": self.fc2_w, "fc2_h": self.fc2_h})
            if fcid == "3x":
                Parameter.update({"fc2_l": self.fc2_l, "fc2_w": self.fc2_w, "fc2_h": self.fc2_h,
                                  "tn_l": self.tn_l, "tn_w": self.tn_w, "tn_h": self.tn_h,
                                  "fc3_l": self.fc3_l, "fc3_w": self.fc3_w, "fc3_h": self.fc3_h})
        return Parameter

    # def volt_pow_cal(self):
    #     spinbox = self.MainWindow.sender()
    #     print(spinbox)
    #     print("driven voltage = {}".format(self.dv))
    #     if spinbox is self.dv:
    #         self.dp.setValue((pow(self.dv.value(),2)/self.Re))
    #     if spinbox is self.dp:
    #         self.dv.setValue(pow(self.dp.value()*self.Re,0.5))
    def retranslateParams(self,fcid,spid):
        # Setup DParameter Table (Start)
        self.Parameters = SPL_Main.ParametersUpdate(self,fcid, spid)
        Parameters_ID, Parameters_Name = Params_Init_Setup(fcid,spid)
        #print(Parameters_ID,Parameters_Name)

        n = 0
        for ID in Parameters_ID:
            #print(n, ID)
            item = self.tableWidget_2.verticalHeaderItem(n)
            item.setText(ID)
            n+=1

        item = self.tableWidget_2.horizontalHeaderItem(0).setText("Parameters")
        item = self.tableWidget_2.horizontalHeaderItem(1).setText("Value")
        #__sortingEnabled = self.tableWidget_2.isSortingEnabled()
        #self.tableWidget_2.setSortingEnabled(False)
        n = 0
        #print("Parameter length is {}".format(len(Parameters_Name)))
        for name in Parameters_Name:
            item = self.tableWidget_2.item(n, 0)
            item.setText(name)
            n+=1
        n = 0
        for k,v in self.Parameters.items():
            if n > 6:
                item = self.tableWidget_2.item(n-7, 1)
                print(n-7,v)
                item.setText(str(v))
            

            #print(n,v)
            n+=1
    def Eq(self):
        self.fv_A = 13*9
        self.SD = self.SD/ 10000 # converted to MKS
        self.Cmm = self.Cmm / 1000 # converted to MKS
        self.Mmm = self.Mmm / 1000 # converted to MKS
        self.fv_v = self.fv_v / pow(10,6)
        self.bc_v = self.bc_v / pow(10,6)
        if ui.radioButton_SP_C.isChecked():
            self.sp_type = 0
            Rsp = self.R_cir_tnl(self.sp_d,self.sp_l,self.sp_n)
            Msp = self.M_cir_tnl(self.sp_d,self.sp_l,self.sp_n)
        else:
            Rsp = self.R_rec_tnl(self.sp_w, self.sp_l, self.sp_h,self.sp_n)
            Msp = self.M_rec_tnl(self.sp_w, self.sp_l, self.sp_h,self.sp_n)
            self.sp_type = 1

        self.freqs = self.frequency(self.freqStart,self.freqEnd,12)
        #print(self.freqs)
        if self.spid == "Circular":
            SP_A = pow(self.sp_d,2)*pi/4*self.sp_n
        else:
            SP_A= self.sp_w*self.sp_h*self.sp_n
        if self.fcid == "1x":

            Cafc1 = self.C_volume(self.fc1_w, self.fc1_l, self.fc1_h, SP_A)
            Mafc1 = self.M_volume(self.fc1_w, self.fc1_l, self.fc1_h, SP_A)
            Rafc1 = self.R_volume(self.fc1_w, self.fc1_l, self.fc1_h)
        if self.fcid == "2x":

            Cafc1 = self.C_volume(self.fc1_w, self.fc1_l, self.fc1_h, SP_A)
            Mafc1 = self.M_volume(self.fc1_w, self.fc1_l, self.fc1_h, SP_A)
            Rafc1 = self.R_volume(self.fc1_w, self.fc1_l, self.fc1_h)
            Cafc2 = self.C_volume(self.fc2_w, self.fc2_l, self.fc2_h, SP_A)
            Mafc2 = self.M_volume(self.fc2_w, self.fc2_l, self.fc2_h, SP_A)
            Rafc2 = self.R_volume(self.fc2_w, self.fc2_l, self.fc2_h)
        if self.fcid == "3x":

            Cafc1 = self.C_volume(self.fc1_w, self.fc1_l, self.fc1_h, SP_A)
            Mafc1 = self.M_volume(self.fc1_w, self.fc1_l, self.fc1_h, SP_A)
            Rafc1 = self.R_volume(self.fc1_w, self.fc1_l, self.fc1_h)
            Cafc2 = self.C_volume(self.fc2_w, self.fc2_l, self.fc2_h, SP_A)
            Mafc2 = self.M_volume(self.fc2_w, self.fc2_l, self.fc2_h, SP_A)
            Rafc2 = self.R_volume(self.fc2_w, self.fc2_l, self.fc2_h)
            Catn = self.C_volume(self.tn_w, self.tn_l, self.tn_h, SP_A)
            Matn = self.M_volume(self.tn_w, self.tn_l, self.tn_h, SP_A)
            Ratn = self.R_volume(self.tn_w, self.tn_l, self.tn_h)
            Cafc3 = self.C_volume(self.fc3_w, self.fc3_l, self.fc3_h, SP_A)
            Mafc3 = self.M_volume(self.fc3_w, self.fc3_l, self.fc3_h, SP_A)
            Rafc3 = self.R_volume(self.fc3_w, self.fc3_l, self.fc3_h)
        Ramesh = self.rayl/SP_A/self.sp_n*1000000
        # Rtnl_1 = self.R_rec_tnl(self.tn1w, self.tn1l , self.tn1h)
        # Mtnl_1 = self.M_rec_tnl(self.tn1w, self.tn1l , self.tn1h)

        Cafv = self.C_chamb(self.fv_v)
        Mafv = self.M_chamb(self.fv_v)
        Cabc = self.C_chamb(self.bc_v)
        Cam = self.Cmm * pow(self.SD,2)
        Mam = self.Mmm / pow(self.SD,2)
        Ram = self.Rmm / pow(self.SD,2)
        Imps = []
        self.Pspls = []
        for freq in self.freqs:
            omega = 2 * pi * freq
            #print("freq = {}".format(freq))
            # angular velocity relevant impedance
            if self.spid == "Circular":
                self.sp_h = 0
            R_rad = self.R_radi(self.sp_w, self.sp_h, self.sp_n, self.sp_d, omega, self.sp_type)
            M_rad = self.M_radi(self.sp_w, self.sp_h, self.sp_n, self.sp_d, omega, self.sp_type)
            # T Matrix
            T_aBL = self.TM_BL(self.BL, self.Re, 1j * omega * self.Le, self.SD)
            T_aMB = self.TM_e(1j * omega * Mam + Ram + 1 / (1j * omega * Cam))
            T_fv = np.dot(self.TM_t(1 / (1j * omega * Cafv)), self.TM_e(1j * omega * Mafv))
            T_fc1 = self.multidot(self.TM_t(1 / (1j * omega * Cafc1)), self.TM_e(1j * omega * Mafc1), self.TM_e(Rafc1))
            #T_tnl_1 = np.dot(self.TM_e(1j * omega * Mtnl_1), self.TM_e(Rtnl_1))
            T_sp = self.multidot(self.TM_e(1j * omega * Msp), self.TM_e(Rsp),self.TM_e(Ramesh))
            T_rad = self.TM_p(R_rad, 1j * omega * M_rad)
            T_aBack = self.TM_e(1 / (1j * omega * Cabc))
            #T_aFront = self.multidot(T_fv, T_fcl_1, T_sp, T_tnl_1, T_rad)
            if self.fcid == "1x":
                T_aFront = self.multidot(T_fv, T_fc1, T_sp, T_rad)
            elif self.fcid == "2x":
                T_fc2 = self.multidot(self.TM_t(1 / (1j * omega * Cafc2)), self.TM_e(1j * omega * Mafc2), self.TM_e(Rafc2))
                T_aFront = self.multidot(T_fv, T_fc1, T_fc2, T_sp, T_rad)
            elif self.fcid == "3x":
                T_fc2 = self.multidot(self.TM_t(1 / (1j * omega * Cafc2)), self.TM_e(1j * omega * Mafc2), self.TM_e(Rafc2))
                T_tn = self.multidot(self.TM_t(1 / (1j * omega * Catn)), self.TM_e(1j * omega * Matn), self.TM_e(Ratn))
                T_fc3 = self.multidot(self.TM_t(1 / (1j * omega * Cafc3)), self.TM_e(1j * omega * Mafc3), self.TM_e(Rafc3))
                T_aFront = self.multidot(T_fv, T_fc1, T_fc2, T_tn, T_fc3, T_sp, T_rad)
            #T_aFront = self.multidot(T_fv, T_fcl_1, T_tnl_1, T_rad)
            Tasum = self.TM_Dot(T_aBL, T_aMB, T_aBack, T_aFront)
            Imp = Tasum[0,1] / Tasum[1,1]
            Imps.append(Imp)
            Uae = self.vdrv * self.BL / self.SD / self.Re
            iae = Uae / Imp
            PV = np.dot(np.linalg.inv(Tasum), [Uae, iae]) # This is a bug that the first cal the data will be missing
            PV = np.dot(np.linalg.inv(Tasum), [Uae, iae])
            Vv = PV[1]
            P = abs(1j * omega * lo * Vv /4 / pi/ self.dist)
            Pspl = 20 * np.log10(P) + 94
            self.Pspls.append(Pspl)
            # print("Vv = {}".format(Vv))
            # print("iae = {}".format(iae))
            # print("Uae = {}".format(Uae))
            # print("Imp = {}".format(Imp))
            # print("PV = {}".format(PV))
            # print("Tasum = {}".format(Tasum))
            # print("P = {}".format(P))
            # print("Pspl = {}".format(Pspl))
        return zip(self.freqs, self.Pspls)

    def frequency(self,start, end, octave):
        freq = start
        freqs = [start]
        n=1
        while freq < end:
            freq =round(start*pow(2,n/octave))
            freqs.append(freq)
            n+=1
        return freqs
    def multidot(self,*argv):
        tn = np.array([[1, 0], [0, 1]])
        for t in argv:
            tn = np.dot(tn, t)
        return tn


    def C_volume(self,w, l, h, Aout):
        # Acoustics volume compliance
        # the input w, l, h, tw, th are in mm. Converted to mks
        global lo
        w = w / 1000
        l = l / 1000
        h = h / 1000
        Aout = Aout / 1000000
        if w*h > Aout:
            return l * (w * h - Aout) / lo / pow(340,2)
        return pow(10,-20)

    def M_volume(self,w, l, h, Aout):
        # Acoustics volume mass
        # the input w, l, h, tw, th are in mm. Converted to mks
        global lo
        w = w / 1000
        l = l / 1000
        h = h / 1000
        Aout = Aout / 1000000
        if w*h > Aout:
            return lo * l / Aout
        return lo*l/w/h

    def R_volume(self,w, l , h):
        # Acoustics resistance of rectangular tunnel
        # the input w, l, h, tw, th are in mm. Converted to mks
        w = w / 1000
        l = l / 1000
        h = h / 1000
        return 12* 1.86 * pow(10,-5) * l / w / pow(h,3)

    def R_rec_tnl(self,w, l , h, n):
        # Acoustics resistance of rectangular tunnel
        # the input w, l, h, tw, th are in mm. Converted to mks
        w = w / 1000
        l = l / 1000
        h = h / 1000
        return 12* 1.86 * pow(10,-5) * l / w / pow(h,3)/n

    def M_rec_tnl(self,w, l , h, n):
        # Acoustics mass of rectangular tunnel
        # the input w, l, h, tw, th are in mm. Converted to mks
        global lo
        w = w / 1000
        l = l / 1000
        h = h / 1000
        return 4 / 3 * lo * l / w / h/n

    def R_cir_tnl(self,d, l, n):
        # Acoustics resistance of rectangular tunnel
        # the input w, l, h, tw, th are in mm. Converted to mks
        a = d / 1000 / 2
        l = l / 1000
        return 8 * 1.86 * pow(10,-5) * l / pi / pow(a,4) / n

    def M_cir_tnl(self,d, l, n):
        # Acoustics mass of rectangular tunnel
        # the input w, l, h, tw, th are in mm. Converted to mks
        global lo
        a = d / 1000 / 2
        l = l / 1000
        return 4 / 3 * lo * l / pi / pow(a,2) / n

    def R_radi(self,w, h, n, d, omega, SP_type):
        global lo
        global c
        w = w / 1000
        h = h / 1000
        k = omega / c
        return 1 / 2 / pi * lo * c * pow(k,2) / n

    def M_radi(self,w, h, n, d, omega, SP_type):
        global lo
        global c
        w = w / 1000
        h = h / 1000
        if SP_type ==1:
            a = pow(w * h / pi, 0.5)
            # print("SP is rectangular")
        else:
            # print("SP is round")
            a = d / 1000 / 2

        return 8 * lo / 3 / a / pow(pi,2) / n

    def C_chamb(self,volume):
        global c
        global lo
        return 1.4*volume/lo/pow(c,2)

    def M_chamb(self,volume):
        global lo
        SD = self.SD
        return volume*lo/pow(SD, 2)

    # T Matrix
    # T Matrix when impedance is in = shape
    def TM_e(self,z):
        return np.array([[1, z], [0, 1]])

    # T Matrix when impedance is in T shape
    def TM_t(self,z):
        return np.array([[1, 0], [1 / z, 1]])

    # T Matrix when impedance is in parallel
    def TM_p(self,z1, z2):

        z = 1 / (1 / z1 + 1 / z2)
        return self.TM_e(z)

    def TM_BL(self,BL, ZRe, ZLe, SD):
        return self.TM_e(pow(BL, 2) / (ZRe + ZLe) / pow(SD, 2))

    def TM_Dot(self,*args):
        arg1 = args[0]
        for arg in args[1:]:
            arg1 = np.dot(arg1, arg)
        return arg1

class SPLPlot(FigureCanvas):
    def __init__(self, parent=None, width = 4, height = 3, dpi = 100):
        fig = Figure(figsize = (width, height), dpi = dpi)
        self.axes = fig.add_subplot(111)
        self.axes.cla
        self.SPL_Figure()
        FigureCanvas.__init__(self,fig)

        self.setParent(parent)

    def SPL_Figure(self):

        SPLCal = SPL_Main()
        self.x, self.y = zip(*SPLCal.Eq())
        #print(x,y)
        self.plot = self.axes.semilogx(self.x,self.y)
        self.axes.set_ylim([20,120])
        self.axes.set_xlim([10,20000])
        self.axes.set_xlabel("Frequency (Hz)")
        self.axes.set_ylabel("dBSPL rel. 20uPa")
        self.axes.set_title("Frequency Response")
        self.axes.yaxis.grid(True, which = 'major')
        self.axes.xaxis.grid(True, which = 'major')
        self.axes.xaxis.grid(True, which = 'minor')
        self.axes.plot()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


