#!/usr/bin/python3
""" testing other classes """


from tests.test_models.test_base_model import TestBaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class TestUser(TestBaseModel):
    """ test user"""

    testing_class = User


class TestAmenity(TestBaseModel):
    """ test """

    testing_class = Amenity


class TestCity(TestBaseModel):
    """ test """

    testing_class = City


class TestPlace(TestBaseModel):
    """ test """

    testing_class = Place


class TestReview(TestBaseModel):
    """ test """

    testing_class = Review

    def test_spelling(self):
        """ make sure I spell review correctly
I TOLD YOU MY HANDS WERE COLD"""
        correct = "Review"
        self.assertEqual(self.__class__.__name__, "Test" + correct)
        self.assertEqual(self.testing_class.__name__, correct)


class TestState(TestBaseModel):
    """ test """

    testing_class = State
