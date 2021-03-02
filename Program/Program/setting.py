
from PyQt5.QtWidgets import QLineEdit,QMainWindow,QScrollArea,QApplication, QWidget , QVBoxLayout, QPushButton, QGroupBox, QGridLayout
import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class  Ui_MainWindow(QMainWindow):
        def __init__(self, parent=None):
                QWidget.__init__(self, parent)

                self.setWindowTitle("Calculation Setting")
                self.setMinimumSize(480, 360) 
                self.showMaximized()
                font = QFont()
                font.setFamily("MS Shell Dlg 2")
                self.setFont(font)
                self.setStyleSheet("background-color: rgb(255, 251, 252);\n"
        "border:5px;\n"
        "")     
                self.centralwidget = QWidget(self)
                self.centralwidget.setGeometry(0, 0, 1380, 960)
                self.centralwidget.setObjectName("centralwidget")


                self.setCentralWidget(self.centralwidget)
                self.box = QVBoxLayout(self.centralwidget) 

                scroll = QScrollArea()
                content_widget = QWidget()
                scroll.setWidget(content_widget)
                scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
                scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
                scroll.setWidgetResizable(True) 

                lay = QVBoxLayout(content_widget)
                self.groupBox = QGroupBox()
                self.groupBox.setFont(QFont("Sanserif", 13))

                gridLayout = QGridLayout(self)

                # self.body = QtWidgets.QFrame(self.centralwidget)
                # self.body.setLocale(QtCore.QLocale(QtCore.QLocale.Thai, QtCore.QLocale.Thailand))
                # self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
                # self.body.setFrameShadow(QtWidgets.QFrame.Raised)
                # self.body.setProperty("Color", QtGui.QColor(0, 0, 0))
                # self.body.setObjectName("body")

                ####################frame1#####################
                self.frame1 = QtWidgets.QFrame(self.centralwidget)
                self.frame1.setAutoFillBackground(False)
                self.frame1.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.539318, y1:0, x2:0.551273, y2:1, stop:0 rgba(56, 74, 173, 255), stop:0.607955 rgba(60, 203, 175, 255), stop:1 rgba(5, 199, 170, 255));")
                self.frame1.setLocale(QtCore.QLocale(QtCore.QLocale.Thai, QtCore.QLocale.Thailand))
                self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame1.setProperty("Color", QtGui.QColor(0, 0, 0))
                self.frame1.setObjectName("frame1")

                sub_gridLayout_result = QGridLayout(self.frame1)
                #label cal
                self.Calself = QtWidgets.QLabel(self.frame1)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(24)
                font.setBold(True)
                font.setUnderline(False)
                font.setWeight(75)
                self.Calself.setFont(font)
                self.Calself.setAutoFillBackground(False)
                self.Calself.setStyleSheet("background-color: transparent;\n"
        "color: white;\n"
        "")
                self.Calself.setObjectName("Calself")

                self.Empty = QtWidgets.QLabel(self.frame1)
                self.Empty.setStyleSheet("background-color: transparent;")
                #result 1
                self.horizontalLayoutWidget1 = QtWidgets.QWidget(self.frame1)
                self.horizontalLayoutWidget1.setObjectName("horizontalLayoutWidget")
                self.horizontalLayoutWidget1.setStyleSheet("background-color: transparent;")

                sub_gridLayout_result1 = QGridLayout(self.horizontalLayoutWidget1)

                self.widget_title_result1 = QtWidgets.QFrame(self.frame1)
                font = QtGui.QFont()
                font.setFamily("TH Sarabun New")
                self.widget_title_result1.setFont(font)
                self.widget_title_result1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border: 0px solid grey;\n"
        "border-radius: 20px;")
                self.widget_title_result1.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.widget_title_result1.setFrameShadow(QtWidgets.QFrame.Raised)
                self.widget_title_result1.setObjectName("widget_title_result1")

                sub_Gridlayout_widget_title_result1 = QGridLayout(self.widget_title_result1)
                self.label_result1 = QtWidgets.QLabel(self.widget_title_result1)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(16)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                font.setKerning(True)
                self.label_result1.setFont(font)
                self.label_result1.setAutoFillBackground(False)
                self.label_result1.setStyleSheet("font: 75 16pt \"Tahoma\";\n"
                "color: \"black\";\n"
                "background-color: rgba(255, 255, 255, 0);")
                self.label_result1.setWordWrap(False)
                self.label_result1.setObjectName("label_result1")
                sub_Gridlayout_widget_title_result1.addWidget(self.label_result1,0,0)
                
                self.result1 = QtWidgets.QFrame(self.frame1)
                font = QtGui.QFont()
                font.setFamily("TH Sarabun New")
                self.result1.setFont(font)
                self.result1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border: 0px solid grey;\n"
        "border-radius: 20px;")
                self.result1.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.result1.setFrameShadow(QtWidgets.QFrame.Raised)
                self.result1.setObjectName("result1")

                sub_Gridlayout_result1 = QGridLayout(self.result1)

                self.widget_file1 = QtWidgets.QWidget(self.result1)
                self.widget_file1.setStyleSheet("background-color:rgb(85, 170, 255);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_file1.setObjectName("widget_file1")
                
                sub_Gridlayout_widget_file1 = QGridLayout(self.widget_file1)

                self.label_calibrationfile1 = QtWidgets.QLabel(self.widget_file1)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_calibrationfile1.setFont(font)
                self.label_calibrationfile1.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_calibrationfile1.setObjectName("label_calibrationfile1")

                self.widget_browse1 = QtWidgets.QWidget(self.widget_file1)
                self.widget_browse1.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;")
                self.widget_browse1.setObjectName("widget_browse1")

                sub_Gridlayout_widget_browse1 = QGridLayout(self.widget_browse1)

                self.label_file1 = QtWidgets.QLabel(self.widget_file1)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_file1.setFont(font)
                self.label_file1.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_file1.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;")
                self.label_file1.setObjectName("label_file1")

                self.pushButton = QtWidgets.QPushButton(self.widget_file1)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setItalic(False)
                font.setUnderline(False)
                font.setStrikeOut(False)
                self.pushButton.setFont(font)
                self.pushButton.setStyleSheet("background-color:rgb(170, 255, 127);\n"
        "border-radius: 15px;")
                self.pushButton.setObjectName("pushButton")
                #label_calibrationfile1
                sub_Gridlayout_widget_browse1.addWidget(self.label_file1,0,0,1,3)
                sub_Gridlayout_widget_browse1.addWidget(self.pushButton,0,3,1,1)

                #widget file1
                sub_Gridlayout_widget_file1.addWidget(self.label_calibrationfile1,0,0)
                sub_Gridlayout_widget_file1.addWidget(self.widget_browse1,1,0)

                
                #widget bias1
                self.widget_bias1 = QtWidgets.QWidget(self.result1)
                self.widget_bias1.setGeometry(QtCore.QRect(10, 90, 331, 61))
                self.widget_bias1.setStyleSheet("background-color:rgb(85, 170, 255);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_bias1.setObjectName("widget_bias1")
                
                sub_Gridlayout_widget_bias1 = QGridLayout(self.widget_bias1)
                
                self.label_bias1 = QtWidgets.QLabel(self.widget_bias1)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_bias1.setFont(font)
                self.label_bias1.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_bias1.setObjectName("label_bias1")
                
                self.widget_biasResult1 = QtWidgets.QWidget(self.widget_bias1)
                self.widget_biasResult1.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;")
                self.widget_biasResult1.setObjectName("widget_biasResult1")

                sub_Gridlayout_widget_biasResult1 = QGridLayout(self.widget_biasResult1)

                self.doubleSpinBox_biasResult1 = QtWidgets.QDoubleSpinBox(self.widget_biasResult1)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setBold(True)
                font.setWeight(75)
                self.doubleSpinBox_biasResult1.setFont(font)
                self.doubleSpinBox_biasResult1.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_biasResult1.setObjectName("doubleSpinBox_biasResult1")

                #doubleSpinBox_biasResult1
                sub_Gridlayout_widget_biasResult1.addWidget(self.doubleSpinBox_biasResult1,0,0)

                #widget_bias1
                sub_Gridlayout_widget_bias1.addWidget(self.label_bias1,0,0)
                sub_Gridlayout_widget_bias1.addWidget(self.widget_biasResult1,1,0)

                #prepro1
                self.widget_preproR1 = QtWidgets.QWidget(self.result1)
                self.widget_preproR1.setStyleSheet("background-color:rgb(170, 170, 255);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_preproR1.setObjectName("widget_preproR1")
                
                #sub_widget_prepro1
                sub_gridlayout_widget_preproR1 = QGridLayout(self.widget_preproR1)

                self.label_prepro1 = QtWidgets.QLabel(self.widget_preproR1)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_prepro1.setFont(font)
                self.label_prepro1.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_prepro1.setObjectName("label_prepro1")

                self.widget_stepResult1 = QtWidgets.QWidget(self.widget_preproR1)
                self.widget_stepResult1.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.widget_stepResult1.setObjectName("widget_stepResult1")

                #step result1
                sub_gridlayout_stepResult1 = QGridLayout(self.widget_stepResult1)

                self.label_step_result1 = QtWidgets.QLabel(self.widget_stepResult1)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setBold(False)
                font.setWeight(50)
                self.label_step_result1.setFont(font)
                self.label_step_result1.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_step_result1.setObjectName("label_step_result1")

                self.label_step1_result1 = QtWidgets.QLabel(self.widget_stepResult1)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.label_step1_result1.setFont(font)
                self.label_step1_result1.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_step1_result1.setObjectName("label_step1_result1")

                self.label_step2_result1 = QtWidgets.QLabel(self.widget_stepResult1)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.label_step2_result1.setFont(font)
                self.label_step2_result1.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_step2_result1.setObjectName("label_step2_result1")

                self.label_step3_result1 = QtWidgets.QLabel(self.widget_stepResult1)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.label_step3_result1.setFont(font)
                self.label_step3_result1.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_step3_result1.setObjectName("label_step3_result1")

                self.comboBox_step1_result1 = QtWidgets.QComboBox(self.widget_stepResult1)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.comboBox_step1_result1.setFont(font)
                self.comboBox_step1_result1.setObjectName("comboBox_step1_result1")
                self.comboBox_step1_result1.addItem("")
                self.comboBox_step1_result1.addItem("")
                self.comboBox_step1_result1.addItem("")
                self.comboBox_step1_result1.addItem("")
                self.comboBox_step1_result1.addItem("")
                self.comboBox_step2_result1 = QtWidgets.QComboBox(self.widget_stepResult1)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.comboBox_step2_result1.setFont(font)
                self.comboBox_step2_result1.setObjectName("comboBox_step2_result1")
                self.comboBox_step2_result1.addItem("")
                self.comboBox_step2_result1.addItem("")
                self.comboBox_step2_result1.addItem("")
                self.comboBox_step2_result1.addItem("")
                self.comboBox_step2_result1.addItem("")
                self.comboBox_step3_result1 = QtWidgets.QComboBox(self.widget_stepResult1)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.comboBox_step3_result1.setFont(font)
                self.comboBox_step3_result1.setObjectName("comboBox_step3_result1")
                self.comboBox_step3_result1.addItem("")
                self.comboBox_step3_result1.addItem("")
                self.comboBox_step3_result1.addItem("")
                self.comboBox_step3_result1.addItem("")
                self.comboBox_step3_result1.addItem("")

                sub_gridlayout_stepResult1.addWidget(self.label_step_result1,0,0,1,3)

                sub_gridlayout_stepResult1.addWidget(self.label_step1_result1,1,0,1,1)
                sub_gridlayout_stepResult1.addWidget(self.label_step2_result1,2,0,1,1)
                sub_gridlayout_stepResult1.addWidget(self.label_step3_result1,3,0,1,1)

                sub_gridlayout_stepResult1.addWidget(self.comboBox_step1_result1,1,1,1,2)
                sub_gridlayout_stepResult1.addWidget(self.comboBox_step2_result1,2,1,1,2)
                sub_gridlayout_stepResult1.addWidget(self.comboBox_step3_result1,3,1,1,2)


                self.widget_R1_1D = QtWidgets.QWidget(self.widget_preproR1)
                self.widget_R1_1D.setStyleSheet("background-color:rgb(170, 255, 127);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_R1_1D.setObjectName("widget_R1_1D")

                sub_gridlayout_widget_R1_1D = QGridLayout(self.widget_R1_1D)
                
                self.label_R1_1stD = QtWidgets.QLabel(self.widget_R1_1D)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_R1_1stD.setFont(font)
                self.label_R1_1stD.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_R1_1stD.setObjectName("label_R1_1stD")

                self.widget_1D_result1_gab = QtWidgets.QWidget(self.widget_R1_1D)
                self.widget_1D_result1_gab.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;\n"
        "")
                self.widget_1D_result1_gab.setObjectName("widget_1D_result1_gab")

                sub_gridlayout_widget_1D_result1_gab = QGridLayout(self.widget_1D_result1_gab)

                self.label_GabResult1_1D = QtWidgets.QLabel(self.widget_1D_result1_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                self.label_GabResult1_1D.setFont(font)
                self.label_GabResult1_1D.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_GabResult1_1D.setObjectName("label_GabResult1_1D")

                self.doubleSpinBox_1D_result1_gab = QtWidgets.QDoubleSpinBox(self.widget_1D_result1_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_1D_result1_gab.setFont(font)
                self.doubleSpinBox_1D_result1_gab.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_1D_result1_gab.setObjectName("doubleSpinBox_1D_result1_gab")

                sub_gridlayout_widget_1D_result1_gab.addWidget(self.label_GabResult1_1D,0,0)
                sub_gridlayout_widget_1D_result1_gab.addWidget(self.doubleSpinBox_1D_result1_gab,0,1)

                self.widget_1D_result1_sg = QtWidgets.QWidget(self.widget_R1_1D)
                self.widget_1D_result1_sg.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;\n"
        "")
                self.widget_1D_result1_sg.setObjectName("widget_1D_result1_sg")

                sub_gridlayout_widget_1D_result1_sg = QGridLayout(self.widget_1D_result1_sg)

                self.label_SGResult1_1D = QtWidgets.QLabel(self.widget_1D_result1_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                self.label_SGResult1_1D.setFont(font)
                self.label_SGResult1_1D.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_SGResult1_1D.setObjectName("label_SGResult1_1D")

                self.doubleSpinBox_1D_result1_sg = QtWidgets.QDoubleSpinBox(self.widget_1D_result1_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_1D_result1_sg.setFont(font)
                self.doubleSpinBox_1D_result1_sg.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_1D_result1_sg.setObjectName("doubleSpinBox_1D_result1_sg")

                sub_gridlayout_widget_1D_result1_sg.addWidget(self.label_SGResult1_1D,0,0)
                sub_gridlayout_widget_1D_result1_sg.addWidget(self.doubleSpinBox_1D_result1_sg,0,1)


                sub_gridlayout_widget_R1_1D.addWidget(self.label_R1_1stD,0,0)
                sub_gridlayout_widget_R1_1D.addWidget(self.widget_1D_result1_gab,1,0)
                sub_gridlayout_widget_R1_1D.addWidget(self.widget_1D_result1_sg,2,0)


                self.widget_R1_2D = QtWidgets.QWidget(self.widget_preproR1)
                self.widget_R1_2D.setStyleSheet("background-color:rgb(170, 255, 127);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_R1_2D.setObjectName("widget_R1_2D")

                sub_gridlayout_widget_R1_2D = QGridLayout(self.widget_R1_2D)
                
                self.label_R1_2ndD = QtWidgets.QLabel(self.widget_R1_2D)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_R1_2ndD.setFont(font)
                self.label_R1_2ndD.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_R1_2ndD.setObjectName("label_R1_2ndD")

                self.widget_2D_result1_gab = QtWidgets.QWidget(self.widget_R1_2D)
                self.widget_2D_result1_gab.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;\n"
        "")
                self.widget_2D_result1_gab.setObjectName("widget_2D_result1_gab")

                sub_gridlayout_widget_2D_result1_gab = QGridLayout(self.widget_2D_result1_gab)

                self.label_GabResult1_2D = QtWidgets.QLabel(self.widget_2D_result1_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                self.label_GabResult1_2D.setFont(font)
                self.label_GabResult1_2D.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_GabResult1_2D.setObjectName("label_GabResult1_2D")

                self.doubleSpinBox_2D_result1_gab = QtWidgets.QDoubleSpinBox(self.widget_2D_result1_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_2D_result1_gab.setFont(font)
                self.doubleSpinBox_2D_result1_gab.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_2D_result1_gab.setObjectName("doubleSpinBox_2D_result1_gab")

                sub_gridlayout_widget_2D_result1_gab.addWidget(self.label_GabResult1_2D,0,0)
                sub_gridlayout_widget_2D_result1_gab.addWidget(self.doubleSpinBox_2D_result1_gab,0,1)

                self.widget_2D_result1_sg = QtWidgets.QWidget(self.widget_R1_2D)
                self.widget_2D_result1_sg.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;\n"
        "")
                self.widget_2D_result1_sg.setObjectName("widget_2D_result1_sg")

                sub_gridlayout_widget_2D_result1_sg = QGridLayout(self.widget_2D_result1_sg)

                self.label_SGResult1_2D = QtWidgets.QLabel(self.widget_2D_result1_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                self.label_SGResult1_2D.setFont(font)
                self.label_SGResult1_2D.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_SGResult1_2D.setObjectName("label_SGResult1_2D")

                self.doubleSpinBox_2D_result1_sg = QtWidgets.QDoubleSpinBox(self.widget_2D_result1_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_2D_result1_sg.setFont(font)
                self.doubleSpinBox_2D_result1_sg.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_2D_result1_sg.setObjectName("doubleSpinBox_2D_result1_sg")

                sub_gridlayout_widget_2D_result1_sg.addWidget(self.label_SGResult1_2D,0,0)
                sub_gridlayout_widget_2D_result1_sg.addWidget(self.doubleSpinBox_2D_result1_sg,0,1)


                sub_gridlayout_widget_R1_2D.addWidget(self.label_R1_2ndD,0,0)
                sub_gridlayout_widget_R1_2D.addWidget(self.widget_2D_result1_gab,1,0)
                sub_gridlayout_widget_R1_2D.addWidget(self.widget_2D_result1_sg,2,0)


                #smoothing size1
                self.widget_sm1 = QtWidgets.QWidget(self.widget_preproR1)
                self.widget_sm1.setStyleSheet("background-color:rgb(170, 255, 127);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_sm1.setObjectName("widget_sm1")

                sub_gridlayout_widget_sm1 = QGridLayout(self.widget_sm1)

                self.label_R1_sm = QtWidgets.QLabel(self.widget_sm1)
                self.label_R1_sm.setGeometry(QtCore.QRect(10, 0, 141, 51))
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(6)
                font.setBold(True)
                font.setWeight(75)
                self.label_R1_sm.setFont(font)
                self.label_R1_sm.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_R1_sm.setObjectName("label_R1_sm")
                
                self.widget_R1_sm_gab = QtWidgets.QWidget(self.widget_sm1)
                self.widget_R1_sm_gab.setGeometry(QtCore.QRect(170, 10, 131, 31))
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.widget_R1_sm_gab.setFont(font)
                self.widget_R1_sm_gab.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;")
                self.widget_R1_sm_gab.setObjectName("widget_R1_sm_gab")

                sub_gridlayout_widget_R1_sm_gab = QGridLayout(self.widget_R1_sm_gab)

                self.label_GabResult1_sm = QtWidgets.QLabel(self.widget_R1_sm_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.label_GabResult1_sm.setFont(font)
                self.label_GabResult1_sm.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_GabResult1_sm.setObjectName("label_GabResult1_sm")

                self.doubleSpinBox_sm_result1_gab = QtWidgets.QDoubleSpinBox(self.widget_R1_sm_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_sm_result1_gab.setFont(font)
                self.doubleSpinBox_sm_result1_gab.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_sm_result1_gab.setObjectName("doubleSpinBox_sm_result1_gab")

                sub_gridlayout_widget_R1_sm_gab.addWidget( self.label_GabResult1_sm,0,0)
                sub_gridlayout_widget_R1_sm_gab.addWidget(self.doubleSpinBox_sm_result1_gab,0,1)

                sub_gridlayout_widget_sm1.addWidget(self.label_R1_sm,0,0)
                sub_gridlayout_widget_sm1.addWidget(self.widget_R1_sm_gab,0,1)

                sub_gridlayout_widget_preproR1.addWidget(self.label_prepro1,0,0,1,2)
                sub_gridlayout_widget_preproR1.addWidget(self.widget_stepResult1,1,0,4,2)
                sub_gridlayout_widget_preproR1.addWidget(self.widget_R1_1D,5,0,3,1)
                sub_gridlayout_widget_preproR1.addWidget(self.widget_R1_2D,5,1,3,1)
                sub_gridlayout_widget_preproR1.addWidget(self.widget_sm1,8,0,2,2)

                #result1 widget
                sub_Gridlayout_result1.addWidget(self.widget_file1,0,0,1,1)
                sub_Gridlayout_result1.addWidget(self.widget_bias1,1,0,1,1)
                sub_Gridlayout_result1.addWidget(self.widget_preproR1,2,0,10,1)

                sub_gridLayout_result1.addWidget(self.widget_title_result1,0,0,1,1)
                sub_gridLayout_result1.addWidget(self.result1,1,0,12,1)

                #result 2
                self.horizontalLayoutWidget2 = QtWidgets.QWidget(self.frame1)
                self.horizontalLayoutWidget2.setStyleSheet("background-color: transparent;")
                self.horizontalLayoutWidget2.setObjectName("horizontalLayoutWidget")

                sub_gridLayout_result2 = QGridLayout(self.horizontalLayoutWidget2)

                self.widget_title_result2 = QtWidgets.QFrame(self.frame1)
                font = QtGui.QFont()
                font.setFamily("TH Sarabun New")
                self.widget_title_result2.setFont(font)
                self.widget_title_result2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border: 0px solid grey;\n"
        "border-radius: 20px;")
                self.widget_title_result2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.widget_title_result2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.widget_title_result2.setObjectName("widget_title_result2")

                sub_Gridlayout_widget_title_result2 = QGridLayout(self.widget_title_result2)
                self.label_result2 = QtWidgets.QLabel(self.widget_title_result2)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(16)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                font.setKerning(True)
                self.label_result2.setFont(font)
                self.label_result2.setAutoFillBackground(False)
                self.label_result2.setStyleSheet("font: 75 16pt \"Tahoma\";\n"
                "color: \"black\";\n"
                "background-color: rgba(255, 255, 255, 0);")
                self.label_result2.setWordWrap(False)
                self.label_result2.setObjectName("label_result1")
                sub_Gridlayout_widget_title_result2.addWidget(self.label_result2,0,0)

                
                self.result2 = QtWidgets.QFrame(self.frame1)
                font = QtGui.QFont()
                font.setFamily("TH Sarabun New")
                self.result2.setFont(font)
                self.result2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border: 0px solid grey;\n"
        "border-radius: 20px;")
                self.result2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.result2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.result2.setObjectName("result2")

                sub_Gridlayout_result2 = QGridLayout(self.result2)

                self.widget_file2 = QtWidgets.QWidget(self.result2)
                self.widget_file2.setStyleSheet("background-color:rgb(85, 170, 255);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_file2.setObjectName("widget_file2")
                
                sub_Gridlayout_widget_file2 = QGridLayout(self.widget_file2)

                self.label_calibrationfile2 = QtWidgets.QLabel(self.widget_file2)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_calibrationfile2.setFont(font)
                self.label_calibrationfile2.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_calibrationfile2.setObjectName("label_calibrationfile2")

                self.widget_browse2 = QtWidgets.QWidget(self.widget_file2)
                self.widget_browse2.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;")
                self.widget_browse2.setObjectName("widget_browse2")

                sub_Gridlayout_widget_browse2 = QGridLayout(self.widget_browse2)

                self.label_file2 = QtWidgets.QLabel(self.widget_file2)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_file2.setFont(font)
                self.label_file2.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_file2.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;")
                self.label_file2.setObjectName("label_file2")

                self.pushButton2= QtWidgets.QPushButton(self.widget_file2)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setItalic(False)
                font.setUnderline(False)
                font.setStrikeOut(False)
                self.pushButton2.setFont(font)
                self.pushButton2.setStyleSheet("background-color:rgb(170, 255, 127);\n"
        "border-radius: 15px;")
                self.pushButton2.setObjectName("pushButton")

                sub_Gridlayout_widget_browse2.addWidget(self.label_file2,0,0,1,3)
                sub_Gridlayout_widget_browse2.addWidget(self.pushButton2,0,3,1,1)

                sub_Gridlayout_widget_file2.addWidget(self.label_calibrationfile2,0,0)
                sub_Gridlayout_widget_file2.addWidget(self.widget_browse2,1,0)
                
                #widget bias2
                self.widget_bias2 = QtWidgets.QWidget(self.result2)
                self.widget_bias2.setStyleSheet("background-color:rgb(85, 170, 255);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_bias2.setObjectName("widget_bias2")
                
                sub_Gridlayout_widget_bias2 = QGridLayout(self.widget_bias2)
                
                self.label_bias2 = QtWidgets.QLabel(self.widget_bias2)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_bias2.setFont(font)
                self.label_bias2.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_bias2.setObjectName("label_bias2")
                
                self.widget_biasResult2 = QtWidgets.QWidget(self.widget_bias2)
                self.widget_biasResult2.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;")
                self.widget_biasResult2.setObjectName("widget_biasResult2")

                sub_Gridlayout_widget_biasResult2 = QGridLayout(self.widget_biasResult2)

                self.doubleSpinBox_biasResult2 = QtWidgets.QDoubleSpinBox(self.widget_biasResult2)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setBold(True)
                font.setWeight(75)
                self.doubleSpinBox_biasResult2.setFont(font)
                self.doubleSpinBox_biasResult2.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_biasResult2.setObjectName("doubleSpinBox_biasResult2")

                #doubleSpinBox_biasResult2
                sub_Gridlayout_widget_biasResult2.addWidget(self.doubleSpinBox_biasResult2,0,0)

                #widget_bias2
                sub_Gridlayout_widget_bias2.addWidget(self.label_bias2,0,0)
                sub_Gridlayout_widget_bias2.addWidget(self.widget_biasResult2,1,0)

                #prepro2
                self.widget_preproR2 = QtWidgets.QWidget(self.result2)
                self.widget_preproR2.setStyleSheet("background-color:rgb(170, 170, 255);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_preproR2.setObjectName("widget_preproR2")

                #sub_widget_prepro2
                sub_gridlayout_widget_preproR2 = QGridLayout(self.widget_preproR2)

                self.label_prepro2 = QtWidgets.QLabel(self.widget_preproR2)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_prepro2.setFont(font)
                self.label_prepro2.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_prepro2.setObjectName("label_prepro2")

                self.widget_stepResult2 = QtWidgets.QWidget(self.widget_preproR2)
                self.widget_stepResult2.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.widget_stepResult2.setObjectName("widget_stepResult2")


                #step result2
                sub_gridlayout_stepResult2 = QGridLayout(self.widget_stepResult2)

                self.label_step_result2 = QtWidgets.QLabel(self.widget_stepResult2)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setBold(False)
                font.setWeight(50)
                self.label_step_result2.setFont(font)
                self.label_step_result2.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_step_result2.setObjectName("label_step_result2")

                self.label_step1_result2 = QtWidgets.QLabel(self.widget_stepResult2)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.label_step1_result2.setFont(font)
                self.label_step1_result2.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_step1_result2.setObjectName("label_step1_result2")

                self.label_step2_result2 = QtWidgets.QLabel(self.widget_stepResult2)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.label_step2_result2.setFont(font)
                self.label_step2_result2.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_step2_result2.setObjectName("label_step2_result2")

                self.label_step3_result2 = QtWidgets.QLabel(self.widget_stepResult2)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.label_step3_result2.setFont(font)
                self.label_step3_result2.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_step3_result2.setObjectName("label_step3_result2")

                self.comboBox_step1_result2 = QtWidgets.QComboBox(self.widget_stepResult2)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.comboBox_step1_result2.setFont(font)
                self.comboBox_step1_result2.setObjectName("comboBox_step1_result2")
                self.comboBox_step1_result2.addItem("")
                self.comboBox_step1_result2.addItem("")
                self.comboBox_step1_result2.addItem("")
                self.comboBox_step1_result2.addItem("")
                self.comboBox_step1_result2.addItem("")
                self.comboBox_step2_result2 = QtWidgets.QComboBox(self.widget_stepResult2)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.comboBox_step2_result2.setFont(font)
                self.comboBox_step2_result2.setObjectName("comboBox_step2_result2")
                self.comboBox_step2_result2.addItem("")
                self.comboBox_step2_result2.addItem("")
                self.comboBox_step2_result2.addItem("")
                self.comboBox_step2_result2.addItem("")
                self.comboBox_step2_result2.addItem("")
                self.comboBox_step3_result2 = QtWidgets.QComboBox(self.widget_stepResult2)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.comboBox_step3_result2.setFont(font)
                self.comboBox_step3_result2.setObjectName("comboBox_step3_result2")
                self.comboBox_step3_result2.addItem("")
                self.comboBox_step3_result2.addItem("")
                self.comboBox_step3_result2.addItem("")
                self.comboBox_step3_result2.addItem("")
                self.comboBox_step3_result2.addItem("")

                sub_gridlayout_stepResult2.addWidget(self.label_step_result2,0,0,1,3)

                sub_gridlayout_stepResult2.addWidget(self.label_step1_result2,1,0,1,1)
                sub_gridlayout_stepResult2.addWidget(self.label_step2_result2,2,0,1,1)
                sub_gridlayout_stepResult2.addWidget(self.label_step3_result2,3,0,1,1)

                sub_gridlayout_stepResult2.addWidget(self.comboBox_step1_result2,1,1,1,2)
                sub_gridlayout_stepResult2.addWidget(self.comboBox_step2_result2,2,1,1,2)
                sub_gridlayout_stepResult2.addWidget(self.comboBox_step3_result2,3,1,1,2)


                self.widget_R2_1D = QtWidgets.QWidget(self.widget_preproR2)
                self.widget_R2_1D.setStyleSheet("background-color:rgb(170, 255, 127);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_R2_1D.setObjectName("widget_R1_1D")

                sub_gridlayout_widget_R2_1D = QGridLayout(self.widget_R2_1D)
                
                self.label_R2_1stD = QtWidgets.QLabel(self.widget_R2_1D)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_R2_1stD.setFont(font)
                self.label_R2_1stD.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_R2_1stD.setObjectName("label_R2_1stD")

                self.widget_1D_result2_gab = QtWidgets.QWidget(self.widget_R2_1D)
                self.widget_1D_result2_gab.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;\n"
        "")
                self.widget_1D_result2_gab.setObjectName("widget_1D_result2_gab")

                sub_gridlayout_widget_1D_result2_gab = QGridLayout(self.widget_1D_result2_gab)

                self.label_GabResult2_1D = QtWidgets.QLabel(self.widget_1D_result2_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                self.label_GabResult2_1D.setFont(font)
                self.label_GabResult2_1D.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_GabResult2_1D.setObjectName("label_GabResult2_1D")

                self.doubleSpinBox_1D_result2_gab = QtWidgets.QDoubleSpinBox(self.widget_1D_result2_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_1D_result2_gab.setFont(font)
                self.doubleSpinBox_1D_result2_gab.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_1D_result2_gab.setObjectName("doubleSpinBox_1D_result2_gab")

                sub_gridlayout_widget_1D_result2_gab.addWidget(self.label_GabResult2_1D,0,0)
                sub_gridlayout_widget_1D_result2_gab.addWidget(self.doubleSpinBox_1D_result2_gab,0,1)

                self.widget_1D_result2_sg = QtWidgets.QWidget(self.widget_R2_1D)
                self.widget_1D_result2_sg.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;\n"
        "")
                self.widget_1D_result2_sg.setObjectName("widget_1D_result2_sg")

                sub_gridlayout_widget_1D_result2_sg = QGridLayout(self.widget_1D_result2_sg)

                self.label_SGResult2_1D = QtWidgets.QLabel(self.widget_1D_result2_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                self.label_SGResult2_1D.setFont(font)
                self.label_SGResult2_1D.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_SGResult2_1D.setObjectName("label_SGResult2_1D")

                self.doubleSpinBox_1D_result2_sg = QtWidgets.QDoubleSpinBox(self.widget_1D_result2_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_1D_result2_sg.setFont(font)
                self.doubleSpinBox_1D_result2_sg.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_1D_result2_sg.setObjectName("doubleSpinBox_1D_result2_sg")

                sub_gridlayout_widget_1D_result2_sg.addWidget(self.label_SGResult2_1D,0,0)
                sub_gridlayout_widget_1D_result2_sg.addWidget(self.doubleSpinBox_1D_result2_sg,0,1)


                sub_gridlayout_widget_R2_1D.addWidget(self.label_R2_1stD,0,0)
                sub_gridlayout_widget_R2_1D.addWidget(self.widget_1D_result2_gab,1,0)
                sub_gridlayout_widget_R2_1D.addWidget(self.widget_1D_result2_sg,2,0)


                self.widget_R2_2D = QtWidgets.QWidget(self.widget_preproR2)
                self.widget_R2_2D.setStyleSheet("background-color:rgb(170, 255, 127);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_R2_2D.setObjectName("widget_R2_2D")

                sub_gridlayout_widget_R2_2D = QGridLayout(self.widget_R2_2D)
                
                self.label_R2_2ndD = QtWidgets.QLabel(self.widget_R2_2D)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_R2_2ndD.setFont(font)
                self.label_R2_2ndD.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_R2_2ndD.setObjectName("label_R2_2ndD")

                self.widget_2D_result2_gab = QtWidgets.QWidget(self.widget_R2_2D)
                self.widget_2D_result2_gab.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;\n"
        "")
                self.widget_2D_result2_gab.setObjectName("widget_2D_result2_gab")

                sub_gridlayout_widget_2D_result2_gab = QGridLayout(self.widget_2D_result2_gab)

                self.label_GabResult2_2D = QtWidgets.QLabel(self.widget_2D_result2_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                self.label_GabResult2_2D.setFont(font)
                self.label_GabResult2_2D.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_GabResult2_2D.setObjectName("label_GabResult2_2D")

                self.doubleSpinBox_2D_result2_gab = QtWidgets.QDoubleSpinBox(self.widget_2D_result2_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_2D_result2_gab.setFont(font)
                self.doubleSpinBox_2D_result2_gab.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_2D_result2_gab.setObjectName("doubleSpinBox_2D_result2_gab")

                sub_gridlayout_widget_2D_result2_gab.addWidget(self.label_GabResult2_2D,0,0)
                sub_gridlayout_widget_2D_result2_gab.addWidget(self.doubleSpinBox_2D_result2_gab,0,1)

                self.widget_2D_result2_sg = QtWidgets.QWidget(self.widget_R2_2D)
                self.widget_2D_result2_sg.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;\n"
        "")
                self.widget_2D_result2_sg.setObjectName("widget_2D_result2_sg")

                sub_gridlayout_widget_2D_result2_sg = QGridLayout(self.widget_2D_result2_sg)

                self.label_SGResult2_2D = QtWidgets.QLabel(self.widget_2D_result2_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                self.label_SGResult2_2D.setFont(font)
                self.label_SGResult2_2D.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_SGResult2_2D.setObjectName("label_SGResult2_2D")

                self.doubleSpinBox_2D_result2_sg = QtWidgets.QDoubleSpinBox(self.widget_2D_result2_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_2D_result2_sg.setFont(font)
                self.doubleSpinBox_2D_result2_sg.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_2D_result2_sg.setObjectName("doubleSpinBox_2D_result2_sg")

                sub_gridlayout_widget_2D_result2_sg.addWidget(self.label_SGResult2_2D,0,0)
                sub_gridlayout_widget_2D_result2_sg.addWidget(self.doubleSpinBox_2D_result2_sg,0,1)


                sub_gridlayout_widget_R2_2D.addWidget(self.label_R2_2ndD,0,0)
                sub_gridlayout_widget_R2_2D.addWidget(self.widget_2D_result2_gab,1,0)
                sub_gridlayout_widget_R2_2D.addWidget(self.widget_2D_result2_sg,2,0)


                #smoothing size1
                self.widget_sm2 = QtWidgets.QWidget(self.widget_preproR2)
                self.widget_sm2.setStyleSheet("background-color:rgb(170, 255, 127);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_sm2.setObjectName("widget_sm1")

                sub_gridlayout_widget_sm2 = QGridLayout(self.widget_sm2)

                self.label_R2_sm = QtWidgets.QLabel(self.widget_sm2)
                self.label_R2_sm.setGeometry(QtCore.QRect(10, 0, 141, 51))
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(6)
                font.setBold(True)
                font.setWeight(75)
                self.label_R2_sm.setFont(font)
                self.label_R2_sm.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_R2_sm.setObjectName("label_R1_sm")
                
                self.widget_R2_sm_gab = QtWidgets.QWidget(self.widget_sm2)
                self.widget_R2_sm_gab.setGeometry(QtCore.QRect(170, 10, 131, 31))
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.widget_R2_sm_gab.setFont(font)
                self.widget_R2_sm_gab.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;")
                self.widget_R2_sm_gab.setObjectName("widget_R2_sm_gab")

                sub_gridlayout_widget_R2_sm_gab = QGridLayout(self.widget_R2_sm_gab)

                self.label_GabResult2_sm = QtWidgets.QLabel(self.widget_R2_sm_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.label_GabResult2_sm.setFont(font)
                self.label_GabResult2_sm.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_GabResult2_sm.setObjectName("label_GabResult2_sm")

                self.doubleSpinBox_sm_result2_gab = QtWidgets.QDoubleSpinBox(self.widget_R2_sm_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_sm_result2_gab.setFont(font)
                self.doubleSpinBox_sm_result2_gab.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_sm_result2_gab.setObjectName("doubleSpinBox_sm_result2_gab")

                sub_gridlayout_widget_R2_sm_gab.addWidget( self.label_GabResult2_sm,0,0)
                sub_gridlayout_widget_R2_sm_gab.addWidget(self.doubleSpinBox_sm_result2_gab,0,1)

                sub_gridlayout_widget_sm2.addWidget(self.label_R2_sm,0,0)
                sub_gridlayout_widget_sm2.addWidget(self.widget_R2_sm_gab,0,1)

                sub_gridlayout_widget_preproR2.addWidget(self.label_prepro2,0,0,1,2)
                sub_gridlayout_widget_preproR2.addWidget(self.widget_stepResult2,1,0,4,2)
                sub_gridlayout_widget_preproR2.addWidget(self.widget_R2_1D,5,0,2,1)
                sub_gridlayout_widget_preproR2.addWidget(self.widget_R2_2D,5,1,2,1)
                sub_gridlayout_widget_preproR2.addWidget(self.widget_sm2,7,0,2,2)

                #result2 widget
                sub_Gridlayout_result2.addWidget(self.widget_file2,0,0,1,1)
                sub_Gridlayout_result2.addWidget(self.widget_bias2,1,0,1,1)
                sub_Gridlayout_result2.addWidget(self.widget_preproR2,2,0,6,1)


                sub_gridLayout_result2.addWidget(self.widget_title_result2,0,0)
                sub_gridLayout_result2.addWidget(self.result2,1,0,8,1)

                #result 3
                self.horizontalLayoutWidget3 = QtWidgets.QWidget(self.frame1)
                self.horizontalLayoutWidget3.setStyleSheet("background-color: transparent;")
                self.horizontalLayoutWidget3.setObjectName("horizontalLayoutWidget")

                sub_gridLayout_result3 = QGridLayout(self.horizontalLayoutWidget3)

                self.widget_title_result3 = QtWidgets.QFrame(self.frame1)
                font = QtGui.QFont()
                font.setFamily("TH Sarabun New")
                self.widget_title_result3.setFont(font)
                self.widget_title_result3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border: 0px solid grey;\n"
        "border-radius: 20px;")
                self.widget_title_result3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.widget_title_result3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.widget_title_result3.setObjectName("widget_title_result3")

                sub_Gridlayout_widget_title_result3 = QGridLayout(self.widget_title_result3)
                self.label_result3 = QtWidgets.QLabel(self.widget_title_result3)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(16)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                font.setKerning(True)
                self.label_result3.setFont(font)
                self.label_result3.setAutoFillBackground(False)
                self.label_result3.setStyleSheet("font: 75 16pt \"Tahoma\";\n"
                "color: \"black\";\n"
                "background-color: rgba(255, 255, 255, 0);")
                self.label_result3.setWordWrap(False)
                self.label_result3.setObjectName("label_result1")
                sub_Gridlayout_widget_title_result3.addWidget(self.label_result3,0,0)
                
                self.result3 = QtWidgets.QFrame(self.frame1)
                font = QtGui.QFont()
                font.setFamily("TH Sarabun New")
                self.result3.setFont(font)
                self.result3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border: 0px solid grey;\n"
        "border-radius: 20px;")
                self.result3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.result3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.result3.setObjectName("result3")

                sub_Gridlayout_result3 = QGridLayout(self.result3)

                self.widget_file3 = QtWidgets.QWidget(self.result3)
                self.widget_file3.setStyleSheet("background-color:rgb(85, 170, 255);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_file3.setObjectName("widget_file3")
                
                sub_Gridlayout_widget_file3 = QGridLayout(self.widget_file3)

                self.label_calibrationfile3= QtWidgets.QLabel(self.widget_file3)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_calibrationfile3.setFont(font)
                self.label_calibrationfile3.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_calibrationfile3.setObjectName("label_calibrationfile3")

                self.widget_browse3 = QtWidgets.QWidget(self.widget_file3)
                self.widget_browse3.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;")
                self.widget_browse3.setObjectName("widget_browse3")

                sub_Gridlayout_widget_browse3 = QGridLayout(self.widget_browse3)

                self.label_file3 = QtWidgets.QLabel(self.widget_file3)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_file3.setFont(font)
                self.label_file3.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_file3.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;")
                self.label_file3.setObjectName("label_file3")

                self.pushButton3 = QtWidgets.QPushButton(self.widget_file3)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setItalic(False)
                font.setUnderline(False)
                font.setStrikeOut(False)
                self.pushButton3.setFont(font)
                self.pushButton3.setStyleSheet("background-color:rgb(170, 255, 127);\n"
        "border-radius: 15px;")
                self.pushButton3.setObjectName("pushButton3")

                sub_Gridlayout_widget_browse3.addWidget(self.label_file3,0,0,1,3)
                sub_Gridlayout_widget_browse3.addWidget(self.pushButton3,0,3,1,1)

                sub_Gridlayout_widget_file3.addWidget(self.label_calibrationfile3,0,0)
                sub_Gridlayout_widget_file3.addWidget(self.widget_browse3,1,0)

                #widget bias3
                self.widget_bias3 = QtWidgets.QWidget(self.result3)
                self.widget_bias3.setStyleSheet("background-color:rgb(85, 170, 255);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_bias3.setObjectName("widget_bias3")
                
                sub_Gridlayout_widget_bias3 = QGridLayout(self.widget_bias3)
                
                self.label_bias3 = QtWidgets.QLabel(self.widget_bias3)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_bias3.setFont(font)
                self.label_bias3.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_bias3.setObjectName("label_bias3")
                
                self.widget_biasResult3 = QtWidgets.QWidget(self.widget_bias3)
                self.widget_biasResult3.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;")
                self.widget_biasResult3.setObjectName("widget_biasResult3")

                sub_Gridlayout_widget_biasResult3 = QGridLayout(self.widget_biasResult3)

                self.doubleSpinBox_biasResult3 = QtWidgets.QDoubleSpinBox(self.widget_biasResult3)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setBold(True)
                font.setWeight(75)
                self.doubleSpinBox_biasResult3.setFont(font)
                self.doubleSpinBox_biasResult3.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_biasResult3.setObjectName("doubleSpinBox_biasResult3")

                #doubleSpinBox_biasResult3
                sub_Gridlayout_widget_biasResult3.addWidget(self.doubleSpinBox_biasResult3,0,0)

                #widget_bias3
                sub_Gridlayout_widget_bias3.addWidget(self.label_bias3,0,0)
                sub_Gridlayout_widget_bias3.addWidget(self.widget_biasResult3,1,0)

                #prepro3
                self.widget_preproR3 = QtWidgets.QWidget(self.result3)
                self.widget_preproR3.setStyleSheet("background-color:rgb(170, 170, 255);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_preproR3.setObjectName("widget_preproR3")

                #sub_widget_prepro3
                sub_gridlayout_widget_preproR3 = QGridLayout(self.widget_preproR3)

                self.label_prepro3 = QtWidgets.QLabel(self.widget_preproR3)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_prepro3.setFont(font)
                self.label_prepro3.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_prepro3.setObjectName("label_prepro3")

                self.widget_stepResult3 = QtWidgets.QWidget(self.widget_preproR3)
                self.widget_stepResult3.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.widget_stepResult3.setObjectName("widget_stepResult3")

                #step result3
                sub_gridlayout_stepResult3 = QGridLayout(self.widget_stepResult3)

                self.label_step_result3 = QtWidgets.QLabel(self.widget_stepResult3)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setBold(False)
                font.setWeight(50)
                self.label_step_result3.setFont(font)
                self.label_step_result3.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_step_result3.setObjectName("label_step_result3")

                self.label_step1_result3 = QtWidgets.QLabel(self.widget_stepResult3)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.label_step1_result3.setFont(font)
                self.label_step1_result3.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_step1_result3.setObjectName("label_step1_result3")

                self.label_step2_result3 = QtWidgets.QLabel(self.widget_stepResult3)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.label_step2_result3.setFont(font)
                self.label_step2_result3.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_step2_result3.setObjectName("label_step2_result3")

                self.label_step3_result3 = QtWidgets.QLabel(self.widget_stepResult3)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.label_step3_result3.setFont(font)
                self.label_step3_result3.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_step3_result3.setObjectName("label_step3_result3")

                self.comboBox_step1_result3 = QtWidgets.QComboBox(self.widget_stepResult3)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.comboBox_step1_result3.setFont(font)
                self.comboBox_step1_result3.setObjectName("comboBox_step1_result3")
                self.comboBox_step1_result3.addItem("")
                self.comboBox_step1_result3.addItem("")
                self.comboBox_step1_result3.addItem("")
                self.comboBox_step1_result3.addItem("")
                self.comboBox_step1_result3.addItem("")
                self.comboBox_step2_result3 = QtWidgets.QComboBox(self.widget_stepResult3)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.comboBox_step2_result3.setFont(font)
                self.comboBox_step2_result3.setObjectName("comboBox_step2_result3")
                self.comboBox_step2_result3.addItem("")
                self.comboBox_step2_result3.addItem("")
                self.comboBox_step2_result3.addItem("")
                self.comboBox_step2_result3.addItem("")
                self.comboBox_step2_result3.addItem("")
                self.comboBox_step3_result3 = QtWidgets.QComboBox(self.widget_stepResult3)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.comboBox_step3_result3.setFont(font)
                self.comboBox_step3_result3.setObjectName("comboBox_step3_result3")
                self.comboBox_step3_result3.addItem("")
                self.comboBox_step3_result3.addItem("")
                self.comboBox_step3_result3.addItem("")
                self.comboBox_step3_result3.addItem("")
                self.comboBox_step3_result3.addItem("")

                sub_gridlayout_stepResult3.addWidget(self.label_step_result3,0,0,1,3)

                sub_gridlayout_stepResult3.addWidget(self.label_step1_result3,1,0,1,1)
                sub_gridlayout_stepResult3.addWidget(self.label_step2_result3,2,0,1,1)
                sub_gridlayout_stepResult3.addWidget(self.label_step3_result3,3,0,1,1)

                sub_gridlayout_stepResult3.addWidget(self.comboBox_step1_result3,1,1,1,2)
                sub_gridlayout_stepResult3.addWidget(self.comboBox_step2_result3,2,1,1,2)
                sub_gridlayout_stepResult3.addWidget(self.comboBox_step3_result3,3,1,1,2)



                self.widget_R3_1D = QtWidgets.QWidget(self.widget_preproR3)
                self.widget_R3_1D.setStyleSheet("background-color:rgb(170, 255, 127);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_R3_1D.setObjectName("widget_R3_1D")

                sub_gridlayout_widget_R3_1D = QGridLayout(self.widget_R3_1D)
                
                self.label_R3_1stD = QtWidgets.QLabel(self.widget_R3_1D)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_R3_1stD.setFont(font)
                self.label_R3_1stD.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_R3_1stD.setObjectName("label_R3_1stD")

                self.widget_1D_result3_gab = QtWidgets.QWidget(self.widget_R3_1D)
                self.widget_1D_result3_gab.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;\n"
        "")
                self.widget_1D_result3_gab.setObjectName("widget_1D_result3_gab")

                sub_gridlayout_widget_1D_result3_gab = QGridLayout(self.widget_1D_result3_gab)

                self.label_GabResult3_1D = QtWidgets.QLabel(self.widget_1D_result3_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                self.label_GabResult3_1D.setFont(font)
                self.label_GabResult3_1D.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_GabResult3_1D.setObjectName("label_GabResult3_1D")

                self.doubleSpinBox_1D_result3_gab = QtWidgets.QDoubleSpinBox(self.widget_1D_result3_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_1D_result3_gab.setFont(font)
                self.doubleSpinBox_1D_result3_gab.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_1D_result3_gab.setObjectName("doubleSpinBox_1D_result3_gab")

                sub_gridlayout_widget_1D_result3_gab.addWidget(self.label_GabResult3_1D,0,0)
                sub_gridlayout_widget_1D_result3_gab.addWidget(self.doubleSpinBox_1D_result3_gab,0,1)

                self.widget_1D_result3_sg = QtWidgets.QWidget(self.widget_R3_1D)
                self.widget_1D_result3_sg.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;\n"
        "")
                self.widget_1D_result3_sg.setObjectName("widget_1D_result3_sg")

                sub_gridlayout_widget_1D_result3_sg = QGridLayout(self.widget_1D_result3_sg)

                self.label_SGResult3_1D = QtWidgets.QLabel(self.widget_1D_result3_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                self.label_SGResult3_1D.setFont(font)
                self.label_SGResult3_1D.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_SGResult3_1D.setObjectName("label_SGResult3_1D")

                self.doubleSpinBox_1D_result3_sg = QtWidgets.QDoubleSpinBox(self.widget_1D_result3_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_1D_result3_sg.setFont(font)
                self.doubleSpinBox_1D_result3_sg.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_1D_result3_sg.setObjectName("doubleSpinBox_1D_result3_sg")

                sub_gridlayout_widget_1D_result3_sg.addWidget(self.label_SGResult3_1D,0,0)
                sub_gridlayout_widget_1D_result3_sg.addWidget(self.doubleSpinBox_1D_result3_sg,0,1)


                sub_gridlayout_widget_R3_1D.addWidget(self.label_R3_1stD,0,0)
                sub_gridlayout_widget_R3_1D.addWidget(self.widget_1D_result3_gab,1,0)
                sub_gridlayout_widget_R3_1D.addWidget(self.widget_1D_result3_sg,2,0)


                self.widget_R3_2D = QtWidgets.QWidget(self.widget_preproR3)
                self.widget_R3_2D.setStyleSheet("background-color:rgb(170, 255, 127);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_R3_2D.setObjectName("widget_R3_2D")

                sub_gridlayout_widget_R3_2D = QGridLayout(self.widget_R3_2D)
                
                self.label_R3_2ndD = QtWidgets.QLabel(self.widget_R3_2D)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_R3_2ndD.setFont(font)
                self.label_R3_2ndD.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_R3_2ndD.setObjectName("label_R3_2ndD")

                self.widget_2D_result3_gab = QtWidgets.QWidget(self.widget_R3_2D)
                self.widget_2D_result3_gab.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;\n"
        "")
                self.widget_2D_result3_gab.setObjectName("widget_2D_result3_gab")

                sub_gridlayout_widget_2D_result3_gab = QGridLayout(self.widget_2D_result3_gab)

                self.label_GabResult3_2D = QtWidgets.QLabel(self.widget_2D_result3_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                self.label_GabResult3_2D.setFont(font)
                self.label_GabResult3_2D.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_GabResult3_2D.setObjectName("label_GabResult3_2D")

                self.doubleSpinBox_2D_result3_gab = QtWidgets.QDoubleSpinBox(self.widget_2D_result3_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_2D_result3_gab.setFont(font)
                self.doubleSpinBox_2D_result3_gab.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_2D_result3_gab.setObjectName("doubleSpinBox_2D_result3_gab")

                sub_gridlayout_widget_2D_result3_gab.addWidget(self.label_GabResult3_2D,0,0)
                sub_gridlayout_widget_2D_result3_gab.addWidget(self.doubleSpinBox_2D_result3_gab,0,1)

                self.widget_2D_result3_sg = QtWidgets.QWidget(self.widget_R3_2D)
                self.widget_2D_result3_sg.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;\n"
        "")
                self.widget_2D_result3_sg.setObjectName("widget_2D_result3_sg")

                sub_gridlayout_widget_2D_result3_sg = QGridLayout(self.widget_2D_result3_sg)

                self.label_SGResult3_2D = QtWidgets.QLabel(self.widget_2D_result3_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                self.label_SGResult3_2D.setFont(font)
                self.label_SGResult3_2D.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_SGResult3_2D.setObjectName("label_SGResult3_2D")

                self.doubleSpinBox_2D_result3_sg = QtWidgets.QDoubleSpinBox(self.widget_2D_result3_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_2D_result3_sg.setFont(font)
                self.doubleSpinBox_2D_result3_sg.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_2D_result3_sg.setObjectName("doubleSpinBox_2D_result3_sg")

                sub_gridlayout_widget_2D_result3_sg.addWidget(self.label_SGResult3_2D,0,0)
                sub_gridlayout_widget_2D_result3_sg.addWidget(self.doubleSpinBox_2D_result3_sg,0,1)


                sub_gridlayout_widget_R3_2D.addWidget(self.label_R3_2ndD,0,0)
                sub_gridlayout_widget_R3_2D.addWidget(self.widget_2D_result3_gab,1,0)
                sub_gridlayout_widget_R3_2D.addWidget(self.widget_2D_result3_sg,2,0)


                #smoothing size3
                self.widget_sm3 = QtWidgets.QWidget(self.widget_preproR3)
                self.widget_sm3.setStyleSheet("background-color:rgb(170, 255, 127);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_sm3.setObjectName("widget_sm3")

                sub_gridlayout_widget_sm3 = QGridLayout(self.widget_sm3)

                self.label_R3_sm = QtWidgets.QLabel(self.widget_sm3)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(6)
                font.setBold(True)
                font.setWeight(75)
                self.label_R3_sm.setFont(font)
                self.label_R3_sm.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_R3_sm.setObjectName("label_R3_sm")
                
                self.widget_R3_sm_gab = QtWidgets.QWidget(self.widget_sm1)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.widget_R3_sm_gab.setFont(font)
                self.widget_R3_sm_gab.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;")
                self.widget_R3_sm_gab.setObjectName("widget_R3_sm_gab")

                sub_gridlayout_widget_R3_sm_gab = QGridLayout(self.widget_R3_sm_gab)

                self.label_GabResult3_sm = QtWidgets.QLabel(self.widget_R3_sm_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.label_GabResult3_sm.setFont(font)
                self.label_GabResult3_sm.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_GabResult3_sm.setObjectName("label_GabResult3_sm")

                self.doubleSpinBox_sm_result3_gab = QtWidgets.QDoubleSpinBox(self.widget_R3_sm_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_sm_result3_gab.setFont(font)
                self.doubleSpinBox_sm_result3_gab.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_sm_result3_gab.setObjectName("doubleSpinBox_sm_result3_gab")

                sub_gridlayout_widget_R3_sm_gab.addWidget( self.label_GabResult3_sm,0,0)
                sub_gridlayout_widget_R3_sm_gab.addWidget(self.doubleSpinBox_sm_result3_gab,0,1)

                sub_gridlayout_widget_sm3.addWidget(self.label_R3_sm,0,0)
                sub_gridlayout_widget_sm3.addWidget(self.widget_R3_sm_gab,0,1)

                sub_gridlayout_widget_preproR3.addWidget(self.label_prepro3,0,0,1,2)
                sub_gridlayout_widget_preproR3.addWidget(self.widget_stepResult3,1,0,4,2)
                sub_gridlayout_widget_preproR3.addWidget(self.widget_R3_1D,5,0,2,1)
                sub_gridlayout_widget_preproR3.addWidget(self.widget_R3_2D,5,1,2,1)
                sub_gridlayout_widget_preproR3.addWidget(self.widget_sm3,7,0,2,2)

                #result3 widget
                sub_Gridlayout_result3.addWidget(self.widget_file3,0,0,1,1)
                sub_Gridlayout_result3.addWidget(self.widget_bias3,1,0,1,1)
                sub_Gridlayout_result3.addWidget(self.widget_preproR3,2,0,6,1)


                sub_gridLayout_result3.addWidget(self.widget_title_result3,0,0)
                sub_gridLayout_result3.addWidget(self.result3,1,0,8,1)

                #result 4
                self.horizontalLayoutWidget4 = QtWidgets.QWidget(self.frame1)
                self.horizontalLayoutWidget4.setStyleSheet("background-color: transparent;")
                self.horizontalLayoutWidget4.setObjectName("horizontalLayoutWidget4")

                sub_gridLayout_result4 = QGridLayout(self.horizontalLayoutWidget4)

                self.widget_title_result4 = QtWidgets.QFrame(self.frame1)
                font = QtGui.QFont()
                font.setFamily("TH Sarabun New")
                self.widget_title_result4.setFont(font)
                self.widget_title_result4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border: 0px solid grey;\n"
        "border-radius: 20px;")
                self.widget_title_result4.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.widget_title_result4.setFrameShadow(QtWidgets.QFrame.Raised)
                self.widget_title_result4.setObjectName("widget_title_result4")

                sub_Gridlayout_widget_title_result4 = QGridLayout(self.widget_title_result4)
                self.label_result4 = QtWidgets.QLabel(self.widget_title_result4)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(16)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                font.setKerning(True)
                self.label_result4.setFont(font)
                self.label_result4.setAutoFillBackground(False)
                self.label_result4.setStyleSheet("font: 75 16pt \"Tahoma\";\n"
                "color: \"black\";\n"
                "background-color: rgba(255, 255, 255, 0);")
                self.label_result4.setWordWrap(False)
                self.label_result4.setObjectName("label_result4")
                sub_Gridlayout_widget_title_result4.addWidget(self.label_result4,0,0)
                
                self.result4 = QtWidgets.QFrame(self.frame1)
                font = QtGui.QFont()
                font.setFamily("TH Sarabun New")
                self.result4.setFont(font)
                self.result4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border: 0px solid grey;\n"
        "border-radius: 20px;")
                self.result4.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.result4.setFrameShadow(QtWidgets.QFrame.Raised)
                self.result4.setObjectName("result4")

                sub_Gridlayout_result4 = QGridLayout(self.result4)

                self.widget_file4 = QtWidgets.QWidget(self.result4)
                self.widget_file4.setStyleSheet("background-color:rgb(85, 170, 255);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_file4.setObjectName("widget_file4")
                
                sub_Gridlayout_widget_file4 = QGridLayout(self.widget_file4)

                self.label_calibrationfile4 = QtWidgets.QLabel(self.widget_file4)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_calibrationfile4.setFont(font)
                self.label_calibrationfile4.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_calibrationfile4.setObjectName("label_calibrationfile4")

                self.widget_browse4 = QtWidgets.QWidget(self.widget_file4)
                self.widget_browse4.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;")
                self.widget_browse4.setObjectName("widget_browse4")

                sub_Gridlayout_widget_browse4 = QGridLayout(self.widget_browse4)

                self.label_file4 = QtWidgets.QLabel(self.widget_file4)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_file4.setFont(font)
                self.label_file4.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_file4.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;")
                self.label_file4.setObjectName("label_file4")

                self.pushButton4 = QtWidgets.QPushButton(self.widget_file4)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setItalic(False)
                font.setUnderline(False)
                font.setStrikeOut(False)
                self.pushButton4.setFont(font)
                self.pushButton4.setStyleSheet("background-color:rgb(170, 255, 127);\n"
        "border-radius: 15px;")
                self.pushButton4.setObjectName("pushButton4")

                sub_Gridlayout_widget_browse4.addWidget(self.label_file4,0,0,1,3)
                sub_Gridlayout_widget_browse4.addWidget(self.pushButton4,0,3,1,1)

                sub_Gridlayout_widget_file4.addWidget(self.label_calibrationfile4,0,0)
                sub_Gridlayout_widget_file4.addWidget(self.widget_browse4,1,0)
                
                #widget bias4
                self.widget_bias4 = QtWidgets.QWidget(self.result4)
                self.widget_bias4.setStyleSheet("background-color:rgb(85, 170, 255);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_bias4.setObjectName("widget_bias4")
                
                sub_Gridlayout_widget_bias4 = QGridLayout(self.widget_bias4)
                
                self.label_bias4 = QtWidgets.QLabel(self.widget_bias4)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_bias4.setFont(font)
                self.label_bias4.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_bias4.setObjectName("label_bias4")
                
                self.widget_biasResult4 = QtWidgets.QWidget(self.widget_bias4)
                self.widget_biasResult4.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;")
                self.widget_biasResult4.setObjectName("widget_biasResult4")

                sub_Gridlayout_widget_biasResult4 = QGridLayout(self.widget_biasResult4)

                self.doubleSpinBox_biasResult4 = QtWidgets.QDoubleSpinBox(self.widget_biasResult4)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setBold(True)
                font.setWeight(75)
                self.doubleSpinBox_biasResult4.setFont(font)
                self.doubleSpinBox_biasResult4.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_biasResult4.setObjectName("doubleSpinBox_biasResult4")

                #doubleSpinBox_biasResult4
                sub_Gridlayout_widget_biasResult4.addWidget(self.doubleSpinBox_biasResult4,0,0)

                #widget_bias4
                sub_Gridlayout_widget_bias4.addWidget(self.label_bias4,0,0)
                sub_Gridlayout_widget_bias4.addWidget(self.widget_biasResult4,1,0)

                #prepro4
                self.widget_preproR4 = QtWidgets.QWidget(self.result4)
                self.widget_preproR4.setStyleSheet("background-color:rgb(170, 170, 255);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_preproR4.setObjectName("widget_prepro4")

                #sub_widget_prepro4
                sub_gridlayout_widget_preproR4 = QGridLayout(self.widget_preproR4)

                self.label_prepro4 = QtWidgets.QLabel(self.widget_preproR4)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_prepro4.setFont(font)
                self.label_prepro4.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_prepro4.setObjectName("label_prepro4")

                self.widget_stepResult4 = QtWidgets.QWidget(self.widget_preproR4)
                self.widget_stepResult4.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.widget_stepResult4.setObjectName("widget_stepResult4")


                #step result4
                sub_gridlayout_stepResult4 = QGridLayout(self.widget_stepResult4)

                self.label_step_result4 = QtWidgets.QLabel(self.widget_stepResult4)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setBold(False)
                font.setWeight(50)
                self.label_step_result4.setFont(font)
                self.label_step_result4.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_step_result4.setObjectName("label_step_result4")

                self.label_step1_result4 = QtWidgets.QLabel(self.widget_stepResult4)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.label_step1_result4.setFont(font)
                self.label_step1_result4.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_step1_result4.setObjectName("label_step1_result4")

                self.label_step2_result4 = QtWidgets.QLabel(self.widget_stepResult4)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.label_step2_result4.setFont(font)
                self.label_step2_result4.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_step2_result4.setObjectName("label_step2_result4")

                self.label_step3_result4 = QtWidgets.QLabel(self.widget_stepResult4)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.label_step3_result4.setFont(font)
                self.label_step3_result4.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_step3_result4.setObjectName("label_step3_result4")

                self.comboBox_step1_result4 = QtWidgets.QComboBox(self.widget_stepResult4)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.comboBox_step1_result4.setFont(font)
                self.comboBox_step1_result4.setObjectName("comboBox_step1_result4")
                self.comboBox_step1_result4.addItem("")
                self.comboBox_step1_result4.addItem("")
                self.comboBox_step1_result4.addItem("")
                self.comboBox_step1_result4.addItem("")
                self.comboBox_step1_result4.addItem("")
                self.comboBox_step2_result4 = QtWidgets.QComboBox(self.widget_stepResult4)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.comboBox_step2_result4.setFont(font)
                self.comboBox_step2_result4.setObjectName("comboBox_step2_result4")
                self.comboBox_step2_result4.addItem("")
                self.comboBox_step2_result4.addItem("")
                self.comboBox_step2_result4.addItem("")
                self.comboBox_step2_result4.addItem("")
                self.comboBox_step2_result4.addItem("")
                self.comboBox_step3_result4 = QtWidgets.QComboBox(self.widget_stepResult4)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.comboBox_step3_result4.setFont(font)
                self.comboBox_step3_result4.setObjectName("comboBox_step3_result4")
                self.comboBox_step3_result4.addItem("")
                self.comboBox_step3_result4.addItem("")
                self.comboBox_step3_result4.addItem("")
                self.comboBox_step3_result4.addItem("")
                self.comboBox_step3_result4.addItem("")

                sub_gridlayout_stepResult4.addWidget(self.label_step_result4,0,0,1,3)

                sub_gridlayout_stepResult4.addWidget(self.label_step1_result4,1,0,1,1)
                sub_gridlayout_stepResult4.addWidget(self.label_step2_result4,2,0,1,1)
                sub_gridlayout_stepResult4.addWidget(self.label_step3_result4,3,0,1,1)

                sub_gridlayout_stepResult4.addWidget(self.comboBox_step1_result4,1,1,1,2)
                sub_gridlayout_stepResult4.addWidget(self.comboBox_step2_result4,2,1,1,2)
                sub_gridlayout_stepResult4.addWidget(self.comboBox_step3_result4,3,1,1,2)

                self.widget_R4_1D = QtWidgets.QWidget(self.widget_preproR4)
                self.widget_R4_1D.setStyleSheet("background-color:rgb(170, 255, 127);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_R4_1D.setObjectName("widget_R4_1D")

                sub_gridlayout_widget_R4_1D = QGridLayout(self.widget_R4_1D)
                
                self.label_R4_1stD = QtWidgets.QLabel(self.widget_R4_1D)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_R4_1stD.setFont(font)
                self.label_R4_1stD.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_R4_1stD.setObjectName("label_R4_1stD")

                self.widget_1D_result4_gab = QtWidgets.QWidget(self.widget_R4_1D)
                self.widget_1D_result4_gab.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;\n"
        "")
                self.widget_1D_result4_gab.setObjectName("widget_1D_result4_gab")

                sub_gridlayout_widget_1D_result4_gab = QGridLayout(self.widget_1D_result4_gab)

                self.label_GabResult4_1D = QtWidgets.QLabel(self.widget_1D_result4_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                self.label_GabResult4_1D.setFont(font)
                self.label_GabResult4_1D.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_GabResult4_1D.setObjectName("label_GabResult4_1D")

                self.doubleSpinBox_1D_result4_gab = QtWidgets.QDoubleSpinBox(self.widget_1D_result4_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_1D_result4_gab.setFont(font)
                self.doubleSpinBox_1D_result4_gab.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_1D_result4_gab.setObjectName("doubleSpinBox_1D_result4_gab")

                sub_gridlayout_widget_1D_result4_gab.addWidget(self.label_GabResult4_1D,0,0)
                sub_gridlayout_widget_1D_result4_gab.addWidget(self.doubleSpinBox_1D_result4_gab,0,1)

                self.widget_1D_result4_sg = QtWidgets.QWidget(self.widget_R4_1D)
                self.widget_1D_result4_sg.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;\n"
        "")
                self.widget_1D_result4_sg.setObjectName("widget_1D_result4_sg")

                sub_gridlayout_widget_1D_result4_sg = QGridLayout(self.widget_1D_result4_sg)

                self.label_SGResult4_1D = QtWidgets.QLabel(self.widget_1D_result4_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                self.label_SGResult4_1D.setFont(font)
                self.label_SGResult4_1D.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_SGResult4_1D.setObjectName("label_SGResult4_1D")

                self.doubleSpinBox_1D_result4_sg = QtWidgets.QDoubleSpinBox(self.widget_1D_result4_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_1D_result4_sg.setFont(font)
                self.doubleSpinBox_1D_result4_sg.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_1D_result4_sg.setObjectName("doubleSpinBox_1D_result4_sg")

                sub_gridlayout_widget_1D_result4_sg.addWidget(self.label_SGResult4_1D,0,0)
                sub_gridlayout_widget_1D_result4_sg.addWidget(self.doubleSpinBox_1D_result4_sg,0,1)


                sub_gridlayout_widget_R4_1D.addWidget(self.label_R4_1stD,0,0)
                sub_gridlayout_widget_R4_1D.addWidget(self.widget_1D_result4_gab,1,0)
                sub_gridlayout_widget_R4_1D.addWidget(self.widget_1D_result4_sg,2,0)


                self.widget_R4_2D = QtWidgets.QWidget(self.widget_preproR4)
                self.widget_R4_2D.setStyleSheet("background-color:rgb(170, 255, 127);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_R4_2D.setObjectName("widget_R4_2D")

                sub_gridlayout_widget_R4_2D = QGridLayout(self.widget_R4_2D)
                
                self.label_R4_2ndD = QtWidgets.QLabel(self.widget_R4_2D)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_R4_2ndD.setFont(font)
                self.label_R4_2ndD.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_R4_2ndD.setObjectName("label_R4_2ndD")

                self.widget_2D_result4_gab = QtWidgets.QWidget(self.widget_R4_2D)
                self.widget_2D_result4_gab.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;\n"
        "")
                self.widget_2D_result4_gab.setObjectName("widget_2D_result4_gab")

                sub_gridlayout_widget_2D_result4_gab = QGridLayout(self.widget_2D_result4_gab)

                self.label_GabResult4_2D = QtWidgets.QLabel(self.widget_2D_result4_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                self.label_GabResult4_2D.setFont(font)
                self.label_GabResult4_2D.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_GabResult4_2D.setObjectName("label_GabResult4_2D")

                self.doubleSpinBox_2D_result4_gab = QtWidgets.QDoubleSpinBox(self.widget_2D_result4_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_2D_result4_gab.setFont(font)
                self.doubleSpinBox_2D_result4_gab.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_2D_result4_gab.setObjectName("doubleSpinBox_2D_result4_gab")

                sub_gridlayout_widget_2D_result4_gab.addWidget(self.label_GabResult4_2D,0,0)
                sub_gridlayout_widget_2D_result4_gab.addWidget(self.doubleSpinBox_2D_result4_gab,0,1)

                self.widget_2D_result4_sg = QtWidgets.QWidget(self.widget_R4_2D)
                self.widget_2D_result4_sg.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;\n"
        "")
                self.widget_2D_result4_sg.setObjectName("widget_2D_result4_sg")

                sub_gridlayout_widget_2D_result4_sg = QGridLayout(self.widget_2D_result4_sg)

                self.label_SGResult4_2D = QtWidgets.QLabel(self.widget_2D_result4_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                self.label_SGResult4_2D.setFont(font)
                self.label_SGResult4_2D.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_SGResult4_2D.setObjectName("label_SGResult4_2D")

                self.doubleSpinBox_2D_result4_sg = QtWidgets.QDoubleSpinBox(self.widget_2D_result4_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_2D_result4_sg.setFont(font)
                self.doubleSpinBox_2D_result4_sg.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_2D_result4_sg.setObjectName("doubleSpinBox_2D_result4_sg")

                sub_gridlayout_widget_2D_result4_sg.addWidget(self.label_SGResult4_2D,0,0)
                sub_gridlayout_widget_2D_result4_sg.addWidget(self.doubleSpinBox_2D_result4_sg,0,1)


                sub_gridlayout_widget_R4_2D.addWidget(self.label_R4_2ndD,0,0)
                sub_gridlayout_widget_R4_2D.addWidget(self.widget_2D_result4_gab,1,0)
                sub_gridlayout_widget_R4_2D.addWidget(self.widget_2D_result4_sg,2,0)


                #smoothing size1
                self.widget_sm4 = QtWidgets.QWidget(self.widget_preproR4)
                self.widget_sm4.setStyleSheet("background-color:rgb(170, 255, 127);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_sm4.setObjectName("widget_sm4")

                sub_gridlayout_widget_sm4 = QGridLayout(self.widget_sm4)

                self.label_R4_sm = QtWidgets.QLabel(self.widget_sm4)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(6)
                font.setBold(True)
                font.setWeight(75)
                self.label_R4_sm.setFont(font)
                self.label_R4_sm.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_R4_sm.setObjectName("label_R4_sm")
                
                self.widget_R4_sm_gab = QtWidgets.QWidget(self.widget_sm4)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.widget_R4_sm_gab.setFont(font)
                self.widget_R4_sm_gab.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;")
                self.widget_R4_sm_gab.setObjectName("widget_R4_sm_gab")

                sub_gridlayout_widget_R4_sm_gab = QGridLayout(self.widget_R4_sm_gab)

                self.label_GabResult4_sm = QtWidgets.QLabel(self.widget_R4_sm_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.label_GabResult4_sm.setFont(font)
                self.label_GabResult4_sm.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_GabResult4_sm.setObjectName("label_GabResult4_sm")

                self.doubleSpinBox_sm_result4_gab = QtWidgets.QDoubleSpinBox(self.widget_R4_sm_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_sm_result4_gab.setFont(font)
                self.doubleSpinBox_sm_result4_gab.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_sm_result4_gab.setObjectName("doubleSpinBox_sm_result4_gab")

                sub_gridlayout_widget_R4_sm_gab.addWidget( self.label_GabResult4_sm,0,0)
                sub_gridlayout_widget_R4_sm_gab.addWidget(self.doubleSpinBox_sm_result4_gab,0,1)

                sub_gridlayout_widget_sm4.addWidget(self.label_R4_sm,0,0)
                sub_gridlayout_widget_sm4.addWidget(self.widget_R4_sm_gab,0,1)

                sub_gridlayout_widget_preproR4.addWidget(self.label_prepro4,0,0,1,2)
                sub_gridlayout_widget_preproR4.addWidget(self.widget_stepResult4,1,0,4,2)
                sub_gridlayout_widget_preproR4.addWidget(self.widget_R4_1D,5,0,2,1)
                sub_gridlayout_widget_preproR4.addWidget(self.widget_R4_2D,5,1,2,1)
                sub_gridlayout_widget_preproR4.addWidget(self.widget_sm4,7,0,2,2)

                #result4 widget
                sub_Gridlayout_result4.addWidget(self.widget_file4,0,0,1,1)
                sub_Gridlayout_result4.addWidget(self.widget_bias4,1,0,1,1)
                sub_Gridlayout_result4.addWidget(self.widget_preproR4,2,0,6,1)


                sub_gridLayout_result4.addWidget(self.widget_title_result4,0,0)
                sub_gridLayout_result4.addWidget(self.result4,1,0,8,1)

                #result 5
                self.horizontalLayoutWidget5 = QtWidgets.QWidget(self.frame1)
                self.horizontalLayoutWidget5.setStyleSheet("background-color: transparent;")
                self.horizontalLayoutWidget5.setObjectName("horizontalLayoutWidget5")

                sub_gridLayout_result5 = QGridLayout(self.horizontalLayoutWidget5)

                self.widget_title_result5 = QtWidgets.QFrame(self.frame1)
                font = QtGui.QFont()
                font.setFamily("TH Sarabun New")
                self.widget_title_result5.setFont(font)
                self.widget_title_result5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border: 0px solid grey;\n"
        "border-radius: 20px;")
                self.widget_title_result5.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.widget_title_result5.setFrameShadow(QtWidgets.QFrame.Raised)
                self.widget_title_result5.setObjectName("widget_title_result5")

                sub_Gridlayout_widget_title_result5 = QGridLayout(self.widget_title_result5)
                self.label_result5 = QtWidgets.QLabel(self.widget_title_result5)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(16)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                font.setKerning(True)
                self.label_result5.setFont(font)
                self.label_result5.setAutoFillBackground(False)
                self.label_result5.setStyleSheet("font: 75 16pt \"Tahoma\";\n"
                "color: \"black\";\n"
                "background-color: rgba(255, 255, 255, 0);")
                self.label_result5.setWordWrap(False)
                self.label_result5.setObjectName("label_result5")
                sub_Gridlayout_widget_title_result5.addWidget(self.label_result5,0,0)
                
                self.result5 = QtWidgets.QFrame(self.frame1)
                font = QtGui.QFont()
                font.setFamily("TH Sarabun New")
                self.result5.setFont(font)
                self.result5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border: 0px solid grey;\n"
        "border-radius: 20px;")
                self.result5.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.result5.setFrameShadow(QtWidgets.QFrame.Raised)
                self.result5.setObjectName("result5")

                sub_Gridlayout_result5 = QGridLayout(self.result5)

                self.widget_file5 = QtWidgets.QWidget(self.result5)
                self.widget_file5.setStyleSheet("background-color:rgb(85, 170, 255);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_file5.setObjectName("widget_file5")
                
                sub_Gridlayout_widget_file5 = QGridLayout(self.widget_file5)

                self.label_calibrationfile5 = QtWidgets.QLabel(self.widget_file5)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_calibrationfile5.setFont(font)
                self.label_calibrationfile5.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_calibrationfile5.setObjectName("label_calibrationfile5")

                self.widget_browse5 = QtWidgets.QWidget(self.widget_file5)
                self.widget_browse5.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;")
                self.widget_browse5.setObjectName("widget_browse5")

                sub_Gridlayout_widget_browse5 = QGridLayout(self.widget_browse5)

                self.label_file5 = QtWidgets.QLabel(self.widget_file5)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_file5.setFont(font)
                self.label_file5.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_file5.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;")
                self.label_file5.setObjectName("label_file5")

                self.pushButton5 = QtWidgets.QPushButton(self.widget_file5)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setItalic(False)
                font.setUnderline(False)
                font.setStrikeOut(False)
                self.pushButton5.setFont(font)
                self.pushButton5.setStyleSheet("background-color:rgb(170, 255, 127);\n"
        "border-radius: 15px;")
                self.pushButton5.setObjectName("pushButton5")

                sub_Gridlayout_widget_browse5.addWidget(self.label_file5,0,0,1,3)
                sub_Gridlayout_widget_browse5.addWidget(self.pushButton5,0,3,1,1)

                sub_Gridlayout_widget_file5.addWidget(self.label_calibrationfile5,0,0)
                sub_Gridlayout_widget_file5.addWidget(self.widget_browse5,1,0)
                
                #widget bias5
                self.widget_bias5 = QtWidgets.QWidget(self.result5)
                self.widget_bias5.setStyleSheet("background-color:rgb(85, 170, 255);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_bias5.setObjectName("widget_bias5")
                
                sub_Gridlayout_widget_bias5 = QGridLayout(self.widget_bias5)
                
                self.label_bias5 = QtWidgets.QLabel(self.widget_bias5)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_bias5.setFont(font)
                self.label_bias5.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_bias5.setObjectName("label_bias5")
                
                self.widget_biasResult5 = QtWidgets.QWidget(self.widget_bias5)
                self.widget_biasResult5.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;")
                self.widget_biasResult5.setObjectName("widget_biasResult5")

                sub_Gridlayout_widget_biasResult5 = QGridLayout(self.widget_biasResult5)

                self.doubleSpinBox_biasResult5 = QtWidgets.QDoubleSpinBox(self.widget_biasResult5)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setBold(True)
                font.setWeight(75)
                self.doubleSpinBox_biasResult5.setFont(font)
                self.doubleSpinBox_biasResult5.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_biasResult5.setObjectName("doubleSpinBox_biasResult5")

                #doubleSpinBox_biasResult5
                sub_Gridlayout_widget_biasResult5.addWidget(self.doubleSpinBox_biasResult5,0,0)

                #widget_bias5
                sub_Gridlayout_widget_bias5.addWidget(self.label_bias5,0,0)
                sub_Gridlayout_widget_bias5.addWidget(self.widget_biasResult5,1,0)

                #prepro5
                self.widget_preproR5 = QtWidgets.QWidget(self.result5)
                self.widget_preproR5.setStyleSheet("background-color:rgb(170, 170, 255);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_preproR5.setObjectName("widget_preproR5")

                #sub_widget_prepro5
                sub_gridlayout_widget_preproR5 = QGridLayout(self.widget_preproR5)

                self.label_prepro5 = QtWidgets.QLabel(self.widget_preproR5)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_prepro5.setFont(font)
                self.label_prepro5.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_prepro5.setObjectName("label_prepro5")

                self.widget_stepResult5 = QtWidgets.QWidget(self.widget_preproR5)
                self.widget_stepResult5.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.widget_stepResult5.setObjectName("widget_stepResult5")


                #step result5
                sub_gridlayout_stepResult5 = QGridLayout(self.widget_stepResult5)

                self.label_step_result5 = QtWidgets.QLabel(self.widget_stepResult5)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setBold(False)
                font.setWeight(50)
                self.label_step_result5.setFont(font)
                self.label_step_result5.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_step_result5.setObjectName("label_step_result5")

                self.label_step1_result5 = QtWidgets.QLabel(self.widget_stepResult5)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.label_step1_result5.setFont(font)
                self.label_step1_result5.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_step1_result5.setObjectName("label_step1_result5")

                self.label_step2_result5 = QtWidgets.QLabel(self.widget_stepResult5)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.label_step2_result5.setFont(font)
                self.label_step2_result5.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_step2_result5.setObjectName("label_step2_result5")

                self.label_step3_result5 = QtWidgets.QLabel(self.widget_stepResult5)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.label_step3_result5.setFont(font)
                self.label_step3_result5.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_step3_result5.setObjectName("label_step3_result5")

                self.comboBox_step1_result5 = QtWidgets.QComboBox(self.widget_stepResult5)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.comboBox_step1_result5.setFont(font)
                self.comboBox_step1_result5.setObjectName("comboBox_step1_result5")
                self.comboBox_step1_result5.addItem("")
                self.comboBox_step1_result5.addItem("")
                self.comboBox_step1_result5.addItem("")
                self.comboBox_step1_result5.addItem("")
                self.comboBox_step1_result5.addItem("")
                self.comboBox_step2_result5 = QtWidgets.QComboBox(self.widget_stepResult5)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.comboBox_step2_result5.setFont(font)
                self.comboBox_step2_result5.setObjectName("comboBox_step2_result5")
                self.comboBox_step2_result5.addItem("")
                self.comboBox_step2_result5.addItem("")
                self.comboBox_step2_result5.addItem("")
                self.comboBox_step2_result5.addItem("")
                self.comboBox_step2_result5.addItem("")
                self.comboBox_step3_result5 = QtWidgets.QComboBox(self.widget_stepResult5)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.comboBox_step3_result5.setFont(font)
                self.comboBox_step3_result5.setObjectName("comboBox_step3_result5")
                self.comboBox_step3_result5.addItem("")
                self.comboBox_step3_result5.addItem("")
                self.comboBox_step3_result5.addItem("")
                self.comboBox_step3_result5.addItem("")
                self.comboBox_step3_result5.addItem("")

                sub_gridlayout_stepResult5.addWidget(self.label_step_result5,0,0,1,3)

                sub_gridlayout_stepResult5.addWidget(self.label_step1_result5,1,0,1,1)
                sub_gridlayout_stepResult5.addWidget(self.label_step2_result5,2,0,1,1)
                sub_gridlayout_stepResult5.addWidget(self.label_step3_result5,3,0,1,1)

                sub_gridlayout_stepResult5.addWidget(self.comboBox_step1_result5,1,1,1,2) 
                sub_gridlayout_stepResult5.addWidget(self.comboBox_step2_result5,2,1,1,2)
                sub_gridlayout_stepResult5.addWidget(self.comboBox_step3_result5,3,1,1,2)

                self.widget_R5_1D = QtWidgets.QWidget(self.widget_preproR5)
                self.widget_R5_1D.setStyleSheet("background-color:rgb(170, 255, 127);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_R5_1D.setObjectName("widget_R5_1D")

                sub_gridlayout_widget_R5_1D = QGridLayout(self.widget_R5_1D)
                
                self.label_R5_1stD = QtWidgets.QLabel(self.widget_R5_1D)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_R5_1stD.setFont(font)
                self.label_R5_1stD.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_R5_1stD.setObjectName("label_R5_1stD")

                self.widget_1D_result5_gab = QtWidgets.QWidget(self.widget_R5_1D)
                self.widget_1D_result5_gab.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;\n"
        "")
                self.widget_1D_result5_gab.setObjectName("widget_1D_result5_gab")

                sub_gridlayout_widget_1D_result5_gab = QGridLayout(self.widget_1D_result5_gab)

                self.label_GabResult5_1D = QtWidgets.QLabel(self.widget_1D_result5_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                self.label_GabResult5_1D.setFont(font)
                self.label_GabResult5_1D.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_GabResult5_1D.setObjectName("label_GabResult5_1D")

                self.doubleSpinBox_1D_result5_gab = QtWidgets.QDoubleSpinBox(self.widget_1D_result5_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_1D_result5_gab.setFont(font)
                self.doubleSpinBox_1D_result5_gab.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_1D_result5_gab.setObjectName("doubleSpinBox_1D_result5_gab")

                sub_gridlayout_widget_1D_result5_gab.addWidget(self.label_GabResult5_1D,0,0)
                sub_gridlayout_widget_1D_result5_gab.addWidget(self.doubleSpinBox_1D_result5_gab,0,1)

                self.widget_1D_result5_sg = QtWidgets.QWidget(self.widget_R5_1D)
                self.widget_1D_result5_sg.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;\n"
        "")
                self.widget_1D_result5_sg.setObjectName("widget_1D_result5_sg")

                sub_gridlayout_widget_1D_result5_sg = QGridLayout(self.widget_1D_result5_sg)

                self.label_SGResult5_1D = QtWidgets.QLabel(self.widget_1D_result5_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                self.label_SGResult5_1D.setFont(font)
                self.label_SGResult5_1D.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_SGResult5_1D.setObjectName("label_SGResult5_1D")

                self.doubleSpinBox_1D_result5_sg = QtWidgets.QDoubleSpinBox(self.widget_1D_result5_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_1D_result5_sg.setFont(font)
                self.doubleSpinBox_1D_result5_sg.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_1D_result5_sg.setObjectName("doubleSpinBox_1D_result5_sg")

                sub_gridlayout_widget_1D_result5_sg.addWidget(self.label_SGResult5_1D,0,0)
                sub_gridlayout_widget_1D_result5_sg.addWidget(self.doubleSpinBox_1D_result5_sg,0,1)


                sub_gridlayout_widget_R5_1D.addWidget(self.label_R5_1stD,0,0)
                sub_gridlayout_widget_R5_1D.addWidget(self.widget_1D_result5_gab,1,0)
                sub_gridlayout_widget_R5_1D.addWidget(self.widget_1D_result5_sg,2,0)


                self.widget_R5_2D = QtWidgets.QWidget(self.widget_preproR5)
                self.widget_R5_2D.setStyleSheet("background-color:rgb(170, 255, 127);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_R5_2D.setObjectName("widget_R5_2D")

                sub_gridlayout_widget_R5_2D = QGridLayout(self.widget_R5_2D)
                
                self.label_R5_2ndD = QtWidgets.QLabel(self.widget_R5_2D)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_R5_2ndD.setFont(font)
                self.label_R5_2ndD.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_R5_2ndD.setObjectName("label_R5_2ndD")

                self.widget_2D_result5_gab = QtWidgets.QWidget(self.widget_R5_2D)
                self.widget_2D_result5_gab.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;\n"
        "")
                self.widget_2D_result5_gab.setObjectName("widget_2D_result5_gab")

                sub_gridlayout_widget_2D_result5_gab = QGridLayout(self.widget_2D_result5_gab)

                self.label_GabResult5_2D = QtWidgets.QLabel(self.widget_2D_result5_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                self.label_GabResult5_2D.setFont(font)
                self.label_GabResult5_2D.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_GabResult5_2D.setObjectName("label_GabResult5_2D")

                self.doubleSpinBox_2D_result5_gab = QtWidgets.QDoubleSpinBox(self.widget_2D_result5_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_2D_result5_gab.setFont(font)
                self.doubleSpinBox_2D_result5_gab.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_2D_result5_gab.setObjectName("doubleSpinBox_2D_result5_gab")

                sub_gridlayout_widget_2D_result5_gab.addWidget(self.label_GabResult5_2D,0,0)
                sub_gridlayout_widget_2D_result5_gab.addWidget(self.doubleSpinBox_2D_result5_gab,0,1)

                self.widget_2D_result5_sg = QtWidgets.QWidget(self.widget_R5_2D)
                self.widget_2D_result5_sg.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;\n"
        "")
                self.widget_2D_result5_sg.setObjectName("widget_2D_result5_sg")

                sub_gridlayout_widget_2D_result5_sg = QGridLayout(self.widget_2D_result5_sg)

                self.label_SGResult5_2D = QtWidgets.QLabel(self.widget_2D_result5_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                self.label_SGResult5_2D.setFont(font)
                self.label_SGResult5_2D.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_SGResult5_2D.setObjectName("label_SGResult5_2D")

                self.doubleSpinBox_2D_result5_sg = QtWidgets.QDoubleSpinBox(self.widget_2D_result5_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_2D_result5_sg.setFont(font)
                self.doubleSpinBox_2D_result5_sg.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_2D_result5_sg.setObjectName("doubleSpinBox_2D_result5_sg")

                sub_gridlayout_widget_2D_result5_sg.addWidget(self.label_SGResult5_2D,0,0)
                sub_gridlayout_widget_2D_result5_sg.addWidget(self.doubleSpinBox_2D_result5_sg,0,1)


                sub_gridlayout_widget_R5_2D.addWidget(self.label_R5_2ndD,0,0)
                sub_gridlayout_widget_R5_2D.addWidget(self.widget_2D_result5_gab,1,0)
                sub_gridlayout_widget_R5_2D.addWidget(self.widget_2D_result5_sg,2,0)


                #smoothing size5
                self.widget_sm5 = QtWidgets.QWidget(self.widget_preproR5)
                self.widget_sm5.setStyleSheet("background-color:rgb(170, 255, 127);\n"
        "border-radius: 10px;\n"
        "")
                self.widget_sm5.setObjectName("widget_sm5")

                sub_gridlayout_widget_sm5 = QGridLayout(self.widget_sm5)

                self.label_R5_sm = QtWidgets.QLabel(self.widget_sm5)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(6)
                font.setBold(True)
                font.setWeight(75)
                self.label_R5_sm.setFont(font)
                self.label_R5_sm.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_R5_sm.setObjectName("label_R5_sm")
                
                self.widget_R5_sm_gab = QtWidgets.QWidget(self.widget_sm5)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.widget_R5_sm_gab.setFont(font)
                self.widget_R5_sm_gab.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "border-radius:15px;")
                self.widget_R5_sm_gab.setObjectName("widget_R5_sm_gab")

                sub_gridlayout_widget_R5_sm_gab = QGridLayout(self.widget_R5_sm_gab)

                self.label_GabResult5_sm = QtWidgets.QLabel(self.widget_R5_sm_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                self.label_GabResult5_sm.setFont(font)
                self.label_GabResult5_sm.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_GabResult5_sm.setObjectName("label_GabResult5_sm")

                self.doubleSpinBox_sm_result5_gab = QtWidgets.QDoubleSpinBox(self.widget_R5_sm_gab)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(9)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_sm_result5_gab.setFont(font)
                self.doubleSpinBox_sm_result5_gab.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.doubleSpinBox_sm_result5_gab.setObjectName("doubleSpinBox_sm_result5_gab")

                sub_gridlayout_widget_R5_sm_gab.addWidget( self.label_GabResult5_sm,0,0)
                sub_gridlayout_widget_R5_sm_gab.addWidget(self.doubleSpinBox_sm_result5_gab,0,1)

                sub_gridlayout_widget_sm5.addWidget(self.label_R5_sm,0,0)
                sub_gridlayout_widget_sm5.addWidget(self.widget_R5_sm_gab,0,1)

                sub_gridlayout_widget_preproR5.addWidget(self.label_prepro5,0,0,1,2)
                sub_gridlayout_widget_preproR5.addWidget(self.widget_stepResult5,1,0,4,2)
                sub_gridlayout_widget_preproR5.addWidget(self.widget_R5_1D,5,0,2,1)
                sub_gridlayout_widget_preproR5.addWidget(self.widget_R5_2D,5,1,2,1)
                sub_gridlayout_widget_preproR5.addWidget(self.widget_sm5,7,0,2,2)

                #result5 widget
                sub_Gridlayout_result5.addWidget(self.widget_file5,0,0,1,1)
                sub_Gridlayout_result5.addWidget(self.widget_bias5,1,0,1,1)
                sub_Gridlayout_result5.addWidget(self.widget_preproR5,2,0,6,1)



                sub_gridLayout_result5.addWidget(self.widget_title_result5,0,0)
                sub_gridLayout_result5.addWidget(self.result5,1,0,8,1)


                ###############################################
                sub_gridLayout_result.addWidget(self.Empty,0,0)
                sub_gridLayout_result.addWidget(self.Empty,0,1)
                sub_gridLayout_result.addWidget(self.Calself,0,2)
                sub_gridLayout_result.addWidget(self.Empty,0,3)
                sub_gridLayout_result.addWidget(self.Empty,0,4)
                sub_gridLayout_result.addWidget(self.horizontalLayoutWidget1,1,0,12,1)
                sub_gridLayout_result.addWidget(self.horizontalLayoutWidget2,1,1,12,1)
                sub_gridLayout_result.addWidget(self.horizontalLayoutWidget3,1,2,12,1)
                sub_gridLayout_result.addWidget(self.horizontalLayoutWidget4,1,3,12,1)
                sub_gridLayout_result.addWidget(self.horizontalLayoutWidget5,1,4,12,1)


                ####################frame2#####################
                self.frame2 = QtWidgets.QFrame(self.centralwidget)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setBold(False)
                font.setWeight(50)
                self.frame2.setFont(font)
                self.frame2.setStyleSheet("")
                self.frame2.setLocale(QtCore.QLocale(QtCore.QLocale.Thai, QtCore.QLocale.Thailand))
                self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame2.setProperty("Color", QtGui.QColor(255, 255, 255))
                self.frame2.setObjectName("frame2")
                ############################################################
                sub_gridLayout = QGridLayout(self.frame2) 
                #start frame2
                #################### label_spectro ########################
                self.widget_spectro = QtWidgets.QWidget(self.frame2)
                self.widget_spectro.setStyleSheet("background-color:rgb(85, 170, 255);\n"
        "border-radius: 5px;\n"
        "")
                self.widget_spectro.setObjectName("widget_spectro")

                # grid widget_spectro
                sub_gridLayout_widget_spectro = QGridLayout(self.widget_spectro)

                self.label_spectro = QtWidgets.QLabel(self.widget_spectro)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_spectro.setFont(font)
                self.label_spectro.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_spectro.setObjectName("label_spectro")
                
                self.widget_spectro_bg = QtWidgets.QWidget(self.widget_spectro)
                self.widget_spectro_bg.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.widget_spectro_bg.setObjectName("widget_spectro_bg")

                sub_gridLayout_widget_spectro.addWidget(self.label_spectro,0,0)
                sub_gridLayout_widget_spectro.addWidget(self.widget_spectro_bg,1,0)

                #start widget_spectro_bg
                sub_gridLayout_widget_spectro_bg = QGridLayout(self.widget_spectro_bg)
                
                #label integTime
                self.label_spectro_integTime = QtWidgets.QLabel(self.widget_spectro_bg)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.label_spectro_integTime.setFont(font)
                self.label_spectro_integTime.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_spectro_integTime.setObjectName("label_spectro_integTime")

                #ms
                self.label_spectro_integTime_ms = QtWidgets.QLabel(self.widget_spectro_bg)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.label_spectro_integTime_ms.setFont(font)
                self.label_spectro_integTime_ms.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_spectro_integTime_ms.setObjectName("label_spectro_integTime_ms")

                #spinbox
                self.doubleSpinBox_spectro = QtWidgets.QDoubleSpinBox(self.widget_spectro_bg)
                font = QtGui.QFont()
                font.setFamily("SimSun")
                font.setPointSize(14)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_spectro.setFont(font)
                self.doubleSpinBox_spectro.setObjectName("doubleSpinBox_spectro")

                sub_gridLayout_widget_spectro_bg.addWidget( self.label_spectro_integTime ,0,0,1,2)
                sub_gridLayout_widget_spectro_bg.addWidget( self.doubleSpinBox_spectro ,0,2)
                sub_gridLayout_widget_spectro_bg.addWidget( self.label_spectro_integTime_ms ,0,3)
                #end widget_spectro_bg
                ##############################################

                #################### widget_wavelength ############
                self.widget_wavelength = QtWidgets.QWidget(self.frame2)
                self.widget_wavelength.setStyleSheet("background-color:rgb(85, 170, 255);\n"
        "border-radius: 5px;\n"
        "")
                self.widget_wavelength.setObjectName("widget_wavelength")

                sub_gridLayout_widget_wavelength = QGridLayout(self.widget_wavelength)

                self.label_wavelenght = QtWidgets.QLabel(self.widget_wavelength)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_wavelenght.setFont(font)
                self.label_wavelenght.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_wavelenght.setObjectName("label_wavelenght")

                self.widget_wavelength_bg_N = QtWidgets.QWidget(self.widget_wavelength)
                self.widget_wavelength_bg_N.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.widget_wavelength_bg_N.setObjectName("widget_wavelength_bg_N")

                sub_gridLayout_widget_wavelength.addWidget(self.label_wavelenght,0,0)
                sub_gridLayout_widget_wavelength.addWidget(self.widget_wavelength_bg_N,1,0,2,1)

                sub_gridLayout_wavelength_bg_N = QGridLayout(self.widget_wavelength_bg_N)

                self.label_wavelength_N = QtWidgets.QLabel(self.widget_wavelength_bg_N) 
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_wavelength_N.setFont(font)
                self.label_wavelength_N.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_wavelength_N.setObjectName("label_wavelength_N")

                self.doubleSpinBox_wavelength_N = QtWidgets.QDoubleSpinBox(self.widget_wavelength_bg_N)
                font = QtGui.QFont()
                font.setFamily("SimSun")
                font.setPointSize(14)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_wavelength_N.setFont(font)
                self.doubleSpinBox_wavelength_N.setObjectName("doubleSpinBox_wavelength_N")

                self.doubleSpinBox_wavelength_M = QtWidgets.QDoubleSpinBox(self.widget_wavelength_bg_N)
                font = QtGui.QFont()
                font.setFamily("SimSun")
                font.setPointSize(14)
                font.setBold(False)
                font.setWeight(50)
                self.doubleSpinBox_wavelength_M.setFont(font)
                self.doubleSpinBox_wavelength_M.setObjectName("doubleSpinBox_wavelength_M")

                self.label_wavelength_M = QtWidgets.QLabel(self.widget_wavelength_bg_N)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_wavelength_M.setFont(font)
                self.label_wavelength_M.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_wavelength_M.setObjectName("label_wavelength_M")

                sub_gridLayout_wavelength_bg_N.addWidget(self.label_wavelength_N,0,0)
                sub_gridLayout_wavelength_bg_N.addWidget(self.doubleSpinBox_wavelength_N,0,1)
                sub_gridLayout_wavelength_bg_N.addWidget(self.label_wavelength_M,0,2)
                sub_gridLayout_wavelength_bg_N.addWidget(self.doubleSpinBox_wavelength_M,0,3)


                #####################################################################

                ################### label_directotyfolder ##########################
                #widget
                self.widget_directotyfolder = QtWidgets.QWidget(self.frame2)
                self.widget_directotyfolder.setStyleSheet("background-color:rgb(85, 170, 255);\n"
        "border-radius: 5px;\n"
        "")
                self.widget_directotyfolder.setObjectName("widget_directotyfolder")
                #set grid
                sub_gridLayout_widget_directotyfolder = QGridLayout(self.widget_directotyfolder)
                #label
                self.label_directotyfolder = QtWidgets.QLabel(self.widget_directotyfolder)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.label_directotyfolder.setFont(font)
                self.label_directotyfolder.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_directotyfolder.setObjectName("label_directotyfolder")
                #button
                self.pushButton_selectfolder = QtWidgets.QPushButton(self.widget_directotyfolder)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(16)
                font.setBold(False)
                font.setWeight(50)
                self.pushButton_selectfolder.setFont(font)
                self.pushButton_selectfolder.setStyleSheet("background-color:rgb(255, 170, 127);\n"
        "border-radius:5px;")
                self.pushButton_selectfolder.setObjectName("pushButton_selectfolder")
                #add grid
                sub_gridLayout_widget_directotyfolder.addWidget(self.label_directotyfolder,0,0)
                sub_gridLayout_widget_directotyfolder.addWidget(self.pushButton_selectfolder,1,0)

                #############################################
                #add grid
                sub_gridLayout.addWidget(QtWidgets.QLabel(self.centralwidget),0,0)
                sub_gridLayout.addWidget(self.widget_spectro,0,1,2,1)
                sub_gridLayout.addWidget(self.widget_wavelength,0,2,2,1)
                sub_gridLayout.addWidget(self.widget_directotyfolder,0,3,2,1)
                sub_gridLayout.addWidget(QtWidgets.QLabel(self.centralwidget),0,4)

                ####################frame3#####################
                self.frame3 = QtWidgets.QFrame(self.centralwidget)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setBold(False)
                font.setWeight(50)
                self.frame3.setFont(font)
                self.frame3.setStyleSheet("")
                self.frame3.setLocale(QtCore.QLocale(QtCore.QLocale.Thai, QtCore.QLocale.Thailand))
                self.frame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame3.setProperty("Color", QtGui.QColor(255, 255, 255))
                self.frame3.setObjectName("frame3")

                ############################################################
                sub_gridLayout3 = QGridLayout(self.frame3)
                ######################## button apply&cancel #######################
                self.apply = QtWidgets.QPushButton(self.frame3)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(20)
                self.apply.setFont(font)
                self.apply.setStyleSheet("border: 0px solid grey;\n"
        "border-radius: 10px;\n"
        "background-color: rgb(106, 255, 106);")
                self.apply.setObjectName("apply")

                self.cancel = QtWidgets.QPushButton(self.frame3)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(20)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(20)
                self.cancel.setFont(font)
                self.cancel.setStyleSheet("border: 0px solid;\n"
        "border-radius: 10px;\n"
        "background-color: rgb(128, 11, 0);\n"
        "color: \"white\";\n"
        "font: 20pt \"Tahoma\";")
                self.cancel.setAutoDefault(False)
                self.cancel.setDefault(False)
                self.cancel.setObjectName("cancel")
                ############################################################
                sub_gridLayout3.addWidget(QtWidgets.QLabel(self.centralwidget),0,0)
                sub_gridLayout3.addWidget(QtWidgets.QLabel(self.centralwidget),0,1)
                sub_gridLayout3.addWidget(self.apply,0,2,1,1)
                sub_gridLayout3.addWidget(QtWidgets.QLabel(self.centralwidget),0,3)
                sub_gridLayout3.addWidget(self.cancel,0,4,1,1)
                sub_gridLayout3.addWidget(QtWidgets.QLabel(self.centralwidget),0,5)
                sub_gridLayout3.addWidget(QtWidgets.QLabel(self.centralwidget),0,6)

                ########### add frame to layout ############
                gridLayout.addWidget(self.frame1,0, 0, 12, 6)
                gridLayout.addWidget(self.frame2,13, 0, 1, 6)
                gridLayout.addWidget(self.frame3,14, 0, 1, 6)
                #############################################
                self.groupBox.setLayout(gridLayout)
                lay.addWidget(self.groupBox)

                # self.Label_STEP.setAlignment(QtCore.Qt.AlignCenter)
                # self.Label_Wave.setAlignment(QtCore.Qt.AlignCenter)
                # scroll.setFixedHeight(960)
                # scroll.setFixedWidth(1280)
                self.box.addWidget(scroll)


                self.Calself.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Tahoma\'; font-size:24pt; font-weight:600; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Calculation Setting</p></body></html>")
                self.label_result1.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Result 1</span></p></body></html>")
                self.label_result2.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Result 2</span></p></body></html>")
                self.label_result3.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Result 3</span></p></body></html>")
                self.label_result4.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Result 4</span></p></body></html>")
                self.label_result5.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Result 5</span></p></body></html>")
                self.label_prepro1.setText("<html><head/><body><p align=\"center\">Pre-Processing</p></body></html>")
                self.label_prepro2.setText("<html><head/><body><p align=\"center\">Pre-Processing</p></body></html>")
                self.label_prepro3.setText("<html><head/><body><p align=\"center\">Pre-Processing</p></body></html>")
                self.label_prepro4.setText("<html><head/><body><p align=\"center\">Pre-Processing</p></body></html>")
                self.label_prepro5.setText("<html><head/><body><p align=\"center\">Pre-Processing</p></body></html>")

                self.label_calibrationfile1.setText("<html><head/><body><p align=\"center\">Calibration file 1</p></body></html>")
                self.pushButton.setText("Browse")
                self.label_bias1.setText("<html><head/><body><p align=\"center\">Bias</p></body></html>")

                self.label_step_result1.setText("<html><head/><body><p align=\"center\">Step</p></body></html>")
                self.label_step1_result1.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step1</span></p></body></html>")
                self.label_step2_result1.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step2</span></p></body></html>")
                self.label_step3_result1.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step3</span></p></body></html>")

                self.label_R1_1stD.setText("<html><head/><body><p align=\"center\">1st Derivative</p></body></html>")
                self.label_GabResult1_1D.setText("<html><head/><body><p align=\"center\">Gab</p></body></html>")
                self.label_SGResult1_1D.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Seg</span></p></body></html>")
                
                self.label_R1_2ndD.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">2nd Derivative</span></p></body></html>")
                self.label_GabResult1_2D.setText("<html><head/><body><p align=\"center\">Gab</p></body></html>")
                self.label_SGResult1_2D.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Seg</span></p></body></html>")

                self.label_R1_sm.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Smoothing Size</span></p></body></html>")
                self.label_GabResult1_sm.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Seg</span></p></body></html>")

                self.comboBox_step1_result1.setItemText(0, "----Select----")
                self.comboBox_step1_result1.setItemText(1, "SNV")
                self.comboBox_step1_result1.setItemText(2, "1st Derivative")
                self.comboBox_step1_result1.setItemText(3, "2nd Derivative")
                self.comboBox_step1_result1.setItemText(4, "Smoothing Size")
                self.comboBox_step2_result1.setItemText(0, "----Select----")
                self.comboBox_step2_result1.setItemText(1, "SNV")
                self.comboBox_step2_result1.setItemText(2, "1st Derivative")
                self.comboBox_step2_result1.setItemText(3, "2nd Derivative")
                self.comboBox_step2_result1.setItemText(4, "Smoothing Size")
                self.comboBox_step3_result1.setItemText(0, "----Select----")
                self.comboBox_step3_result1.setItemText(1, "SNV")
                self.comboBox_step3_result1.setItemText(2, "1st Derivative")
                self.comboBox_step3_result1.setItemText(3, "2nd Derivative")
                self.comboBox_step3_result1.setItemText(4, "Smoothing Size")

                self.label_step_result2.setText("<html><head/><body><p align=\"center\">Step</p></body></html>")
                self.label_step1_result2.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step1</span></p></body></html>")
                self.label_step2_result2.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step2</span></p></body></html>")
                self.label_step3_result2.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step3</span></p></body></html>")

                self.label_calibrationfile2.setText("<html><head/><body><p align=\"center\">Calibration file 2</p></body></html>")
                self.pushButton2.setText("Browse")
                self.label_bias2.setText("<html><head/><body><p align=\"center\">Bias</p></body></html>")

                self.label_step_result2.setText("<html><head/><body><p align=\"center\">Step</p></body></html>")
                self.label_step1_result2.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step1</span></p></body></html>")
                self.label_step2_result2.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step2</span></p></body></html>")
                self.label_step3_result2.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step3</span></p></body></html>")

                self.label_R2_1stD.setText("<html><head/><body><p align=\"center\">1st Derivative</p></body></html>")
                self.label_GabResult2_1D.setText("<html><head/><body><p align=\"center\">Gab</p></body></html>")
                self.label_SGResult2_1D.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Seg</span></p></body></html>")
                
                self.label_R2_2ndD.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">2nd Derivative</span></p></body></html>")
                self.label_GabResult2_2D.setText("<html><head/><body><p align=\"center\">Gab</p></body></html>")
                self.label_SGResult2_2D.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Seg</span></p></body></html>")

                self.label_R2_sm.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Smoothing Size</span></p></body></html>")
                self.label_GabResult2_sm.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Seg</span></p></body></html>")

                self.comboBox_step1_result2.setItemText(0, "----Select----")
                self.comboBox_step1_result2.setItemText(1, "SNV")
                self.comboBox_step1_result2.setItemText(2, "1st Derivative")
                self.comboBox_step1_result2.setItemText(3, "2nd Derivative")
                self.comboBox_step1_result2.setItemText(4, "Smoothing Size")
                self.comboBox_step2_result2.setItemText(0, "----Select----")
                self.comboBox_step2_result2.setItemText(1, "SNV")
                self.comboBox_step2_result2.setItemText(2, "1st Derivative")
                self.comboBox_step2_result2.setItemText(3, "2nd Derivative")
                self.comboBox_step2_result2.setItemText(4, "Smoothing Size")
                self.comboBox_step3_result2.setItemText(0, "----Select----")
                self.comboBox_step3_result2.setItemText(1, "SNV")
                self.comboBox_step3_result2.setItemText(2, "1st Derivative")
                self.comboBox_step3_result2.setItemText(3, "2nd Derivative")
                self.comboBox_step3_result2.setItemText(4, "Smoothing Size")

                self.label_step_result3.setText("<html><head/><body><p align=\"center\">Step</p></body></html>")
                self.label_step1_result3.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step1</span></p></body></html>")
                self.label_step2_result3.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step2</span></p></body></html>")
                self.label_step3_result3.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step3</span></p></body></html>")

                self.label_calibrationfile3.setText("<html><head/><body><p align=\"center\">Calibration file 3</p></body></html>")
                self.pushButton3.setText("Browse")
                self.label_bias3.setText("<html><head/><body><p align=\"center\">Bias</p></body></html>")

                self.label_step_result3.setText("<html><head/><body><p align=\"center\">Step</p></body></html>")
                self.label_step1_result3.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step1</span></p></body></html>")
                self.label_step2_result3.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step2</span></p></body></html>")
                self.label_step3_result3.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step3</span></p></body></html>")

                self.label_R3_1stD.setText("<html><head/><body><p align=\"center\">1st Derivative</p></body></html>")
                self.label_GabResult3_1D.setText("<html><head/><body><p align=\"center\">Gab</p></body></html>")
                self.label_SGResult3_1D.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Seg</span></p></body></html>")
                
                self.label_R3_2ndD.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">2nd Derivative</span></p></body></html>")
                self.label_GabResult3_2D.setText("<html><head/><body><p align=\"center\">Gab</p></body></html>")
                self.label_SGResult3_2D.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Seg</span></p></body></html>")

                self.label_R3_sm.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Smoothing Size</span></p></body></html>")
                self.label_GabResult3_sm.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Seg</span></p></body></html>")

                self.comboBox_step1_result3.setItemText(0, "----Select----")
                self.comboBox_step1_result3.setItemText(1, "SNV")
                self.comboBox_step1_result3.setItemText(2, "1st Derivative")
                self.comboBox_step1_result3.setItemText(3, "2nd Derivative")
                self.comboBox_step1_result3.setItemText(4, "Smoothing Size")
                self.comboBox_step2_result3.setItemText(0, "----Select----")
                self.comboBox_step2_result3.setItemText(1, "SNV")
                self.comboBox_step2_result3.setItemText(2, "1st Derivative")
                self.comboBox_step2_result3.setItemText(3, "2nd Derivative")
                self.comboBox_step2_result3.setItemText(4, "Smoothing Size")
                self.comboBox_step3_result3.setItemText(0, "----Select----")
                self.comboBox_step3_result3.setItemText(1, "SNV")
                self.comboBox_step3_result3.setItemText(2, "1st Derivative")
                self.comboBox_step3_result3.setItemText(3, "2nd Derivative")
                self.comboBox_step3_result3.setItemText(4, "Smoothing Size")

                self.label_step_result4.setText("<html><head/><body><p align=\"center\">Step</p></body></html>")
                self.label_step1_result4.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step1</span></p></body></html>")
                self.label_step2_result4.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step2</span></p></body></html>")
                self.label_step3_result4.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step3</span></p></body></html>")

                self.label_calibrationfile4.setText("<html><head/><body><p align=\"center\">Calibration file 4</p></body></html>")
                self.pushButton4.setText("Browse")
                self.label_bias4.setText("<html><head/><body><p align=\"center\">Bias</p></body></html>")

                self.label_step_result4.setText("<html><head/><body><p align=\"center\">Step</p></body></html>")
                self.label_step1_result4.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step1</span></p></body></html>")
                self.label_step2_result4.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step2</span></p></body></html>")
                self.label_step3_result4.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step3</span></p></body></html>")

                self.label_R4_1stD.setText("<html><head/><body><p align=\"center\">1st Derivative</p></body></html>")
                self.label_GabResult4_1D.setText("<html><head/><body><p align=\"center\">Gab</p></body></html>")
                self.label_SGResult4_1D.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Seg</span></p></body></html>")
                
                self.label_R4_2ndD.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">2nd Derivative</span></p></body></html>")
                self.label_GabResult4_2D.setText("<html><head/><body><p align=\"center\">Gab</p></body></html>")
                self.label_SGResult4_2D.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Seg</span></p></body></html>")

                self.label_R4_sm.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Smoothing Size</span></p></body></html>")
                self.label_GabResult4_sm.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Seg</span></p></body></html>")

                self.comboBox_step1_result4.setItemText(0, "----Select----")
                self.comboBox_step1_result4.setItemText(1, "SNV")
                self.comboBox_step1_result4.setItemText(2, "1st Derivative")
                self.comboBox_step1_result4.setItemText(3, "2nd Derivative")
                self.comboBox_step1_result4.setItemText(4, "Smoothing Size")
                self.comboBox_step2_result4.setItemText(0, "----Select----")
                self.comboBox_step2_result4.setItemText(1, "SNV")
                self.comboBox_step2_result4.setItemText(2, "1st Derivative")
                self.comboBox_step2_result4.setItemText(3, "2nd Derivative")
                self.comboBox_step2_result4.setItemText(4, "Smoothing Size")
                self.comboBox_step3_result4.setItemText(0, "----Select----")
                self.comboBox_step3_result4.setItemText(1, "SNV")
                self.comboBox_step3_result4.setItemText(2, "1st Derivative")
                self.comboBox_step3_result4.setItemText(3, "2nd Derivative")
                self.comboBox_step3_result4.setItemText(4, "Smoothing Size")

                self.label_step_result5.setText("<html><head/><body><p align=\"center\">Step</p></body></html>")
                self.label_step1_result5.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step1</span></p></body></html>")
                self.label_step2_result5.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step2</span></p></body></html>")
                self.label_step3_result5.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step3</span></p></body></html>")


                self.label_calibrationfile5.setText("<html><head/><body><p align=\"center\">Calibration file 5</p></body></html>")
                self.pushButton5.setText("Browse")
                self.label_bias5.setText("<html><head/><body><p align=\"center\">Bias</p></body></html>")

                self.label_step_result5.setText("<html><head/><body><p align=\"center\">Step</p></body></html>")
                self.label_step1_result5.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step1</span></p></body></html>")
                self.label_step2_result5.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step2</span></p></body></html>")
                self.label_step3_result5.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Step3</span></p></body></html>")

                self.label_R5_1stD.setText("<html><head/><body><p align=\"center\">1st Derivative</p></body></html>")
                self.label_GabResult5_1D.setText("<html><head/><body><p align=\"center\">Gab</p></body></html>")
                self.label_SGResult5_1D.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Seg</span></p></body></html>")
                
                self.label_R5_2ndD.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">2nd Derivative</span></p></body></html>")
                self.label_GabResult5_2D.setText("<html><head/><body><p align=\"center\">Gab</p></body></html>")
                self.label_SGResult5_2D.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Seg</span></p></body></html>")

                self.label_R5_sm.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Smoothing Size</span></p></body></html>")
                self.label_GabResult5_sm.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Seg</span></p></body></html>")

                self.comboBox_step1_result5.setItemText(0, "----Select----")
                self.comboBox_step1_result5.setItemText(1, "SNV")
                self.comboBox_step1_result5.setItemText(2, "1st Derivative")
                self.comboBox_step1_result5.setItemText(3, "2nd Derivative")
                self.comboBox_step1_result5.setItemText(4, "Smoothing Size")
                self.comboBox_step2_result5.setItemText(0, "----Select----")
                self.comboBox_step2_result5.setItemText(1, "SNV")
                self.comboBox_step2_result5.setItemText(2, "1st Derivative")
                self.comboBox_step2_result5.setItemText(3, "2nd Derivative")
                self.comboBox_step2_result5.setItemText(4, "Smoothing Size")
                self.comboBox_step3_result5.setItemText(0, "----Select----")
                self.comboBox_step3_result5.setItemText(1, "SNV")
                self.comboBox_step3_result5.setItemText(2, "1st Derivative")
                self.comboBox_step3_result5.setItemText(3, "2nd Derivative")
                self.comboBox_step3_result5.setItemText(4, "Smoothing Size")

                self.apply.setText("APPLY")
                self.cancel.setText("CANCEL")
                self.label_spectro.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Spectrometer Setting</span></p></body></html>")
                self.label_spectro_integTime.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:400;\">Integration time</span></p></body></html>")
                self.label_spectro_integTime_ms.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:400;\">ms</span></p></body></html>")
                self.label_wavelenght.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Wave Length</span></p></body></html>")
                self.label_wavelength_N.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:400;\">N</span></p></body></html>")
                self.label_wavelength_M.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:400;\">M</span></p></body></html>")
                self.label_directotyfolder.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Directory Folder</span></p></body></html>")
                self.pushButton_selectfolder.setText("Browse")
                
# if __name__ == '__main__':
#         import sys
#         app = QtWidgets.QApplication(sys.argv)
#         self = QtWidgets.QMainWindow()
#         # app = QApplication(sys.argv)
#         ui = Ui_MainWindow()
#         ui.setupUi(self)
#         self.show()
#         sys.exit(app.exec_())