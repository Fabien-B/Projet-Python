from PyQt4.QtCore import pyqtSlot, Qt
from PyQt4.QtGui import QWidget, QListWidgetItem
from PyQt4 import QtCore, QtGui
from window import Ui_MainWindow
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


class Ihm(Ui_MainWindow,QtCore.QObject):

    def __init__(self,MainWindow):
        super(Ihm, self).__init__()
        self.MainWindow = MainWindow
        self.latitude = 43.564995   #latitude et longitudes de départ
        self.longitude = 1.481650
        self.arret = None
        self.ptRecherche = None
        self.locator = Get_GPS.GPScoord(None, None)
        self.equipmentSet = set()
        self.pointAff = []
        self.nocover = nmhr.No_Covering(self)
        self.monFiltre = filtres.Filtre()
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
        self.attributsNames = {'Quartier':'quartier','Activités':'activities','Revêtement':'revetement','Éclairage':'eclairage','Arrosage':'arrosage','Toilettes Handicapés':'toilettesHand'}

    def built(self):
        self.dockWidget_2.hide()
        self.build_map()
        self.Quitter.triggered.connect(quit)
        self.actionInspecteur.triggered.connect(self.afficher_inspecteur)
        self.actionProxy.triggered.connect(self.afficher_params_proxy)
        self.actionViderCacheDonnees.triggered.connect(self.vider_cache_donnes)
        self.actionViderCacheCarte.triggered.connect(self.vider_cache_carte)
        self.ButtonDSelectAll.clicked.connect(lambda : self.select_deselect_all(self.listActivities))
        self.lineEditFiltresActivities.textEdited.connect(lambda  : self.update_checkbox(self.listActivities, self.lineEditFiltresActivities.text()))
        self.listActivities.itemClicked.connect(self.itemClicked)
        #self.HandAccessCheckBox.stateChanged.connect(lambda : self.hand_changement(self.listActivities))
        self.lineEdit.returnPressed.connect(self.affiche_addresse)
        self.pushButton_7.clicked.connect(self.get_stopArea)
        self.pushButton.clicked.connect(self.graphicsView.zoommodif)
        self.connect(self.comboBox, QtCore.SIGNAL('currentIndexChanged(QString)'), self.changer_filtre)
#        self.update_affichage_equipements()

    def build_map(self):
        self.scene = Sceneclicked.SceneClickable()
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)  # allow drag and drop of the view
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)
        self.graphicsView.FinishInit()
        self.graphicsView.ihm = self
        self.graphicsView.download(self.latitude, self.longitude)
        self.connections()
    #pour obtenir les coordonnées GPS d'un point de la carte, appeler: self.graphicsView.get_gps_from_map(Xscene,Yscene) avec (Xscene,Yscene) les coordonnées du point dans la scène.
    #pour dessiner un point sur la carte appeler: self.graphicsView.draw_point(lat,lon [, legend = 'ma legende']), lat et lon étant la latitude et la longitude du point.
    # Retenir la Qellipse retournée (dans une variable) pour pouvoir l'effacer quand on veut.

    def finish_init_with_datas(self):
        self.add_checkboxs(self.listActivities,'activities')
        self.add_combo_items()

    def update_affichage_equipements(self):
        for point in self.pointAff:
            if point in self.scene.items():
                self.scene.removeItem(point)
        for equip in self.equipmentSet:
            self.pointAff.append(self.graphicsView.draw_equipment(equip))
            self.scene.update()
        self.nocover.cluster(self.pointAff)

    def update_checkbox(self,concernedList, txt):
        #txt = self.lineEditFiltresActivities.text()
        liste = []
        paramSet = concernedList.item(0).param + 'Set'
        for key in self.monFiltre.__dict__[paramSet]:
            if txt.capitalize() in key:
                liste.append(key)
        print(liste)
        for i in range(concernedList.count()):
                checkbox = concernedList.item(i)
                if checkbox.text() not in liste:
                    checkbox.setHidden(True)
                else:
                    checkbox.setHidden(False)
        self.update_affichage_equipements()

    def select_deselect_all(self,concernedList):
        check = 2 if not concernedList.item(0).checkState() else 0
        param = concernedList.item(0).param
        activitiesList = []
        for i in range(concernedList.count()):
                checkbox = concernedList.item(i)
                if not checkbox.isHidden():
                    checkbox.setCheckState(check)
                    activitiesList.append(checkbox.text())
        if check:
            self.equipmentSet.update(self.monFiltre.filtrer_set_par_acti(param,activitiesList,self.HandAccessCheckBox.checkState()))
        else:
            self.equipmentSet.difference_update(self.monFiltre.filtrer_set_par_acti(param,activitiesList))
        self.update_affichage_equipements()

    def add_checkboxs(self,listView,param):
        print('param ==== ', param)
        paramSet = param + 'Set'
        listView.clear()
        for name in sorted(self.monFiltre.__dict__[paramSet]):
            name = str(name)
            if name == '999':
                name = 'Non renseigné'
            lwItem = filtres.myListWidgetItem(name, listView)
            lwItem.param = param
            lwItem.setFlags(Qt.ItemIsEnabled)
            lwItem.setCheckState(Qt.Unchecked)

    def add_combo_items(self):
        for key in equipement.Equipment().__dict__:
            if key in self.attributsNames.values():
                for cle in self.attributsNames:
                    if self.attributsNames[cle] == key:
                        self.comboBox.addItem(cle)
        self.listWidget.itemClicked.connect(self.itemClicked)

    def itemClicked(self, item):
        print(item.param)
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
            eqASupprimer = self.monFiltre.filtrer_set_par_acti(item.param,[item.text()])
            for i in range(item.liste.count()):
                checkbox = item.liste.item(i)
                if checkbox.checkState() == Qt.Checked:
                    eqASupprimer -= self.monFiltre.filtrer_set_par_acti(item.param,[checkbox.text()])
            self.equipmentSet.difference_update(eqASupprimer)
        else:
            item.setCheckState(Qt.Checked)
            self.equipmentSet.update(self.monFiltre.filtrer_set_par_acti(item.param,[item.text()],self.HandAccessCheckBox.checkState()))
        self.update_affichage_equipements()

    def hand_changement(self,concernedList):
        if self.HandAccessCheckBox.checkState():
            self.equipmentSet.difference_update(self.monFiltre.filtrer_acces_hand(self.equipmentSet,False))
        else:
            param = concernedList.item(0).param
            paramList = []
            for i in range(concernedList.count()):
                checkbox = concernedList.item(i)
                if checkbox.checkState():
                    paramList.append(checkbox.text())
            self.equipmentSet = self.monFiltre.filtrer_set_par_acti(param,paramList)
        self.update_affichage_equipements()

    def changer_filtre(self,txt):
        self.add_checkboxs(self.listWidget,str(self.attributsNames[txt]))
        self.selectAllSecondFiltreButton.clicked.connect(lambda : self.select_deselect_all(self.listWidget))
        self.HandAccessCheckBox.stateChanged.connect(lambda : self.hand_changement(self.listWidget))
        self.lineEditFiltres.textEdited.connect(lambda  : self.update_checkbox(self.listWidget, self.lineEditFiltres.text()))

    def affiche_addresse(self):
        """ affiche un point à l'addresse que l'utilisateur entre"""
        self.statusbar.showMessage("Recherche ...")  #TODO n'a pas l'air de marcher ...
        txt = self.lineEdit.text()
        if self.ptRecherche != None:
            self.scene.removeItem(self.ptRecherche)
        coords = self.locator.find(txt,txt)
        if coords != None:
            self.ptRecherche = self.graphicsView.draw_img_point(coords[0], coords[1],'vous_etes_ici', txt)
        else:
            print("adresse non trouvée")
            self.statusbar.showMessage("adresse non trouvée")

    def get_stopArea(self):     #TODO rame trop, à mettre dans un thread
        self.statusbar.showMessage("Recherche ...")  #TODO n'a pas l'air de marcher ...
        txt = self.lineEdit.text()
        if self.arret != None:
            self.scene.removeItem(self.arret)
        coords = self.locator.find(txt, txt)
        (nomArret, latArret, lonArret) = tisseo.get_closest_sa(coords[0], coords[1])

        self.arret = self.graphicsView.draw_img_point(latArret, lonArret, 'arret_transport_en_commun', nomArret)

    def notif_chrgmt_equip(self, infos):
        if infos[0] == 'échec':
            self.statusbar.showMessage("Échec: {}       {}/{}".format(infos[1],infos[2],infos[3]),2000)
        if infos[0] == 'cache':
            self.statusbar.showMessage('Chargement depuis le cache', 2000)
        else:
            self.statusbar.showMessage("Adresse trouvée: {}       {}/{}".format(infos[0], infos[1], infos[2]), 2000)

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
        self.paramsWindow=params.Dialogue(self)  #QtGui.QDialog()
        dialogParams = proxy_params.Ui_Proxy()
        dialogParams.setupUi(self.paramsWindow)
        self.paramsWindow.dialog=dialogParams
        self.paramsWindow.finishedSignal.connect(self.regler_proxy)
        self.set_default_proxy_params(dialogParams)
        self.paramsWindow.show()

    def regler_proxy(self, infos):
        self.proxy = infos[0]
        self.port = infos[1]
        self.user = infos[2]
        self.password = infos[3]
        self.proxycache.save(infos[:-1],'proxy')
        print('proxy:',self.proxy,self.port,self.user)
    def set_default_proxy_params(self, dialogParams):
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
