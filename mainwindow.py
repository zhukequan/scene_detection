# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.openButton = QtWidgets.QPushButton(self.widget)
        self.openButton.setObjectName("openButton")
        self.verticalLayout_3.addWidget(self.openButton)
        self.openimgButton = QtWidgets.QPushButton(self.widget)
        self.openimgButton.setObjectName("openimgButton")
        self.verticalLayout_3.addWidget(self.openimgButton)
        self.lastButton = QtWidgets.QPushButton(self.widget)
        self.lastButton.setObjectName("lastButton")
        self.verticalLayout_3.addWidget(self.lastButton)
        self.nextButton = QtWidgets.QPushButton(self.widget)
        self.nextButton.setObjectName("nextButton")
        self.verticalLayout_3.addWidget(self.nextButton)
        self.imgsegButton = QtWidgets.QPushButton(self.widget)
        self.imgsegButton.setObjectName("imgsegButton")
        self.verticalLayout_3.addWidget(self.imgsegButton)
        self.detectionButton = QtWidgets.QPushButton(self.widget)
        self.detectionButton.setObjectName("detectionButton")
        self.verticalLayout_3.addWidget(self.detectionButton)
        self.segmentButton = QtWidgets.QPushButton(self.widget)
        self.segmentButton.setObjectName("segmentButton")
        self.verticalLayout_3.addWidget(self.segmentButton)
        self.playButton = QtWidgets.QPushButton(self.widget)
        self.playButton.setObjectName("playButton")
        self.verticalLayout_3.addWidget(self.playButton)
        self.stopButton = QtWidgets.QPushButton(self.widget)
        self.stopButton.setObjectName("stopButton")
        self.verticalLayout_3.addWidget(self.stopButton)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.drawLabel1 = QtWidgets.QLabel(self.widget_4)
        self.drawLabel1.setText("")
        self.drawLabel1.setObjectName("drawLabel1")
        self.verticalLayout.addWidget(self.drawLabel1)
        self.drawLabel2 = QtWidgets.QLabel(self.widget_4)
        self.drawLabel2.setText("")
        self.drawLabel2.setObjectName("drawLabel2")
        self.verticalLayout.addWidget(self.drawLabel2)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.imgEdit = QtWidgets.QLineEdit(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.imgEdit.setFont(font)
        self.imgEdit.setObjectName("imgEdit")
        self.horizontalLayout_2.addWidget(self.imgEdit)
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.detEdit = QtWidgets.QLineEdit(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.detEdit.setFont(font)
        self.detEdit.setObjectName("detEdit")
        self.horizontalLayout_2.addWidget(self.detEdit)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.apEdit = QtWidgets.QLineEdit(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.apEdit.setFont(font)
        self.apEdit.setObjectName("apEdit")
        self.horizontalLayout_2.addWidget(self.apEdit)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.FPEdit = QtWidgets.QLineEdit(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.FPEdit.setFont(font)
        self.FPEdit.setObjectName("FPEdit")
        self.horizontalLayout_2.addWidget(self.FPEdit)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.verticalLayout_2.setStretch(0, 15)
        self.verticalLayout_2.setStretch(1, 2)
        self.horizontalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openButton.setText(_translate("MainWindow", "打开视频"))
        self.openimgButton.setText(_translate("MainWindow", "打开图片"))
        self.lastButton.setText(_translate("MainWindow", "上一张图"))
        self.nextButton.setText(_translate("MainWindow", "下一张图"))
        self.imgsegButton.setText(_translate("MainWindow", "图片分割"))
        self.detectionButton.setText(_translate("MainWindow", "目标检测"))
        self.segmentButton.setText(_translate("MainWindow", "实例分割"))
        self.playButton.setText(_translate("MainWindow", "播放"))
        self.stopButton.setText(_translate("MainWindow", "停止播放"))
        self.label.setText(_translate("MainWindow", "image"))
        self.label_4.setText(_translate("MainWindow", "ap_det"))
        self.label_2.setText(_translate("MainWindow", "ap_seg"))
        self.label_3.setText(_translate("MainWindow", "FAR_seg"))
