from PyQt4.QtCore import pyqtSlot, Qt
from PyQt4.QtGui import QWidget, QListWidgetItem
from PyQt4 import QtCore, QtGui
from window import Ui_MainWindow
import carte
import filtres
import No_More_Horse_Riding as nmhr


class Ihm(Ui_MainWindow):

    def __init__(self):
        super(Ihm, self).__init__()
        self.equipmentDict={}
        self.latitude = 43.564995   #latitude et longitudes de départ
        self.longitude = 1.481650
        self.checkstate = False

    def set_equipements(self,eqList):
        for eq in eqList:
            self.equipmentDict[eq] = None   #Mettre en valeur les Qellipses affichée, ou None si l'équipement n'est pas affiché.

    def built(self):
        self.build_map()
        self.pushButton.clicked.connect(self.selectall)
        self.lineEdit_1.textEdited.connect(self.update_checkbox)
        self.lw.itemClicked.connect(self.itemClicked)
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
        self.update_checkbox()
    #pour obtenir les coordonnées GPS d'un point de la carte, appeler: self.graphicsView.get_gps_from_map(Xscene,Yscene) avec (Xscene,Yscene) les coordonnées du point dans la scène.
    #pour dessiner un point sur la carte appeler: self.graphicsView.draw_point(lat,lon [, legend = 'ma legende']), lat et lon étant la latitude et la longitude du point.
    # Retenir la Qellipse retournée (dans une variable) pour pouvoir l'effacer quand on veut.

    def update_affichage_equipements(self):
        for (equip, point) in self.equipmentDict.items():
            if equip.affiche and point == None:
                #self.equipmentDict[equip] = self.graphicsView.draw_point(equip.coords[0],equip.coords[1], legend=equip.name, equipment = equip)
                self.equipmentDict[equip] = self.graphicsView.draw_equipment(equip)
            if not equip.affiche and point != None:
                self.scene.removeItem(point)
                self.equipmentDict[equip]=None
                self.scene.update()
        # nmhr.repulse(self.equipmentDict, self.scene)
        # self.scene.update()

    def update_checkbox(self):
        txt = self.lineEdit_1.text()
        print(txt)
        self.addcheckbox(txt, self.checkstate)

    def changeaff(self):
        for (equip, point) in self.equipmentDict.items():
            equip.affiche = not equip.affiche

    def addcheckbox(self, search, checkstate):
        self.lw.clear()
        liste = []
        for key in filtres.sets:
            if search.capitalize() in key:
                liste.append(key)
        if search != ['']:
            for name in sorted(filtres.sets.intersection(liste)):
                lwItem = QtGui.QListWidgetItem(name, self.lw)
                lwItem.setFlags(Qt.ItemIsEnabled)
                if checkstate == 0:
                    lwItem.setCheckState(Qt.Unchecked)
                else:
                    lwItem.setCheckState(Qt.Checked)
        else:
            for name in sorted(filtres.sets):
                lwItem = QtGui.QListWidgetItem(name, self.lw)
                lwItem.setFlags(Qt.ItemIsEnabled)
                if checkstate == 0:
                    lwItem.setCheckState(Qt.Unchecked)
                else:
                    lwItem.setCheckState(Qt.Checked)

    def selectall(self):
        self.checkstate = not self.checkstate
        print(self.checkstate)
        self.update_checkbox()

    def itemClicked(self, item):
        print('item: ', item, ', state :', item.checkState(), ', acti :', item.text())
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)








