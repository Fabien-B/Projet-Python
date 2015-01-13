from PyQt4 import QtGui, QtCore
from  PyQt4.QtCore import Qt
import equipement

class Filtre(QtCore.QObject):

    updateSignal = QtCore.pyqtSignal()

    def __init__(self, tabWidget,equipmentSet,pointAff,nocover, graphicsView, scene):
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
        self.nocover = nocover
        self.graphicsView = graphicsView
        self.scene = scene

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

        self.connect(self.comboBox, QtCore.SIGNAL('currentIndexChanged(QString)'), self.changer_filtre)
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


    def update_checkbox(self,concernedList, txt):
        liste = []
        paramSet = concernedList.item(0).param + 'Set'
        for key in self.__dict__[paramSet]:
            if txt.capitalize() in key:
                liste.append(key)
        print(liste)
        for i in range(concernedList.count()):
                checkbox = concernedList.item(i)
                if checkbox.text() not in liste:
                    checkbox.setHidden(True)
                else:
                    checkbox.setHidden(False)
        self.updateSignal.emit()
        #self.update_affichage_equipements()

    def select_deselect_all(self,concernedList):
        check = 2 if not concernedList.item(0).checkState() else 0
        param = concernedList.item(0).param
        activitiesList = []
        for i in range(concernedList.count()):
                checkbox = concernedList.item(i)
                if not checkbox.isHidden():
                    checkbox.setCheckState(check)
                    activitiesList.append(checkbox.text())
        if check:
            self.equipmentSet.update(self.filtrer_set_par_acti(param,activitiesList,self.HandAccessCheckBox.checkState()))
        else:
            self.equipmentSet.difference_update(self.filtrer_set_par_acti(param,activitiesList))
        self.update_affichage_equipements()

    def add_checkboxs(self,listView,param):
        paramSet = param + 'Set'
        listView.clear()
        for name in sorted(self.__dict__[paramSet]):
            name = str(name)
            if name == '999':
                name = 'Non renseigné'
            lwItem = myListWidgetItem(name, listView)
            lwItem.param = param
            lwItem.setFlags(Qt.ItemIsEnabled)
            lwItem.setCheckState(Qt.Unchecked)

    def add_combo_items(self):
        print('eeeee')
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
        self.update_affichage_equipements()

    def hand_changement(self,concernedList):
        if self.HandAccessCheckBox.checkState():
            self.equipmentSet.difference_update(self.filtrer_acces_hand(self.equipmentSet,False))
        else:
            param = concernedList.item(0).param
            paramList = []
            for i in range(concernedList.count()):
                checkbox = concernedList.item(i)
                if checkbox.checkState():
                    paramList.append(checkbox.text())
            self.equipmentSet = self.filtrer_set_par_acti(param,paramList)
        self.update_affichage_equipements()

    def changer_filtre(self,txt):
        self.add_checkboxs(self.listWidget,str(self.attributsNames[txt]))
        self.selectAllSecondFiltreButton.clicked.connect(lambda : self.select_deselect_all(self.listWidget))
        self.HandAccessCheckBox.stateChanged.connect(lambda : self.hand_changement(self.listWidget))
        self.lineEditFiltre.textEdited.connect(lambda  : self.update_checkbox(self.listWidget, self.lineEditFiltre.text()))

    def update_affichage_equipements(self):
        for point in self.pointAff:
            if point in self.scene.items():
                self.scene.removeItem(point)
        for equip in self.equipmentSet:
            self.pointAff.append(self.graphicsView.draw_equipment(equip))
            self.scene.update()
        self.nocover.cluster(self.pointAff)


class myListWidgetItem(QtGui.QListWidgetItem):
    def __init__(self,name, listView):
        super(myListWidgetItem,self).__init__(name, listView)
        self.param = ''
        self.liste = listView