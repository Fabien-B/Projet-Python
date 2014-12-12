from PyQt4 import QtCore, QtGui, QtNetwork
import math
import design

TILEDIM = 256
lcas=(44.98332, 1.71525,17)

BOURRIN = 1

class Carte(design.Ui_MainWindow):
    updated = QtCore.pyqtSignal(QtCore.QRect)
    def __init__(self):
        super(Carte, self).__init__()
        self.latitude = 43.56439
        self.longitude = 1.48267
        self.ZOOM = 14

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

        self.manager = QtNetwork.QNetworkAccessManager()
        cache = QtNetwork.QNetworkDiskCache()
        cache.setCacheDirectory(QtGui.QDesktopServices.storageLocation(QtGui.QDesktopServices.CacheLocation))
        self.manager.setCache(cache)
        self.manager.finished.connect(self.gererDonnees)

        self.test1.clicked.connect(lambda f: self.graphicsView.centerOn(8269*256+100, 5894*256) )
        self.pushButton.clicked.connect(lambda f: self.zoom(1.5))
        self.pushButtonZoomm.clicked.connect(lambda f: self.zoom(1/1.5))
        self.pushButtonPoint.clicked.connect(lambda f: self.draw_point(43.56736,1.47770))

        self.m_tilePixmaps = {}


    def finish(self):
        #self.download(43.56491, 1.47881)
        self.download(44.989, 1.699)
        (X,Y,resx,resy) = self.get_tile_nbs(43.56491, 1.47881)
        posX=X*TILEDIM + resx*TILEDIM
        posY=Y*TILEDIM + resy*TILEDIM
        self.graphicsView.centerOn(8269*256+100, 5894*256)
        #self.zoom(1/2)


    # une tuile fait 256 X 256 pixels
    def get_tile_nbs(self,lat,lon):
        zn = float(1 << self.ZOOM)
        tx = float(lon + 180.0) / 360.0
        ty = (1.0 - math.log(math.tan(lat * math.pi / 180.0) + 1.0 / math.cos(lat * math.pi / 180.0)) / math.pi) / 2.0
        X = int(tx * zn)
        Y = int(ty * zn)
        resX = tx * zn - X
        resY = ty * zn - Y
        print(X,Y)
        return (X,Y,resX,resY)

    def download(self,lat,lon):
        (X,Y,resx,resy) = self.get_tile_nbs(lat,lon)
        if BOURRIN:
            nbw = 50
            nbh = 50
        else:
            nbw=int(self.graphicsView.width()/TILEDIM)+1
            nbh=int(self.graphicsView.height()/TILEDIM)+1
        biw=int(-nbw/2)
        bih=int(-nbh/2)
        for i in range(biw,nbw+biw):
            for j in range(bih,bih+nbh):
                path = 'http://tile.openstreetmap.org/%d/%d/%d.png' % (self.ZOOM, X+i, Y+j)
                url = QtCore.QUrl(path)
                request = QtNetwork.QNetworkRequest()
                request.setUrl(url)
                request.setRawHeader('User-Agent', 'Une belle tuile')
                request.setAttribute(QtNetwork.QNetworkRequest.User, (X+i,Y+j,self.ZOOM,i,j))
                self.manager.get(request)

    def gererDonnees(self, reply):
        img = QtGui.QImage()
        tu = reply.request().attribute(QtNetwork.QNetworkRequest.User)
        url = reply.url()
        if not reply.error():
            if img.load(reply, None):
                self.m_tilePixmaps[tu] = QtGui.QPixmap.fromImage(img)
                tuile=self.scene.addPixmap(self.m_tilePixmaps[tu])
                #self.scene.addEllipse(tu[0]*TILEDIM, tu[1]*TILEDIM,50,50)
                tuile.setPos(tu[0]*TILEDIM,tu[1]*TILEDIM)
        reply.deleteLater()
    
    def draw_point(self,lat,lon, PEN = QtGui.QPen(QtCore.Qt.red, 2), BRUSH = QtCore.Qt.red):
        dlon=360/(1 << self.ZOOM)
        (X,Y,resX,resY)=self.get_tile_nbs(lat,lon)
        posX=X*TILEDIM + resX*TILEDIM
        posY=Y*TILEDIM + resY*TILEDIM
        self.scene.addEllipse(posX, posY,20,20,PEN,BRUSH)


    def zoom(self,factor):
        self.graphicsView.scale(factor,factor)



class myQGraphicsView(QtGui.QGraphicsView):
    def __init__(self,parent):
        super(myQGraphicsView, self).__init__(parent)

    def wheelEvent(self,e):
        x=e.x()
        y=e.y()
        a=self.mapToScene(x,y)
        self.centerOn(a.x(),a.y())
        print(a.x(),a.y())
        if e.delta() > 0 :
            self.scale(1.5,1.5)
        else:
            self.scale(1/1.5,1/1.5)
        self.translate(1,1)


