import requests

class Tisseo():
    def __init__(self):
        self.proxy = None

    def get_closest_sa(self, lat,lon):
        url="""https://api.tisseo.fr/v1/stop_points.json?sortByDistance=1&number=3&displayCoordXY=1&bbox={}%2C{}%2C{}%2C{}&key=a65ccc5d3b7d6d99063240434ef117d54""".format(lon-0.1,lat-0.1,lon+0.1,lat+0.1)
        if self.proxy == None:
            r = requests.get(url)
        else:
            r = requests.get(url, proxies= self.proxy)
        ans = r.json()['physicalStops']['physicalStop'][0]['stopArea']
        rep = (ans['name'], float(ans['y']), float(ans['x']))
        print(rep)
        return rep


    def getinfo(self, keyword):
        url="""https://api.tisseo.fr/v1/places.json?term="{}"&key=a65ccc5d3b7d6d99063240434ef117d54""".format(keyword)
        if self.proxy == None:
            r = requests.get(url)
        else:
            r = requests.get(url, proxies=self.proxy)
        a=r.json()['placesList']['place']
        return a

    def gettrail(self, arret1, arret2):
        url="""http://api.tisseo.fr/v1/journeys.json?departurePlace={}&arrivalPlace={}&number=1&displayWording=1&key=a65ccc5d3b7d6d99063240434ef117d54""".format(arret1,arret2)
        if self.proxy == None:
            r = requests.get(url)
        else:
            r = requests.get(url, proxies=self.proxy)
        a=r.json()
        a = a['routePlannerResult']['journeys'][0]['journey']['chunks']
        # ['wkt'].strip('LINESTRING ()').split()
        return a

    def extractlinecoord(self, answer):
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
        if list[0]=='':
            self.proxy = None
        else:
            self.proxy = 'http://' + str(list[2]) + ":" + str(list[3]) + "@" + str(list[0]) + ':' + str(list[1])

