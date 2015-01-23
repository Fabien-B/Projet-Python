from PyQt4 import QtCore, QtGui
import os


class Point(QtGui.QGraphicsItemGroup):
    """La classe parent de tout ce qui est un Point (ou une icone)"""
    def __init__(self, x, y, img='', PEN = QtGui.QPen(QtCore.Qt.red, 2), BRUSH = QtCore.Qt.red, Zvalue = 10, legend='', equipment = None, lat=0, lon=0, decx=0, decy=0):
        super(Point,self).__init__()
        self.equipment = equipment
        self.legend = legend
        self.coords = (lat, lon)
        self.setZValue(Zvalue)
        self.selected = False
        if equipment != None:

            nameImg = equipment.type.lower().split()[0]
            path = 'icones/' + nameImg + '.png'
            self.legend = equipment.name
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
            self.icone = QtGui.QGraphicsEllipseItem()
            self.icone.setPen(PEN)
            self.icone.setBrush(BRUSH)
            self.icone.setRect(0, 0, 20, 20)
            self.icone.setPos(x-10, y-10)
            txtToolTip = equipment.name if equipment != None else legend
            self.icone.setToolTip(txtToolTip)
            self.addToGroup(self.icone)




    def Pos(self):
        """Permet de renvoyer la position sous forme d'un tuple"""
        return(self.icone.pos().x(), self.icone.pos().y())

    def SetPos(self, x, y):
        self.icone.setPos(x, y)


class Equipement_point(Point):
    """La classe des points représentant des équipements"""
    def __init__(self,x,y, equipement=None, Zvalue = 10, img='', legend='',decx=0, decy=0):
        super(Equipement_point, self).__init__(x, y, img= img, legend= legend, decx = decx, decy = decy, equipment= equipement, Zvalue= Zvalue)

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
        """Retourne la taille du cluster"""
        return len(self.equipointlist)

    def tooltiper(self):
        """Paramètre l'info bulle"""
        names = [point.equipment.name for point in self.equipointlist]
        self.setToolTip('\n'.join(names))

    def digitalize(self):
        """Ecrit le nombre d'équipement contenu dans le cluster sur le cluster"""
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
        """Gère le clic sur un cluster"""
        if self.icone.isUnderMouse():
            QGraphicsSceneMouseEvent.accept()
            self.thescene.clusterclicked(self)


class BackGroundCluster(QtGui.QGraphicsEllipseItem):
    """La classe qui dessine, anime, gère le clic le background quand on explose un cluster"""
    def __init__(self, rayon, the_cluster, scene):
        super(BackGroundCluster, self).__init__(0, 0, rayon+30, rayon+30)
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
            """the class that will animate the opening
            Inspired by TD de QT ENAC"""
            def __init__(self, item):
                super(Adapter, self).__init__()
                self.item = item
            opening = QtCore.pyqtProperty(float,lambda s: s.item.boundingRect().height(), lambda s, v: s.item.makebig(v))


        anim = QtCore.QPropertyAnimation(Adapter(self), 'opening')
        anim.setDuration(200)
        anim.setStartValue(0)
        anim.setEndValue(rayon+30)
        anim.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        anim.start()
        self.anim = anim  # prevents GC to collect the anim instance

    def makebig(self, v):
        """Sert a faire grossir depuis le centre pour l'animation d'ouverture"""
        self.setPos(self.the_cluster.Pos()[0]+12 - v/2, self.the_cluster.Pos()[1]+12 -v/2)
        self.setRect(0,0,v,v)

    def mousePressEvent(self, QGraphicsSceneMouseEvent):
        """Gère le clic"""
        QGraphicsSceneMouseEvent.accept()
        self.thescene.bgclicked(self)


class SelectBackground(QtGui.QGraphicsEllipseItem):
    """La classe de l'icone de selection d'un equipement"""
    def __init__(self, equipoint):
        super(SelectBackground, self).__init__()
        self.equipoint = equipoint
        self.setZValue(equipoint.zValue()-1)
        equipwitdth = equipoint.boundingRect().width()
        equipheight = equipoint.boundingRect().height()
        width = equipwitdth + 10
        height = equipheight + 10
        self.setRect(0,0,width, height)
        self.setPos(equipoint.Pos()[0] - width/2 + equipwitdth/2, equipoint.Pos()[1] - height/2 + equipheight/2)
        self.setBrush(QtCore.Qt.darkBlue)

        class Adapter(QtCore.QObject):
            """the class that will animate the opacity
            Inspired by TD de QT ENAC"""
            def __init__(self, item):
                super(Adapter, self).__init__()
                self.item = item
            fading = QtCore.pyqtProperty(float,lambda s: s.item.opacity(), lambda s, v: s.item.setOpacity(v))

        anim = QtCore.QPropertyAnimation(Adapter(self), 'fading')
        anim.setDuration(2500)
        anim.setStartValue(0.4)
        anim.setKeyValueAt(0.5, 1)
        anim.setEndValue(0.4)
        anim.setLoopCount(-1)
        anim.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        anim.start()
        self.anim = anim
