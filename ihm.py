from PyQt4.QtCore import pyqtSlot, Qt
from PyQt4.QtGui import QWidget, QListWidgetItem
from PyQt4 import QtCore, QtGui
from window import Ui_MainWindow
import carte
import filtres
import poi
import tisseo
import Get_GPS
import Sceneclicked
import No_More_Horse_Riding as nmhr


class Ihm(Ui_MainWindow):

    def __init__(self,MainWindow):
        super(Ihm, self).__init__()
        self.MainWindow = MainWindow
        self.equipmentDict = {}
        self.latitude = 43.564995   #latitude et longitudes de départ
        self.longitude = 1.481650
        self.checkstate = False
        self.checkBoxs = []
        self.boxChecked =[]
        self.arret = None
        self.ptRecherche = None
        self.locator = Get_GPS.GPScoord(None)
        self.equipmentSet = set()
        self.pointAff = []
        self.nocover = nmhr.No_Covering(self)
    def set_equipements(self, eqList):
        for eq in eqList:
            self.equipmentDict[eq] = None   #Mettre en valeur les Qellipses affichée, ou None si l'équipement n'est pas affiché.

    def update_equipements(self, newSet, bool):
        if bool:
            self.equipmentSet.update(newSet)
        else:
            self.equipmentSet.difference_update(newSet)
        self.update_affichage_equipements()
        return self.equipmentSet  #TODO a supprimer après le return (ou pas)

    def built(self):
        self.dockWidget_2.hide()
        self.build_map()
        self.Quitter.triggered.connect(quit)
        self.actionInspecteur.triggered.connect(self.dockWidget_2.show)
        self.ButtonDSelectAll.clicked.connect(lambda f : self.update_checkbox(True))
        self.lineEditFiltresActivities.textEdited.connect(self.update_checkbox)
        self.listActivities.itemClicked.connect(self.itemClicked)
        self.lineEdit.returnPressed.connect(self.affiche_addresse)
#        self.update_affichage_equipements()

    def build_map(self):
        self.scene = Sceneclicked.SceneClickable()
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setDragMode(QtGui.QGraphicsView.ScrollHandDrag) # allow drag and drop of the view
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)
        self.graphicsView.FinishInit()
        self.graphicsView.ihm = self
        self.graphicsView.download(self.latitude,self.longitude)
        self.connections()
    #pour obtenir les coordonnées GPS d'un point de la carte, appeler: self.graphicsView.get_gps_from_map(Xscene,Yscene) avec (Xscene,Yscene) les coordonnées du point dans la scène.
    #pour dessiner un point sur la carte appeler: self.graphicsView.draw_point(lat,lon [, legend = 'ma legende']), lat et lon étant la latitude et la longitude du point.
    # Retenir la Qellipse retournée (dans une variable) pour pouvoir l'effacer quand on veut.

    def update_affichage_equipements(self):
        for point in self.pointAff:
            if point in self.scene.items():
                self.scene.removeItem(point)
        for equip in self.equipmentSet:
            self.pointAff.append(self.graphicsView.draw_equipment(equip))
            self.scene.update()

        #actiChecked = set()
        #for box in self.boxChecked:
        #    actiChecked.add(box.text())
        #for (equip, point) in self.equipmentDict.items():
        #    currentEquipActi = set()
        #    if equip.activities != None:
        #        for key in dict.keys(equip.activities):
        #            currentEquipActi.add(key)
        #    if currentEquipActi.intersection(actiChecked) != set():
            #if equip.affiche and point == None:
                #self.equipmentDict[equip] = self.graphicsView.draw_point(equip.coords[0],equip.coords[1], legend=equip.name, equipment = equip)
            #self.equipmentDict[equip] = self.graphicsView.draw_equipment(equip)
            #if not equip.affiche and point != None:
            #    if type(point) is poi.Equipment_Group:
            #        for equipoint in point.equipointlist:
            #            self.equipmentDict[equipoint.equipment] = None
            #    self.scene.removeItem(point)
            #    self.equipmentDict[equip] = None
        # self.equipmentDict = nmhr.cluster(self.equipmentDict, self.scene)

    def update_checkbox(self, checkstate = False):
        txt = self.lineEditFiltresActivities.text()
        print(txt)
        liste = []
        for key in filtres.sets:
            if txt.capitalize() in key:
                liste.append(key)
        for checkbox in self.checkBoxs:
            if checkbox.text() not in liste:
                checkbox.setHidden(True)
            else:
                checkbox.setHidden(False)
        if checkstate is True:
            check = not self.checkBoxs[0].checkState()
            for checkbox in self.checkBoxs:
                if checkbox.isHidden() is False and check is True:
                    checkbox.setCheckState(Qt.Checked)
                    self.boxChecked.append(checkbox)
                if checkbox.isHidden() is False and check is False:
                    checkbox.setCheckState(Qt.Unchecked)
                    self.boxChecked.remove(checkbox)
        self.update_affichage_equipements()

    def changeaff(self):
        for (equip, point) in self.equipmentDict.items():
            equip.affiche = not equip.affiche

    def addcheckbox(self):
        self.listActivities.clear()
        for name in sorted(filtres.sets):
            lwItem = QtGui.QListWidgetItem(name, self.listActivities)
            lwItem.setFlags(Qt.ItemIsEnabled)
            lwItem.setCheckState(Qt.Unchecked)
            self.checkBoxs.append(lwItem)

    def itemClicked(self, item):
        #print('item: ', item, ', state :', item.checkState(), ', acti :', item.text())
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
            self.boxChecked.remove(item)
            self.update_equipements(filtres.filtrer_set_par_acti(item.text()), False)
        else:
            item.setCheckState(Qt.Checked)
            self.boxChecked.append(item)
            self.update_equipements(filtres.filtrer_set_par_acti(item.text()), True)
        self.update_affichage_equipements()

    def affiche_addresse(self):
        """ affiche un point à l'addresse que l'utilisateur entre"""
        self.statusbar.showMessage("Recherche ...") #TODO n'a pas l'air de marcher ...
        txt = self.lineEdit.text()
        if self.ptRecherche != None:
            self.scene.removeItem(self.ptRecherche)
        coords = self.locator.find(txt,txt)
        print(coords)

        if self.arret != None:
            self.scene.removeItem(self.arret)
        if coords != None:
            self.ptRecherche = self.graphicsView.draw_point(coords[0], coords[1], QtGui.QPen(QtCore.Qt.black, 3), QtCore.Qt.yellow, 20, txt) #TODO faire un truc plus joli (avec une icone)
            (nomArret, latArret, lonArret) = tisseo.get_closest_sa(coords[0],coords[1])
            self.arret = self.graphicsView.draw_point(latArret,lonArret, QtGui.QPen(QtCore.Qt.blue, 3), QtCore.Qt.red, 20, nomArret) #TODO faire un truc plus joli (avec une icone)
        else:
            print("adresse non trouvée")
            self.statusbar.showMessage("adresse non trouvée")


    def notif_chrgmt_equip(self, infos):
        if infos[0]=='échec':
            self.statusbar.showMessage("Échec: {}       {}/{}".format(infos[1],infos[2],infos[3]),2000)
        if infos[0]=='cache':
            self.statusbar.showMessage('Chargement depuis le cache',2000)
        else:
            self.statusbar.showMessage("Adresse trouvée: {}       {}/{}".format(infos[0],infos[1],infos[2]),2000)

    def connections(self):
        self.scene.clusterisclicked.connect(self.nocover.explode)
        self.scene.equipointisclicked.connect(self.eclic)

    def eclic(self, equipoint):
        print(equipoint.equipment.name, 'has been clicked and the information has traveled with the speed of \nlight thanks to a SIGNAL')
