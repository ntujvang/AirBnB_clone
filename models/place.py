'''
This is the 'place' module.

place contains the class 'Place', which is a sub-class of BaseModel.
'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''This is the 'Place' class.

    Place contains twelve public attributes: 'city_id', 'user_id', 'name',
    'description', 'number_rooms', 'number_bathrooms', 'max_guest',
    'price_by_night', 'number_rooms', 'latitude', 'longitude', 'amenities'
    '''
    def __init__(self):
        '''This is the initialization method.
        '''
        self.city_id = ''
        self.user_id = ''
        self.name = ''
        self.description = ''
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.number_rooms = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenities = []
