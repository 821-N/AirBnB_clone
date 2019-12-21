#!/usr/bin/python3
""" City class """


from models.base_model import BaseModel


class City(BaseModel):
    """ read the line above this one """

    state_id = ""
    name = ""

    template = {
        "state_id": "",
        "name": ""
    }
