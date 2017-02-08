#!/usr/bin/python3
import json, os

'''
This is the file_storage module.

file_storage contains one class: FileStorage; two private attributes: file_path,
objects; and four instances: all, new, save, reload.

'''


class FileStorage:
    '''This is the FileStorage class.
    '''
    __file_path = 'hbnb.json'
    __objects = {}

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

    def save(self):
        '''This is the 'save' instance.
        Serializes __objects to JSON file

        Return: JSON file
        '''
        with open(self.__file_path, 'w+', encoding='utf-8') as fn:
            fn.write(self.to_json())

    def reload(self):
        '''This is the 'reload' instance.
        Deserializes the JSON file to __objects.
        If JSON file does not exist, do nothing.

        Return: __object or nothing
        '''
        if os.path.isfile(self.__file_path) is True:
            with open(self.__file_path, 'w+', encoding='utf-8') as fn:
                self.__objects = json.load(fn)
        else:
            pass
