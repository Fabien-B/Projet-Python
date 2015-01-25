from PyQt4 import QtCore, QtGui


class Cache_Dialogue(QtGui.QDialog):

    def __init__(self, appli):
        super(Cache_Dialogue, self).__init__()
        self.dialog = None
        self.appli = appli

