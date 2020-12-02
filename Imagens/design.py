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
        MainWindow.resize(573, 501)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widthInput = QtWidgets.QLineEdit(self.centralwidget)
        self.widthInput.setStyleSheet("border: 1px solid #0000001")
        self.widthInput.setObjectName("widthInput")
        self.gridLayout.addWidget(self.widthInput, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.changeButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeButton.setObjectName("changeButton")
        self.gridLayout.addWidget(self.changeButton, 2, 4, 1, 1)
        self.heightInput = QtWidgets.QLineEdit(self.centralwidget)
        self.heightInput.setEnabled(False)
        self.heightInput.setStyleSheet("background-color: #FFF;  border: 1px solid rgba(0, 0, 0, .5); color: black")
        self.heightInput.setText("")
        self.heightInput.setObjectName("heightInput")
        self.gridLayout.addWidget(self.heightInput, 2, 3, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 553, 394))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.imgArea = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imgArea.setStyleSheet("")
        self.imgArea.setText("")
        self.imgArea.setObjectName("imgArea")
        self.gridLayout_2.addWidget(self.imgArea, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 5)
        self.openBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openBtn.setObjectName("openBtn")
        self.gridLayout.addWidget(self.openBtn, 1, 4, 1, 1)
        self.pathInput = QtWidgets.QLineEdit(self.centralwidget)
        self.pathInput.setObjectName("pathInput")
        self.gridLayout.addWidget(self.pathInput, 1, 0, 1, 4)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 3, 0, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Redimensioner"))
        self.label.setText(_translate("MainWindow", "Width"))
        self.label_2.setText(_translate("MainWindow", "Height"))
        self.changeButton.setText(_translate("MainWindow", "Change"))
        self.openBtn.setText(_translate("MainWindow", "Find image"))
        self.saveButton.setText(_translate("MainWindow", "Save As"))
