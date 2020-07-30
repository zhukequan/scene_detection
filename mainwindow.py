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
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.drawLabel1 = QtWidgets.QLabel(self.widget_2)
        self.drawLabel1.setText("")
        self.drawLabel1.setObjectName("drawLabel1")
        self.verticalLayout.addWidget(self.drawLabel1)
        self.drawLabel2 = QtWidgets.QLabel(self.widget_2)
        self.drawLabel2.setText("")
        self.drawLabel2.setObjectName("drawLabel2")
        self.verticalLayout.addWidget(self.drawLabel2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.setStretch(0, 15)
        self.horizontalLayout.addWidget(self.widget_2)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 10)
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
        self.openButton.setText(_translate("MainWindow", "打开文件"))
        self.detectionButton.setText(_translate("MainWindow", "目标检测"))
        self.segmentButton.setText(_translate("MainWindow", "实例分割"))
        self.playButton.setText(_translate("MainWindow", "播放"))
        self.stopButton.setText(_translate("MainWindow", "停止播放"))
