from PyQt4 import QtCore, QtGui
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import filtres

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


def itemClicked(item):
    print('item: ', item, ', state :', item.checkState(), ', acti :', item.text())
    if item.checkState() == Qt.Checked:
        item.setCheckState(Qt.Unchecked)
    else:
        item.setCheckState(Qt.Checked)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1000, 650)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(290, 10, 700, 610))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(270, 0, 20, 630))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.toolBox = QtGui.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(10, 10, 260, 580))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.toolBoxPage1 = QtGui.QWidget()
        self.toolBoxPage1.setObjectName(_fromUtf8("toolBoxPage1"))
        self.widget = QtGui.QWidget(self.toolBoxPage1)
        self.widget.setGeometry(QtCore.QRect(0, 0, 260, 480))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.selectall)
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lineEdit_1 = QtGui.QLineEdit(self.widget)
        self.lineEdit_1.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_1.setPlaceholderText('Rechercher activité')
        self.lineEdit_1.textEdited.connect(self.update_checkbox)
        self.verticalLayout.addWidget(self.lineEdit_1)
        self.scrollArea_2 = QtGui.QScrollArea(self.widget)
        self.scrollArea_2.setMouseTracking(True)
        self.scrollArea_2.setAutoFillBackground(True)
        self.scrollArea_2.setFrameShape(QtGui.QFrame.WinPanel)
        self.scrollArea_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(False)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.lw = QtGui.QListWidget(self.scrollAreaWidgetContents_2)
        self.lw.setMinimumSize(330, 5000)
        self.lw.itemClicked.connect(itemClicked)
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 240, len(filtres.sets)*22))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.toolBox.addItem(self.toolBoxPage1, _fromUtf8(""))
        self.toolBoxPage2 = QtGui.QWidget()
        self.toolBoxPage2.setObjectName(_fromUtf8("toolBoxPage2"))
        self.checkBox = QtGui.QCheckBox(self.toolBoxPage2)
        self.checkBox.setGeometry(QtCore.QRect(10, 20, 100, 20))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.toolBox.addItem(self.toolBoxPage2, _fromUtf8(""))
        self.toolBoxPage3 = QtGui.QWidget()
        self.toolBoxPage3.setObjectName(_fromUtf8("toolBoxPage3"))
        self.widget1 = QtGui.QWidget(self.toolBoxPage3)
        self.widget1.setGeometry(QtCore.QRect(20, 30, 220, 30))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.widget1)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.toolBox.addItem(self.toolBoxPage3, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName(_fromUtf8("menuFichier"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.Quitter = QtGui.QAction(MainWindow)
        self.Quitter.setCheckable(True)
        self.Quitter.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.Quitter.setSoftKeyRole(QtGui.QAction.PositiveSoftKey)
        self.Quitter.setObjectName(_fromUtf8("Quitter"))
        self.menuFichier.addAction(self.Quitter)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage1), _translate("MainWindow", "Activité", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage2), _translate("MainWindow", "A voir", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage3), _translate("MainWindow", "A voir encore apres", None))
        self.pushButton.setText(_translate("MainWindow", "Tout (dé)sélectionner", None))
        self.checkBox.setText(_translate("MainWindow", "CheckBox Page 2", None))
        self.label.setText(_translate("MainWindow", "Rechercher", None))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier", None))
        self.Quitter.setText(_translate("MainWindow", "Quitter", None))
        self.Quitter.setToolTip(_translate("MainWindow", "Quitter", None))



