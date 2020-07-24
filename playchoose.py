# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playchoose.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(11, 11, 378, 243))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.originRadio = QtWidgets.QRadioButton(self.groupBox)
        self.originRadio.setObjectName("originRadio")
        self.horizontalLayout_2.addWidget(self.originRadio)
        self.detectionRadio = QtWidgets.QRadioButton(self.groupBox)
        self.detectionRadio.setObjectName("detectionRadio")
        self.horizontalLayout_2.addWidget(self.detectionRadio)
        self.instanceRadio = QtWidgets.QRadioButton(self.groupBox)
        self.instanceRadio.setObjectName("instanceRadio")
        self.horizontalLayout_2.addWidget(self.instanceRadio)
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(290, 270, 93, 28))
        self.okButton.setObjectName("okButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.originRadio.setText(_translate("Dialog", "播放原视频"))
        self.detectionRadio.setText(_translate("Dialog", "播放目标检测"))
        self.instanceRadio.setText(_translate("Dialog", "播放实例分割‘"))
        self.okButton.setText(_translate("Dialog", "ok"))
