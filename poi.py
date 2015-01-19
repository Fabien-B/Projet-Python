from PyQt4 import QtCore, QtGui, QtNetwork
import carte
import os


class POI(QtGui.QGraphicsItemGroup):
    def __init__(self, Zvalue = 10):
        super(POI, self).__init__()
        self.setZValue(Zvalue)


class Point(POI):
    def __init__(self, x, y, img='', PEN = QtGui.QPen(QtCore.Qt.red, 2), BRUSH = QtCore.Qt.red, Zvalue = 10, legend='', equipment = None, lat=0, lon=0, decx=0, decy=0):
        super(Point,self).__init__(Zvalue)
        self.equipment = equipment
        self.legend = legend
        self.coords = (lat, lon)

        path = 'icones/' + img + '.png'
        if os.path.exists(path):
            self.icone = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(path))
            self.icone.setToolTip(self.legend)
            if path == 'icones/vous_etes_ici.png':
                self.icone.scale(1/8, 1/8)
            else:
                self.icone.scale(2/3, 2/3)
            self.icone.setPos(x+decx,y+decy)
            self.addToGroup(self.icone)
        else:
            self.PEN = PEN
            self.BRUSH = BRUSH
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


class Equipement_point(POI):
    def __init__(self,x,y, equipement=None, Zvalue = 10, img='', legend='',decx=0, decy=0):
        super(Equipement_point, self).__init__(Zvalue)
        self.equipment = equipement
        self.legend = legend
        if equipement != None:
            nameImg = equipement.type.lower().split()[0]
            path = 'icones/' + nameImg + '.png'
            self.legend = equipement.name
        else:
            path = 'icones/' + img + '.png'
        if os.path.exists(path):
            self.icone = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(path))
            self.icone.setToolTip(self.legend)
            if path == 'icones/vous_etes_ici.png':
                self.icone.scale(1/8, 1/8)
            else:
                self.icone.scale(2/3, 2/3)
            self.icone.setPos(x+decx,y+decy)
            self.addToGroup(self.icone)
        else:
            PEN = QtGui.QPen(QtCore.Qt.darkGreen, 2)
            self.icone = QtGui.QGraphicsEllipseItem()
            self.icone.setPen(PEN)
            self.icone.setBrush(QtCore.Qt.darkGreen)
            self.icone.setRect(0, 0, 20, 20)
            self.icone.setPos(x-10, y-10)
            txtToolTip = equipement.name if equipement != None else legend
            self.icone.setToolTip(txtToolTip)
            self.addToGroup(self.icone)

    def Pos(self):
        return(self.icone.pos().x(), self.icone.pos().y())

    def SetPos(self, x, y):
        self.icone.setPos(x, y)

    def mousePressEvent(self, QGraphicsSceneMouseEvent):
        QGraphicsSceneMouseEvent.accept()
        scene = self.scene()
        if self.icone.isUnderMouse():
            scene.equipclicked(self)


class Equipment_Group(Point):
    """La classe qui dessine, compte le nombre d'équipement, affiche le nombre, gère le clic des cluster (fermés)"""
    def __init__(self, scene, x, y):
        super(Equipment_Group, self).__init__(x, y, PEN = QtGui.QPen(QtCore.Qt.red, 2), BRUSH = QtCore.Qt.red, Zvalue = 11, legend='', equipment = None)
        self.thescene = scene
        self.equipointlist = []
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
        if self.ellipse.isUnderMouse():
            QGraphicsSceneMouseEvent.accept()
            self.thescene.clusterclicked(self)


class BackGroundCluster(QtGui.QGraphicsEllipseItem):
    """La classe qui dessine, anime, gère le clic le background quand on explose un cluster"""
    def __init__(self, rayon, the_cluster, scene):
        super(BackGroundCluster, self).__init__(0, 0, rayon+30, rayon+30)
        self.setTransformOriginPoint(the_cluster.Pos()[0]+12 + (rayon+30)/2,the_cluster.Pos()[1]+12 +(rayon+30)/2)
        self.thescene = scene
        self.rayon = rayon+30
        self.equippointlist = []
        self.the_cluster = the_cluster
        self.setPen(QtGui.QPen(QtCore.Qt.black, 2))
        self.setBrush(QtCore.Qt.red)
        self.setZValue(13)
        self.setOpacity(0.8)
        self.thescene.addItem(self)

        class Adapter(QtCore.QObject):
            """the class that will animate the opacity
            Inspired by TD de QT ENAC"""
            def __init__(self, item):
                super(Adapter, self).__init__()
                self.item = item
            opening = QtCore.pyqtProperty(float,lambda s: s.item.boundingRect().height(), lambda s, v: s.item.makebig(v))


        anim = QtCore.QPropertyAnimation(Adapter(self), 'opening')
        anim.setDuration(200)
        anim.setStartValue(0)
        anim.setKeyValueAt(0.5, 1)
        anim.setEndValue(rayon+30)
        anim.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        anim.start()
        self.anim = anim  # prevents GC to collect the anim instance

    def makebig(self, v):
        self.setPos(self.the_cluster.Pos()[0]+12 - v/2, self.the_cluster.Pos()[1]+12 -v/2)
        self.setRect(0,0,v,v)

    def mousePressEvent(self, QGraphicsSceneMouseEvent):
        QGraphicsSceneMouseEvent.accept()
        self.thescene.bgclicked(self)
