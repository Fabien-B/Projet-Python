from PyQt4 import QtCore
import r_w_fichier
import Cache_use
import Get_GPS
from PyQt4 import QtGui
import sys
import ihm
import filtres

FILENAME = 'data/ES2011.xls'

def notif_chrgmt_equip(name,i,j):
    print('\n\n')
    print(name,i,j)
    print('\n\n')


def get_equipment():
    if not my_cache.isalive('equipmentList.cache'):
        equipmentList = []
        r_w_fichier.import_file(FILENAME, equipmentList)
        my_cache.save(equipmentList, 'equipmentList.cache')
        print('First use')
    else:
        equipmentList = my_cache.rescue('equipmentList.cache')
        print('Equipment loaded from cache')

    equipmentList = my_locator.findall(equipmentList)

    # for equip in equipmentList:
    #     filtres.create_set(equip)

    return equipmentList

my_cache = Cache_use.Cache('.cache/')
my_locator = Get_GPS.GPScoord(my_cache)

QtCore.QObject.connect(my_locator, QtCore.SIGNAL("address_found(const QString & text,int,int)"), notif_chrgmt_equip)




def run():
    fenetre = QtGui.QMainWindow()
    appli = ihm.Ihm()
    appli.setupUi(fenetre)
    appli.built()
    fenetre.show()
    equipmentList = get_equipment()
    appli.set_equipements(equipmentList)
    for equip in equipmentList:
        filtres.create_set(equip)
        appli.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 240, len(filtres.sets)*22))
    appli.addcheckbox()
    return app.exec_()


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    sys.exit(run())
