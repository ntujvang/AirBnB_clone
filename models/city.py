#!/usr/bin/python3
from models.base_model import BaseModel
'''
This is the 'city' module.

city contains the class 'City', which is a sub-class of BaseModel.
'''


class City(BaseModel):
    '''This is the 'City' class.

    City contains two public attributes: 'state_id' and 'name'.
    '''
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        '''This is the initialization function.
        '''
        super().__init__(*args, **kwargs)
