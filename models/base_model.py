#!/usr/bin/python3
from datetime import datetime, date, time
import uuid
import models
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
        if len(args) > 0:
            if type(args[0]) is dict:
                self.__dict__ = args[0]
                self.__dict__['created_at'] = datetime.strptime(
                    (self.__dict__['created_at']), "%Y-%m-%d %H:%M:%S.%f")
                self.__dict__['updated_at'] = datetime.strptime(
                    (self.__dict__['updated_at']), "%Y-%m-%d %H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.created_at = datetime.now()
            models.storage.new(self)

    def save(self):
        '''This is the save method.
        save updates the updated_at attribute with current date and time.
        save calls on the FileStorage class to save new instances of BaseModel.
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_json(self):
        '''This is the to_json method.
        The method returns a dictionary with all key/value pairs.

        Returns: dictionary
        '''
        my_dict = self.__dict__
        new_dict = {}
        for i in my_dict.keys():
            if (isinstance(my_dict[i], datetime)):
                new_dict[i] = str(my_dict[i])
            else:
                new_dict[i] = my_dict[i]
        new_dict['__class__'] = self.__class__.__name__
        return new_dict

    def __str__(self):
        '''This is the string method.

        Returns: formatted string to print
        '''
        class_name = self.__class__.__name__
        id_string = self.id
        my_dict = self.__dict__
        return ("[{}] ({}) {}".format(class_name, id_string, my_dict))
