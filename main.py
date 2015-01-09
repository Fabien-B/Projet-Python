from PyQt4 import QtCore
import r_w_fichier
import Cache_use
import Get_GPS
from PyQt4 import QtGui
import sys
import ihm
import threading

FILENAME = 'data/ES2011.xls'


class Importeur(QtCore.QObject):
    cache_charging_signal = QtCore.pyqtSignal(list)
    def __init__(self,appli):
        QtCore.QObject.__init__(self)
        self.appli=appli
        self.my_cache = Cache_use.Cache('.cache/')
        self.my_locator = Get_GPS.GPScoord(self.my_cache)


    def charging(self,equipmentList):
        self.appli.monFiltre.create_set(equipmentList)
        self.appli.monFiltre.equip_set(equipmentList)
        self.appli.addcheckbox()


    def get_equipment(self):
        if not self.my_cache.isalive('equipmentList.cache'):
            equipmentList = []
            r_w_fichier.import_file(FILENAME, equipmentList)
            self.my_cache.save(equipmentList, 'equipmentList.cache')
            print('First use')
        else:
            self.cache_charging_signal.emit(['cache'])
            equipmentList = self.my_cache.rescue('equipmentList.cache')
            print('Equipment loaded from cache')

        equipmentList = self.my_locator.findall(equipmentList)
        #equipmentList = self.my_locator.get_random(equipmentList)
        if equipmentList != None:
            self.charging(equipmentList)




def run():
    fenetre = QtGui.QMainWindow()
    appli = ihm.Ihm(fenetre)
    appli.setupUi(fenetre)
    appli.built()
    fenetre.show()

    monImporteur=Importeur(appli)
    monImporteur.my_locator.succesSignal.connect(appli.notif_chrgmt_equip)
    monImporteur.cache_charging_signal.connect(appli.notif_chrgmt_equip)
    threadImportation = threading.Thread(None,monImporteur.get_equipment)
    threadImportation.start()
    return (app.exec_(),monImporteur.my_locator)




if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    threadImportation = None
    (retour, locator) = run()
    locator.odre_arret()
    sys.exit()
