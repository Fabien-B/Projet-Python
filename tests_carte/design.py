# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created: Fri Dec 12 22:26:07 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(813, 672)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        # self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        # self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        # self.horizontalLayout.addWidget(self.graphicsView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.test1 = QtGui.QPushButton(self.dockWidgetContents)
        self.test1.setObjectName(_fromUtf8("test1"))
        self.verticalLayout.addWidget(self.test1)
        self.test2 = QtGui.QPushButton(self.dockWidgetContents)
        self.test2.setObjectName(_fromUtf8("test2"))
        self.verticalLayout.addWidget(self.test2)
        self.pushButtonPoint = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButtonPoint.setObjectName(_fromUtf8("pushButtonPoint"))
        self.verticalLayout.addWidget(self.pushButtonPoint)
        self.pushButton = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButtonZoomm = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButtonZoomm.setObjectName(_fromUtf8("pushButtonZoomm"))
        self.verticalLayout.addWidget(self.pushButtonZoomm)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.test1.setText(_translate("MainWindow", "Test1", None))
        self.test2.setText(_translate("MainWindow", "Test2", None))
        self.pushButtonPoint.setText(_translate("MainWindow", "Draw point", None))
        self.pushButton.setText(_translate("MainWindow", "Zoom +", None))
        self.pushButtonZoomm.setText(_translate("MainWindow", "Zoom -", None))

