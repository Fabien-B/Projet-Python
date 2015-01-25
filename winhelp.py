from PyQt4 import QtCore, QtGui
import help


class Help(QtGui.QDialog):

    changerImageSignal = QtCore.pyqtSignal(int)

    def __init__(self,appli):
        super(Help, self).__init__()
        self.dialog = None
        self.appli = appli
        self.index = 1

    def next(self):
        if self.index < 9:
            self.index += 1
        else:
            self.index = 1
        self.changerImageSignal.emit(self.index)

    def prec(self):
        if self.index > 1:
            self.index -= 1
        else:
            self.index = 9
        self.changerImageSignal.emit(self.index)
