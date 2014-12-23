from PyQt4 import QtCore, QtGui, QtNetwork
import carte
import os

class POI(QtGui.QGraphicsItemGroup):
    def __init__(self, Zvalue = 10):
        super(POI, self).__init__()
        self.setZValue(Zvalue)

class point(POI):
    def __init__(self, x, y, PEN = QtGui.QPen(QtCore.Qt.red, 2), BRUSH = QtCore.Qt.red, Zvalue = 10, legend='', equipment = None):
        super(point,self).__init__(Zvalue)
        self.PEN = PEN
        self.BRUSH = BRUSH
        self.equipment = equipment

        self.ellipse = QtGui.QGraphicsEllipseItem()
        self.ellipse.setPen(PEN)
        self.ellipse.setBrush(BRUSH)
        self.ellipse.setRect(0, 0, 20, 20)
        self.ellipse.setPos(x, y)
        self.ellipse.setToolTip(legend)
        self.addToGroup(self.ellipse)

    def mousePressEvent(self, QGraphicsSceneMouseEvent):
        QGraphicsSceneMouseEvent.accept()
        print(self.equipment.name, self.equipment.coords)




class equipement_point(POI):
    def __init__(self,equipement,x,y, Zvalue = 10):
        super(equipement_point,self).__init__(Zvalue)
        self.equipment = equipement
        #print(equipement.type)

        path = 'icones/' + equipement.type.lower() + '.png'
        if os.path.exists(path):
            self.icone = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(path))
            self.icone.setPos(x,y)
            self.icone.setToolTip(equipement.name)
            self.addToGroup(self.icone)
        else:
            PEN = QtGui.QPen(QtCore.Qt.darkGreen, 2)
            self.ellipse = QtGui.QGraphicsEllipseItem()
            self.ellipse.setPen(PEN)
            self.ellipse.setBrush(QtCore.Qt.darkGreen)
            self.ellipse.setRect(0, 0, 20, 20)
            self.ellipse.setPos(x, y)
            self.ellipse.setToolTip(equipement.name)
            self.addToGroup(self.ellipse)

    def mousePressEvent(self, QGraphicsSceneMouseEvent):
        QGraphicsSceneMouseEvent.accept()
        print(self.equipment.name, self.equipment.coords, self.icone.pos().x())
