import pickle
import os

class Cache:
    def __init__(self, path):
        self.path = path
        if not os.path.exists(path):
            os.makedirs(path)

    def save(self, obj, fle):
        try:
            with open(str(self.path)+str(fle), 'w+b') as f:
                pickle.dump(obj, f)
                return
        except:
            pass


    def rescue(self, fle):
        try:
            with open(str(self.path)+str(fle), 'r+b') as f:
                return pickle.load(f)
        except:
            print('ET MERDE')

    def erase(self, fle):
        try:
            os.remove(str(self.path)+str(fle))
        except:
            print('ET MERDE')



my_cache = Cache('cache/')
a = [12, 24, 62]
my_cache.save(a, 'plop2.c')
b = my_cache.rescue('plop2.c')
print(b)
my_cache.erase('plop2.c')
