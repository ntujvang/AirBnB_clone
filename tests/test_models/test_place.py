#!/usr/bin/python3
'''
This is the 'test_place' module.

test_amenity uses unittest to test the 'models/place' module.
All credit for this module goes to Danton Rodriguez
(https://github.com/p0516357)
'''
import unittest
from models.place import Place
import datetime


class TestBaseModel(unittest.TestCase):
    """Test for BaseModel class """
    def setUp(self):
        """sets up objects for testing later"""
        self.test_model1 = Place()
        self.test_model2 = Place()

    def test_basic_setup(self):
        """test for to_json method of BaseModel class """
        self.assertTrue(hasattr(self.test_model1, "name"))
        self.assertTrue(hasattr(self.test_model1, "city_id"))
        self.assertTrue(hasattr(self.test_model2, "user_id"))
        self.assertTrue(hasattr(self.test_model1, "number_rooms"))
        self.assertTrue(hasattr(self.test_model2, "latitude"))
        self.assertTrue(hasattr(self.test_model1, "amenities"))
        self.assertTrue(self.test_model1.id != self.test_model2.id)
        m1c = self.test_model1.created_at
        m2c = self.test_model2.created_at
        self.assertTrue(m1c != m2c)
        self.assertTrue(type(m1c) is datetime.datetime)
        m1_attr = self.test_model1.number_rooms
        self.assertTrue(type(m1_attr) is int)
        m1_attr = self.test_model1.latitude
        self.assertTrue(type(m1_attr) is float)
        m1_attr = self.test_model1.name
        self.assertTrue(type(m1_attr) is str)

    def test_save(self):
        """testing whether save updates the updated_at attribute"""
        m1u = self.test_model1.updated_at
        self.test_model1.save()
        m1u_saved = self.test_model1.updated_at
        self.assertFalse(m1u == m1u_saved)

if __name__ == '__main__':
    unittest.main()
