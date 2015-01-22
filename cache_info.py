# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cache_info.ui'
#
# Created: Thu Jan 22 14:04:39 2015
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

class Ui_Cache(object):
    def setupUi(self, Cache):
        Cache.setObjectName(_fromUtf8("Cache"))
        Cache.resize(705, 300)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Cache)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label = QtGui.QLabel(Cache)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_6.addWidget(self.label)
        self.line_2 = QtGui.QFrame(Cache)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_6.addWidget(self.line_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(Cache)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.Label_TailleCacheImage = QtGui.QLabel(Cache)
        self.Label_TailleCacheImage.setObjectName(_fromUtf8("Label_TailleCacheImage"))
        self.horizontalLayout_2.addWidget(self.Label_TailleCacheImage)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_6 = QtGui.QLabel(Cache)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.Label_NombreDeDalles = QtGui.QLabel(Cache)
        self.Label_NombreDeDalles.setObjectName(_fromUtf8("Label_NombreDeDalles"))
        self.horizontalLayout_3.addWidget(self.Label_NombreDeDalles)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.VideCache1 = QtGui.QPushButton(Cache)
        self.VideCache1.setAutoDefault(False)
        self.VideCache1.setObjectName(_fromUtf8("VideCache1"))
        self.verticalLayout_6.addWidget(self.VideCache1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.line = QtGui.QFrame(Cache)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_6.addWidget(self.line)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_2 = QtGui.QLabel(Cache)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_5.addWidget(self.label_2)
        self.line_3 = QtGui.QFrame(Cache)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_5.addWidget(self.line_3)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_8 = QtGui.QLabel(Cache)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_4.addWidget(self.label_8)
        self.Label_TailleCacheDonne = QtGui.QLabel(Cache)
        self.Label_TailleCacheDonne.setObjectName(_fromUtf8("Label_TailleCacheDonne"))
        self.horizontalLayout_4.addWidget(self.Label_TailleCacheDonne)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.VideCache2 = QtGui.QPushButton(Cache)
        self.VideCache2.setAutoDefault(False)
        self.VideCache2.setObjectName(_fromUtf8("VideCache2"))
        self.verticalLayout_5.addWidget(self.VideCache2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.pushButton = QtGui.QPushButton(Cache)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_7.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.retranslateUi(Cache)
        QtCore.QMetaObject.connectSlotsByName(Cache)

    def retranslateUi(self, Cache):
        Cache.setWindowTitle(_translate("Cache", "Paramètres du Proxy", None))
        self.label.setText(_translate("Cache", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Cache Image</span></p></body></html>", None))
        self.label_4.setText(_translate("Cache", "Taille du cache :", None))
        self.Label_TailleCacheImage.setText(_translate("Cache", "TextLabel", None))
        self.label_6.setText(_translate("Cache", "Nombre de dalles OSM:", None))
        self.Label_NombreDeDalles.setText(_translate("Cache", "TextLabel", None))
        self.VideCache1.setText(_translate("Cache", "Vider le cache image", None))
        self.label_2.setText(_translate("Cache", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Cache des infos equipements</span></p></body></html>", None))
        self.label_8.setText(_translate("Cache", "Taille du cache :", None))
        self.Label_TailleCacheDonne.setText(_translate("Cache", "TextLabel", None))
        self.VideCache2.setText(_translate("Cache", "Vider le cache equipement", None))
        self.pushButton.setText(_translate("Cache", "OK", None))

