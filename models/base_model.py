#!/usr/bin/python3
import datetime
import uuid
from models.engine.file_storage import FileStorage
storage = FileStorage()
'''
This is the 'base_model' module.

base_model contains one class: 'BaseModel'.

BaseModel contains four methods: 'init', 'save', 'to_json', 'str'.
'''


class BaseModel():
    '''This is the BaseModel class.
    '''
    def __init__(self, *args, **kwargs):
        '''This is the initialization method.
        This method sets three attributes: 'id', 'created_at', 'updated_at'
        '''
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.datetime.utcnow())
        self.updated_at = str(datetime.datetime.utcnow())
        for x in args:
            if type(x) is dict:
                self.__dict__ = x
                sotrage.new(x)
            else:
                if kwargs is not {}:
                    for key, value in kwargs:
                        self.key = value
                    storage.new(self)

    def save(self):
        '''This is the save method.
        save updates the updated_at attribute with current date and time.
        save calls on the FileStorage class to save new instances of BaseModel.
        '''
        self.updated_at = str(datetime.datetime.utcnow())
        storage.new(self)
        storage.save()

    def to_json(self):
        '''This is the to_json method.
        The method returns a dictionary with all key/value pairs.

        Returns: dictionary
        '''
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        return my_dict

    def __str__(self):
        '''This is the string method.

        Returns: formatted string to print
        '''
        class_name = type(self).__name__
        id_string = self.id
        return ("[{}] ({}) {}".format(class_name, id_string, self.__dict__))
