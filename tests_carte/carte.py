from PyQt4 import QtCore, QtGui, QtNetwork
import math
import os
import design

TILEDIM = 256
lcas=(44.98332, 1.71525,17)

BOURRIN = 0

class Carte(design.Ui_MainWindow):
    updated = QtCore.pyqtSignal(QtCore.QRect)
    def __init__(self):
        super(Carte, self).__init__()
        self.latitude = 44.98347
        self.longitude = 1.71482

    def build(self):
        self.graphicsView=myQGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        self.scene = QtGui.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setDragMode(QtGui.QGraphicsView.ScrollHandDrag) # allow drag and drop of the view
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff);
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff);
        self.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)
        self.graphicsView.FinishInit()

#DEBUG
        self.test1.clicked.connect(lambda f: self.graphicsView.centerOnPosition(44.98347,1.71482) )
        self.test2.clicked.connect(self.graphicsView.debug)
        self.pushButton.clicked.connect(lambda f: self.graphicsView.zoom(1.5))
        self.pushButtonZoomm.clicked.connect(lambda f: self.graphicsView.zoom(1/1.5))
        self.pushButtonPoint.clicked.connect(lambda f: self.graphicsView.draw_point(44.98347,1.71482))
# END DEBUG

    def finish(self):
        self.graphicsView.download(self.latitude,self.longitude)





class myQGraphicsView(QtGui.QGraphicsView):
    def __init__(self,parent):
        super(myQGraphicsView, self).__init__(parent)
        self.x=0
        self.y=0

    def FinishInit(self):
        self.maScene = self.scene()
        self.ZOOM = 13
        self.manager = QtNetwork.QNetworkAccessManager()
        cache = QtNetwork.QNetworkDiskCache()
        cache.setCacheDirectory(QtGui.QDesktopServices.storageLocation(QtGui.QDesktopServices.CacheLocation))
        self.manager.setCache(cache)
        self.manager.finished.connect(self.gererDonnees)
        self.m_tilePixmaps = {}

    def wheelEvent(self,e):
        print("WHEEL")
        for zoom in self.m_tilePixmaps:                 #on remet tous les indicateurs d'affichages à 0
            for cle in self.m_tilePixmaps[zoom]:
                self.m_tilePixmaps[zoom][cle][1] = 0
        self.maScene.clear()                            #et on efface tout
        x=e.x()     #on regarde à peu près ou on est
        y=e.y()
        a=self.mapToScene(x,y) #dans les coordonnéées de scène...
        print(self.get_tile_nbs(44.989, 1.699))
        if e.delta() > 0 :
            self.ZOOM += 1
        else:
            self.ZOOM -= 1
        print(self.ZOOM)
       # self.download(44.989, 1.699)
        #self.centerOn(8269*TILEDIM,2947*TILEDIM)
        print('poss = ',a.x()/256,a.y()/256)
        NX=int(a.x()/2)
        NY=int(a.y()/2)
        print('NX,NY = ',NX,NY, '-----',NX/256,NY/256)
        self.centerOn(NX,NY)
        rect = self.sceneRect()
        print('le rectangle: ',rect.x()/256,rect.y()/256)
        mon_rect=QtCore.QRectF(NX,NY,self.width(),self.height())
        self.setSceneRect(mon_rect)
        self.update_tiles()
        print(self.get_tile_nbs(44.989, 1.699))

    def mouseMoveEvent(self, e):
        super().mouseMoveEvent(e)
        self.update_tiles()

    def mouseDoubleClickEvent(self, e):
        #print("Double Click")
        x=e.x()
        y=e.y()
        a=self.mapToScene(x,y)
        (X,Y,_,_) = self.get_tile_nbs(44.989, 1.699)
        self.centerOn(X*256+100,Y*256)
        #self.update_tiles()


    def zoom(self,factor):
        self.scale(factor,factor)

    def draw_point(self,lat,lon, PEN = QtGui.QPen(QtCore.Qt.red, 2), BRUSH = QtCore.Qt.red):
        (X,Y,resX,resY)=self.get_tile_nbs(lat,lon)
        posX=X*TILEDIM + resX*TILEDIM
        posY=Y*TILEDIM + resY*TILEDIM
        el = self.maScene.addEllipse(posX, posY,20,20,PEN,BRUSH)
        print("point === ", el.scenePos())

    def centerOnPosition(self,lat,lon):
        (X,Y,resX,resY)=self.get_tile_nbs(lat,lon)
        posX=X*TILEDIM + resX*TILEDIM
        posY=Y*TILEDIM + resY*TILEDIM
        self.centerOn(posX,posY)

    def get_tile_nbs(self,lat,lon):
        #print("Get Tiles")
        zn = float(1 << self.ZOOM)
        tx = float(lon + 180.0) / 360.0
        latrad=lat * math.pi / 180.0
        ty =  0.5 - (0.5/math.pi)*math.log(math.tan(latrad) + 1.0 / math.cos(latrad))
        X = int(tx * zn)
        Y = int(ty * zn)
        resX = tx * zn - X
        resY = ty * zn - Y
        print('get tile',X,Y)
        return (X,Y,resX,resY)

    def download(self,lat,lon):
        #print("DL")
        (X,Y,resx,resy) = self.get_tile_nbs(lat,lon)
        if BOURRIN:
            nbw = 50
            nbh = 50
        else:
            nbw=int(self.width()/TILEDIM)+1
            nbh=int(self.height()/TILEDIM)+1
        biw=int(-nbw/2)
        bih=int(-nbh/2)
        for i in range(biw,nbw+biw):
            for j in range(bih,bih+nbh):
                self.add_tile(X+i,Y+j)

    def add_tile(self,X,Y):
        name='/home/fabien/cache_Images/' + str((X,Y,self.ZOOM)) + '.png'
        if not os.path.exists(name):
            path = 'http://tile.openstreetmap.org/%d/%d/%d.png' % (self.ZOOM, X, Y)
            url = QtCore.QUrl(path)
            request = QtNetwork.QNetworkRequest()
            request.setUrl(url)
            print(url,self.ZOOM,X,Y)
            request.setRawHeader('User-Agent', 'Une belle tuile')
            request.setAttribute(QtNetwork.QNetworkRequest.User, (X,Y,self.ZOOM))
            self.manager.get(request)
        else:
            #print("loaded from disk")
            self.load_tile_from_disk((X,Y,self.ZOOM))

    def gererDonnees(self, reply):
        if self.ZOOM not in self.m_tilePixmaps:
            self.m_tilePixmaps[self.ZOOM]={}
        cle = reply.request().attribute(QtNetwork.QNetworkRequest.User)
        if not reply.error():
            name='/home/fabien/cache_Images/' + str(cle) + '.png'
            file = QtCore.QFile(name)
            file.open(QtCore.QIODevice.WriteOnly)
            file.write(reply.readAll())
            file.close()
            reply.deleteLater()
            self.load_tile_from_disk(cle)

    def load_tile_from_disk(self,cle):
        img = QtGui.QImage()
        name='/home/fabien/cache_Images/' + str(cle) + '.png'
        img.load(name)
        if self.ZOOM not in self.m_tilePixmaps:
            self.m_tilePixmaps[self.ZOOM]={}
        self.m_tilePixmaps[self.ZOOM][cle] = [QtGui.QPixmap.fromImage(img),0]
        self.afficher_tuile(cle)


    def afficher_tuile(self,cle):
        if self.m_tilePixmaps[self.ZOOM][cle][1] == 0:
            (X,Y,ZOOM) = cle
            tuile=self.maScene.addPixmap(self.m_tilePixmaps[ZOOM][cle][0])
            self.m_tilePixmaps[ZOOM][cle][1] = 1
            tuile.setPos(X*TILEDIM,Y*TILEDIM)


    def update_tiles(self):
        if self.ZOOM not in self.m_tilePixmaps:
            self.m_tilePixmaps[self.ZOOM]={}
        pos1=self.mapToScene(0,0)
        pos2=self.mapToScene(self.width(),self.height())
        X1=int(pos1.x()/TILEDIM)
        X2=int(pos2.x()/TILEDIM)
        Y1=int(pos1.y()/TILEDIM)
        Y2=int(pos2.y()/TILEDIM)
        for i in range(X1-1,X2+1):
            for j in range(Y1-1,Y2+1):
                cle=(i,j,self.ZOOM)
                if cle not in self.m_tilePixmaps[self.ZOOM]:    #si la cle n'est pas en mémoire, on essaie de la charger du disque, ou on la télecharge
                    self.add_tile(i,j)
                else:
                    self.afficher_tuile(cle)    #sinon (la clé est en mémoire): on l'affiche (controle si déja dans la scene dans la fonction)




    def debug(self):
        print("Debug")
        self.centerOn(2067*TILEDIM,1473*TILEDIM)
        rect = self.sceneRect()
        print('le rectangle: ',rect.x(),rect.y())