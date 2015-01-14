import pickle
import os
import sys


class Cache():
    def __init__(self, path):
        self.path = path
        if not os.path.exists(path):
            os.makedirs(path)

    def save(self, obj, fle):
        """Puts the data into the cache"""
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
        """Gets the data from the cache"""
        try:
            with open(str(self.path)+str(fle), 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            print('Error : This file does not exist.')
        except:
            print('Unexpected error', sys.exc_info()[0])
            raise

    def erase(self, fle):
        """Deletes the cache"""
        try:
            os.remove(str(self.path)+str(fle))
        except FileNotFoundError:
            print('Error : This file does not exist.')
        except:
            print('Unexpected error', sys.exc_info()[0])
            raise

    def isempty(self):
        """Test to know if the cache is empty or not"""
        if not os.path.exists(self.path) or not os.listdir(self.path):
            return True
        else:
            return False

    def isalive(self, fle):
        if os.path.exists(self.path+str(fle)):
            return True
        else:
            return False