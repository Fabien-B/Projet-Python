# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created: Thu Jan 22 21:54:12 2015
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
        MainWindow.resize(996, 653)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.toolBox = QtGui.QToolBox(self.splitter)
        self.toolBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.toolBox.setToolTip(_fromUtf8(""))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.toolBoxPage2 = QtGui.QWidget()
        self.toolBoxPage2.setGeometry(QtCore.QRect(0, 0, 259, 434))
        self.toolBoxPage2.setObjectName(_fromUtf8("toolBoxPage2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.toolBoxPage2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.toolBoxPage2)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.handAccessButton = QtGui.QCheckBox(self.toolBoxPage2)
        self.handAccessButton.setObjectName(_fromUtf8("handAccessButton"))
        self.verticalLayout_3.addWidget(self.handAccessButton)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.ajouterFiltreButton = QtGui.QToolButton(self.toolBoxPage2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icones/ajouterFiltre.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ajouterFiltreButton.setIcon(icon)
        self.ajouterFiltreButton.setObjectName(_fromUtf8("ajouterFiltreButton"))
        self.horizontalLayout_3.addWidget(self.ajouterFiltreButton)
        self.label_2 = QtGui.QLabel(self.toolBoxPage2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.toolBox.addItem(self.toolBoxPage2, _fromUtf8(""))
        self.toolBoxPage3 = QtGui.QWidget()
        self.toolBoxPage3.setGeometry(QtCore.QRect(0, 0, 277, 348))
        self.toolBoxPage3.setObjectName(_fromUtf8("toolBoxPage3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.toolBoxPage3)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.toolBoxPage3)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.pushButton_7 = QtGui.QPushButton(self.toolBoxPage3)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.verticalLayout_6.addWidget(self.pushButton_7)
        self.label_3 = QtGui.QLabel(self.toolBoxPage3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_6.addWidget(self.label_3)
        self.Findequiarret_2_button = QtGui.QPushButton(self.toolBoxPage3)
        self.Findequiarret_2_button.setObjectName(_fromUtf8("Findequiarret_2_button"))
        self.verticalLayout_6.addWidget(self.Findequiarret_2_button)
        self.findPathFromPinButton = QtGui.QPushButton(self.toolBoxPage3)
        self.findPathFromPinButton.setObjectName(_fromUtf8("findPathFromPinButton"))
        self.verticalLayout_6.addWidget(self.findPathFromPinButton)
        self.label_19 = QtGui.QLabel(self.toolBoxPage3)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.verticalLayout_6.addWidget(self.label_19)
        self.textEdit = QtGui.QTextEdit(self.toolBoxPage3)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_6.addWidget(self.textEdit)
        self.toolBox.addItem(self.toolBoxPage3, _fromUtf8(""))
        self.graphicsView = myQGraphicsView(self.splitter)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout_9.addWidget(self.splitter)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_9.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 996, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName(_fromUtf8("menuFichier"))
        self.menuAffichage = QtGui.QMenu(self.menubar)
        self.menuAffichage.setObjectName(_fromUtf8("menuAffichage"))
        self.menuOutils = QtGui.QMenu(self.menubar)
        self.menuOutils.setObjectName(_fromUtf8("menuOutils"))
        self.menuVue = QtGui.QMenu(self.menubar)
        self.menuVue.setObjectName(_fromUtf8("menuVue"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_2 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName(_fromUtf8("dockWidget_2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.scrollArea = QtGui.QScrollArea(self.dockWidgetContents_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 353, 786))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.pushButton_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_8.addWidget(self.pushButton_2)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.layoutNom = QtGui.QHBoxLayout()
        self.layoutNom.setObjectName(_fromUtf8("layoutNom"))
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.layoutNom.addWidget(self.label_4)
        self.nomLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.nomLineEdit.setEnabled(True)
        self.nomLineEdit.setReadOnly(True)
        self.nomLineEdit.setObjectName(_fromUtf8("nomLineEdit"))
        self.layoutNom.addWidget(self.nomLineEdit)
        self.verticalLayout_4.addLayout(self.layoutNom)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_15.addWidget(self.label_5)
        self.typeLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.typeLineEdit.setReadOnly(True)
        self.typeLineEdit.setObjectName(_fromUtf8("typeLineEdit"))
        self.horizontalLayout_15.addWidget(self.typeLineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_16.addWidget(self.label_6)
        self.activitiesListWidget = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.activitiesListWidget.setObjectName(_fromUtf8("activitiesListWidget"))
        self.horizontalLayout_16.addWidget(self.activitiesListWidget)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label_7 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_17.addWidget(self.label_7)
        self.revetementLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.revetementLineEdit.setReadOnly(True)
        self.revetementLineEdit.setObjectName(_fromUtf8("revetementLineEdit"))
        self.horizontalLayout_17.addWidget(self.revetementLineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_8 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_14.addWidget(self.label_8)
        self.eclairageLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.eclairageLineEdit.setReadOnly(True)
        self.eclairageLineEdit.setObjectName(_fromUtf8("eclairageLineEdit"))
        self.horizontalLayout_14.addWidget(self.eclairageLineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_9 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_13.addWidget(self.label_9)
        self.vestiairesLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.vestiairesLineEdit.setReadOnly(True)
        self.vestiairesLineEdit.setObjectName(_fromUtf8("vestiairesLineEdit"))
        self.horizontalLayout_13.addWidget(self.vestiairesLineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.label_15 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_22.addWidget(self.label_15)
        self.sanitairesLineEdit_5 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.sanitairesLineEdit_5.setReadOnly(True)
        self.sanitairesLineEdit_5.setObjectName(_fromUtf8("sanitairesLineEdit_5"))
        self.horizontalLayout_22.addWidget(self.sanitairesLineEdit_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_11 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_11.addWidget(self.label_11)
        self.douchesLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.douchesLineEdit.setReadOnly(True)
        self.douchesLineEdit.setObjectName(_fromUtf8("douchesLineEdit"))
        self.horizontalLayout_11.addWidget(self.douchesLineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.label_14 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_21.addWidget(self.label_14)
        self.sanitairesLineEdit_4 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.sanitairesLineEdit_4.setReadOnly(True)
        self.sanitairesLineEdit_4.setObjectName(_fromUtf8("sanitairesLineEdit_4"))
        self.horizontalLayout_21.addWidget(self.sanitairesLineEdit_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.label_13 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_20.addWidget(self.label_13)
        self.sanitairesLineEdit_3 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.sanitairesLineEdit_3.setReadOnly(True)
        self.sanitairesLineEdit_3.setObjectName(_fromUtf8("sanitairesLineEdit_3"))
        self.horizontalLayout_20.addWidget(self.sanitairesLineEdit_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.label_12 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_19.addWidget(self.label_12)
        self.sanitairesLineEdit_2 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.sanitairesLineEdit_2.setReadOnly(True)
        self.sanitairesLineEdit_2.setObjectName(_fromUtf8("sanitairesLineEdit_2"))
        self.horizontalLayout_19.addWidget(self.sanitairesLineEdit_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_10 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_12.addWidget(self.label_10)
        self.sanitairesLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.sanitairesLineEdit.setReadOnly(True)
        self.sanitairesLineEdit.setObjectName(_fromUtf8("sanitairesLineEdit"))
        self.horizontalLayout_12.addWidget(self.sanitairesLineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.label_17 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_24.addWidget(self.label_17)
        self.sanitairesLineEdit_7 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.sanitairesLineEdit_7.setReadOnly(True)
        self.sanitairesLineEdit_7.setObjectName(_fromUtf8("sanitairesLineEdit_7"))
        self.horizontalLayout_24.addWidget(self.sanitairesLineEdit_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_28 = QtGui.QHBoxLayout()
        self.horizontalLayout_28.setObjectName(_fromUtf8("horizontalLayout_28"))
        self.label_21 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_28.addWidget(self.label_21)
        self.sanitairesLineEdit_11 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.sanitairesLineEdit_11.setReadOnly(True)
        self.sanitairesLineEdit_11.setObjectName(_fromUtf8("sanitairesLineEdit_11"))
        self.horizontalLayout_28.addWidget(self.sanitairesLineEdit_11)
        self.verticalLayout_4.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_27 = QtGui.QHBoxLayout()
        self.horizontalLayout_27.setObjectName(_fromUtf8("horizontalLayout_27"))
        self.label_20 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_27.addWidget(self.label_20)
        self.sanitairesLineEdit_10 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.sanitairesLineEdit_10.setReadOnly(True)
        self.sanitairesLineEdit_10.setObjectName(_fromUtf8("sanitairesLineEdit_10"))
        self.horizontalLayout_27.addWidget(self.sanitairesLineEdit_10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_26 = QtGui.QHBoxLayout()
        self.horizontalLayout_26.setObjectName(_fromUtf8("horizontalLayout_26"))
        self.label_18 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_26.addWidget(self.label_18)
        self.sanitairesLineEdit_9 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.sanitairesLineEdit_9.setReadOnly(True)
        self.sanitairesLineEdit_9.setObjectName(_fromUtf8("sanitairesLineEdit_9"))
        self.horizontalLayout_26.addWidget(self.sanitairesLineEdit_9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.label_16 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_23.addWidget(self.label_16)
        self.sanitairesLineEdit_6 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.sanitairesLineEdit_6.setReadOnly(True)
        self.sanitairesLineEdit_6.setObjectName(_fromUtf8("sanitairesLineEdit_6"))
        self.horizontalLayout_23.addWidget(self.sanitairesLineEdit_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.verticalLayout_4.addLayout(self.horizontalLayout_18)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_7.addWidget(self.scrollArea)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_2)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.Quitter = QtGui.QAction(MainWindow)
        self.Quitter.setCheckable(True)
        self.Quitter.setChecked(False)
        self.Quitter.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.Quitter.setSoftKeyRole(QtGui.QAction.PositiveSoftKey)
        self.Quitter.setObjectName(_fromUtf8("Quitter"))
        self.actionInspecteur = QtGui.QAction(MainWindow)
        self.actionInspecteur.setCheckable(True)
        self.actionInspecteur.setObjectName(_fromUtf8("actionInspecteur"))
        self.actionProxy = QtGui.QAction(MainWindow)
        self.actionProxy.setObjectName(_fromUtf8("actionProxy"))
        self.actionViderCache = QtGui.QAction(MainWindow)
        self.actionViderCache.setObjectName(_fromUtf8("actionViderCache"))
        self.actionViderCacheCarte = QtGui.QAction(MainWindow)
        self.actionViderCacheCarte.setObjectName(_fromUtf8("actionViderCacheCarte"))
        self.actionZoom = QtGui.QAction(MainWindow)
        self.actionZoom.setObjectName(_fromUtf8("actionZoom"))
        self.actionZoom_2 = QtGui.QAction(MainWindow)
        self.actionZoom_2.setObjectName(_fromUtf8("actionZoom_2"))
        self.menuFichier.addAction(self.Quitter)
        self.menuAffichage.addAction(self.actionInspecteur)
        self.menuOutils.addAction(self.actionProxy)
        self.menuOutils.addAction(self.actionViderCache)
        self.menuVue.addAction(self.actionZoom)
        self.menuVue.addAction(self.actionZoom_2)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuAffichage.menuAction())
        self.menubar.addAction(self.menuOutils.menuAction())
        self.menubar.addAction(self.menuVue.menuAction())
        self.toolBar.addAction(self.Quitter)
        self.toolBar.addAction(self.actionInspecteur)
        self.toolBar.addAction(self.actionZoom)
        self.toolBar.addAction(self.actionZoom_2)
        self.toolBar.addAction(self.actionViderCache)
        self.toolBar.addAction(self.actionProxy)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "VEST - Visualisation des Équipements Sportifs Toulousain", None))
        self.handAccessButton.setText(_translate("MainWindow", "Accès Handicapés", None))
        self.ajouterFiltreButton.setText(_translate("MainWindow", "...", None))
        self.label_2.setText(_translate("MainWindow", "Ajouter un filtre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage2), _translate("MainWindow", "Filtres", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Rechercher ( press Enter ) ", None))
        self.pushButton_7.setText(_translate("MainWindow", "Trouver l\'arrêt le plus proche", None))
        self.label_3.setText(_translate("MainWindow", "Chercher un itinéraire\n"
"vers l\'équipement:", None))
        self.Findequiarret_2_button.setText(_translate("MainWindow", "depuis l\'adresse", None))
        self.findPathFromPinButton.setText(_translate("MainWindow", "depuis l\'épingle", None))
        self.label_19.setText(_translate("MainWindow", "Instructions\n"
"itinéraire:", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage3), _translate("MainWindow", "Rechercher une adresse", None))
        self.pushButton.setText(_translate("MainWindow", "Revenir au Zoom Initial", None))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier", None))
        self.menuAffichage.setTitle(_translate("MainWindow", "Affichage", None))
        self.menuOutils.setTitle(_translate("MainWindow", "Outils", None))
        self.menuVue.setTitle(_translate("MainWindow", "Vue", None))
        self.pushButton_2.setText(_translate("MainWindow", "Trouver un itinéraire", None))
        self.label_4.setText(_translate("MainWindow", "Nom:", None))
        self.label_5.setText(_translate("MainWindow", "Type:", None))
        self.label_6.setText(_translate("MainWindow", "Activités:", None))
        self.label_7.setText(_translate("MainWindow", "Revetement:", None))
        self.label_8.setText(_translate("MainWindow", "Éclairage", None))
        self.label_9.setText(_translate("MainWindow", "Vestiaires:", None))
        self.label_15.setText(_translate("MainWindow", "Sanitaires:", None))
        self.label_11.setText(_translate("MainWindow", "Douches:", None))
        self.label_14.setText(_translate("MainWindow", "Accès Handicapés:", None))
        self.label_13.setText(_translate("MainWindow", "Toilettes Handicapés:", None))
        self.label_12.setText(_translate("MainWindow", "Tribunes:", None))
        self.label_10.setText(_translate("MainWindow", "Club House:", None))
        self.label_17.setText(_translate("MainWindow", "Dimensions:", None))
        self.label_21.setText(_translate("MainWindow", "Capacité:", None))
        self.label_20.setText(_translate("MainWindow", "Adresse:", None))
        self.label_18.setText(_translate("MainWindow", "Catégorie:", None))
        self.label_16.setText(_translate("MainWindow", "GPS:", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.Quitter.setText(_translate("MainWindow", "Quitter", None))
        self.Quitter.setToolTip(_translate("MainWindow", "Quitter", None))
        self.Quitter.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionInspecteur.setText(_translate("MainWindow", "Inspecteur", None))
        self.actionInspecteur.setShortcut(_translate("MainWindow", "Ctrl+I", None))
        self.actionProxy.setText(_translate("MainWindow", "Paramètres de proxy", None))
        self.actionViderCache.setText(_translate("MainWindow", "Vider le cache", None))
        self.actionViderCacheCarte.setText(_translate("MainWindow", "Vider le cache carte", None))
        self.actionZoom.setText(_translate("MainWindow", "Zoom +", None))
        self.actionZoom_2.setText(_translate("MainWindow", "Zoom -", None))

from carte import myQGraphicsView
