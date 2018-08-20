# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scan.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 255)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 50, 421, 191))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(350, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(9, 9, 48, 16))
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(70, 10, 46, 20))
        self.spinBox.setMinimum(50)
        self.spinBox.setMaximum(150)
        self.spinBox.setSingleStep(10)
        self.spinBox.setObjectName("spinBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "正方批量测试"))
        self.pushButton.setText(_translate("Form", "start"))
        self.label.setText(_translate("Form", "线程数："))

