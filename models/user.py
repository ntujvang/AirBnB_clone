#!/usr/bin/python3
from models.base_model import BaseModel
'''
This is the 'user' module.

user contains one class: 'User', which inherits from the BaseModel class.

'''


class User(BaseModel):
    '''This is the 'User' class.
    User contains the attributes: email, password, first_name, last_name.
    '''
    def __init__(self, *args, **kwargs):
        '''This is the initialization function.
        initializes User with class attributes set to empty strings.
        '''
        super().__init__(*args, **kwargs)
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
