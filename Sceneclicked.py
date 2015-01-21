from PyQt4 import QtGui, QtCore
import poi
import os

class SceneClickable(QtGui.QGraphicsScene):
    """Version de la scène qui envoie des signaux"""
    clusterisclicked = QtCore.pyqtSignal(poi.Equipment_Group)
    equipointisclicked = QtCore.pyqtSignal(poi.Equipement_point)
    backgroundclicked = QtCore.pyqtSignal(poi.BackGroundCluster)
    giveEqCoordsSignal = QtCore.pyqtSignal(tuple)

    def __init__(self):
        super(SceneClickable, self).__init__()
        self.selectbackground = None

    def clusterclicked(self, cluster):
        """Si un cluster est cliké envoyer un signal"""
        self.clusterisclicked.emit(cluster)

    def equipclicked(self, equipoint):
        self.equipointisclicked.emit(equipoint)
        if equipoint.equipment:
            self.giveEqCoordsSignal.emit(equipoint.equipment.coords)
        self.draw_back_equip_select(equipoint)

    def draw_back_equip_select(self, equipoint):
        equipoint.selected = True
        if self.selectbackground:
            self.removeItem(self.selectbackground)
        self.selectbackground = poi.SelectBackground(equipoint)
        self.addItem(self.selectbackground)

    def bgclicked(self, background):
        self.backgroundclicked.emit(background)
