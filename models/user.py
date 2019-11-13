#!/usr/bin/python3
""" User class """


from models.base_model import BaseModel


class User(BaseModel):
    """ user """

    def __init__(self, *args, **kwargs):
        """ init """
        if kwargs:
            self.email = kwargs["email"]
            self.password = kwargs["password"]
            self.first_name = kwargs["first_name"]
            self.last_name = kwargs["last_name"]
        else:
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
        BaseModel.__init__(self, *args, **kwargs)

    def to_dict(self):
        """ to dict """
        d = BaseModel.to_dict(self)
        d["email"] = self.email
        d["password"] = self.password
        d["first_name"] = self.first_name
        d["last_name"] = self.last_name
        return d  # eez nuts
