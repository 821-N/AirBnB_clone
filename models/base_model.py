#!/usr/bin/python3


""" Base Model """


from uuid import uuid4
from datetime import datetime
from models.engine.file_storage import FileStorage


def read_datetime(iso):
    """ 2019-11-09T15:10:22.860383 """
    return datetime(
        int(iso[:4]), int(iso[5:7]), int(iso[8:10]),
        int(iso[11:13]), int(iso[14:16]), int(iso[17:19]),
        int(float(iso[19:]) * 1000000)
    )


class BaseModel:
    """ BaseModel """

    def __init__(self, *args, **kwargs):
        """ init """
        if kwargs:
            self.id = kwargs["id"]
            self.created_at = read_datetime(kwargs["created_at"])
            self.updated_at = read_datetime(kwargs["updated_at"])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            FileStorage.new(None, self)

    def __str__(self):
        """ str """
        return "[%s] (%s) %s" % (self.__class__.__name__, self.id, self.
                                 __dict__)

    def save(self):
        """ save """
        self.updated_at = datetime.now()
        FileStorage.save(None)

    def to_dict(self):
        """ to_dict """
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
