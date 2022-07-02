#!/usr/bin/python3

"""
FileStorage class that serializes instances to a JSON file and deserializes
JSON file to instances:
"""

import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json


class FileStorage:
    """
    The FileStorage class
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Function that return the dictionary object
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Function that add elements in the dictionary.
        Args:
            obj: The object to set with key <obj class name>.id
        """
        if obj:
            FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        new_dict = {}
        for keys, values in FileStorage.__objects.items():
            new_dict[keys] = values.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as file:
                new_object_dict = json.load(file)
            for keys, val in new_object_dict.items():
                FileStorage.__objects[keys] = eval(val['__class__'])(**val)
