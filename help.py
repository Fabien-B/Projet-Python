# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aide.ui'
#
# Created: Sun Jan 25 15:56:39 2015
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

class Ui_Aide(object):
    def setupUi(self, Aide):
        Aide.setObjectName(_fromUtf8("Aide"))
        Aide.resize(820, 627)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Aide)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.graphicsView = QtGui.QGraphicsView(Aide)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.Prec = QtGui.QPushButton(Aide)
        self.Prec.setMaximumSize(QtCore.QSize(25, 25))
        self.Prec.setObjectName(_fromUtf8("Prec"))
        self.horizontalLayout_2.addWidget(self.Prec)
        self.radioButton_1 = QtGui.QRadioButton(Aide)
        self.radioButton_1.setText(_fromUtf8(""))
        self.radioButton_1.setObjectName(_fromUtf8("radioButton_1"))
        self.horizontalLayout_2.addWidget(self.radioButton_1)
        self.radioButton_2 = QtGui.QRadioButton(Aide)
        self.radioButton_2.setText(_fromUtf8(""))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(Aide)
        self.radioButton_3.setText(_fromUtf8(""))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout_2.addWidget(self.radioButton_3)
        self.radioButton_4 = QtGui.QRadioButton(Aide)
        self.radioButton_4.setText(_fromUtf8(""))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_5 = QtGui.QRadioButton(Aide)
        self.radioButton_5.setText(_fromUtf8(""))
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.horizontalLayout_2.addWidget(self.radioButton_5)
        self.radioButton_6 = QtGui.QRadioButton(Aide)
        self.radioButton_6.setText(_fromUtf8(""))
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.horizontalLayout_2.addWidget(self.radioButton_6)
        self.radioButton_7 = QtGui.QRadioButton(Aide)
        self.radioButton_7.setText(_fromUtf8(""))
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))
        self.horizontalLayout_2.addWidget(self.radioButton_7)
        self.radioButton_8 = QtGui.QRadioButton(Aide)
        self.radioButton_8.setText(_fromUtf8(""))
        self.radioButton_8.setObjectName(_fromUtf8("radioButton_8"))
        self.horizontalLayout_2.addWidget(self.radioButton_8)
        self.radioButton_9 = QtGui.QRadioButton(Aide)
        self.radioButton_9.setText(_fromUtf8(""))
        self.radioButton_9.setObjectName(_fromUtf8("radioButton_9"))
        self.horizontalLayout_2.addWidget(self.radioButton_9)
        self.Next = QtGui.QPushButton(Aide)
        self.Next.setMaximumSize(QtCore.QSize(25, 25))
        self.Next.setObjectName(_fromUtf8("Next"))
        self.horizontalLayout_2.addWidget(self.Next)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton = QtGui.QPushButton(Aide)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Aide)
        QtCore.QMetaObject.connectSlotsByName(Aide)

    def retranslateUi(self, Aide):
        Aide.setWindowTitle(_translate("Aide", "Aide", None))
        self.Prec.setText(_translate("Aide", "<", None))
        self.Next.setText(_translate("Aide", ">", None))
        self.pushButton.setText(_translate("Aide", "Ok", None))

