from pygeocoder import Geocoder


class GPScoord():
    def __init__(self):
        '''
        Set the locator and initialize the number of succes and the number of tries
        '''
        self.geolocator = Geocoder()
        self.succes = 0
        self.timestried = 0

    def find(self,eqpmt):
        '''
        Try 20 times to get the GPS coordinates from the geolocator
        '''
        try:
            self.timestried += 1
            loc = self.geolocator.geocode(str(eqpmt.adresse)+', Toulouse, France')
            if loc == None:
                print('GPS coordinates are missing for', eqpmt.name)
            else:
                eqpmt.coords = loc[0].coordinates
                self.succes +=1
                self.timestried = 0
        except:
            if self.timestried <= 20:
                print('Error : retrying')
                self.find(eqpmt)
            else:
                print('Tried 20 times, can\'t reach out, GPS coorinates are missing for', eqpmt.name)
                self.timestried = 0

    def findall(self, eqpmtlist):
        '''
        Read through the list and use 'find' on each equipment in it
        '''
        for eqpmt in eqpmtlist:
            self.find(eqpmt)


