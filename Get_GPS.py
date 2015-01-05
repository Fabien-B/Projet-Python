import pygeocoder
import random

class GPScoord():
    """
    Class used for getting the GPS coordinates
    """
    def __init__(self, cache):
        """
        Set the locator and initialize the number of successes and the number of tries
        """
        self.geolocator = pygeocoder.Geocoder()
        self.cache = cache
        self.success = 0
        self.timestried = 0



    def find(self,adresse, name='unknow Name'):
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
                return loc[0].coordinates

        except:
            if self.timestried <= 20:
                print('Error : retrying')
                self.find(adresse,name)
            else:
                print('Tried 20 times, can\'t reach out, GPS coordinates are missing for', name)
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
                    eqpmtlist[i].coords = self.find(eqpmtlist[i].adresse,eqpmtlist[i].name)
            else:
                self.success +=1
            self.cache.save(eqpmtlist, 'equipmentList.cache')
        return eqpmtlist

    def get_random(self, eqpmtlist):
         for i in range(len(eqpmtlist)):
            if eqpmtlist[i].coords == None:
                if eqpmtlist[i].adresse == eqpmtlist[i-1].adresse:
                    eqpmtlist[i].coords = eqpmtlist[i-1].coords
                    self.success += 1
                else:
                    eqpmtlist[i].coords = (random.randint(43571,43649)/1000,random.randint(1405, 1504)/1000)
            else:
                self.success +=1
            self.cache.save(eqpmtlist, 'equipmentList.cache')
         return eqpmtlist


