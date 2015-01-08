import pygeocoder
import random
from PyQt4 import QtCore
import time

class GPScoord(QtCore.QObject):
    """
    Class used for getting the GPS coordinates
    """
    succesSignal = QtCore.pyqtSignal(list)

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



    def find(self,adresse, name='unknow Name', i=0,j=0):
        """
        Try 20 times to get the GPS coordinates from the geolocator with addresses
        """
        try:
            self.timestried += 1
            print('Getting coordinates for', name)
            loc = self.geolocator.geocode(str(adresse)+', Toulouse, France')
            if loc == None:
                print('GPS coordinates are missing for', name)
                return None
            else:
                self.success +=1
                self.timestried = 0
                self.succesSignal.emit([name,i,j])
                return loc[0].coordinates

        except:
            if self.timestried <= 20:
                print('Error : retrying')
                self.find(adresse,name,i,j)
            else:
                print('Tried 20 times, can\'t reach out, GPS coordinates are missing for', name)
                self.succesSignal.emit(["échec",name,i,j])
                self.timestried = 0
                return None


    def findall(self, eqpmtlist):
        """
        Read through the list pu the same coordinate if the adress is the same as before
         else use 'find' on each equipment in the list.
        """
        for i in range(len(eqpmtlist)):
            if eqpmtlist[i].coords == None:
                if eqpmtlist[i].adresse == eqpmtlist[i-1].adresse:
                    eqpmtlist[i].coords = eqpmtlist[i-1].coords
                    self.success += 1
                else:
                    eqpmtlist[i].coords = self.find(eqpmtlist[i].adresse,eqpmtlist[i].name,i,len(eqpmtlist))
            else:
                self.success +=1
            self.cache.save(eqpmtlist, 'equipmentList.cache')
            if self.arreter:
                return None
        return eqpmtlist

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
                    self.succesSignal.emit([eqpmtlist[i].name,i,len(eqpmtlist)])
            else:
                self.success +=1
            self.cache.save(eqpmtlist, 'equipmentList.cache')
            if self.arreter:
                return None
         return eqpmtlist

    def odre_arret(self):
        self.arreter = True

