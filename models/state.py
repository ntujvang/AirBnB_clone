#!/usr/bin/python3
'''
This is the 'state' module.

state contains the 'State' class, a sub-class of BaseModel.
'''


class State(BaseModel):
    '''This is the 'State' class.
    '''
    def __init__(self):
        '''This is the initialization function.

        This function contains one attribute, 'name'.
        '''
        self.name = ''
