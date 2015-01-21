from PyQt4 import QtCore, QtGui
import math
import poi

class No_Covering(QtCore.QObject):

    equipoint_clicked_in_cluster = QtCore.pyqtSignal(poi.Equipment_Group)

    def __init__(self, ihm):
        super(No_Covering, self).__init__()
        self.ihm = ihm
        self.scene = None
        self.equipoint_selected_clustered = None

    def cluster(self, equipList):
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
                        self.equipoint_selected_clustered = point
                        self.equipoint_clicked_in_cluster.emit(equicluster)
                        equicluster.selected = True
                    self.scene.removeItem(point)
                equicluster.tooltiper()
                equicluster.digitalize()
                clusterlist.append(equicluster)
                self.scene.addItem(equicluster)
        return equipListClustered


    def explode(self, the_cluster):
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
        bg = poi.BackGroundCluster(rayon, the_cluster, self.scene)
        return bg


    def regroup(self, background):
        for point in background.equippointlist:
            if point.selected:
                self.scene.draw_back_equip_select(background.the_cluster)
                self.equipoint_selected_clustered = point
            self.scene.removeItem(point)
        self.scene.addItem(background.the_cluster)
        background.the_cluster.exploded = None
        self.scene.removeItem(background)





class No_Covering_Active(QtCore.QObject):
    def __init__(self, ihm):
        super(No_Covering_Active, self).__init__()
        self.ihm = ihm
        self.scene = None
    def repulse(self, equipList):
        self.scene = self.ihm.scene
        equipListClustered = equipList
        clusterlist = []
        packed = []
        icons = list(set(equipList) - set([None]))
        for elicon1 in icons:
            collidingitems = elicon1.collidingItems()
            colliding = list(set(collidingitems) & set(icons) - set(packed))
            if colliding:
                    trait = QtGui.QGraphicsLineItem()
                    pen = QtGui.QPen(QtCore.Qt.red, 2, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin)
                    trait.setPen(pen)
                    trait.setLine(elicon1.Pos()[0], elicon1.Pos()[1], elicon1.Pos()[0]+20, elicon1.Pos()[1]+20)
                    trait.setZValue(4)
                    self.scene.addItem(trait)
                    # elicon1.SetPos()
                    elicon2.SetPos(elicon2.Pos()[0]+40, elicon2.Pos()[1]+40)
                    elicon2.setOpacity(0.5)

    def repulse2(self, equipList):
            global tries
            changed = 0
            checked = []
            for (equip1, point1) in equipList:
                for (equip2, point2) in equipList:
                    if point1 != None and point2 != None and equip1 != equip2 and equip1 not in checked and equip2 not in checked:
                        try :
                            pos1 = (point1.icone.scenePos().x(), point2.icone.scenePos().y())
                            print(pos1)
                        except AttributeError:
                         try:
                            pos1 = (point1.ellipse.scenePos().x(), point2.icone.scenePos().x())
                            print(pos1)
                         except AttributeError:
                            pos1 = (0,0)

                    # pos2 = (point2.ellipse.rect().x(), point2.ellipse.rect().y())

                    # norm = math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)
                    # if norm == 0:
                    #     point1.ellipse.setRect(pos1[0] - 7, pos1[1] ,point1.ellipse.rect().width(), point1.ellipse.rect().height() )
                    #     point2.ellipse.setRect(pos2[0] + 7 , pos2[1] ,point1.ellipse.rect().width(), point1.ellipse.rect().height() )
                    #     newpos = (pos1[0] - 10 +(pos2[0] - pos1[0]), pos1[1] - 10 +(pos2[1] - pos1[1]))
                    #     point1.BRUSH = QtCore.Qt.blue
                    #     point2.BRUSH = QtCore.Qt.blue
                    #     print("\"",equip1.name, equip2.name, "\"")
                        # checked.append(equip1)
                        # checked.append(equip2)
                        # changed = 1
                    if  0 < 10 < 11:
                        # print(norm)
                        # point1.ellipse.setRect(2*(pos1[0] - 15 -(pos2[0] - pos1[0])), 2*(pos1[1] - 15 -(pos2[1] - pos1[1])),point1.ellipse.rect().width(), point1.ellipse.rect().height() )
                        # point2.ellipse.setRect(2*(pos1[0] + 15 +(pos2[0] - pos1[0])), 2*(pos1[1] + 15 +(pos2[1] - pos1[1])),point1.ellipse.rect().width(), point1.ellipse.rect().height() )
                        newpos = (pos1[0] - 10 +(pos1[0] - pos1[0]), pos1[1] - 10 +(pos1[1] - pos1[1]))

                        ellipse = QtGui.QGraphicsEllipseItem()
                        ellipse.setPen(QtCore.Qt.red)
                        ellipse.setBrush(QtCore.Qt.red)
                        ellipse.setRect(pos1[0], pos1[1], 20, 20)
                        ellipse.setZValue(150)
                        self.scene.addItem(ellipse)
                        # print("\"",equip1.name, equip2.name, "\"")
                        checked.append(equip1)
                        checked.append(equip2)
                        changed = 1
            if changed == 1:
                tries += 1
                print(tries)
            # if tries <= 5:
                # repulse(self.equipList)
            # else:
            #     tries = 0
            #     return


def repulsewithQT(equipList, scene):
    for (equip1, point1) in equipList.items():
            pos1 = (point1.ellipse.rect().x(), point1.ellipse.rect().y())
            # pos2 = (point2.ellipse.rect().x(), point2.ellipse.rect().y())
            for point2 in point1.ellipse.collidingItems():
                pass



# def arrow(pointfrom, pointto, scene):
