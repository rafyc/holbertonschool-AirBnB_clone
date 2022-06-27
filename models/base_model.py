#!/usr/bin/python3

"""
BaseModel class that defines all common attributes/methods for other classes.
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    The BaseModel Class
    """

    def __init__(self):
        """
        Function that init an instance of class BaseModel with uniq ID
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Function that return the string representation.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Function that updates the public instance attribute updated_at with
        the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()

        return instance_dict
