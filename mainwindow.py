# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1040, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1040, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1040, 720))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.tittle = QtWidgets.QLabel(self.centralWidget)
        self.tittle.setGeometry(QtCore.QRect(0, 0, 1041, 71))
        self.tittle.setText("")
        self.tittle.setPixmap(QtGui.QPixmap("images/tittle.png"))
        self.tittle.setObjectName("tittle")
        self.background = QtWidgets.QLabel(self.centralWidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1051, 721))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("images/background.png"))
        self.background.setWordWrap(False)
        self.background.setObjectName("background")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(40, 130, 581, 451))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 600, 131, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 600, 171, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.background.raise_()
        self.tittle.raise_()
        self.frame.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BGraph"))
        self.pushButton.setText(_translate("MainWindow", " Открыть файл"))
        self.pushButton_2.setText(_translate("MainWindow", "Построить решение"))
