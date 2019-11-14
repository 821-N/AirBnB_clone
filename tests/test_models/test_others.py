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
    template = {
        "email": "",
        "password": "",
        "first_name": "",
        "last_name": ""
    }


class TestAmenity(TestBaseModel):
    """ test """

    testing_class = Amenity
    template = {
        "name": ""
    }


class TestCity(TestBaseModel):
    """ test """

    testing_class = City
    template = {
        "state_id": "",
        "name": ""
    }


class TestPlace(TestBaseModel):
    """ test """

    testing_class = Place
    template = {
        "city_id": "",
        "user_id": "",
        "name": "",
        "description": "",
        "number_rooms": 0,
        "number_bathrooms": 0,
        "max_guest": 0,
        "price_by_night": 0,
        "latitude": 0.0,
        "longitude": 0.0,
        "amenity_ids": [],
    }


class TestReview(TestBaseModel):
    """ test """

    testing_class = Review
    template = {
        "place_id": "",
        "user_id": "",
        "text": ""
    }

    def test_spelling(self):
        """ make sure I spell review correctly
I TOLD YOU MY HANDS WERE COLD"""
        correct = "Review"
        self.assertEqual(self.__class__.__name__, "Test" + correct)
        self.assertEqual(self.testing_class.__name__, correct)


class TestState(TestBaseModel):
    """ test """

    testing_class = State
    template = {
        "name": ""
    }
