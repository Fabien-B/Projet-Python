from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QWidget, QListWidgetItem

from window import Ui_MainWindow


class Ihm(Ui_MainWindow):
    """ Widget displaying information about a Flight """

    def __init__(self):
        super(Ihm, self).__init__()

    def built(self):
        print('coucou')
