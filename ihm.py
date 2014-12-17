from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QWidget, QListWidgetItem
from window import Ui_MainWindow
import carte
from PyQt4 import QtCore, QtGui, QtNetwork


class Ihm(Ui_MainWindow):
    """ Widget displaying information about a Flight """

    def __init__(self):
        super(Ihm, self).__init__()
        self.equipmentDict={}
        self.latitude = 43.564995   #latitude et longitudes de départ
        self.longitude = 1.481650

    def set_equipements(self,eqList):
        for eq in eqList:
            self.equipmentDict[eq] = None   #Mettre en valeur les Qellipses affichée, ou None si l'équipement n'est pas affiché.

    def built(self):
        self.build_map()
        self.update_affichage_equipements()

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
        self.graphicsView.download(self.latitude,self.longitude)
    #pour obtenir les coordonnées GPS d'un point de la carte, appeler: self.graphicsView.get_gps_from_map(Xscene,Yscene) avec (Xscene,Yscene) les coordonnées du point dans la scène.
    #pour dessiner un point sur la carte appeler: self.graphicsView.draw_point(lat,lon), lat et lon étant la latitude et la longitude du point.
    # Retenir la Qellipse retournée (dans une variable) pour pouvoir l'effacer quand on veut.

    def update_affichage_equipements(self, eqList):
        dico = {}
        for eq in eqList:
            dico[eq] = [eq.coords] #Associe les équipements à leurs coordonnées réelles
        for points in dico:
            ellipse = self.graphicsView.draw_point(points[1][0], points[1][1])  #Dessine le point pour chaque équipement, et le conserve dans le dictionnaire
            points[1].append(ellipse)
            self.equipmentDict[points[1]] = 1
            # points[1].append(self.graphicsView.get_gps_from_map(ellipse.coords[0], ellipse.coords[1])) Pour ajouter a la liste les coords du point dans le scene

