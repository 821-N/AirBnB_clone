#!/usr/bin/python3


""" Base Model """


import json


class FileStorage:
    """ FileStorage """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ get __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ add object """
        name = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[name] = obj

    def save(self):
        """ Save data to json file """
        objs = {}
        for id in FileStorage.__objects:
            objs[id] = FileStorage.__objects[id].to_dict()
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(objs))

    def reload(self):
        """ Load data from json file into __objects """
        from models.base_model import BaseModel
        from models.user import User
        models = {
            "BaseModel": BaseModel,
            "User": User
        }

        try:
            with open(FileStorage.__file_path) as f:
                objs = json.loads(f.read())
                for name in objs:
                    classname = name.split(".")[0]
                    if classname not in models:
                        raise ValueError(
                            "Invalid " +
                            "JSON " +
                            "Data: " +
                            "unknown " +
                            "class '" +
                            classname +
                            "'"
                        )
                    FileStorage.__objects[name] = models[classname](
                        **
                        objs[name]
                    )
        except FileNotFoundError:
            pass
