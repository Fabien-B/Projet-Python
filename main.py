import r_w_fichier
import Cache_use

FILENAME='data/ES2011.xls'
my_cache = Cache_use.Cache('.cache/')

if my_cache.isempty():
    equipmentList=[]
    r_w_fichier.import_file(FILENAME,equipmentList)
    my_cache.save(equipmentList, 'equipmentList.c')
    print('First use')
else:
    equipmentList = my_cache.rescue('equipmentList.c')
    print('From cache')