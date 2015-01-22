from PyQt4.QtCore import pyqtSlot, Qt
from PyQt4.QtGui import QWidget, QListWidgetItem
from PyQt4 import QtCore, QtGui
from window import Ui_MainWindow
from cache_info import Ui_Cache
import cache_info
import wincache
import carte
import filtres
import equipement
import os
import tisseo
import Get_GPS
import Sceneclicked
import No_More_Horse_Riding as nmhr
import proxy_params
import params
import Cache_use
import threading

class Ihm(Ui_MainWindow, QtCore.QObject):
    """Classe principale du programme"""
    def __init__(self, MainWindow):
        super(Ihm, self).__init__()
        self.MainWindow = MainWindow
        self.latitude = 43.564995   #latitude et longitudes de départ
        self.longitude = 1.481650
        self.tisseo = tisseo.Tisseo()
        self.arrets = [None, None, None]     #arrive, depart1, départ2
        self.tisseopath = None
        self.answer = None
        self.pinPoint = None
        self.ptRecherche = None
        self.equipointSelected = None
        self.locator = Get_GPS.GPScoord(None)
        self.equipmentSet = set()
        self.allEquipmentSet = set()
        self.pointAff = []
        self.mesFiltres = []
        self.nocover = nmhr.No_Covering(self)
        self.proxycache = Cache_use.Cache('.cache/proxy/')
        if self.proxycache.isalive('proxy'):
            self.proxy = self.proxycache.rescue('proxy')[0]
            self.port = self.proxycache.rescue('proxy')[1]
            self.user = self.proxycache.rescue('proxy')[2]
        else:
            self.proxy = ''
            self.port = '8888'
            self.user = ''
        self.password = ''
        self.attributsNames = {'Quartier': 'quartier','Activités': 'activities', 'Revêtement': 'revetement', 'Éclairage': 'eclairage', 'Arrosage': 'arrosage', 'Toilettes Handicapés': 'toilettesHand'}

    def built(self):
        """"suite de l'initialisation"""
        self.dockWidget_2.hide()
        self.build_map()
        self.Quitter.triggered.connect(quit)
        self.actionInspecteur.triggered.connect(self.afficher_inspecteur)
        self.actionProxy.triggered.connect(self.afficher_params_proxy)
        self.actionViderCache.triggered.connect(self.afficher_params_cache)
        self.lineEdit.returnPressed.connect(self.affiche_addresse)
        self.pushButton_7.clicked.connect(lambda : self.get_stopArea(1, self.locator.find(self.lineEdit.text(), self.lineEdit.text())))
        self.pushButton.clicked.connect(self.graphicsView.reset_affichage)
        self.ajouterFiltreButton.clicked.connect(lambda: self.ajouter_filtre())
        self.handAccessButton.stateChanged.connect(self.update_affichage_equipements)
        self.Findequiarret_2_button.pressed.connect(lambda : self.get_equiStop(1))
        self.findPathFromPinButton.pressed.connect(lambda : self.get_equiStop(2))
        self.tisseo.closetASignal.connect(self.draw_stop_point_and_path)
        self.tisseo.errorSignal.connect(lambda txt: self.statusbar.showMessage(txt, 2000))
        self.graphicsView.signalEmetteur.doubleClickSignal.connect(self.get_pin)
        self.graphicsView.signalEmetteur.coordoneeErrorSignal.connect(lambda txt: self.statusbar.showMessage(txt, 2000))
        self.toolBox.resize(400, 1000)

    def build_map(self):
        """initialisation de la carte"""
        self.scene = Sceneclicked.SceneClickable()
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)  # allow drag and drop of the view
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)
        self.graphicsView.FinishInit()
        self.graphicsView.download(self.latitude, self.longitude)
        self.scene.clusterisclicked.connect(self.nocover.explode)
        self.scene.backgroundclicked.connect(self.nocover.regroup)
        self.scene.equipointisclicked.connect(self.fill_inspector)
        self.scene.giveEqCoordsSignal.connect(self.take_equipment_coordonnates)
        self.nocover.equipoint_clicked_in_cluster.connect(self.scene.draw_back_equip_select)
        self.graphicsView.updateZoomLevel.connect(self.update_after_zoom)
        self.graphicsView.updateZoomLevel.connect(self.mouse_simu_move)


    def finish_init_with_datas(self,equipmentList):
        """fin de l'initialisation après l'import des équipements"""
        self.equipmentList = equipmentList
        self.allEquipmentSet = set(equipmentList)
        self.ajouter_filtre()

    def ajouter_filtre(self):
        """crée et initialise un filtre"""
        self.mesFiltres.append(filtres.Filtre(self.tabWidget,self.pointAff))
        self.mesFiltres[-1].updateSignal.connect(self.update_affichage_equipements)
        self.mesFiltres[-1].create_set(self.equipmentList)
        self.mesFiltres[-1].equip_set(self.equipmentList)
        self.mesFiltres[-1].removeSignal.connect(self.remove_filtre)
        i = self.mesFiltres[-1].comboBox.findText('Activités')
        self.mesFiltres[-1].comboBox.setCurrentIndex(i)

    def remove_filtre(self, widget):
        """supprime un filtre"""
        i = self.tabWidget.indexOf(widget)
        self.tabWidget.removeTab(i)
        del self.mesFiltres[i]
        self.update_affichage_equipements()

    def get_pin(self, point):
        if self.pinPoint != None:
            self.scene.removeItem(self.pinPoint)
        self.pinPoint = point

    def update_affichage_equipements(self):
        """met à jour l'affichage des équipements en fonction des filtres"""
        setEquipements = set(self.allEquipmentSet)
        for fifi in self.mesFiltres:
            setEquipements &= fifi.equipmentSet
        if self.handAccessButton.checkState():
                setEquipements = self.filtrer_acces_hand(setEquipements)
        for point in self.pointAff:
            if point in self.scene.items():
                self.scene.removeItem(point)
        self.pointAff = []
        for equip in setEquipements:
            self.pointAff.append(self.graphicsView.draw_equipment(equip))
            if self.equipointSelected and equip == self.equipointSelected.equipment:
                self.scene.draw_back_equip_select(self.pointAff[-1])
                self.pointAff[-1].selected = True
            self.scene.update()
        self.nocover.cluster(self.pointAff)

    def update_after_zoom(self):
        self.update_affichage_equipements()
        if self.ptRecherche != None:
            coords = self.ptRecherche.coords
            txt = self.ptRecherche.legend
            self.ptRecherche = self.graphicsView.draw_point(coords[0], coords[1], img='vous_etes_ici', legend=txt)
        if self.tisseopath != None and self.answer != None:
            self.draw_path(self.answer)
        if self.pinPoint != None:
            coords = self.pinPoint.coords
            self.graphicsView.dessiner_pinPoint(coords[0], coords[1])
        for (i, pt) in enumerate(self.arrets):
            if pt != None:
               infos = (pt.legend, pt.coords[0], pt.coords[1], i, '0', '0')
               self.draw_tisseoStopPoint(infos)

    def filtrer_acces_hand(self, equipSet,state = True):
        """prend en paramètre un set d'équipements, renvoie un set de ceux avec (ou sans) accès handicapés (suivant l'état de state)"""
        tempSet = set()
        for equip in equipSet:
            if not state ^ equip.accesHand:     #pour se la péter! "if non (state ou_exclusif accesHand)"
                    tempSet.add(equip)
        return tempSet

    def affiche_addresse(self):
        """ affiche un point à l'addresse que l'utilisateur entre dans la lineEdit"""
        txt = self.lineEdit.text()
        if self.ptRecherche != None:
            self.scene.removeItem(self.ptRecherche)
        coords = self.locator.find(txt, txt)
        if coords != None:
            self.ptRecherche = self.graphicsView.draw_point(coords[0], coords[1], img='vous_etes_ici', legend=txt)
            self.graphicsView.centerOnPosition(coords[0], coords[1])
        else:
            print("adresse non trouvée")
            self.statusbar.showMessage("adresse non trouvée")

    def get_stopArea(self,pointIndex,coords, isItineraire = False, departurePoint=0):
        """recherche avec l'API tisséo l'arret le plus proche"""
        self.statusbar.showMessage("Recherche ...")
        if self.arrets[pointIndex] != None:
            self.scene.removeItem(self.arrets[pointIndex])
        threadClosestStopPoint = threading.Thread(target = lambda : self.tisseo.get_closest_sa(coords[0], coords[1], point=pointIndex, isItineraire=isItineraire, departurePoint=departurePoint))     #True : itinéraire
        threadClosestStopPoint.start()

    def draw_tisseoStopPoint(self, infos):
        (nomArret, latArret, lonArret, i, _,_) = infos
        self.arrets[i] = self.graphicsView.draw_point(latArret, lonArret, img='arret_transport_en_commun', legend=nomArret)

    def get_equiStop(self,departurePointIndex):
        if self.nomLineEdit.text() == "":
            self.statusbar.showMessage("Aucun équipement sportif sélectionné")
            return
        if departurePointIndex == 1 and self.lineEdit.text() == "":                     #départ: adresse
            self.statusbar.showMessage("Veuillez selectionner un point de départ")
            return
        if departurePointIndex == 2 and self.pinPoint == None:                         #départ: épingle
            self.statusbar.showMessage("Veuillez double clicker pour selectionner un point de départ")

        if departurePointIndex == 1:
            txt = self.lineEdit.text()
            coords = self.locator.find(txt, txt)
        if departurePointIndex == 2:
            coords = self.pinPoint.coords

        if self.arrets[departurePointIndex] != None:
            self.scene.removeItem(self.arrets[departurePointIndex])
            self.arrets[departurePointIndex] = None
        self.statusbar.showMessage("Recherche...")
        self.get_stopArea(departurePointIndex,coords, True,departurePoint=departurePointIndex)

    def draw_stop_point_and_path(self, infos):
        self.draw_tisseoStopPoint(infos)
        self.statusbar.clearMessage()
        if infos[4]:        #si c'est un calcul d'itinéraire
            if not infos[3]:    #si on a calculé le point d'arrivée
                self.get_path(infos[5])
            else:
                self.get_stopArea(0,self.currentEquipmentCoords,True,infos[5])

    def get_path(self,indexDeparturePoint):
        answer = self.tisseo.gettrail(self.arrets[indexDeparturePoint].legend, self.arrets[0].legend)
        if answer != None:
            self.draw_path(answer)
            self.print_instructions_path(self.tisseo.extractinstruct(answer))
            self.answer = answer

    def print_instructions_path(self,instructions):
        txt = '\n\n'.join(instructions)
        self.textEdit.setText(txt)

    def draw_path(self, answer):
        if self.tisseopath != None:
            self.scene.removeItem(self.tisseopath)
        self.tisseopath = QtGui.QGraphicsItemGroup()

        def get_color(n):
            """Renvoie une QColor en fonction de l'entier 'n'
            BY TP noté 2 de Python ENAC"""
            d = (0xff, 0xdd, 0xbb, 0x99, 0x77, 0x55)[(n // 6) % 6]
            r, v, b = ((d, 0, 0), (0, d, 0), (0, 0, d), (d, d, 0), (d, 0, d), (0, d, d))[n % 6]
            return QtGui.QColor(r, v, b)

        pathlist, pointlist = self.tisseo.extractlinecoord(answer)
        for i in range(len(pathlist)):
            pen = QtGui.QPen(get_color(i), 5)
            departnbs = self.graphicsView.get_tile_nbs(float(pathlist[i][0][1]), float(pathlist[i][0][0]))
            depart = tuple(((departnbs[0]+departnbs[2])*carte.TILEDIM, (departnbs[1]+departnbs[3])*carte.TILEDIM))
            for j in range(len(pathlist[i])-1):
                arriveenbs = self.graphicsView.get_tile_nbs(float(pathlist[i][j+1][1]), float(pathlist[i][j+1][0]))
                arrivee = tuple(((arriveenbs[0]+arriveenbs[2])*carte.TILEDIM, (arriveenbs[1]+arriveenbs[3])*carte.TILEDIM))
                line = QtGui.QGraphicsLineItem(depart[0], depart[1], arrivee[0], arrivee[1])
                line.setPen(pen)
                line.setZValue(13)
                self.tisseopath.addToGroup(line)
                depart = arrivee
        for i in range(len(pointlist)):
            coordpoint = self.graphicsView.get_tile_nbs(float(pointlist[i][1]), float(pointlist[i][0]))
            xpoint = (coordpoint[0]+coordpoint[2])*carte.TILEDIM
            ypoint = (coordpoint[1]+coordpoint[3])*carte.TILEDIM
            pen = QtGui.QPen(get_color(i+1),2)
            brush = QtGui.QBrush(get_color(i))
            point = QtGui.QGraphicsEllipseItem()
            point.setPen(pen)
            point.setBrush(brush)
            point.setRect(0, 0, 16, 16)
            point.setPos(xpoint-8, ypoint-8)
            point.setZValue(14)
            self.tisseopath.addToGroup(point)
        self.scene.addItem(self.tisseopath)

    def notif_chrgmt_equip(self, infos):
        """notifier dans la barre d'état le chargement"""
        self.statusbar.showMessage(infos,2000)

    def take_equipment_coordonnates(self,coords):
        self.currentEquipmentCoords = coords

    def afficher_inspecteur(self):
        """change l'affichage de l'inspecteur"""
        if self.dockWidget_2.isVisible():
            self.dockWidget_2.hide()
        else:
            self.dockWidget_2.show()

    def fill_inspector(self, equipoint):
        """Met à jour l'inspecteur contenant les informations sur l'équipement cliqué"""
        if self.equipointSelected:
            self.equipointSelected.selected = False
        self.equipointSelected = equipoint
        if equipoint.equipment == None:
            return
        self.nomLineEdit.setText(equipoint.equipment.name)

        self.typeLineEdit.setText(equipoint.equipment.type)

        self.activitiesListWidget.clear()
        for activ in equipoint.equipment.activities:
            activityStr = activ + '(' + str(equipoint.equipment.activities[activ]) + ')'
            QtGui.QListWidgetItem(activityStr, self.activitiesListWidget)

        revetement = ' '.join(equipoint.equipment.revetement)
        self.revetementLineEdit.setText(revetement)

        if equipoint.equipment.eclairage == 1:
            self.eclairageLineEdit.setText('Oui')
        else:
            self.eclairageLineEdit.setText('Non')
        self.vestiairesLineEdit.setText('Joueurs : ' + str(equipoint.equipment.vestiaire[0]) + ' Arbitres : ' + str(equipoint.equipment.vestiaire[1]))
        if equipoint.equipment.sanitaires == None:
            self.sanitairesLineEdit_5.setText('Non renseigné')
        elif equipoint.equipment.sanitaires != 'non':
            self.sanitairesLineEdit_5.setText('Oui')
        if equipoint.equipment.douches == [None, None]:
            self.douchesLineEdit.setText('Non renseigné')
        else:
            txt = str(equipoint.equipment.douches[0]) + ' ind. , ' + str(equipoint.equipment.douches[1]) + ' coll.'
            txt = txt.replace('None', 'aucune')
            self.douchesLineEdit.setText(txt)
        if equipoint.equipment.accesHand == 1:
            self.sanitairesLineEdit_4.setText('Oui')
        elif equipoint.equipment.accesHand == 0:
            self.sanitairesLineEdit_4.setText('Non')
        else:
            self.sanitairesLineEdit_4.setText('Non renseigné')
        if equipoint.equipment.toilettesHand == 1:
            self.sanitairesLineEdit_3.setText('Oui')
        elif equipoint.equipment.toilettesHand == 0:
            self.sanitairesLineEdit_3.setText('Non')
        else:
            self.sanitairesLineEdit_3.setText('Non renseigné')
        if equipoint.equipment.tribunes == 0:
            self.sanitairesLineEdit_2.setText('Non renseigné')
        else:
            self.sanitairesLineEdit_2.setText(str(equipoint.equipment.tribunes))
        if equipoint.equipment.clubHouse == None:
            self.sanitairesLineEdit.setText('Non')
        else:
            self.sanitairesLineEdit.setText('Oui')
        if equipoint.equipment.size == [()]:
            self.sanitairesLineEdit_7.setText('Non renseigné')
        else:
            self.sanitairesLineEdit_7.setText(str(equipoint.equipment.size))
        if equipoint.equipment.capaMax == 0:
            self.sanitairesLineEdit_11.setText('Non renseigné')
        else:
            self.sanitairesLineEdit_11.setText(str(equipoint.equipment.capaMax))
        self.sanitairesLineEdit_10.setText(str(equipoint.equipment.adresse))
        if equipoint.equipment.categorie == 0:
            self.sanitairesLineEdit_9.setText('Non renseigné')
        else:
            self.sanitairesLineEdit_9.setText(str(equipoint.equipment.categorie))
        self.sanitairesLineEdit_6.setText(str(equipoint.equipment.coords))
        self.dockWidget_2.show()

    def afficher_params_proxy(self):
        """ouvre la boite de dialogue de réglage de proxy"""
        self.paramsWindow = params.Dialogue(self)  #QtGui.QDialog()
        dialogParams = proxy_params.Ui_Proxy()
        dialogParams.setupUi(self.paramsWindow)
        self.paramsWindow.dialog = dialogParams
        self.paramsWindow.finishedSignal.connect(self.regler_proxy)
        self.set_default_proxy_params(dialogParams)
        self.paramsWindow.show()

    def afficher_params_cache(self):
        """ouvre la boite de dialogue du cache"""
        self.cacheWindow = wincache.Cache_Dialogue(self)
        dialogCache = cache_info.Ui_Cache()
        dialogCache.setupUi(self.cacheWindow)
        self.cacheWindow.dialog = dialogCache
        self.maj_taille_cache(dialogCache)
        self.cacheWindow.show()

    def maj_taille_cache(self, dialogCache):
        infos = self.cache_size()
        dialogCache.Label_TailleCacheImage.setText(str(infos[0])[:5] + ' Mo')
        dialogCache.Label_NombreDeDalles.setText(str(infos[1]))
        dialogCache.Label_TailleCacheDonne.setText(str(infos[2])[:5] + ' ko')

    def regler_proxy(self, infos):
        self.proxy = infos[0]
        self.port = infos[1]
        self.user = infos[2]
        self.password = infos[3]
        self.proxycache.save(infos[:-1],'proxy')
        self.locator.setproxy(infos)
        self.graphicsView.setproxy(infos)
        self.tisseo.setproxy(infos)
        print('proxy:',self.proxy,self.port,self.user)

    def set_default_proxy_params(self, dialogParams):
        dialogParams.lineEditProxy.setText(self.proxy)
        dialogParams.lineEditPort.setText(self.port)
        dialogParams.lineEditUser.setText(self.user)

    def vider_cache_donnes(self):
        """supprime le cache des équipements"""
        if os.path.exists('.cache/equipmentList.cache'):
            os.remove('.cache/equipmentList.cache')

    def vider_cache_carte(self):
        """supprime les tuiles OSM"""
        if os.path.exists('.cache_Images'):
            for fichier in os.listdir('.cache_Images/'):
                path = '.cache_Images/' + fichier
                os.remove(path)

    def mouse_simu_move(self):
        """ Permet de ne pas avoir a bouger la souris pour afficher les tuiles apres un changement de niveau de zoom  """
        cur = self.MainWindow.cursor()
        pos = cur.pos()
        q = QtCore.QPoint(1, 1)
        pos = pos + q
        cur.setPos(pos)
        pos = pos - q
        cur.setPos(pos)

    def cache_size(self):
        """retourne la taille du cache image en Mo et du cache des données en ko"""
        sizeOfCacheImage = 0
        sizeOfCacheDonnee = 0
        numberOfTiles = 0
        if os.path.exists('.cache_Images'):
            for fichier in os.listdir('.cache_Images/'):
                path = '.cache_Images/' + fichier
                sizeOfCacheImage += os.path.getsize(path)
                numberOfTiles += 1
        if os.path.exists('.cache/equipmentList.cache'):
            sizeOfCacheDonnee = os.path.getsize('.cache/equipmentList.cache')
        return (sizeOfCacheImage/(1024*1024), numberOfTiles, sizeOfCacheDonnee/1024)
