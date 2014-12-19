from PyQt4 import QtCore, QtGui, QtNetwork
import carte

class POI(QtGui.QGraphicsItemGroup):
    def __init__(self, Zvalue = 10):
        super(POI, self).__init__()
        self.setZValue(Zvalue)

class point(POI):
    def __init__(self, x, y, PEN = QtGui.QPen(QtCore.Qt.red, 2), BRUSH = QtCore.Qt.red, Zvalue = 10, legend=''):
        super(point,self).__init__(Zvalue)
        self.PEN = PEN
        self.BRUSH = BRUSH

        self.ellipse = QtGui.QGraphicsEllipseItem()
        self.ellipse.setPen(PEN)
        self.ellipse.setBrush(BRUSH)
        self.ellipse.setRect(x, y, 20, 20)
        self.ellipse.setToolTip(legend)
        self.addToGroup(self.ellipse)



class equipement_point(POI):
    def __init__(self,equipement):
        pass #TODO on affichera ici l'icone correspondant à l'équipement