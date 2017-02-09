#!/usr/bin/python3
import json
import os

'''
This is the file_storage module.

file_storage contains one class: FileStorage; two private attributes:
file_path, objects; and four instances: all, new, save, reload.

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
        return FileStorage.__objects

    def new(self, obj):
        '''This is the 'new' instance.
        Sets __object as @obj with key obj.id

        @obj: object
        '''
        FileStorage.__objects[obj.id] = obj

    def save(self):
        '''This is the 'save' instance.
        Serializes __objects to JSON file

        Return: JSON file
        '''
        new_dict = {} #serialized
        for key in FileStorage.__objects.keys():
            new_dict[key] = FileStorage.__objects[key].to_json()
        with open(FileStorage.__file_path, 'w+', encoding='utf-8') as fn:
            json.dump(new_dict, fn)

    def reload(self):
        '''This is the 'reload' instance.
        Deserializes the JSON file to __objects.
        If JSON file does not exist, do nothing.

        Return: __object or nothing
        '''
        from models.base_model import BaseModel
        if os.path.isfile(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r+', encoding='utf-8') as fn:
                obj = json.load(fn)
                for key in obj.keys():
                    FileStorage.__objects[key] = BaseModel(obj[key])
        else:
            pass
