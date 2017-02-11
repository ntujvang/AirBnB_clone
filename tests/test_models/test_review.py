#!/usr/bin/python3
'''
This is the 'test_review' module.

test_review uses unittest to test the 'models/review' module.
All credit for this module goes to Danton Rodriguez
(https://github.com/p0516357)
'''
import unittest
from models.review import Review
import datetime


class TestBaseModel(unittest.TestCase):
    """Test for BaseModel class """
    def setUp(self):
        """sets up objects for testing later"""
        self.test_model1 = Review()
        self.test_model2 = Review()

    def test_basic_setup(self):
        """test for to_json method of BaseModel class """
        self.assertTrue(hasattr(self.test_model1, "place_id"))
        self.assertTrue(hasattr(self.test_model1, "user_id"))
        self.assertTrue(hasattr(self.test_model1, "text"))
        self.assertTrue(self.test_model1.id != self.test_model2.id)
        m1c = self.test_model1.place_id
        m2c = self.test_model2.place_id
        self.assertTrue(m1c == m2c)
        self.assertTrue(type(m1c) is str)

    def test_save(self):
        """testing whether save updates the updated_at attribute"""
        m1u = self.test_model1.updated_at
        self.test_model1.save()
        m1u_saved = self.test_model1.updated_at
        self.assertFalse(m1u == m1u_saved)

if __name__ == '__main__':
    unittest.main()
