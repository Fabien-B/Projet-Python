from PyQt4.QtCore import pyqtSlot, Qt
from PyQt4.QtGui import QWidget, QListWidgetItem
from PyQt4 import QtCore, QtGui
from window import Ui_MainWindow
import carte
import filtres
import main
import poi
import No_More_Horse_Riding as nmhr


class Ihm(Ui_MainWindow):

    def __init__(self):
        super(Ihm, self).__init__()
        self.equipmentDict={}
        self.latitude = 43.564995   #latitude et longitudes de départ
        self.longitude = 1.481650
        self.checkstate = False
        self.checkBoxs = []
        self.boxChecked =[]

    def set_equipements(self,eqList):
        for eq in eqList:
            self.equipmentDict[eq] = None   #Mettre en valeur les Qellipses affichée, ou None si l'équipement n'est pas affiché.

    def built(self):
        self.build_map()
        self.pushButton.clicked.connect(self.selectall)
        self.lineEdit_1.textEdited.connect(self.update_checkbox)
        self.lw.itemClicked.connect(self.itemClicked)
        self.lineEdit.returnPressed.connect(self.affiche_addresse)
#        self.update_affichage_equipements()

    def build_map(self):
        self.graphicsView = carte.myQGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(290, 10, 700, 610))
        self.graphicsView.setObjectName("graphicsView")
        self.scene = QtGui.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setDragMode(QtGui.QGraphicsView.ScrollHandDrag) # allow drag and drop of the view
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)
        self.graphicsView.FinishInit()
        self.graphicsView.ihm = self
        self.graphicsView.download(self.latitude,self.longitude)
        self.addcheckbox()
    #pour obtenir les coordonnées GPS d'un point de la carte, appeler: self.graphicsView.get_gps_from_map(Xscene,Yscene) avec (Xscene,Yscene) les coordonnées du point dans la scène.
    #pour dessiner un point sur la carte appeler: self.graphicsView.draw_point(lat,lon [, legend = 'ma legende']), lat et lon étant la latitude et la longitude du point.
    # Retenir la Qellipse retournée (dans une variable) pour pouvoir l'effacer quand on veut.

    def update_affichage_equipements(self):
        actiChecked = set()
        for box in self.boxChecked:
            print(box.text())
        for box in self.boxChecked:
            actiChecked.add(box.text())
        print(actiChecked)
        for (equip, point) in self.equipmentDict.items():
            currentEquipActi = set()
            if equip.activities != None:
                for key in dict.keys(equip.activities):
                    currentEquipActi.add(key)
            #print('hop',currentEquipActi.intersection(actiChecked),currentEquipActi,actiChecked)
            if currentEquipActi.intersection(actiChecked) != set():
                if equip.affiche and point == None:
                    #self.equipmentDict[equip] = self.graphicsView.draw_point(equip.coords[0],equip.coords[1], legend=equip.name, equipment = equip)
                    self.equipmentDict[equip] = self.graphicsView.draw_equipment(equip)
                if not equip.affiche and point != None:
                    if type(point) is poi.Equipment_Group:
                        for equipoint in point.equipointlist:
                            self.equipmentDict[equipoint.equipment] = None
                    self.scene.removeItem(point)
                    self.equipmentDict[equip] = None
                    self.scene.update()
        # self.equipmentDict = nmhr.cluster(self.equipmentDict, self.scene)
        # self.scene.update()

    def update_checkbox(self, checkstate):
        txt = self.lineEdit_1.text()
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
        self.lw.clear()
        for name in sorted(filtres.sets):
            lwItem = QtGui.QListWidgetItem(name, self.lw)
            lwItem.setFlags(Qt.ItemIsEnabled)
            lwItem.setCheckState(Qt.Unchecked)
            self.checkBoxs.append(lwItem)

    def selectall(self):
        self.update_checkbox(True)

    def itemClicked(self, item):
        print('item: ', item, ', state :', item.checkState(), ', acti :', item.text())
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
            self.boxChecked.remove(item)
        else:
            item.setCheckState(Qt.Checked)
            self.boxChecked.append(item)
        self.update_affichage_equipements()

    def affiche_addresse(self):
        # affiche un point à l'addresse que l'utilisateur entre
        txt = self.lineEdit.text()
        coords = main.my_locator.find(txt)
        self.graphicsView.draw_point(coords[0], coords[1], QtGui.QPen(QtCore.Qt.black, 3), QtCore.Qt.yellow, 20, txt)
        print(txt)



