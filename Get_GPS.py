import pygeocoder
import random
from PyQt4 import QtCore
import time

class GPScoord(QtCore.QObject):
    """
    Class used for getting the GPS coordinates
    """
    succesSignal = QtCore.pyqtSignal(str)

    def __init__(self, cache):
        """
        Set the locator and initialize the number of successes and the number of tries
        """
        QtCore.QObject.__init__(self)
        self.geolocator = pygeocoder.Geocoder()
        self.cache = cache
        self.success = 0
        self.timestried = 0
        self.arreter = False
        self.equipmentlist = []



    def find(self,adresse, name='unknow Name', i=0,j=0):
        """
        Try 20 times to get the GPS coordinates from the geolocator with addresses
        """

        try:
            self.timestried += 1
            #print('Getting coordinates for', name)
            loc = self.geolocator.geocode(str(adresse)+', Toulouse, France')
            if loc == None or loc[0].coordinates == (43.604652, 1.444209):
                print('GPS coordinates are missing for', name)
                return None
            else:
                self.success +=1
                self.timestried = 0
                self.succesSignal.emit("Adresse trouvée: {}       {}/{}".format(name,i,j))
                return loc[0].coordinates

        except:
            if self.timestried <= 20:
                print('Error : retrying')
                self.find(adresse,name,i,j)
            else:
                print('Tried 20 times, can\'t reach out, GPS coordinates are missing for', name)
                self.succesSignal.emit("Échec: {}       {}/{}".format(name,i,j))
                self.timestried = 0
                return None


    def findall(self, eqpmtlist = None):
        """
        Read through the list pu the same coordinate if the adress is the same as before
         else use 'find' on each equipment in the list.
        """
        if eqpmtlist != None:
            self.equipmentlist = eqpmtlist
        for i in range(len(self.equipmentlist)):
            if self.equipmentlist[i].coords == None:
                if self.equipmentlist[i].adresse == self.equipmentlist[i-1].adresse:
                    self.equipmentlist[i].coords = self.equipmentlist[i-1].coords
                    self.success += 1
                else:
                    self.equipmentlist[i].coords = self.find(self.equipmentlist[i].adresse,self.equipmentlist[i].name,i,len(self.equipmentlist))
            else:
                self.success +=1
            self.cache.save(self.equipmentlist, 'equipmentList.cache')
            if self.arreter:
                return None
        return self.equipmentlist

    def get_random(self, eqpmtlist):

         for i in range(len(eqpmtlist)):
            if eqpmtlist[i].coords == None:
                if eqpmtlist[i].adresse == eqpmtlist[i-1].adresse:
                    eqpmtlist[i].coords = eqpmtlist[i-1].coords
                    self.success += 1
                else:
                    eqpmtlist[i].coords = (random.randint(43571,43649)/1000,random.randint(1405, 1504)/1000)
                    time.sleep(0.05)
                    print('get random for {}'.format(eqpmtlist[i].name))
                    self.succesSignal.emit("Échec: {}       {}/{}".format(eqpmtlist[i],i,len(eqpmtlist)))
            else:
                self.success +=1
            self.cache.save(eqpmtlist, 'equipmentList.cache')
            if self.arreter:
                return None
         return eqpmtlist

    def setproxy(self, list):
        if list[0] != '':
            proxyline = 'http://' + str(list[2]) + ":" + str(list[3]) + "@" + str(list[0]) + ':' + str(list[1])
            self.geolocator.set_proxy(proxyline)
        else:
            self.geolocator.set_proxy(None)

    def odre_arret(self):
        self.arreter = True
        return

