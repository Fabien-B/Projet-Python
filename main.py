"""
Premier module de la fonction, chargeant tous les parametres
et lancant l'application
"""

from PyQt4 import QtCore
import r_w_fichier
import cache_use
from PyQt4 import QtGui
import sys
import ihm
import threading

FILENAME = 'data/ES2011.xls'


class Importeur(QtCore.QObject):
    """
    Classe d'importation des donnees,
    get_equipment executee dans un thread separe
    """
    cache_charging_signal = QtCore.pyqtSignal(str)
    equipment_import_finish_signal = QtCore.pyqtSignal(list)

    def __init__(self, appli):
        QtCore.QObject.__init__(self)
        self.appli = appli
        self.my_cache = cache_use.Cache('.cache/')
        self.my_locator = None

    def get_equipment(self):
        """
        Charge les equipements depuis le cache (si il existe) et
        lance la recherche des coordonnees GPS
        """
        if not self.my_cache.isalive('equipmentList.cache'):
            equipment_list = []
            r_w_fichier.import_file(FILENAME, equipment_list)
            self.my_cache.save(equipment_list, 'equipmentList.cache')
        else:
            self.cache_charging_signal.emit('Chargement des '
                                            'équipements depuis le cache ...')
            equipment_list = self.my_cache.rescue('equipmentList.cache')
        self.my_locator.cache = self.my_cache
        equipment_list = self.appli.locator.findall(equipment_list)
        self.appli.equipmentlist = equipment_list
        if equipment_list != None:
            self.equipment_import_finish_signal.emit(equipment_list)
        return 0


def run(main_app):
    """
    Demarre le thread et l'appli
    :return:
    """
    fenetre = QtGui.QMainWindow()
    appli = ihm.Ihm(fenetre)
    appli.setupUi(fenetre)
    appli.built()
    fenetre.show()
    mon_importeur = Importeur(appli)
    mon_importeur.my_locator = appli.locator
    mon_importeur.my_locator.succesSignal.connect(appli.notif_chrgmt_equip)
    mon_importeur.cache_charging_signal.connect(appli.notif_chrgmt_equip)
    mon_importeur.equipment_import_finish_signal.connect(appli.finish_init_with_datas)
    thread_importation = threading.Thread(target=mon_importeur.get_equipment)
    thread_importation.start()
    return (main_app.exec_(), mon_importeur.my_locator)

if __name__ == '__main__':

    Main_app = QtGui.QApplication(sys.argv)
    Threadimportation = None
    (Retour, Locator) = run(Main_app)
    Locator.odre_arret()
    sys.exit(0)
