import r_w_fichier
import Cache_use
import Get_GPS

FILENAME='data/ES2011.xls'
my_cache = Cache_use.Cache('.cache/')
my_locator = Get_GPS.GPScoord()

if not my_cache.isalive('equipmentList.cache'):
    equipmentList=[]
    r_w_fichier.import_file(FILENAME, equipmentList)
    my_cache.save(equipmentList, 'equipmentList.cache')
    print('First use')
else:
    equipmentList = my_cache.rescue('equipmentList.cache')
    print('Equipment loaded from cache')
equipmentList = my_locator.findall(equipmentList)
my_cache.save(equipmentList, 'equipmentList.cache')