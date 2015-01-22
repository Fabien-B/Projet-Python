from PyQt4 import QtCore, QtGui

class Dialogue(QtGui.QDialog):

    finishedSignal = QtCore.pyqtSignal(list)

    def __init__(self, appli):
        super(Dialogue, self).__init__()
        self.dialog = None
        self.appli = appli

    def accept(self):
        super().accept()
        proxy = self.dialog.lineEditProxy.text()
        port = self.dialog.lineEditPort.text()
        user = self.dialog.lineEditUser.text()
        password = self.dialog.lineEditPassword.text()
        self.finishedSignal.emit([proxy,port,user,password])
