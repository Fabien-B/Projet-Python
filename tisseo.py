import requests

def get_closest_sa(lat,lon):
    url="""https://api.tisseo.fr/v1/stop_points.json?sortByDistance=1&number=3&displayCoordXY=1&bbox={}%2C{}%2C{}%2C{}&key=a65ccc5d3b7d6d99063240434ef117d54""".format(lon-0.1,lat-0.1,lon+0.1,lat+0.1)
    r = requests.get(url)
    ans = r.json()['physicalStops']['physicalStop'][0]['stopArea']
    rep = (ans['name'], float(ans['y']), float(ans['x']))
    print(rep)
    return rep


def getinfo(keyword):
    url="""https://api.tisseo.fr/v1/places.json?term="{}"&key=a65ccc5d3b7d6d99063240434ef117d54""".format(keyword)
    r = requests.get(url)
    a=r.json()['placesList']['place']
    return a