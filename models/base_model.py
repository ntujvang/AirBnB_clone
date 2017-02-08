#!/usr/bin/python3

import datetime, uuid, storage

class BaseModel():

    def __init__(self, id='', created_at='', updated_at=''):
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.datetime.utcnow())
        self.updated_at = str(datetime.datetime.utcnow())

    def save(self):
        self.updated_at = str(datetime.datetime.utcnow())

    def to_json(self):
        my_dict = self.__dict__
        my_dict['__class__'] = type(self).__name__
        return my_dict

    def __str__(self):
        class_name = type(self).__name__
        id_string = str(self.id)
        return "[" + class_name + "] (" + id_string + str(self.__dict__) + ")"
