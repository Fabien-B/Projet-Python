import r_w_fichier
import Cache_use
import Get_GPS
from PyQt4 import QtGui
import sys
import ihm
import filtres
import carte

FILENAME = 'data/ES2011.xls'
my_cache = Cache_use.Cache('.cache/')
my_locator = Get_GPS.GPScoord(my_cache)


if not my_cache.isalive('equipmentList.cache'):
    equipmentList = []
    r_w_fichier.import_file(FILENAME, equipmentList)
    my_cache.save(equipmentList, 'equipmentList.cache')
    print('First use')
else:
    equipmentList = my_cache.rescue('equipmentList.cache')
    print('Equipment loaded from cache')

equipmentList = my_locator.findall(equipmentList)
# equipmentList = my_locator.get_random(equipmentList)


for equip in equipmentList:
    filtres.create_set(equip)

def affiche():
    fenetre = QtGui.QMainWindow()
    appli = ihm.Ihm()
    appli.setupUi(fenetre)
    appli.built()
    appli.set_equipements(equipmentList)
    fenetre.show()
    return app.exec_()


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    sys.exit(affiche())