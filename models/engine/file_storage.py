#!/usr/bin/python3
'''
This is the file_storage module.

file_storage contains one class: FileStorage; two private attributes: file_path,
objects; and four instances: all, new, save, reload.

'''


import json

class FileStorage:
    '''This is the FileStorage class.
    '''
    def __init__(self, file_path='', objects={}):
        '''This is the initialization of FileStorage.
        '''
        self.__file_path = file_path
        self.__objects = objects

   # @property
   # def file_path(self):
    #    '''This is the getter for file_path.
    #    '''
    #    return self.__file_path

    #@file_path.setter

   # @property
   # def objects(self):
    #    '''This is the getter for objects.
     #   '''
      #  return self.__objects

    #@objects.setter

    def all(self):
        '''This is the 'all' instance

        Return: __objects
        '''
        return self.__objects

    def new(self, obj):
        '''This is the 'new' instance.
        Sets __object as @obj with key obj.id

        @obj: object
        Return: ####fill me in #####
        '''
        self.__objects[obj.id] = obj
        return self.__objects

    def save(self):
        '''This is the 'save' instance.
        Serializes __objects to JSON file

        Return: JSON file
        '''
        return json.dump(self.__objects, self.__file_path)

    def reload(self):
        '''This is the 'reload' instance.
        Deserializes the JSON file to __objects.
        If JSON file does not exist, do nothing.

        Return: __object or nothing
        '''
        with open(self.__file_path, mode='a') as fn:
            return json.load(fn)
