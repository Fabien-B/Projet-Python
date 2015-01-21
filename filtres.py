from PyQt4 import QtGui, QtCore
from  PyQt4.QtCore import Qt
import equipement

class Filtre(QtCore.QObject):

    updateSignal = QtCore.pyqtSignal()

    removeSignal = QtCore.pyqtSignal(QtGui.QWidget)

    def __init__(self, tabWidget, pointAff):
        super(Filtre,self).__init__()
        self.activitiesSet = set()
        self.quartierSet = set()
        self.allEquipSet = set()
        self.revetementSet = set()
        self.typeSet = set()
        self.equipmentSet = set()
        self.pointAff = pointAff

        self.tabWidget = tabWidget
        self.attributsNames = {'Quartier':'quartier','Activités':'activities','Revêtement':'revetement','Type':'type'}
        self.quartiersNames = {"1.1":"Capitole, Arnaud Bernard, Carmes","1.2":"Amidonniers, Compans-Cafarelli","1.3":"Les Chalets, Bayard, Belfort, Saint-Aubin, Dupuy","2.1":"Saint-Cyprien","2.2":"Croix-de-Pierre, Route d'Espagne","2.3":"Fontaine-Lestang, Bagatelle, Papus, Tabar, Bordelongue","2.4":"Fontaine-Bayonne, Cartoucherie ","3.1":"Minimes, Barrière-de-Paris","3.2":"Sept-Deniers, Ginestous, Lalande","3.3":"Trois Cocus, Borderouge, Croix-Daurade, Paleficat, Grand-Selve","3.4":"Les Izards, Trois Cocus, Borderouge, Croix-Daurade","4.1":"Bonnefoy, Roseraie, Gramont","4.2":"Jolimont, Bonhoure, Soupetard","4.3":"Côte-Pavée, L'Hers, Limayrac ","5.1":"Pont-des-Demoiselles, Montaudran, La Terrasse","5.2":"Rangueil, Sauzelong, Pech-David, Pouvourville","5.3":"Saint-Michel Empalot, Saint-Agne, Le Busca","6.1":"Arènes Romaines, Saint-Martin-du-Touch","6.2":"Lardenne, Pradettes, Basso-Cambo","6.3":"Mirail, Reynerie, Bellefontaine","6.4":"Saint-Simon, Lafourguette","6.5":"Lafourguette","":"Non renseigné"}
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Activité")
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
        self.lineEditFiltre.setPlaceholderText('Rechercher')
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
                    self.revetementSet.add(item.capitalize())
                self.typeSet.add(equip.type)

    def equip_set(self,equiplist):
        """crée un set de tous les équipements"""
        for equip in equiplist:
            self.allEquipSet.add(equip)


    def filtrer_set_par_acti(self,param,paramNames):
        """filtre les équipements selon le critère de filtrage suivant la liste donnée"""
        tempSet = set()
        for equip in self.allEquipSet:
            if param == 'activities':
                paramSet = set(equip.__dict__[param])
            elif param == 'revetement':
                paramSet = set(equip.__dict__[param])
            else:
                paramSet = set([equip.__dict__[param]])
            ActiRequestSet = set(paramNames)
            if param == 'quartier':
                newParams = []
                for quart in paramNames:
                    for key in self.quartiersNames:
                        if self.quartiersNames[key] == quart:
                            newParams.append(key)
                ActiRequestSet = set(newParams)
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
        """Selectionne/désélectionne tous les équipements présents dans le widget"""
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
        """Ajoute les checkboxs souhaitées à la listwidget"""
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), txt)
        self.lineEditFiltre.clear()
        param = str(self.attributsNames[txt])
        paramSet = param + 'Set'
        self.listWidget.clear()
        for name in sorted(self.__dict__[paramSet]):
            name = str(name)
            if name == '999':
                name = 'Non renseigné'
            if param == 'quartier':
                name = self.quartiersNames[name]
            lwItem = myListWidgetItem(name, self.listWidget)
            lwItem.param = param
            lwItem.setFlags(Qt.ItemIsEnabled)
            lwItem.setCheckState(Qt.Unchecked)


    def add_combo_items(self):
        """Ajoute les choix dans la comboBox"""
        for key in equipement.Equipment().__dict__:
            if key in self.attributsNames.values():
                for cle in self.attributsNames:
                    if self.attributsNames[cle] == key:
                        self.comboBox.addItem(cle)
        self.listWidget.itemClicked.connect(self.item_clicked)

    def item_clicked(self, item):
        """calcule les nouveaux équipements suivant l'état de la checBox et ce qu'elle désigne"""
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
        """actualise les équipements à afficher avec/sans accès handicapés"""
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
    """redéfinition de QListWidgetItem afin de savoir à qui il appartient, et quel paramètre il désigne"""
    def __init__(self,name, listView):
        super(myListWidgetItem,self).__init__(name, listView)
        self.param = ''
        self.liste = listView