__author__ = 'fabien'
import carte
import sys
from PyQt4 import QtCore, QtGui, QtNetwork

app = QtGui.QApplication(sys.argv)
fenetre = QtGui.QMainWindow()

ca = carte.Carte()
ca.setupUi(fenetre)
ca.build()
fenetre.show()
ca.finish()
#ca.download(44.98342,1.71525,14)
#ca.download(43.56491, 1.47881)
app.exec_()