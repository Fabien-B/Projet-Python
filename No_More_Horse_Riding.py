from PyQt4 import QtCore, QtGui
import math
import poi
tries = 0


def repulse(equipList, scene):
    for elicon1 in equipList.values():
        collidingitems = elicon1.collidingItems()
        for elicon2 in collidingitems:
            if elicon2 in equipList.values():
                trait = QtGui.QGraphicsLineItem()
                pen = QtGui.QPen(QtCore.Qt.red, 2, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin)
                trait.setPen(pen)
                trait.setLine(elicon1.Pos()[0], elicon1.Pos()[1], elicon1.Pos()[0]+20, elicon1.Pos()[1]+20)
                trait.setZValue(4)
                scene.addItem(trait)
                # elicon1.SetPos()
                elicon2.SetPos(elicon2.Pos()[0]+40, elicon2.Pos()[1]+40)
                elicon2.setOpacity(0.5)

def repulse2(equipList, scene):
        global tries
        changed = 0
        checked = []
        for (equip1, point1) in equipList.items():
            for (equip2, point2) in equipList.items():
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
                        scene.addItem(ellipse)
                        # print("\"",equip1.name, equip2.name, "\"")
                        checked.append(equip1)
                        checked.append(equip2)
                        changed = 1
        if changed == 1:
            tries += 1
            print(tries)
            # if tries <= 5:
                # repulse(equipList)
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
