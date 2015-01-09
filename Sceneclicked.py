from PyQt4 import QtGui, QtCore
import poi
import os

class SceneClickable(QtGui.QGraphicsScene):

    clusterisclicked = QtCore.pyqtSignal(poi.Equipment_Group)
    equipointisclicked = QtCore.pyqtSignal(poi.equipement_point)

    def __init__(self):
        super(SceneClickable, self).__init__()

    def clusterclicked(self, cluster):
        self.clusterisclicked.emit(cluster)

    def equipclicked(self, equipoint):
        self.equipointisclicked.emit(equipoint)
