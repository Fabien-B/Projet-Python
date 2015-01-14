from PyQt4 import QtGui, QtCore
from  PyQt4.QtCore import Qt
import equipement

class Filtre(QtCore.QObject):

    updateSignal = QtCore.pyqtSignal()

    removeSignal = QtCore.pyqtSignal(QtGui.QWidget)

    def __init__(self, tabWidget,pointAff):
        super(Filtre,self).__init__()
        self.activitiesSet = set()
        self.quartierSet = set()
        self.allEquipSet = set()
        self.revetementSet = set()
        #self.toilettesHandSet = set()
        #self.arrosageSet = set()
        #self.eclairageSet = set()
        self.typeSet = set()

        self.equipmentSet = set()
        self.pointAff = pointAff

        self.tabWidget = tabWidget
        #self.attributsNames = {'Quartier':'quartier','Activités':'activities','Revêtement':'revetement','Éclairage':'eclairage','Arrosage':'arrosage','Toilettes Handicapés':'toilettesHand','Type':'type'}
        self.attributsNames = {'Quartier':'quartier','Activités':'activities','Revêtement':'revetement','Type':'type'}
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),"Activité")
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtGui.QComboBox(self.tab)
        self.comboBox.setObjectName("comboBox")
        self.hLbas = QtGui.QHBoxLayout()
        self.hLbas.setObjectName("hLbas")
        self.retirerFiltreButton = QtGui.QToolButton()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icones/retirerFiltre.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.retirerFiltreButton.setIcon(icon)
        self.retirerFiltreButton.setObjectName("retirerFiltreButton")
        self.verticalLayout.addLayout(self.hLbas)
        self.hLbas.addWidget(self.comboBox)
        self.hLbas.addWidget(self.retirerFiltreButton)
        self.selectAllSecondFiltreButton = QtGui.QPushButton(self.tab)
        self.selectAllSecondFiltreButton.setObjectName("selectAllSecondFiltreButton")
        self.verticalLayout.addWidget(self.selectAllSecondFiltreButton)
        self.lineEditFiltre = QtGui.QLineEdit(self.tab)
        self.lineEditFiltre.setObjectName("lineEditFiltres")
        self.verticalLayout.addWidget(self.lineEditFiltre)
        self.listWidget = QtGui.QListWidget(self.tab)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.selectAllSecondFiltreButton.setText("Tout (dé)sélectionner")
        self.selectAllSecondFiltreButton.clicked.connect(self.select_deselect_all)
        self.lineEditFiltre.textEdited.connect(self.update_checkbox)
        self.connect(self.comboBox, QtCore.SIGNAL('currentIndexChanged(QString)'), self.add_checkboxs)
        self.retirerFiltreButton.clicked.connect(lambda : self.removeSignal.emit(self.tab))

        self.add_combo_items()


    def create_set(self, equiplist):
        """Récupère les activités, quartier, revêtement et type des équipements"""
        for equip in equiplist:
            if equip.activities is not None:
                for key in equip.activities:
                    if key != '':
                        self.activitiesSet.add(key)
                self.quartierSet.add(equip.quartier)
                for item in equip.revetement:
                    self.revetementSet.add(item)
                self.typeSet.add(equip.type)
                #self.toilettesHandSet.add(equip.toilettesHand)
                #self.arrosageSet.add(equip.arrosage)
                #self.eclairageSet.add(equip.eclairage)

    def equip_set(self,equiplist):
        for equip in equiplist:
            self.allEquipSet.add(equip)


    def filtrer_set_par_acti(self,param,paramNames):
        """Regarde le critère de filtrage"""
        tempSet = set()
        for equip in self.allEquipSet:
            if param == 'activities':
                paramSet = set(equip.__dict__[param])
            elif param == 'revetement':
                paramSet = set(equip.__dict__[param])
            else:
                paramSet = set([equip.__dict__[param]])
            ActiRequestSet = set(paramNames)
            if ActiRequestSet & paramSet != set():
                tempSet.add(equip)
        return tempSet

    def printkey(self):
        for key in self.activitiesSet:
            print(key)
        print('nombre clé :', len(self.activitiesSet))


    def update_checkbox(self, txt):
        """Ajoute les équipements correspondant au filtre demandé à la liste à afficher, cache ceux qui ne correspondent pas"""
        liste = []
        paramSet = self.listWidget.item(0).param + 'Set'
        for key in self.__dict__[paramSet]:
            if txt.capitalize() in key:
                liste.append(key)
        for i in range(self.listWidget.count()):
                checkbox = self.listWidget.item(i)
                if checkbox.text() not in liste:
                    checkbox.setHidden(True)
                else:
                    checkbox.setHidden(False)
        self.updateSignal.emit()

    def select_deselect_all(self):
        """Selectionne tous les équipements présents dans le widget"""
        try:
            check = 2 if not self.listWidget.item(0).checkState() else 0
            param = self.listWidget.item(0).param
            paramList = []
            for i in range(self.listWidget.count()):
                    checkbox = self.listWidget.item(i)
                    if not checkbox.isHidden():
                        checkbox.setCheckState(check)
                        paramList.append(checkbox.text())
            if check:
                self.equipmentSet.update(self.filtrer_set_par_acti(param,paramList))
            else:
                self.equipmentSet.difference_update(self.filtrer_set_par_acti(param,paramList))
            self.updateSignal.emit()
        except AttributeError:
            print('sélectionnez un paramètre différent')

    def add_checkboxs(self,txt):
        """Ajoute les checkboxes souhaitées à la listwidget"""
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),txt)
        param = str(self.attributsNames[txt])
        paramSet = param + 'Set'
        self.listWidget.clear()
        for name in sorted(self.__dict__[paramSet]):
            name = str(name)
            if name == '999':
                name = 'Non renseigné'
            lwItem = myListWidgetItem(name, self.listWidget)
            lwItem.param = param
            lwItem.setFlags(Qt.ItemIsEnabled)
            lwItem.setCheckState(Qt.Unchecked)

    def add_combo_items(self):
        for key in equipement.Equipment().__dict__:
            if key in self.attributsNames.values():
                for cle in self.attributsNames:
                    if self.attributsNames[cle] == key:
                        self.comboBox.addItem(cle)
        self.listWidget.itemClicked.connect(self.itemClicked)

    def itemClicked(self, item):
        print(item.param)
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
            eqASupprimer = self.filtrer_set_par_acti(item.param,[item.text()])
            for i in range(item.liste.count()):
                checkbox = item.liste.item(i)
                if checkbox.checkState() == Qt.Checked:
                    eqASupprimer -= self.filtrer_set_par_acti(item.param,[checkbox.text()])
            self.equipmentSet.difference_update(eqASupprimer)
        else:
            item.setCheckState(Qt.Checked)
            self.equipmentSet.update(self.filtrer_set_par_acti(item.param,[item.text()]))
        self.updateSignal.emit()

    def hand_changement(self):
        if self.HandAccessCheckBox.checkState():
            self.equipmentSet.difference_update(self.filtrer_acces_hand(self.equipmentSet,False))
        else:
            param = self.listWidget.item(0).param
            paramList = []
            for i in range(self.listWidget.count()):
                checkbox = self.listWidget.item(i)
                if checkbox.checkState():
                    paramList.append(checkbox.text())
            self.equipmentSet.update(self.filtrer_set_par_acti(param,paramList))
            print(self.equipmentSet)
        self.updateSignal.emit()


class myListWidgetItem(QtGui.QListWidgetItem):
    def __init__(self,name, listView):
        super(myListWidgetItem,self).__init__(name, listView)
        self.param = ''
        self.liste = listView