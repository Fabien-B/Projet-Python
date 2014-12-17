from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QWidget, QListWidgetItem

from window import Ui_MainWindow
import carte
from PyQt4 import QtCore, QtGui, QtNetwork


class Ihm(Ui_MainWindow):
    """ Widget displaying information about a Flight """

    def __init__(self):
        super(Ihm, self).__init__()
        self.latitude = 43.564995   #latitude et longitudes de départ
        self.longitude = 1.481650

    def built(self):
        self.build_map()
        print('coucou')

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
#pour dessiner un point sur la carte appeler: self.graphicsView.draw_point(lat,lon), lat et lon étant la latitude et la longitude du point
