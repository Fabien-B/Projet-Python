from geopy.geocoders import Nominatim


class GPScoord():
    def __init__(self):
        self.geolocator = Nominatim()
        self.succes = 0

    def find(self,eqpmt):
        try:
            loc = self.geolocator.geocode(str(eqpmt.adresse)+' Toulouse')
            if loc == None:
                print('Coord GPS manquantes pour ', eqpmt.name)
            else:
                eqpmt.coords = (loc.latitude, loc.longitude)
                self.succes +=1
        except:
            print('Error : retrying')
            self.find(eqpmt)

    def findall(self, eqpmtlist):
        for eqpmt in eqpmtlist:
            self.find(eqpmt)


