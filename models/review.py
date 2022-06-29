#!/usr/bin/python3

"""
The class Review that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ The Review Class
    """
    place_id = ""
    user_id = ""
    text = ""
