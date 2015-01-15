from PyQt4 import QtCore, QtGui, QtNetwork
import math
import poi
import os

TILEDIM = 256

class myQGraphicsView(QtGui.QGraphicsView):
    def __init__(self, parent):
        super(myQGraphicsView, self).__init__(parent)
        self.ZOOM_INIT = 14  #attention:Ne pas le modifier
        self.ZOOM = self.ZOOM_INIT  #attention: ce zoom correspond au niveau de zoom des tuiles OSM. Aucun rapport avec le zoom molette.
        self.cur_zoom = 1
        self.x = 0
        self.y = 0
        self.setTransformationAnchor(2)
        self.ZoomMode = 0
        # en attendant que le zoom fonctionne bien
        self.latitude = 43.564995
        self.longitude = 1.481650

    def FinishInit(self):
        """fini l'initialisation """
        if not os.path.exists('.cache_Images/'):
            os.makedirs('.cache_Images/')
        self.maScene = self.scene()
        self.manager = QtNetwork.QNetworkAccessManager()
        cache = QtNetwork.QNetworkDiskCache()
        cache.setCacheDirectory(QtGui.QDesktopServices.storageLocation(QtGui.QDesktopServices.CacheLocation))
        self.manager.setCache(cache)
        self.manager.finished.connect(self.gererDonnees)
        self.m_tilePixmaps = {}

    def wheelEvent(self, e):
        """Zoom sur la carte """
        if self.ZoomMode:
            if e.delta() > 0:
                if self.ZOOM < 16:
                    self.ZOOM += 1
                    self.centerOnPosition(self.latitude, self.longitude)
            else:
                if self.ZOOM > 13:
                    self.ZOOM -= 1
                    self.centerOnPosition(self.latitude, self.longitude)
        else:
            if e.delta() > 0:
                if self.cur_zoom < 2:
                    self.zoom(1.1)
            else:
                if self.cur_zoom > 0.4:
                    self.zoom(1/1.1)
        self.update_tiles()

    def mouseMoveEvent(self, e):
        """ met à jour les tuiles à afficher quand on déplace la carte"""
        super().mouseMoveEvent(e)
        self.update_tiles()

    def mouseDoubleClickEvent(self, QMouseEvent):
        print(QMouseEvent.x(),QMouseEvent.y())
        print(self.get_gps_from_map(QMouseEvent.x(),QMouseEvent.y()))

    def zoom(self, factor):
        """zoom du facteur 'factor'"""
        self.cur_zoom *= factor
        self.scale(factor, factor)

    def draw_point(self, lat, lon, PEN = QtGui.QPen(QtCore.Qt.red, 2), BRUSH = QtCore.Qt.red, Zvalue = 10,  legend=''):
        """affiche un point aux coordonnées lat, lon."""
        (X, Y, resX, resY)=self.get_tile_nbs(lat, lon)
        posX = (X + resX)*TILEDIM
        posY = (Y + resY)*TILEDIM
        point = poi.point(posX,posY, PEN, BRUSH, legend=legend, lat=lat, lon=lon)
        self.maScene.addItem(point)
        return point

    def draw_equipment(self, equipment, Zvalue = 10):
        try:
            lat = equipment.coords[0]
            lon = equipment.coords[1]
        except TypeError:
            lat = 0
            lon = 0
            print("Erreur d'importation coordonnées ")
        (X, Y, resX, resY) = self.get_tile_nbs(lat, lon)
        posX = (X + resX)*TILEDIM
        posY = (Y + resY)*TILEDIM
        if lat < 43.7 and lat > 43.5 and lon < 1.6 and lon > 1.3:
            point = poi.equipement_point(posX, posY, equipment, Zvalue)
            self.maScene.addItem(point)
            return point

    def draw_img_point(self,lat,lon, img,legend=''):
        (X, Y, resX, resY)=self.get_tile_nbs(lat, lon)
        posX = (X + resX)*TILEDIM
        posY = (Y + resY)*TILEDIM
        point = poi.equipement_point(posX, posY, img=img, legend=legend)
        self.maScene.addItem(point)
        return point

    def centerOnPosition(self, lat, lon):
        """centre la carte sur la position définie par une latitude et une longitude"""
        #TODO : à refaire avec des self.setSceneRect()
        (X, Y, resX, resY)=self.get_tile_nbs(lat, lon)
        posX = (X + resX) * TILEDIM
        posY = (Y + resY) * TILEDIM
        self.centerOn(posX, posY)

    def get_tile_nbs(self, lat, lon):
        """prend en argument une latitude et une longitude, retoune (X,Y,resX,resY) ou:
        X et Y sont les parties entières (coordonnée de la tuile sur OSM)
        resX et resY les parties décimales, utiles pour positionner correctement un point sur la carte
        les coordonnées scènes du point sont: ((X + resX)*TILEDIM, (Y + resY)*TILEDIM)"""
        zn = float(1 << self.ZOOM)
        tx = float(lon + 180.0) / 360.0
        latrad = lat * math.pi / 180.0
        ty = 0.5 - (0.5/math.pi)*math.log(math.tan(latrad) + 1.0 / math.cos(latrad))
        X = int(tx * zn)
        Y = int(ty * zn)
        resX = tx * zn - X
        resY = ty * zn - Y
        return (X, Y, resX, resY)

    def get_gps_from_map(self, Xscene, Yscene):
        """prend en argument des coordonnées scènes, retourne la latitude et la longitude correspondantes"""
        X = Xscene / TILEDIM
        Y = Yscene / TILEDIM
        zn = float(1 << self.ZOOM)
        lon = X * 360 / zn - 180
        A = math.exp(2 * math.pi * (0.5 - Y / zn))
        lat = math.atan((A ** 2 - 1)/(2 * A))
        lat = lat * 180 / math.pi
        return (lat, lon)

    def download(self, lat, lon):
        """télécharge toutes le tuiles autour d'une position donnée (en fonction des dimensions de la graphicsView) """
        (X, Y, resx, resy) = self.get_tile_nbs(lat, lon)
        #nbw = int(self.width() / TILEDIM) + 1
        #nbh = int(self.height() / TILEDIM) + 1
        nbw = 3
        nbh = 3
        biw = int(-nbw / 2)
        bih = int(-nbh / 2)
        for i in range(biw, nbw + biw):
            for j in range(bih, bih + nbh):
                self.add_tile(X + i, Y + j)

    def add_tile(self, X, Y):
        """charge une tuile depuis le dique si elle existe, ou va la télécharger"""
        name='.cache_Images/' + str((X, Y, self.ZOOM)) + '.png'
        #  X < int(8270*2**(self.ZOOM-self.ZOOM_INIT)) and Y < int(6000*2**(self.ZOOM-self.ZOOM_INIT)) and X > int(8250*2**(self.ZOOM-self.ZOOM_INIT)) and Y > int(5970*2**(self.ZOOM-self.ZOOM_INIT)):
        if not os.path.exists(name):
            path = 'http://tile.openstreetmap.org/%d/%d/%d.png' % (self.ZOOM, X, Y)
            url = QtCore.QUrl(path)
            request = QtNetwork.QNetworkRequest()
            request.setUrl(url)
            print(url, self.ZOOM, X, Y, self.manager.proxy().hostName())
            request.setRawHeader('User-Agent', 'Une belle tuile')
            request.setAttribute(QtNetwork.QNetworkRequest.User, (X, Y, self.ZOOM))
            self.manager.get(request)
        else:
            self.load_tile_from_disk((X, Y, self.ZOOM))


    def gererDonnees(self, reply):
        """réceptionne l'image téléchargée, l'enregistre sur le disque, puis l'affiche"""
        if self.ZOOM not in self.m_tilePixmaps:
            self.m_tilePixmaps[self.ZOOM]={}
        cle = reply.request().attribute(QtNetwork.QNetworkRequest.User)
        if not reply.error():
            name = '.cache_Images/' + str(cle) + '.png'
            file = QtCore.QFile(name)
            file.open(QtCore.QIODevice.WriteOnly)
            file.write(reply.readAll())
            file.close()
            reply.deleteLater()
            self.load_tile_from_disk(cle)

    def load_tile_from_disk(self, cle):
        """charge une tuile depuis le disque dur et l'affiche"""
        img = QtGui.QImage()
        name = '.cache_Images/' + str(cle) + '.png'
        img.load(name)
        if self.ZOOM not in self.m_tilePixmaps:
            self.m_tilePixmaps[self.ZOOM]={}
        self.m_tilePixmaps[self.ZOOM][cle] = [QtGui.QPixmap.fromImage(img), 0]
        self.afficher_tuile(cle)

    def afficher_tuile(self, cle):
        """ajoute une tuile à la scène"""
        if self.m_tilePixmaps[self.ZOOM][cle][1] == 0:
            (X, Y, ZOOM) = cle
            tuile = self.maScene.addPixmap(self.m_tilePixmaps[ZOOM][cle][0])
            self.m_tilePixmaps[ZOOM][cle][1] = 1
            tuile.setPos(X*TILEDIM, Y*TILEDIM)

    def update_tiles(self):
        """affiche les tuiles nécessaires, en les prenant depuis la mémoire, le disque ou internet"""
        if self.ZOOM not in self.m_tilePixmaps:
            self.m_tilePixmaps[self.ZOOM] = {}
        pos1 = self.mapToScene(0, 0)
        pos2 = self.mapToScene(self.width(), self.height())
        X1 = int(pos1.x()/TILEDIM*2**(self.ZOOM-self.ZOOM_INIT))
        X2 = int(pos2.x()/TILEDIM*2**(self.ZOOM-self.ZOOM_INIT))
        Y1 = int(pos1.y()/TILEDIM*2**(self.ZOOM-self.ZOOM_INIT))
        Y2 = int(pos2.y()/TILEDIM*2**(self.ZOOM-self.ZOOM_INIT))
        for i in range(X1-2, X2+3):
            for j in range(Y1-2, Y2+3):
                cle = (i, j, self.ZOOM)
                if cle not in self.m_tilePixmaps[self.ZOOM]:    #si la cle n'est pas en mémoire, on essaie de la charger du disque, ou on la télecharge
                    self.add_tile(i, j)
                else:
                    self.afficher_tuile(cle)    #sinon (la clé est en mémoire): on l'affiche (controle si déja dans la scene dans la fonction)

    def zoommodif(self):
        self.ZoomMode = not self.ZoomMode
        self.zoom(1/self.cur_zoom)
        self.cur_zoom = 1
        self.update_tiles()

    def update_tiles2(self):  #ancienne update tiles
        """affiche les tuiles nécessaires, en les prenant depuis la mémoire, le disque ou internet"""
        if self.ZOOM not in self.m_tilePixmaps:
            self.m_tilePixmaps[self.ZOOM] = {}
        pos1 = self.mapToScene(0, 0)
        pos2 = self.mapToScene(self.width(), self.height())
        X1 = int(pos1.x()/TILEDIM)
        X2 = int(pos2.x()/TILEDIM)
        Y1 = int(pos1.y()/TILEDIM)
        Y2 = int(pos2.y()/TILEDIM)
        for i in range(X1-2, X2+3):
            for j in range(Y1-2, Y2+3):
                cle = (i, j, self.ZOOM)
                if cle not in self.m_tilePixmaps[self.ZOOM]:    #si la cle n'est pas en mémoire, on essaie de la charger du disque, ou on la télecharge
                    self.add_tile(i, j)
                else:
                    self.afficher_tuile(cle)    #sinon (la clé est en mémoire): on l'affiche (controle si déja dans la scene dans la fonction)

    def setproxy(self, list):
        if list[0] != self.manager.proxy().hostName():
            proxy = QtNetwork.QNetworkProxy()
            proxy.setType(QtNetwork.QNetworkProxy.DefaultProxy)
            proxy.setHostName(str(list[0]))
            proxy.setPort(int(list[1]))
            proxy.setUser(str(list[2]))
            proxy.setPassword(str(list[3]))
            self.manager.setProxy(proxy)
            print((self.manager.proxy().hostName(), self.manager.proxy().port(), self.manager.proxy().user(), self.manager.proxy().password()))