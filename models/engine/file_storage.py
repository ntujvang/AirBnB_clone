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
    def __init__(self):
        '''This is the initialization of FileStorage.
        '''
        self.__file_path = "hbnb.json"
        self.__objects = {}

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
        with open(self.__file_path, mode="r+", encoding='utf-8') as fn:
            fn.write(json.dumps(self.__objects))

    def reload(self):
        '''This is the 'reload' instance.
        Deserializes the JSON file to __objects.
        If JSON file does not exist, do nothing.

        Return: __object or nothing
        '''
        with open(self.__file_path, mode='r+', encoding='utf-8') as fn:
            self.__objects = json.loads(fn.read())
