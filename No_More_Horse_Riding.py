from PyQt4 import QtCore, QtGui
import math
tries = 0

def repulse(equipList, scene):
        global tries
        changed = 0
        checked = []
        for (equip1, point1) in equipList.items():
            for (equip2, point2) in equipList.items():
                # print(pos1, pos2)
                if point1 != None and point2 != None and equip1 != equip2 and equip1 not in checked and equip2 not in checked:
                    pos1 = (point1.ellipse.rect().x(), point1.ellipse.rect().y())
                    pos2 = (point2.ellipse.rect().x(), point2.ellipse.rect().y())
                    norm = math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)
                    if  norm < 10:
                        # print(norm)
                        # point1.ellipse.setRect(2*(pos1[0] - 10 +(pos2[0] - pos1[0])), 2*(pos1[1] - 10 +(pos2[1] - pos1[1])),point1.ellipse.rect().width(), point1.ellipse.rect().height() )
                        # point2.ellipse.setRect(2*(pos1[0] + 10 -(pos2[0] - pos1[0])), 2*(pos1[1] + 10 -(pos2[1] - pos1[1])),point1.ellipse.rect().width(), point1.ellipse.rect().height() )
                        newpos = (pos1[0] - 10 +(pos2[0] - pos1[0]), pos1[1] - 10 +(pos2[1] - pos1[1]))
                        point1.BRUSH = QtCore.Qt.blue
                        point2.BRUSH = QtCore.Qt.blue
                        # print("\"",equip1.name, equip2.name, "\"")
                        checked.append(equip1)
                        checked.append(equip2)
                        changed = 1
        scene.update()
        if changed == 1:
            tries += 1
            print(tries)
            if tries <= 5:
                repulse(equipList, scene)
            else:
                tries = 0
                return
