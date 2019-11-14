#!/usr/bin/python3
""" testing BaseModel """


import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ test basemodel """

    testing_class = BaseModel

    def test_create(self):
        x = self.testing_class()
        self.assertIsInstance(x, self.testing_class)
        self.assertIsInstance(x.id, str)
        self.assertIsInstance(x.created_at, datetime)
        self.assertIsInstance(x.updated_at, datetime)

    def test_dict(self):
        x = self.testing_class()
        xd = x.to_dict()
        y = self.testing_class(**xd)
        self.assertEqual(xd, y.to_dict())
