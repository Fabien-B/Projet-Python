import requests
from PyQt4 import QtCore

class Tisseo(QtCore.QObject):
    """Classe qui gère l'envoie et la réception de requètes
    à l'API Tisseo"""

    closetASignal = QtCore.pyqtSignal(tuple)
    railGettedSignal = QtCore.pyqtSignal(list)
    errorSignal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Tisseo,self).__init__()
        self.proxy = None

    def get_closest_sa(self, lat, lon, point=None, isItineraire = False, departurePoint=0):
        """
        Trouve l'arret Tisseo le plus proche de puis des coordonnés GPS données
        :param lat: Latitude
        :param lon: Longitude
        :param point:
        :param isItineraire:
        :param departurePoint:
        :return:
        """
        print(lat, lon)
        url="""https://api.tisseo.fr/v1/stop_points.json?sortByDistance=1&number=3&displayCoordXY=1&bbox={}%2C{}%2C{}%2C{}&key=a65ccc5d3b7d6d99063240434ef117d54""".format(lon-0.1,lat-0.1,lon+0.1,lat+0.1)
        if self.proxy == None:
            r = requests.get(url)
        else:
            r = requests.get(url, proxies= self.proxy)
        ans = r.json()['physicalStops']['physicalStop'][0]['stopArea']
        rep = (ans['name'], float(ans['y']), float(ans['x']), point, isItineraire, departurePoint)
        self.closetASignal.emit(rep)

    def getinfo(self, keyword):
        url = """https://api.tisseo.fr/v1/places.json?term="{}"&key=a65ccc5d3b7d6d99063240434ef117d54""".format(keyword)
        if self.proxy == None:
            r = requests.get(url)
        else:
            r = requests.get(url, proxies=self.proxy)
        a = r.json()['placesList']['place']
        return a

    def gettrail(self, arret1, arret2):
        """
        Cherche le trajet le plus rapide à l'heure à laquelle la requète est
        envoyée entre 2 arrets
        :param arret1: arret de départ
        :param arret2: arret d'arrivée
        :return: Réponse de l'API prétraitée
        """
        url="""http://api.tisseo.fr/v1/journeys.json?departurePlace={}&arrivalPlace={}&number=1&displayWording=1&key=a65ccc5d3b7d6d99063240434ef117d54""".format(arret1,arret2)
        if self.proxy == None:
            r = requests.get(url)
        else:
            r = requests.get(url, proxies=self.proxy)
        a = r.json()
        try:
            a = a['routePlannerResult']['journeys'][0]['journey']['chunks']
        except KeyError:
            self.errorSignal.emit('Aucun trajet trouvé')
            return None
        return a

    def extractlinecoord(self, answer):
        """
        A partir de la réponse du trajet entre deux arrets
        extrait la liste des coordonées des points constituant
        le trajet et la liste des coordonnées des arrets
        :param answer: Réponse de l'API prétraitée
        :return: (Liste des coordonnées trajet, Liste des coordonnées arrets)
        """
        patheslines = []
        stoppoint = []
        for i in range(len(answer)):
            try:
                nontreat = answer[i]['service']['wkt'].strip('LINESTRING ()').split(', ')
                tupled = [tuple(nontreat[i].split()) for i in range(len(nontreat))]
                patheslines.append(tupled)
            except KeyError:
                try:
                    nontreat = answer[i]['street']['wkt'].strip('MULTILINESTRING (())\"').split(', ')
                    tupled = [tuple(nontreat[i].strip('()').split()) for i in range(len(nontreat))]
                    patheslines.append(tupled)
                except KeyError:
                    try:
                        nontreat = answer[i]['stop']['connectionPlace']
                        tupled = tuple((nontreat['longitude'], nontreat['latitude']))
                        stoppoint.append(tupled)
                    except KeyError:
                        pass

        return (patheslines, stoppoint)

    def extractinstruct(self, answer):
        """
        A partir de la réponse de l'API extrait la liste des
        instructions nécessaire au bon déroulement du trajet
        :param answer: Réponse de l'API prétraitée
        :return: La liste des instructions
        """
        instructlist =[]
        for i in range(len(answer)):
            try:
                partie = answer[i]['stop']['text']['text']
            except KeyError:
                try:
                    partie = answer[i]['street']['text']['text']
                except KeyError:
                    partie = answer[i]['service']['text']['text']
            instructlist.append(partie)
        return instructlist

    def setproxy(self, list):
        """
        Parmatre un proxy pour les requètes Tisseo
        :param list: La liste contenant les paramtres proxy
        [Host, Port, UserName, PassWord]
        :return:
        """
        if list[0]=='':
            self.proxy = None
        else:
            self.proxy = 'http://' + str(list[2]) + ":" + str(list[3]) + "@" + str(list[0]) + ':' + str(list[1])

