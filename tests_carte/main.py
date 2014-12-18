__author__ = 'fabien'
import cartesimple
import sys
from PyQt4 import QtCore, QtGui, QtNetwork

app = QtGui.QApplication(sys.argv)
fenetre = QtGui.QMainWindow()

ca = cartesimple.Carte()
ca.setupUi(fenetre)
ca.build()
fenetre.show()
ca.finish()
app.exec_()