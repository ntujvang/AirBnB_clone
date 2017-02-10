'''
This is the 'review' module.

review contains the class 'Review', which is a sub-class of BaseModel.
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''This is the 'Review' class.

    Review contains three public attributes: 'place_id', 'user_id', 'text'.
    '''
    def __init__(self, *args, **kwargs):
        '''This is the initialization method.
        '''
        if type(args[0]) is dict:
            super().__init__(args[0])
        else:
            super().__init__()

        self.place_id = ''
        self.user_id = ''
        self.text = ''
