#!/usr/bin/python3
'''
This is the 'state' module.

state contains the 'State' class, a sub-class of BaseModel.
'''


class State(BaseModel):
    '''This is the 'State' class.

    State contains one public attribute, 'name'.
    '''
    def __init__(self):
        '''This is the initialization function.
        '''
        self.name = ''
