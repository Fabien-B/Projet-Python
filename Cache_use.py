import pickle
import os
import sys

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
        except FileNotFoundError:
            print('Error : This file does not exist.')
        except:
            print('Unexpected error', sys.exc_info()[0])
            raise


    def rescue(self, fle):
        try:
            with open(str(self.path)+str(fle), 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            print('Error : This file does not exist.')
        except:
            print('Unexpected error', sys.exc_info()[0])
            raise

    def erase(self, fle):
        try:
            os.remove(str(self.path)+str(fle))
        except FileNotFoundError:
            print('Error : This file does not exist.')
        except:
<<<<<<< HEAD
            print('Unexpected error', sys.exc_info()[0])
            raise

    def isempty(self):
        if not os.path.exists(self.path) or not os.listdir(self.path):
            return True
        else:
            return False
=======
            print('ET MERDE')



my_cache = Cache('cache/')
a = [12, 24, 62]
my_cache.save(a, 'plop2.c')
b = my_cache.rescue('plop2.c')
print(b)
my_cache.erase('plop2.c')
>>>>>>> bc68dcaa0795e4920cde70781c2dd1df6b884de9
