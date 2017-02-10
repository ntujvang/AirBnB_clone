#!/usr/bin/python3
from models.base_model import BaseModel
'''
This is the 'state' module.

state contains the 'State' class, a sub-class of BaseModel.
'''


class State(BaseModel):
    '''This is the 'State' class.

    State contains one public attribute, 'name'.
    '''
    def __init__(self, *args, **kwargs):
        '''This is the initialization function.
        '''
        super().__init__(*args, **kwargs)
        self.name = ''
