#!/usr/bin/python3
""" testing BaseModel """


import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ test basemodel """

    testing_class = BaseModel
    template = {}

    def test_create(self):
        """
        see if making instances
        basically works, mostly
        """
        x = self.testing_class()
        self.assertIsInstance(x, self.testing_class)
        self.assertIsInstance(x.id, str)
        self.assertIsInstance(x.created_at, datetime)
        self.assertIsInstance(x.updated_at, datetime)

    def test_dict(self):
        """
        make sure to_dict works,
        and that the data can be
        restored from this form.
        """
        x = self.testing_class()
        xd = x.to_dict()
        y = self.testing_class(**xd)
        self.assertEqual(xd, y.to_dict())

    def test_attr(self):
        """
        This tests that each sub
        class has all its proper
        attributes, and that the
        default values are right
        """
        x = self.testing_class()
        for name in self.template:
            self.assertEqual(getattr(x, name), self.template[name])
