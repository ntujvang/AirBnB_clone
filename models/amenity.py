#!/usr/bin/python3
from models.base_model import BaseModel
'''
This is the 'amenity' module.

amenity contains the class 'Amenity', a sub-class of BaseModel.
'''


class Amenity(BaseModel):
    '''This is the 'Amenity' class.

    The class contains one public attribute, 'name'.
    '''
    def __init__(self):
        '''This is the initialization method.
        '''
        self.name = ''
