#!/usr/bin/python3

import datetime, uuid, storage

class BaseModel():

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()

    def save(self):
        self.updated_at = datetime.datetime.utcnow()
        storage.save(self)

    def to_json(self):
        if type(self.args) is dict:
            my_dict = self.__dict__
            for x in my_dict.keys():
                if (isinstance(my_dict[x], datetime)):
                    my_dict[x] = str(my_dict[x])
        else:
            my_dict = storage.new(self, args)
        my_dict['__class__'] = type(self).__name__
        return my_dict

    def __str__(self):
        class_name = type(self).__name__
        id_string = str(self.id)
        return ("[{}] ({}) {}".format(class_name, id_string, self.__dict__))
