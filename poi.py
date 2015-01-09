from PyQt4 import QtCore, QtGui, QtNetwork
import carte
import os

class POI(QtGui.QGraphicsItemGroup):
    def __init__(self, Zvalue = 10):
        super(POI, self).__init__()
        self.setZValue(Zvalue)

class point(POI):
    def __init__(self, x, y, PEN = QtGui.QPen(QtCore.Qt.red, 2), BRUSH = QtCore.Qt.red, Zvalue = 10, legend='', equipment = None, lat=0, lon=0):
        super(point,self).__init__(Zvalue)
        self.PEN = PEN
        self.BRUSH = BRUSH
        self.equipment = equipment
        self.legend = legend
        self.coords = (lat,lon)

        self.ellipse = QtGui.QGraphicsEllipseItem()
        self.ellipse.setPen(PEN)
        self.ellipse.setBrush(BRUSH)
        self.ellipse.setRect(0, 0, 20, 20)
        self.ellipse.setPos(x, y)
        self.ellipse.setToolTip(self.legend)
        self.addToGroup(self.ellipse)


    def Pos(self):
        return(self.ellipse.pos().x(), self.ellipse.pos().y())

    def SetPos(self, x, y):
        self.ellipse.setPos(x, y)





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
            self.icone.scale(2/3, 2/3)
            self.addToGroup(self.icone)
        else:
            PEN = QtGui.QPen(QtCore.Qt.darkGreen, 2)
            self.icone = QtGui.QGraphicsEllipseItem()
            self.icone.setPen(PEN)
            self.icone.setBrush(QtCore.Qt.darkGreen)
            self.icone.setRect(0, 0, 20, 20)
            self.icone.setPos(x, y)
            self.icone.setToolTip(equipement.name)
            self.addToGroup(self.icone)


    def Pos(self):
        return(self.icone.pos().x(), self.icone.pos().y())

    def SetPos(self, x, y):
        self.icone.setPos(x, y)



    def mousePressEvent(self, QGraphicsSceneMouseEvent):
        QGraphicsSceneMouseEvent.accept()
        scene = self.scene()
        scene.equipclicked(self)

class Equipment_Group(point):

    def __init__(self, scene, x, y):
        super(Equipment_Group, self).__init__(x, y, PEN = QtGui.QPen(QtCore.Qt.red, 2), BRUSH = QtCore.Qt.red, Zvalue = 8, legend='', equipment = None)
        self.scene = scene
        self.equipointlist = []
        self.equipmentItemGroup = QtGui.QGraphicsItemGroup()
        self.text = None
        self.exploded = None

    def size(self):
        return len(self.equipointlist)

    def tooltiper(self):
        names = [point.equipment.name for point in self.equipointlist]
        self.setToolTip('\n'.join(names))

    def digitalize(self):
        self.text = QtGui.QGraphicsSimpleTextItem()
        self.text.setZValue(12)
        self.text.setBrush(QtCore.Qt.black)
        self.text.setText(str(self.size()))
        font = QtGui.QFont('Courier', 12, QtGui.QFont.Bold)
        self.text.setFont(font)
        textposx = self.Pos()[0]+self.boundingRect().width()/2-self.text.boundingRect().width()/2
        textposy = self.Pos()[1]+self.boundingRect().height()/2-self.text.boundingRect().height()/2
        self.text.setPos(textposx, textposy)
        self.addToGroup(self.text)

    def mousePressEvent(self, QGraphicsSceneMouseEvent):
        QGraphicsSceneMouseEvent.accept()
        self.scene.clusterclicked(self)

class BackGroundCluster(QtGui.QGraphicsItemGroup):
    def __init__(self, rayon, the_cluster):
        super(BackGroundCluster, self).__init__()
        self.the_cluster = the_cluster
        PEN = QtGui.QPen(QtCore.Qt.gray)
        self.background = QtGui.QGraphicsEllipseItem()
        self.background.setPen(PEN)
        self.background.setBrush(QtCore.Qt.gray)
        self.background.setRect(0, 0, rayon+30, rayon+30)
        self.background.setPos(the_cluster.Pos()[0]+12 - (rayon+30)/2, the_cluster.Pos()[1]+12 -(rayon+30)/2)
        self.background.setZValue(8)

    def mousePressEvent(self, QGraphicsSceneMouseEvent):
        QGraphicsSceneMouseEvent.accept()
        self.scene.bgclicked(self)
        print('bg')
