import r_w_fichier
import Cache_use

FILENAME='data/ES2011.xls'
my_cache = Cache_use.Cache('.cache/')

if not my_cache.isalive('equipmentList.cache'):
    equipmentList=[]
    r_w_fichier.import_file(FILENAME,equipmentList)
    my_cache.save(equipmentList, 'equipmentList.cache')
    print('First use')
else:
    equipmentList = my_cache.rescue('equipmentList.cache')
    print('From cache')