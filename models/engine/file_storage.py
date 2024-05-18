#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from models.user import User
from hashlib import md5


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            tempDict = {}
            for key, value in self.__objects.items():
                if value.__class__ == cls or cls == value.__class__.__name__:
                    if "password" in value.__dict__:
                        hpwd = md5()
                        hpwd.update(value.__dict__["password"].encode("utf-8"))
                        value.__dict__["password"] = hpwd.hexdigest()
                    tempDict[key] = value
            return tempDict
        else:
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, "w") as f:
            temp = {}
            temp.update(self.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """Deletes the Object from storage dictionary"""
        if obj is None:
            return

        temp = {}
        temp.update(self.__objects)
        for key, val in temp.items():
            if val == obj:
                del self.__objects[key]

    def reload(self):
        """Loads storage dictionary from file"""
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        try:
            temp = {}
            with open(self.__file_path, "r") as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val["__class__"]](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """reloads and deserialize JSON file ot Objects"""
        self.reload()
