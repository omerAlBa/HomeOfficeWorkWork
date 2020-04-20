# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui\mainwindow_bmi.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(348, 447)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 80, 281, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.boxHeight = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.boxHeight.setObjectName("boxHeight")
        self.verticalLayout.addWidget(self.boxHeight)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.boxWeight = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.boxWeight.setSpecialValueText("")
        self.boxWeight.setKeyboardTracking(True)
        self.boxWeight.setObjectName("boxWeight")
        self.verticalLayout.addWidget(self.boxWeight)
        self.labelResult = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelResult.setObjectName("labelResult")
        self.verticalLayout.addWidget(self.labelResult)
        self.button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button.setObjectName("button")
        self.verticalLayout.addWidget(self.button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 348, 26))
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
        self.label_2.setText(_translate("MainWindow", "Your weight in kg:"))
        self.label.setText(_translate("MainWindow", "Your height in m:"))
        self.labelResult.setText(_translate("MainWindow", "Result is : "))
        self.button.setText(_translate("MainWindow", "C\'est cummon?"))
