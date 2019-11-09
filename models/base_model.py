#!/usr/bin/python3


""" Base Model """


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ BaseModel """

    def __init__(self):
        """ init """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ str """
        return "[BaseModel] (%d) %s" % (self.id, self.__dict__)

    def save(self):
        """ save """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ to_dict """
        d = self.__dict__
        d["__class__"] = "BaseModel"
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
