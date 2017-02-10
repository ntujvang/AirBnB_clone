'''
This is the 'review' module.

review contains the class 'Review', which is a sub-class of BaseModel.
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''This is the 'Review' class.

    Review contains three public attributes: 'place_id', 'user_id', 'text'.
    '''
    def __init__(self):
        '''This is the initialization method.
        '''
        self.place_id = ''
        self.user_id = ''
        self.text = ''