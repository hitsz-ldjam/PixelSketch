# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui',
# licensing of 'MainWindow.ui' applies.
#
# Created: Fri Jan 18 23:55:26 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1197, 800)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMouseTracking(False)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setStyleSheet("background-color: rgb(150, 150, 150);\n"
"")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1197, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setMinimumSize(QtCore.QSize(30, 30))
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.sideToolBar = QtWidgets.QToolBar(MainWindow)
        self.sideToolBar.setMinimumSize(QtCore.QSize(30, 30))
        self.sideToolBar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sideToolBar.setObjectName("sideToolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.sideToolBar)
        self.menuFileCreate = QtWidgets.QAction(MainWindow)
        self.menuFileCreate.setObjectName("menuFileCreate")
        self.menuFileOpen = QtWidgets.QAction(MainWindow)
        self.menuFileOpen.setObjectName("menuFileOpen")
        self.menuFileSave = QtWidgets.QAction(MainWindow)
        self.menuFileSave.setObjectName("menuFileSave")
        self.menuFileSaveAs = QtWidgets.QAction(MainWindow)
        self.menuFileSaveAs.setObjectName("menuFileSaveAs")
        self.menuFileQuit = QtWidgets.QAction(MainWindow)
        self.menuFileQuit.setObjectName("menuFileQuit")
        self.menuHelpAbout = QtWidgets.QAction(MainWindow)
        self.menuHelpAbout.setCheckable(False)
        self.menuHelpAbout.setObjectName("menuHelpAbout")
        self.menuFile.addAction(self.menuFileCreate)
        self.menuFile.addAction(self.menuFileOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuFileSave)
        self.menuFile.addAction(self.menuFileSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuFileQuit)
        self.menuHelp.addAction(self.menuHelpAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Pixel Mix", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.menuEdit.setTitle(QtWidgets.QApplication.translate("MainWindow", "Edit", None, -1))
        self.menuHelp.setTitle(QtWidgets.QApplication.translate("MainWindow", "Help", None, -1))
        self.mainToolBar.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "toolBar", None, -1))
        self.sideToolBar.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "toolBar", None, -1))
        self.menuFileCreate.setText(QtWidgets.QApplication.translate("MainWindow", "New", None, -1))
        self.menuFileCreate.setToolTip(QtWidgets.QApplication.translate("MainWindow", "New", None, -1))
        self.menuFileCreate.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+N", None, -1))
        self.menuFileOpen.setText(QtWidgets.QApplication.translate("MainWindow", "Open", None, -1))
        self.menuFileOpen.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Open", None, -1))
        self.menuFileOpen.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+O", None, -1))
        self.menuFileSave.setText(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.menuFileSave.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.menuFileSave.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+S", None, -1))
        self.menuFileSaveAs.setText(QtWidgets.QApplication.translate("MainWindow", "Save as ...", None, -1))
        self.menuFileSaveAs.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, -1))
        self.menuFileQuit.setText(QtWidgets.QApplication.translate("MainWindow", "Quit", None, -1))
        self.menuFileQuit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Q", None, -1))
        self.menuHelpAbout.setText(QtWidgets.QApplication.translate("MainWindow", "About", None, -1))

