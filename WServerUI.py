# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WServerUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 272)
        MainWindow.setMinimumSize(QtCore.QSize(430, 272))
        MainWindow.setMaximumSize(QtCore.QSize(430, 272))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber_NbClients = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_NbClients.setGeometry(QtCore.QRect(300, 10, 121, 23))
        self.lcdNumber_NbClients.setObjectName("lcdNumber_NbClients")
        self.lineEdit_portNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_portNumber.setGeometry(QtCore.QRect(10, 10, 113, 20))
        self.lineEdit_portNumber.setToolTip("")
        self.lineEdit_portNumber.setStatusTip("")
        self.lineEdit_portNumber.setWhatsThis("")
        self.lineEdit_portNumber.setInputMask("")
        self.lineEdit_portNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_portNumber.setPlaceholderText("")
        self.lineEdit_portNumber.setObjectName("lineEdit_portNumber")
        self.pushButton_StartStop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_StartStop.setGeometry(QtCore.QRect(10, 40, 111, 23))
        self.pushButton_StartStop.setObjectName("pushButton_StartStop")
        self.textEdit_Resume = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Resume.setGeometry(QtCore.QRect(10, 70, 411, 161))
        self.textEdit_Resume.setReadOnly(True)
        self.textEdit_Resume.setObjectName("textEdit_Resume")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WServer"))
        self.lineEdit_portNumber.setText(_translate("MainWindow", "8080"))
        self.pushButton_StartStop.setText(_translate("MainWindow", "Start"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

