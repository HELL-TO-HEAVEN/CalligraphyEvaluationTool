# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'strokeExtractingMainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1278, 667)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 171, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.open_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.open_btn.setObjectName("open_btn")
        self.verticalLayout.addWidget(self.open_btn)
        self.clear_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.clear_btn.setObjectName("clear_btn")
        self.verticalLayout.addWidget(self.clear_btn)
        self.exit_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exit_btn.setObjectName("exit_btn")
        self.verticalLayout.addWidget(self.exit_btn)
        self.image_view = QtWidgets.QGraphicsView(self.centralwidget)
        self.image_view.setGeometry(QtCore.QRect(200, 10, 1061, 591))
        self.image_view.setObjectName("image_view")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 130, 171, 151))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radicalExtract_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.radicalExtract_btn.setObjectName("radicalExtract_btn")
        self.verticalLayout_2.addWidget(self.radicalExtract_btn)
        self.radical_listview = QtWidgets.QListView(self.verticalLayoutWidget_2)
        self.radical_listview.setObjectName("radical_listview")
        self.verticalLayout_2.addWidget(self.radical_listview)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 287, 174, 351))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.auto_extract_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.auto_extract_btn.setObjectName("auto_extract_btn")
        self.verticalLayout_3.addWidget(self.auto_extract_btn)
        self.extract_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.extract_btn.setObjectName("extract_btn")
        self.verticalLayout_3.addWidget(self.extract_btn)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.delete_stroke_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.delete_stroke_btn.setObjectName("delete_stroke_btn")
        self.horizontalLayout.addWidget(self.delete_stroke_btn)
        self.add_stroke_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.add_stroke_btn.setObjectName("add_stroke_btn")
        self.horizontalLayout.addWidget(self.add_stroke_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.stroke_listview = QtWidgets.QListView(self.verticalLayoutWidget_3)
        self.stroke_listview.setObjectName("stroke_listview")
        self.verticalLayout_3.addWidget(self.stroke_listview)
        self.saveStroke_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.saveStroke_btn.setObjectName("saveStroke_btn")
        self.verticalLayout_3.addWidget(self.saveStroke_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1278, 22))
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
        self.open_btn.setText(_translate("MainWindow", "Open"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))
        self.radicalExtract_btn.setText(_translate("MainWindow", "Radicals Extracting"))
        self.auto_extract_btn.setText(_translate("MainWindow", "Auto-extracting"))
        self.extract_btn.setText(_translate("MainWindow", "Extracting"))
        self.delete_stroke_btn.setText(_translate("MainWindow", "DELETE"))
        self.add_stroke_btn.setText(_translate("MainWindow", "ADD"))
        self.saveStroke_btn.setText(_translate("MainWindow", "Save Strokes"))

