from PyQt4 import QtCore, QtGui
import math
import poi

class No_Covering(QtCore.QObject):
    """La classe qui s'occupe d'effectuer que deux icones ne se recouvrent pas"""

    equipoint_clicked_in_cluster = QtCore.pyqtSignal(poi.Equipment_Group)

    def __init__(self, ihm):
        super(No_Covering, self).__init__()
        self.ihm = ihm
        self.scene = None
        self.equipoint_selected_clustered = None

    def cluster(self, equipList):
        """Mettre tous les icones qui se touchent dans un cluster"""
        self.scene = self.ihm.scene
        equipListClustered = equipList
        clusterlist = []
        packed = []
        icons = list(set(equipList) - set([None]))
        for elicon1 in icons:
            collidingitems = elicon1.collidingItems()
            colliding = list(set(collidingitems) & set(icons) - set(packed))
            if colliding:
                posx = [i.Pos()[0] for i in colliding] + [elicon1.Pos()[0]]
                posy = [i.Pos()[1] for i in colliding] + [elicon1.Pos()[1]]
                equicluster = poi.Equipment_Group(self.scene, sum(posx)/len(posx), sum(posy)/len(posy))
                equicluster.equipointlist = colliding + [elicon1]
                for point in equicluster.equipointlist:
                    packed.append(point)
                    equipListClustered.append(equicluster)
                    if point.selected:
                        self.equipointselectedisclustered(point, equicluster)
                    self.scene.removeItem(point)
                equicluster.tooltiper()
                equicluster.digitalize()
                clusterlist.append(equicluster)
                self.scene.addItem(equicluster)
        return equipListClustered

    def equipointselectedisclustered(self, point, equicluster):
        """Si l'équipement sélctionné est mis dans un cluster, on l'enregistre et on envoie un signal du cluster"""
        self.equipoint_selected_clustered = point
        self.equipoint_clicked_in_cluster.emit(equicluster)
        equicluster.selected = True

    def explode(self, the_cluster):
        """Lorsque l'on clique sur le cluster fermé, le faire ouvrir en affichant les équipements qu'il contient
        ainsi qu'un background"""
        if the_cluster.exploded == None:
            size = the_cluster.size()
            rayon = sum([the_cluster.equipointlist[i].boundingRect().height()*size/2 for i in range(size)])/size + 10
            deltaangle = math.radians(360/size)
            list_angle = [i*deltaangle for i in range(size)]
            bg = self.drawbackground(the_cluster, rayon)
            for i in range(size):
                pos = (the_cluster.Pos()[0] + rayon/2*math.sin(list_angle[i]), the_cluster.Pos()[1] + rayon/2*math.cos(list_angle[i]))
                point = poi.Equipement_point(pos[0], pos[1], the_cluster.equipointlist[i].equipment, Zvalue=14)
                if self.equipoint_selected_clustered and self.equipoint_selected_clustered.equipment == point.equipment:
                    self.scene.draw_back_equip_select(point)
                bg.equippointlist.append(point)
                self.scene.addItem(point)
                self.ihm.pointAff.append(point)
            the_cluster.exploded = not the_cluster.exploded
            self.ihm.pointAff.append(bg)
            self.scene.removeItem(the_cluster)

    def drawbackground(self, the_cluster, rayon):
        """Dessine le background d'un cluster ouvert"""
        bg = poi.BackGroundCluster(rayon, the_cluster, self.scene)
        return bg


    def regroup(self, background):
        """Lorsque l'on clique sur le background d'un cluster ouvert, le fermer en réaffichant le point
        en enlevant le background et les équipements visibles"""
        for point in background.equippointlist:
            if point.selected:
                self.scene.draw_back_equip_select(background.the_cluster)
                self.equipoint_selected_clustered = point
            self.scene.removeItem(point)
        self.scene.addItem(background.the_cluster)
        background.the_cluster.exploded = None
        self.scene.removeItem(background)