from PyQt4 import QtGui, QtCore
from  PyQt4.QtCore import Qt
import equipement

class Filtre(QtCore.QObject):

    updateSignal = QtCore.pyqtSignal()

    def __init__(self, tabWidget,equipmentSet,pointAff):
        super(Filtre,self).__init__()
        self.activitiesSet = set()
        self.quartierSet = set()
        self.allEquipSet = set()
        self.revetementSet = set()
        self.toilettesHandSet = set()
        self.arrosageSet = set()
        self.eclairageSet = set()

        self.equipmentSet = equipmentSet
        self.pointAff = pointAff

        self.tabWidget = tabWidget
        self.attributsNames = {'Quartier':'quartier','Activités':'activities','Revêtement':'revetement','Éclairage':'eclairage','Arrosage':'arrosage','Toilettes Handicapés':'toilettesHand'}
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("dfhgdh")
        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),"Autre Filtre")
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")

        self.comboBox = QtGui.QComboBox(self.tab)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.selectAllSecondFiltreButton = QtGui.QPushButton(self.tab)
        self.selectAllSecondFiltreButton.setObjectName("selectAllSecondFiltreButton")
        self.verticalLayout.addWidget(self.selectAllSecondFiltreButton)
        self.lineEditFiltre = QtGui.QLineEdit(self.tab)
        self.lineEditFiltre.setObjectName("lineEditFiltres")
        self.verticalLayout.addWidget(self.lineEditFiltre)
        self.listWidget = QtGui.QListWidget(self.tab)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.HandAccessCheckBox = QtGui.QCheckBox(self.tab)
        self.HandAccessCheckBox.setObjectName("HandAccessCheckBox")
        self.verticalLayout.addWidget(self.HandAccessCheckBox)
        self.selectAllSecondFiltreButton.setText("Tout (dé)sélectionner")
        self.HandAccessCheckBox.setText("Accès Handicapés")
        self.selectAllSecondFiltreButton.clicked.connect(self.select_deselect_all)
        self.HandAccessCheckBox.stateChanged.connect(self.hand_changement)
        self.lineEditFiltre.textEdited.connect(self.update_checkbox)
        #self.connect(self.comboBox, QtCore.SIGNAL('currentIndexChanged(QString)'), self.changer_filtre)
        self.connect(self.comboBox, QtCore.SIGNAL('currentIndexChanged(QString)'), self.add_checkboxs)
        self.add_combo_items()

    def create_set(self, equiplist):
        for equip in equiplist:
            if equip.activities is not None:
                for key in equip.activities:
                    if key != '':
                        self.activitiesSet.add(key)
                self.quartierSet.add(equip.quartier)
                for item in equip.revetement:
                    self.revetementSet.add(item)
                self.toilettesHandSet.add(equip.toilettesHand)
                self.arrosageSet.add(equip.arrosage)
                self.eclairageSet.add(equip.eclairage)

    def equip_set(self,equiplist):
        for equip in equiplist:
            self.allEquipSet.add(equip)


    def filtrer_set_par_acti(self,param,paramNames,accesHand = False):
        tempSet = set()
        for equip in self.allEquipSet:
            paramSet = set()
            if param == 'activities':
                paramSet = set(equip.__dict__[param])
            elif param == 'revetement':
                paramSet = set(equip.__dict__[param])
            else:
                paramSet = set([equip.__dict__[param]])
            ActiRequestSet = set(paramNames)
            if ActiRequestSet & paramSet != set():
                tempSet.add(equip)
        if accesHand:
            print('Acces Hand')
            return self.filtrer_acces_hand(tempSet)
        return tempSet

    def filtrer_acces_hand(self,equipSet,state = True):     #state = True <=> renvoie les eqs AVEC acces hand, state = False <=> renvoie ceux SANS acces hand
        tempSet = set()
        for equip in equipSet:
            if state:
                if equip.accesHand:
                    tempSet.add(equip)
            else:
                if not equip.accesHand:
                    tempSet.add(equip)
        return tempSet

    def printkey(self):
        for key in self.activitiesSet:
            print(key)
        print('nombre clé :', len(self.activitiesSet))


    def update_checkbox(self, txt):
        liste = []
        paramSet = self.listWidget.item(0).param + 'Set'
        for key in self.__dict__[paramSet]:
            if txt.capitalize() in key:
                liste.append(key)
        print(liste)
        for i in range(self.listWidget.count()):
                checkbox = self.listWidget.item(i)
                if checkbox.text() not in liste:
                    checkbox.setHidden(True)
                else:
                    checkbox.setHidden(False)
        self.updateSignal.emit()

    def select_deselect_all(self):
        check = 2 if not self.listWidget.item(0).checkState() else 0
        param = self.listWidget.item(0).param
        paramList = []
        for i in range(self.listWidget.count()):
                checkbox = self.listWidget.item(i)
                if not checkbox.isHidden():
                    checkbox.setCheckState(check)
                    paramList.append(checkbox.text())
        if check:
            self.equipmentSet.update(self.filtrer_set_par_acti(param,paramList,self.HandAccessCheckBox.checkState()))
        else:
            self.equipmentSet.difference_update(self.filtrer_set_par_acti(param,paramList))
        self.updateSignal.emit()

    def add_checkboxs(self,txt):
        print('taaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
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
            self.equipmentSet.update(self.filtrer_set_par_acti(item.param,[item.text()],self.HandAccessCheckBox.checkState()))
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
            #self.equipmentSet = self.filtrer_set_par_acti(param,paramList)
            self.equipmentSet.update(self.filtrer_set_par_acti(param,paramList))
            print(self.equipmentSet)
        self.updateSignal.emit()

    def changer_filtre(self,txt):
        pass
#        self.add_checkboxs(str(self.attributsNames[txt]))


class myListWidgetItem(QtGui.QListWidgetItem):
    def __init__(self,name, listView):
        super(myListWidgetItem,self).__init__(name, listView)
        self.param = ''
        self.liste = listView