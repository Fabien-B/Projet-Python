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
            print('Unexpected error', sys.exc_info()[0])
            raise

    def isempty(self):
        if not os.path.exists(self.path) or not os.listdir(self.path):
            return True
        else:
            return False