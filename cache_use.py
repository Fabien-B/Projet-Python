"""
Module definissant la classe gerant le cache
"""


import pickle
import os
import sys


class Cache():
    """
    Classe gerant le cache
    """
    def __init__(self, path):
        self.path = path
        if not os.path.exists(path):
            os.makedirs(path)

    def save(self, obj, fle):
        """Puts the data into the cache"""
        try:
            with open(str(self.path)+str(fle), 'w+b') as files:
                pickle.dump(obj, files)
                return
        except FileNotFoundError:
            print('Error : This file does not exist.')
        except:
            print('Unexpected error', sys.exc_info()[0])
            raise

    def rescue(self, fle):
        """Gets the data from the cache"""
        try:
            with open(str(self.path)+str(fle), 'rb') as files:
                return pickle.load(files)
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
        """
        Check if the file where the cache must be in
        is really existing
        :param fle: the file to check
        :return: Bool
        """
        if os.path.exists(self.path+str(fle)):
            return True
        else:
            return False
