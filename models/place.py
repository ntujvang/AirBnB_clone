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
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    number_rooms = 0
    latitude = 0.0
    longitude = 0.0
    amenities = []

    def __init__(self, *args, **kwargs):
        '''This is the initialization method.
        '''
        super().__init__(*args, **kwargs)
