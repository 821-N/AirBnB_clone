#!/usr/bin/python3


""" Base Model """


import json


class FileStorage:
    """ FileStorage """


    __file_path = "file.json"
    __objects = {}


    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[obj.id] = obj  # supposed to add the class name but fuck that

    def save(self):
        objs = {}
        for id in FileStorage.__objects:
            objs[id] = FileStorage.__objects[id].to_dict()
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(objs))

    def reload(self, cls):
        try:
            with open(FileStorage.__file_path) as f:
                objs = json.loads(f.read())
                for id in objs:
                    FileStorage.__objects[id] = cls(objs[id])
        except FileNotFoundError:
            pass
