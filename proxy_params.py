# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proxy_params.ui'
#
# Created: Fri Jan  9 21:34:22 2015
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

class Ui_Proxy(object):
    def setupUi(self, Proxy):
        Proxy.setObjectName(_fromUtf8("Proxy"))
        Proxy.resize(705, 300)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Proxy)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Proxy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEditProxy = QtGui.QLineEdit(Proxy)
        self.lineEditProxy.setObjectName(_fromUtf8("lineEditProxy"))
        self.horizontalLayout.addWidget(self.lineEditProxy)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(Proxy)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEditPort = QtGui.QLineEdit(Proxy)
        self.lineEditPort.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditPort.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditPort.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEditPort.setObjectName(_fromUtf8("lineEditPort"))
        self.horizontalLayout_3.addWidget(self.lineEditPort)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Proxy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEditUser = QtGui.QLineEdit(Proxy)
        self.lineEditUser.setObjectName(_fromUtf8("lineEditUser"))
        self.horizontalLayout_2.addWidget(self.lineEditUser)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_4 = QtGui.QLabel(Proxy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEditPassword = QtGui.QLineEdit(Proxy)
        self.lineEditPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPassword.setObjectName(_fromUtf8("lineEditPassword"))
        self.horizontalLayout_5.addWidget(self.lineEditPassword)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Proxy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Proxy)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Proxy.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Proxy.reject)
        QtCore.QMetaObject.connectSlotsByName(Proxy)

    def retranslateUi(self, Proxy):
        Proxy.setWindowTitle(_translate("Proxy", "Paramètres du Proxy", None))
        self.label.setText(_translate("Proxy", "Proxy : ", None))
        self.label_3.setText(_translate("Proxy", "Port : ", None))
        self.label_2.setText(_translate("Proxy", "Utilisateur : ", None))
        self.label_4.setText(_translate("Proxy", "Mot de passe : ", None))

