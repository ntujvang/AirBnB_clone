#!/usr/bin/python3
import datetime, uuid
from models.engine.file_storage import FileStorage

storage = FileStorage()

class BaseModel():

    def __init__(self, *args, **kwargs):
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
        self.updated_at = str(datetime.datetime.utcnow())
        storage.new(self)
        storage.save()

    def to_json(self):
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        return my_dict

    def __str__(self):
        class_name = type(self).__name__
        id_string = self.id
        return ("[{}] ({}) {}".format(class_name, id_string, self.__dict__))
