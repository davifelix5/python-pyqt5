# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(656, 268)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.inputFile = QtWidgets.QLineEdit(self.centralwidget)
        self.inputFile.setGeometry(QtCore.QRect(260, 10, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inputFile.setFont(font)
        self.inputFile.setReadOnly(True)
        self.inputFile.setObjectName("inputFile")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 60, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.outputFile = QtWidgets.QLineEdit(self.centralwidget)
        self.outputFile.setGeometry(QtCore.QRect(260, 60, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.outputFile.setFont(font)
        self.outputFile.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.outputFile.setReadOnly(True)
        self.outputFile.setObjectName("outputFile")
        self.pwd = QtWidgets.QLineEdit(self.centralwidget)
        self.pwd.setGeometry(QtCore.QRect(260, 120, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pwd.setFont(font)
        self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd.setObjectName("pwd")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 120, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.findButton = QtWidgets.QPushButton(self.centralwidget)
        self.findButton.setGeometry(QtCore.QRect(530, 10, 71, 31))
        self.findButton.setObjectName("findButton")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(530, 60, 71, 31))
        self.saveBtn.setObjectName("saveBtn")
        self.finalButton = QtWidgets.QPushButton(self.centralwidget)
        self.finalButton.setGeometry(QtCore.QRect(250, 170, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.finalButton.setFont(font)
        self.finalButton.setObjectName("finalButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Encriptador de PDF"))
        self.label.setText(_translate("MainWindow", "Arquivo de entrada"))
        self.label_2.setText(_translate("MainWindow", "Arquivo de saída"))
        self.label_3.setText(_translate("MainWindow", "Senha"))
        self.findButton.setText(_translate("MainWindow", "Escolher"))
        self.saveBtn.setText(_translate("MainWindow", "Escolher"))
        self.finalButton.setText(_translate("MainWindow", "SALVAR"))
