#!/usr/bin/python3
'''
This is the 'city' module.

city contains the class 'City', which is a sub-class of BaseModel.
'''


class City(BaseModel):
    '''This is the 'City' class.

    City contains two public attributes: 'state_id' and 'name'.
    '''
    def __init__(self):
        '''This is the initialization function.
        '''
        self.state_id = ''
        self.name = ''
