from PyQt5.QtWidgets import QLineEdit, QMainWindow, QScrollArea, QApplication, QWidget, QVBoxLayout, QPushButton, \
    QGroupBox, QGridLayout, QSpinBox
import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Ui_MainWindow(QMainWindow):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setWindowTitle("Pre Processing")
        self.setMinimumSize(950, 660)
        self.showMaximized()
        font = QFont()
        font.setFamily("MS Shell Dlg 2")
        self.setFont(font)
        self.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                           "border:0px;\n"
                           "")
        self.centralwidget = QWidget(self)
        self.centralwidget.setGeometry(0, 0, 1280, 960)
        self.centralwidget.setObjectName("centralwidge t")
        #         self.centralwidget.setStyleSheet("border-radius:0px;\n"
        # "background-color:rgb(255, 0, 0);\n"
        # "font-size:32px;\n"
        # "color:#fff;")

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
        gridLayout = QGridLayout(self)

        self.body = QtWidgets.QFrame(self.centralwidget)
        self.body.setLocale(QtCore.QLocale(QtCore.QLocale.Thai, QtCore.QLocale.Thailand))
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setProperty("Color", QtGui.QColor(0, 0, 0))
        self.body.setObjectName("body")

        subBody_gridLayout = QGridLayout(self.body)
        self.groupBox_cal = QtWidgets.QGroupBox(self.body)
        self.groupBox_cal.setStyleSheet("border-radius: 10px;\n"
                                        "background-color: rgb(236, 236, 236);\n"
                                        "border: 0px solid black")
        self.groupBox_cal.setObjectName("groupBox")

        sub_groupbox_cal = QGridLayout(self.groupBox_cal)

        self.Label = QtWidgets.QLabel()  # Topic_Cal
        self.Label.setAutoFillBackground(False)
        self.Label.setStyleSheet("border-radius: 10px;\n"
                                 "border: 0px solid black;\n font-size:20pt bold;\n background-color: transparent;");
        self.Label.setAlignment(QtCore.Qt.AlignCenter)


        self.widget_28 = QtWidgets.QWidget(self.groupBox_cal)
        self.widget_28.setStyleSheet("background-color:rgb(158, 158, 158);\n"
                                     "border:none")
        self.widget_28.setObjectName("widget_28")



        sub_GridCal_1 = QGridLayout(self.widget_28)
        self.label_8 = QtWidgets.QLabel(self.widget_28)
        self.label_8.setStyleSheet("align:\"center\";\n" "font-size:14pt;\n" "color:#fff")
        self.label_8.setObjectName("label_8")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        sub_GridCal_1.addWidget(self.label_8,0,3,1,1)

        self.label_8.setText("1st Derivative")

        self.label_22 = QtWidgets.QLabel(self.widget_28)
        self.label_22.setGeometry(QtCore.QRect(3, 5, 100, 20))
        self.label_22.setStyleSheet("background-color: rgb(236, 236, 236);\n"
                                    "border-radius:10px;\n" "align:\"center\";\n"
                                    "font-size:14pt;")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        sub_GridCal_1.addWidget(self.label_22, 1, 3, 1, 1)

        self.widget_30 = QtWidgets.QWidget(self.widget_28)  # grab_1
        self.widget_30.setStyleSheet("border-radius: 10px;\n"
                                     "background-color: rgb(255, 255, 255);")
        self.widget_30.setObjectName("widget_30")
        sub_GridCal_1.addWidget(self.widget_30, 2, 3, 1, 1)

        sub_GridCal_4_1 = QGridLayout(self.widget_30)
        self.spinBox_7 = QtWidgets.QDoubleSpinBox(self.widget_30)  # grab_1
        self.spinBox_7.setObjectName("spinBox_7")
        sub_GridCal_4_1.addWidget(self.spinBox_7, 0, 0)
        self.spinBox_7.setMaximum(1000000)
        self.spinBox_7.setMinimum(-100000)
        self.spinBox_7.setStyleSheet(
                                     "border-radius:8px;	"
                                     "min-height:25px;"
                                     "max-height:25px;"
                                     "font-size: 14pt;" "font-weight:bold;"
                                     "qproperty-alignment: AlignCenter;"
                                     "border-radius:10px;	"

                                     )

        self.Seg_1st = QtWidgets.QLabel(self.widget_28)
        self.Seg_1st.setGeometry(QtCore.QRect(3, 5, 100, 20))  # grab_1
        self.Seg_1st.setStyleSheet("background-color: rgb(236, 236, 236);\n"
                                   "border-radius:10px;\n" "align:\"center\";\n"
                                   "font-size:14pt;")
        self.Seg_1st.setAlignment(QtCore.Qt.AlignCenter)
        self.Seg_1st.setObjectName("Seg_1st")
        sub_GridCal_1.addWidget(self.Seg_1st, 1, 4, 1, 1)

        self.Seg_1st_W = QtWidgets.QWidget(self.widget_28)  # spinBox_Seg_1st
        self.Seg_1st_W.setStyleSheet("border-radius: 10px;\n"
                                     "background-color: rgb(255, 255, 255);" "font-size:14pt")
        self.Seg_1st_W.setObjectName("Seg_1st_W")
        sub_GridCal_1.addWidget(self.Seg_1st_W, 2, 4, 1, 1)

        sub_GridCal_4_2 = QGridLayout(self.Seg_1st_W)
        self.spinBox_Seg_1st = QtWidgets.QDoubleSpinBox(self.widget_30)  # spinBox_Seg_1st
        self.spinBox_Seg_1st.setObjectName("spinBox_Seg_1st ")
        sub_GridCal_4_2.addWidget(self.spinBox_Seg_1st, 0, 0)
        self.spinBox_Seg_1st.setMaximum(1000000)
        self.spinBox_Seg_1st.setMinimum(-100000)
        self.spinBox_Seg_1st.setStyleSheet(
                                           "border-radius:8px;	"
                                           "min-height:25px;"
                                           "max-height:25px;"
                                           "font-size: 14pt;" "font-weight:bold;"
                                           "qproperty-alignment: AlignCenter;")

        self.widget_35 = QtWidgets.QWidget(self.groupBox_cal)  # 2
        self.widget_35.setStyleSheet("background-color:rgb(158, 158, 158);\n"
                                     "border:none")
        self.widget_35.setObjectName("widget_35")

#2ndDerGrid
        sub_GridCal_1 = QGridLayout(self.widget_35)

        self.snTopic = QtWidgets.QLabel(self.widget_35)
        self.snTopic.setStyleSheet("align:\"center\";\n" "font-size:14pt;\n" "color:#fff")
        self.snTopic.setObjectName("snTopic")
        sub_GridCal_1.addWidget(self.snTopic,0,3,1,1)
        self.snTopic.setAlignment(QtCore.Qt.AlignCenter)
        self.snTopic.setText("2nd Derivative")

        self.label_24 = QtWidgets.QLabel(self.widget_35)
        self.label_24.setStyleSheet("background-color: rgb(236, 236, 236);\n"
                                    "border-radius:10px;\n" "align:\"center\";\n"
                                    "font-size:14pt;")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")

        sub_GridCal_1.addWidget(self.label_24, 1, 3, 1, 1) #gab

        self.widget_41 = QtWidgets.QWidget(self.widget_35)  # gab2_value
        self.widget_41.setStyleSheet("border-radius: 10px;\n"
                                     "background-color: rgb(255, 255, 255);"
                                     "border-radius:10px;	")
        self.widget_41.setObjectName("widget_41")

        sub_GridCal_1.addWidget(self.widget_41, 2, 3, 1, 1) # gab2_value

        sub_GridCal_5_1 = QGridLayout(self.widget_41)
        self.spinBox_8 = QtWidgets.QDoubleSpinBox(self.widget_41)  # gab2
        self.spinBox_8.setObjectName("spinBox_8")
        sub_GridCal_5_1.addWidget(self.spinBox_8, 0, 0)
        self.spinBox_8.setMaximum(1000000)
        self.spinBox_8.setMinimum(-100000)
        self.spinBox_8.setStyleSheet(
                                     "border-radius:10px;	"
                                     "min-height:25px;"
                                     "max-height:25px;"
                                     "font-size: 14pt;" "font-weight:bold;"
                                     "qproperty-alignment: AlignCenter;")

        self.Seg_2nd = QtWidgets.QLabel(self.widget_35)
        self.Seg_2nd.setStyleSheet( "background-color: rgb(236, 236, 236);\n"
                                   "border-radius:10px;\n" "align:\"center\";\n"
                                   "font-size:14pt;")
        self.Seg_2nd.setAlignment(QtCore.Qt.AlignCenter)
        self.Seg_2nd.setObjectName("Seg_2nd")
        sub_GridCal_1.addWidget(self.Seg_2nd, 1, 4, 1, 1)

        self.Seg_2nd_W = QtWidgets.QWidget(self.widget_35)  # Seg_2nd_W
        self.Seg_2nd_W.setStyleSheet("border-radius: 10px;\n"
                                     "background-color: rgb(255, 255, 255);")
        self.Seg_2nd_W.setObjectName("Seg_2nd_W")
        sub_GridCal_1.addWidget(self.Seg_2nd_W, 2, 4, 1, 1)

        sub_GridCal_5_2 = QGridLayout(self.Seg_2nd_W)
        self.spinBox_Seg_2nd = QtWidgets.QDoubleSpinBox(self.Seg_2nd_W)  # Seg_2nd_W
        self.spinBox_Seg_2nd.setObjectName("spinBox_Seg_2nd")
        sub_GridCal_5_2.addWidget(self.spinBox_Seg_2nd, 0, 0)
        self.spinBox_Seg_2nd.setMaximum(1000000)
        self.spinBox_Seg_2nd.setMinimum(-100000)
        self.spinBox_Seg_2nd.setStyleSheet(
                                           "border-radius:10px;	"
                                           "min-height:25px;"
                                           "max-height:25px;"
                                           "font-size: 14pt;" "font-weight:bold;"
                                           "qproperty-alignment: AlignCenter;")

        self.Smoothing = QtWidgets.QWidget(self.groupBox_cal)  # Smoothing
        self.Smoothing.setStyleSheet("background-color:rgb(158, 158, 158);\n"
                                     "border:none" )
        self.Smoothing.setObjectName("Smoothing")

#SmoothingSize Grid
        sub_GridCal_6 = QGridLayout(self.Smoothing)
        self.tmp = QtWidgets.QLabel(self.Smoothing)  # Smoothing
        self.tmp.setStyleSheet("align:\"center\";\n" "font-size:14pt;\n" "color:#fff")
        self.tmp.setObjectName("tmp")
        sub_GridCal_6.addWidget(self.tmp, 0, 3,1,1)
        self.tmp.setText("Smoothing Size")
        self.tmp.setAlignment(QtCore.Qt.AlignCenter)






        sub_GridCal_6.addWidget(self.Smoothing, 1, 0, 1, 0)

        self.grab_Smoothing = QtWidgets.QLabel(self.Smoothing)
        self.grab_Smoothing.setStyleSheet("background-color: rgb(236, 236, 236);\n"
                                          "border-radius:10px;\n" "align:\"center\";\n"
                                          "font-size:14pt;") #gab_sm
        self.grab_Smoothing.setAlignment(QtCore.Qt.AlignCenter)
        self.grab_Smoothing.setObjectName("grab_Smoothing")
        sub_GridCal_6.addWidget(self.grab_Smoothing, 1, 3, 1, 1)

        self.grab_Smoothing_w = QtWidgets.QWidget(self.Smoothing)  # grab_smValue
        self.grab_Smoothing_w.setStyleSheet("border-radius: 10px;\n"
                                            "background-color: rgb(255, 255, 255);")
        self.grab_Smoothing_w.setObjectName("grab_Smoothing_w")
        sub_GridCal_6.addWidget(self.grab_Smoothing_w, 2, 3, 1, 1)

        sub_GridCal_6_1 = QGridLayout(self.grab_Smoothing_w)
        self.spinBox_grab_Smoothing_w = QtWidgets.QDoubleSpinBox(self.grab_Smoothing_w)  # gab2
        self.spinBox_grab_Smoothing_w.setObjectName("grab_Smoothing_w")
        sub_GridCal_6_1.addWidget(self.spinBox_grab_Smoothing_w, 0, 0)
        self.spinBox_grab_Smoothing_w.setMaximum(1000000)
        self.spinBox_grab_Smoothing_w.setMinimum(-100000)
        self.spinBox_grab_Smoothing_w.setStyleSheet(
                                                    "border-radius:10px;	"
                                                    "min-height:25px;"
                                                    "max-height:25px;"
                                                    "font-size: 14pt;" "font-weight:bold;"
                                                    "qproperty-alignment: AlignCenter;")

        self.Seg_Smoothing = QtWidgets.QLabel(self.Smoothing)
        self.Seg_Smoothing.setStyleSheet("background-color: rgb(236, 236, 236);\n"
                                         "border-radius:10px;\n" "align:\"center\";\n"
                                         "font-size:14pt;")
        self.Seg_Smoothing.setAlignment(QtCore.Qt.AlignCenter)
        self.Seg_Smoothing.setObjectName("Seg_Smoothing")
        sub_GridCal_6.addWidget(self.Seg_Smoothing, 1, 4, 1, 1)

        self.Seg_Smoothing_W = QtWidgets.QWidget(self.widget_35)  # Seg_Smoothing
        self.Seg_Smoothing_W.setStyleSheet("border-radius: 10px;\n"
                                           "background-color: rgb(255, 255, 255);")
        self.Seg_Smoothing_W.setObjectName("Seg_Smoothing_W")
        sub_GridCal_6.addWidget(self.Seg_Smoothing_W, 2, 4, 1, 1)

        sub_GridCal_6_2 = QGridLayout(self.Seg_Smoothing_W)
        self.spinBox_Seg_Smoothing = QtWidgets.QDoubleSpinBox(self.Seg_Smoothing_W)  # Seg_Smoothing
        self.spinBox_Seg_Smoothing.setObjectName("spinBox_Seg_Smoothing")
        sub_GridCal_6_2.addWidget(self.spinBox_Seg_Smoothing, 0, 0)
        self.spinBox_Seg_Smoothing.setMaximum(1000000)
        self.spinBox_Seg_Smoothing.setMinimum(-100000)
        self.spinBox_Seg_Smoothing.setStyleSheet(
                                                 "border-radius:10px;	"
                                                 "min-height:25px;"
                                                 "max-height:25px;"
                                                 "font-size: 14pt;" "font-weight:bold;"
                                                 "qproperty-alignment: AlignCenter;")

        sub_groupbox_cal.addWidget(self.Label, 0, 0, 1, 6)
        #        sub_groupbox_cal.addWidget(self.widget_4, 1, 1, 1, 4)
        #       sub_groupbox_cal.addWidget(self.widget_7, 2, 1, 1, 4)
        #      sub_groupbox_cal.addWidget(self.widget_9, 3, 1, 1, 4)
        sub_groupbox_cal.addWidget(self.widget_28, 4, 1, 1, 4)
        sub_groupbox_cal.addWidget(self.widget_35, 5, 1, 1, 4)
        sub_groupbox_cal.addWidget(self.Smoothing, 6, 1, 1, 4)

        self.groupBox_Spec = QtWidgets.QGroupBox(self.body)
        self.groupBox_Spec.setStyleSheet("border-radius: 10px;\n"
                                         "border: 0px solid black;\n" "background-color: rgb(236, 236, 236);\n")
        self.groupBox_Spec.setObjectName("groupBox_Spec")

        sub_GridSpec = QGridLayout(self.groupBox_Spec)

        self.groupBox_Spec_integration = QtWidgets.QGroupBox(self.groupBox_Spec)
        self.groupBox_Spec_integration.setStyleSheet("border-radius: 0px;\n"
                                                     "border: 0px solid black;\n background-color: transparent;")

        sub_groupBox_Spec_integration = QGridLayout(self.groupBox_Spec_integration)

        self.Label_STEP = QtWidgets.QLabel(self.groupBox_Spec_integration)
        self.Label_STEP.setStyleSheet("color:black;\n" "border-radius: 10px;\n"
                                      "border: none;\n" "font-size:14pt bold;\n")

        self.widget_6 = QtWidgets.QWidget(self.groupBox_Spec_integration)
        self.widget_6.setStyleSheet("\n"
                                    "background-color: rgb(255,255,255);\n"
                                    "border: 0px solid #000000;\n")
        self.widget_6.setObjectName("widget_6")

        integration = QGridLayout(self.widget_6)

        self.label_step1 = QtWidgets.QLabel()
        self.label_step1.setStyleSheet("align:\"center\";\n" "border-radius: 10px;\n"
                                       "font-size: 14pt;" )
        self.label_step1.setObjectName("label_step1")

        self.comboBox = QtWidgets.QComboBox(self.widget_6)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        # self.comboBox.addItem("")

        self.comboBox.setStyleSheet("\n""background-color: rgb(255, 255, 255);\n" 
                                    "border:none;\n align: \"center\";\n""font-size: 14pt;\n")

        self.label_step2 = QtWidgets.QLabel()
        self.label_step2.setStyleSheet("align:\"center\";\n"
                                       "font-size: 14pt;")
        self.label_step2.setObjectName("label_step2")
        self.comboBox2 = QtWidgets.QComboBox(self.widget_6)
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        # self.comboBox2.addItem("")

        self.comboBox2.setStyleSheet("\n""background-color: rgb(255, 255, 255);\n"
                                     "border:none;\n align: \"center\";\n""font-size: 14pt;\n")

        self.label_step3 = QtWidgets.QLabel()
        self.label_step3.setStyleSheet("align:\"center\";\n"
                                       "font-size: 14pt;")
        self.label_step3.setObjectName("label_step3")
        self.comboBox3 = QtWidgets.QComboBox(self.widget_6)
        self.comboBox3.setObjectName("comboBox2")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        # self.comboBox3.addItem("")

        self.comboBox3.setStyleSheet("\n""background-color: rgb(255, 255, 255);\n"
                                     "border:none;\n align: \"center\";\n""font-size: 14pt;\n")

        integration.addWidget(self.label_step1, 0, 0)
        integration.addWidget(self.comboBox, 0, 1)
        integration.addWidget(self.label_step2, 1, 0)
        integration.addWidget(self.comboBox2, 1, 1)
        integration.addWidget(self.label_step3, 2, 0)
        integration.addWidget(self.comboBox3, 2, 1)



        self.Export = QtWidgets.QPushButton(self.groupBox_Spec_integration)
        self.Export.setStyleSheet(
                                  "background-color:rgb(0, 170, 0);\n"
                                  "font-size:24px;\n"
                                  "color:#fff;\n" "border-radius: 10px;\n")
        self.Export.setObjectName("Export")
        self.Export.setText("Export")
        sub_groupBox_Spec_integration.addWidget(self.Label_STEP, 0, 0)
        sub_groupBox_Spec_integration.addWidget(self.widget_6, 1, 0)
        sub_groupBox_Spec_integration.addWidget(QtWidgets.QLabel(""), 2, 0)


        self.groupBox_Spec_Wave = QtWidgets.QGroupBox(self.groupBox_Spec)
        self.groupBox_Spec_Wave.setStyleSheet("border-radius: 8px;\n"
                                             "color:rgb(236, 236, 236") #typeYourname
        sub_groupBox_Spec_Wave = QGridLayout(self.groupBox_Spec_Wave)

        self.Label_Wave = QtWidgets.QLabel(self.groupBox_Spec_Wave)
        self.Label_Wave.setStyleSheet("color:black;\n"
                                      "border: none;\n" "font-size:14pt bold;\n")
        self.Label_Wave.setObjectName("Label_Wave")

        self.widget_name = QtWidgets.QLineEdit(self.groupBox_Spec_Wave)
        self.widget_name.setStyleSheet("\n"
                                       "background-color: rgb(255, 255, 255);\n"
                                       "border: 0px solid rgb(236, 236, 236);\n font-size:14pt bold;\n")
        self.widget_name.setObjectName("widget_name")
        self.widget_name.setAlignment(QtCore.Qt.AlignCenter)
        self.widget_name.move(10, 200)
        self.widget_name.resize(400, 50)

        sub_groupBox_Spec_integration.addWidget(self.Export, 8, 0, 1, 1)

        sub_groupBox_Spec_Wave.addWidget(self.Label_Wave, 1,0)
        # sub_groupBox_Spec_Wave.addWidget(self.widget_name,1,0)

        # sub_groupBox_Spec_Wave(200)
        sub_GridSpec.addWidget(self.groupBox_Spec_integration, 0, 0)
        sub_GridSpec.addWidget(self.groupBox_Spec_Wave, 1, 0)
        # sub_GridSpec.addWidget(self.widget_name,3,0)

        subBody_gridLayout.addWidget(self.groupBox_cal, 0, 0, 1, 3) #Scaleprepro
        subBody_gridLayout.addWidget(self.groupBox_Spec, 0, 3, 1, 1) #Scalecalstep


        gridLayout.addWidget(self.body, 0, 0, 5, 6)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setLocale(QtCore.QLocale(QtCore.QLocale.Thai, QtCore.QLocale.Thailand))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setProperty("Color", QtGui.QColor(0, 0, 0))
        self.frame.setObjectName("frame")

        sub_gridLayout = QGridLayout(self.frame)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setStyleSheet("border-radius:30px;\n"
                                        "background-color:rgb(0, 170, 0);\n"
                                        "font-size:24px;\n"
                                        "color:#fff;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setStyleSheet("border-radius:30px;\n"
                                        "background-color:#aa0000;\n"
                                        "font-size:24px;\n"
                                        "color:#fff;")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4.setFixedHeight(60)
        self.pushButton_3.setFixedHeight(60)

        sub_gridLayout.addWidget(QtWidgets.QLabel(self.body), 0, 0)
        sub_gridLayout.addWidget(self.pushButton_4, 0, 1)
        sub_gridLayout.addWidget(QtWidgets.QLabel(self.body), 0, 2)
        sub_gridLayout.addWidget(self.pushButton_3, 0, 3)
        sub_gridLayout.addWidget(QtWidgets.QLabel(self.body), 0, 4)

        gridLayout.addWidget(self.frame, 5, 0, 1, 6)

        self.groupBox.setLayout(gridLayout)
        lay.addWidget(self.groupBox)
        # lay.addStretch()
        self.Label_STEP.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Wave.setAlignment(QtCore.Qt.AlignCenter)
        # scroll.setFixedHeight(960)
        # scroll.setFixedWidth(1280)
        self.box.addWidget(scroll)
        self.pushButton_3.clicked.connect(self.close)
        # self.retranslateUi(MainWindow)

        # # def setIcon(self):
        # #         appIcon = QIcon("icon.png")
        # #         MainWindow.setWindowIcon(appIcon)
        # def retranslateUi(self, MainWindow):
        #     _translate = QtCore.QCoreApplication.translate
        self.Label.setText("Pre-Processing")
        # self.Topic_RAW.setText("RAW")
        # self.label_RAW.setText("...")
        # self.Topic_SNV.setText("SNV")
        # self.label_SNV.setText("...")
        # self.Topic_MSC.setText("MSC")
        # self.label_MSC.setText("...")

        # self.label_1stDeri.setText("...")


        self.grab_Smoothing.setText("Gab")
        self.Seg_Smoothing.setText("Segment")


        self.label_24.setText("Gab")
        self.Seg_2nd.setText("Segment")

        self.label_22.setText("Gab")
        self.Seg_1st.setText("Segment")

        self.Label_STEP.setText("CALCULATION STEP")
        self.label_step1.setText("Step 1")
        self.comboBox.setItemText(0, "---select---")
        # self.comboBox.setItemText(1, "RAW")
        self.comboBox.setItemText(1, "SNV")
        self.comboBox.setItemText(2, "MSC")
        self.comboBox.setItemText(3, "1st Derivative")
        self.comboBox.setItemText(4, "2nd Derivative")
        self.comboBox.setItemText(5, "Smoothing Size")
        self.label_step2.setText("Step 2")
        self.comboBox2.setItemText(0, "---select---")
        # self.comboBox2.setItemText(1, "RAW")
        self.comboBox2.setItemText(1, "SNV")
        self.comboBox2.setItemText(2, "MSC")
        self.comboBox2.setItemText(3, "1st Derivative")
        self.comboBox2.setItemText(4, "2nd Derivative")
        self.comboBox2.setItemText(5, "Smoothing Size")

        self.label_step3.setText("Step 3")
        self.comboBox3.setItemText(0, "---select---")
        # self.comboBox3.setItemText(1, "RAW")
        self.comboBox3.setItemText(1, "SNV")
        self.comboBox3.setItemText(2, "MSC")
        self.comboBox3.setItemText(3, "1st Derivative")
        self.comboBox3.setItemText(4, "2nd Derivative")
        self.comboBox3.setItemText(5, "Smoothing Size")

        self.Label_Wave.setText("Username")
        self.widget_name.setText("Type your name...")
        self.pushButton_3.setText("CANCEL")
        self.pushButton_4.setText("APPLY")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = Ui_MainWindow()
    myapp.show()
    sys.exit(app.exec_())