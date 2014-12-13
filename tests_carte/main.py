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
app.exec_()