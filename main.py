import r_w_fichier
import Cache_use
import Get_GPS
from PyQt4 import QtGui
import sys
import ihm

FILENAME = 'data/ES2011.xls'
my_cache = Cache_use.Cache('.cache/')
my_locator = Get_GPS.GPScoord()

if not my_cache.isalive('equipmentList.cache'):
    equipmentList = []
    r_w_fichier.import_file(FILENAME, equipmentList)
    my_locator.findall(equipmentList)
    print(my_locator.succes,'addresses found.')
    my_cache.save(equipmentList, 'equipmentList.cache')
    print('First use')
else:
    equipmentList = my_cache.rescue('equipmentList.cache')
    print('From cache')

app = QtGui.QApplication(sys.argv)
fenetre = QtGui.QMainWindow()
appli = ihm.Ihm()
appli.setupUi(fenetre)
appli.built()
fenetre.show()
app.exec_()