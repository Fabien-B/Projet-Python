from PyQt4.QtCore import pyqtSlot, Qt
from PyQt4.QtGui import QWidget, QListWidgetItem
from PyQt4 import QtCore, QtGui
from window import Ui_MainWindow
import carte
import filtres
import poi
import os
import tisseo
import Get_GPS
import Sceneclicked
import No_More_Horse_Riding as nmhr
import proxy_params
import params


class Ihm(Ui_MainWindow):

    def __init__(self,MainWindow):
        super(Ihm, self).__init__()
        self.MainWindow = MainWindow
        self.latitude = 43.564995   #latitude et longitudes de départ
        self.longitude = 1.481650
        self.checkBoxs = []
        self.arret = None
        self.ptRecherche = None
        self.locator = Get_GPS.GPScoord(None)
        self.equipmentSet = set()
        self.pointAff = []
        self.nocover = nmhr.No_Covering(self)
        self.monFiltre = filtres.Filtre()
        self.proxy = '10.2.5.9'
        self.port = '8888'
        self.user = 'eleve-enac\\'
        #self.password = 'toto'     #Il vaut sans doute mieux ne pas enregistrer le mot de passe

    def built(self):
        self.dockWidget_2.hide()
        self.build_map()
        self.Quitter.triggered.connect(quit)
        self.actionInspecteur.triggered.connect(self.afficher_inspecteur)
        self.actionProxy.triggered.connect(self.afficher_params_proxy)
        self.actionViderCacheDonnees.triggered.connect(self.vider_cache_donnes)
        self.actionViderCacheCarte.triggered.connect(self.vider_cache_carte)
        self.ButtonDSelectAll.clicked.connect(lambda : self.update_checkbox(True))
        self.lineEditFiltresActivities.textEdited.connect(self.update_checkbox)
        self.listActivities.itemClicked.connect(self.itemClicked)
        self.lineEdit.returnPressed.connect(self.affiche_addresse)
        self.pushButton_7.clicked.connect(self.get_stopArea)
#        self.update_affichage_equipements()

    def build_map(self):
        self.scene = Sceneclicked.SceneClickable()
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setDragMode(QtGui.QGraphicsView.ScrollHandDrag) # allow drag and drop of the view
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)
        self.graphicsView.FinishInit()
        self.graphicsView.ihm = self
        self.graphicsView.download(self.latitude,self.longitude)
        self.connections()
    #pour obtenir les coordonnées GPS d'un point de la carte, appeler: self.graphicsView.get_gps_from_map(Xscene,Yscene) avec (Xscene,Yscene) les coordonnées du point dans la scène.
    #pour dessiner un point sur la carte appeler: self.graphicsView.draw_point(lat,lon [, legend = 'ma legende']), lat et lon étant la latitude et la longitude du point.
    # Retenir la Qellipse retournée (dans une variable) pour pouvoir l'effacer quand on veut.

    def update_affichage_equipements(self):
        for point in self.pointAff:
            if point in self.scene.items():
                self.scene.removeItem(point)
        for equip in self.equipmentSet:
            self.pointAff.append(self.graphicsView.draw_equipment(equip))
            self.scene.update()
        self.nocover.cluster(self.pointAff)

    def update_checkbox(self, checkstate = False):
        txt = self.lineEditFiltresActivities.text()
        liste = []
        for key in self.monFiltre.activitiesSet:
            if txt.capitalize() in key:
                liste.append(key)
        for checkbox in self.checkBoxs:
            if checkbox.text() not in liste:
                checkbox.setHidden(True)
            else:
                checkbox.setHidden(False)
        if checkstate is True:
            check = not self.checkBoxs[0].checkState()
            for checkbox in self.checkBoxs:
                if checkbox.isHidden() is False and check is True:
                    checkbox.setCheckState(Qt.Checked)
                    self.equipmentSet.update(self.monFiltre.filtrer_set_par_acti([checkbox.text()],self.HandAccessCheckBox.checkState()))
                if checkbox.isHidden() is False and check is False:
                    checkbox.setCheckState(Qt.Unchecked)
                    self.equipmentSet.difference_update(self.monFiltre.filtrer_set_par_acti([checkbox.text()]))
        self.update_affichage_equipements()

    def addcheckbox(self):
        self.listActivities.clear()
        for name in sorted(self.monFiltre.activitiesSet):
            lwItem = QtGui.QListWidgetItem(name, self.listActivities)
            lwItem.setFlags(Qt.ItemIsEnabled)
            lwItem.setCheckState(Qt.Unchecked)
            self.checkBoxs.append(lwItem)

    def itemClicked(self, item):
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
            eqASupprimer = self.monFiltre.filtrer_set_par_acti([item.text()])
            for checkbox in self.checkBoxs:
                if checkbox.checkState() == Qt.Checked:
                    eqASupprimer -= self.monFiltre.filtrer_set_par_acti([checkbox.text()])
            self.equipmentSet.difference_update(eqASupprimer)
        else:
            item.setCheckState(Qt.Checked)
            self.equipmentSet.update(self.monFiltre.filtrer_set_par_acti([item.text()],self.HandAccessCheckBox.checkState()))
        self.update_affichage_equipements()

    def affiche_addresse(self):
        """ affiche un point à l'addresse que l'utilisateur entre"""
        self.statusbar.showMessage("Recherche ...") #TODO n'a pas l'air de marcher ...
        txt = self.lineEdit.text()
        if self.ptRecherche != None:
            self.scene.removeItem(self.ptRecherche)
        coords = self.locator.find(txt,txt)

        # if self.arret != None:
        #     self.scene.removeItem(self.arret)
        if coords != None:
            #self.ptRecherche = self.graphicsView.draw_point(coords[0], coords[1], QtGui.QPen(QtCore.Qt.black, 3), QtCore.Qt.yellow, 20, txt) #TODO faire un truc plus joli (avec une icone)
            self.ptRecherche = self.graphicsView.draw_img_point(coords[0], coords[1],'vous_etes_ici', 'AAZZDD')
            #self.get_stopArea(coords[0], coords[1])
        else:
            print("adresse non trouvée")
            self.statusbar.showMessage("adresse non trouvée")

    def get_stopArea(self):     #TODO rame trop, à mettre dans un thread
        self.statusbar.showMessage("Recherche ...") #TODO n'a pas l'air de marcher ...
        txt = self.lineEdit.text()
        if self.arret != None:
            self.scene.removeItem(self.arret)
        coords = self.locator.find(txt,txt)
        (nomArret, latArret, lonArret) = tisseo.get_closest_sa(coords[0], coords[1])

        self.arret = self.graphicsView.draw_img_point(latArret, lonArret,'arret_transport_en_commun', nomArret)


    def notif_chrgmt_equip(self, infos):
        if infos[0]=='échec':
            self.statusbar.showMessage("Échec: {}       {}/{}".format(infos[1],infos[2],infos[3]),2000)
        if infos[0]=='cache':
            self.statusbar.showMessage('Chargement depuis le cache',2000)
        else:
            self.statusbar.showMessage("Adresse trouvée: {}       {}/{}".format(infos[0],infos[1],infos[2]),2000)

    def connections(self):
        self.scene.clusterisclicked.connect(self.nocover.explode)
        self.scene.backgroundclicked.connect(self.nocover.regroup)
        self.scene.equipointisclicked.connect(self.fill_inspector)

    def afficher_inspecteur(self):
        if self.dockWidget_2.isVisible():
            self.dockWidget_2.hide()
        else:
            self.dockWidget_2.show()

    def fill_inspector(self, equipoint):
        """Met à jour l'inspecteur de droite contenant les informations sur l'équipement cliqué"""

        if equipoint.equipment == None:
            return
        self.nomLineEdit.setText(equipoint.equipment.name)

        self.typeLineEdit.setText(equipoint.equipment.type)

        self.activitiesListWidget.clear()
        for activ in equipoint.equipment.activities:
            activityStr = activ + '(' + str(equipoint.equipment.activities[activ]) + ')'
            QtGui.QListWidgetItem(activityStr, self.activitiesListWidget)

        if equipoint.equipment.revetement != []:
            revetement = ''
            for i in range(0, len(equipoint.equipment.revetement)):
                revetement += str(equipoint.equipment.revetement[i])
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
        if equipoint.equipment.douches == [None,None]:     #TODO: n'a pas l'air de marcher, renvoie toujours non renseigné
            self.douchesLineEdit.setText('Non renseigné')
        else:
            txt = str(equipoint.equipment.douches[0]) + ' ind. , ' + str(equipoint.equipment.douches[1]) + ' coll.'
            txt = txt.replace('None', 'aucune')
            self.douchesLineEdit.setText(txt)
            # self.douchesLineEdit.setText('Individuelles : ' + equipoint.equipment.douches[0] + ' Collectives : ' + equipoint.equipment.douches[1])
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
        self.paramsWindow=params.Dialogue(self)#QtGui.QDialog()
        dialogParams = proxy_params.Ui_Proxy()
        dialogParams.setupUi(self.paramsWindow)
        self.paramsWindow.dialog=dialogParams
        self.paramsWindow.finishedSignal.connect(self.regler_proxy)
        self.set_default_proxy_params(dialogParams)
        self.paramsWindow.show()

    def regler_proxy(self,infos):
        self.proxy = infos[0]
        self.port = infos[1]
        self.user = infos[2]
        self.password = infos[3]
        print('proxy:',self.proxy,self.port,self.user,self.password)

    def set_default_proxy_params(self,dialogParams):
        dialogParams.lineEditProxy.setText(self.proxy)
        dialogParams.lineEditPort.setText(self.port)
        dialogParams.lineEditUser.setText(self.user)
        #dialogParams.lineEditPassword.setText(self.password)

    def vider_cache_donnes(self):
        if os.path.exists('.cache/equipmentList.cache'):
            os.remove('.cache/equipmentList.cache')

    def vider_cache_carte(self):
        if os.path.exists('.cache_Images'):
            for fichier in os.listdir('.cache_Images/'):
                path = '.cache_Images/' + fichier
                os.remove(path)
