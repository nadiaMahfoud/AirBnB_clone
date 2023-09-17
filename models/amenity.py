#!/usr/bin/python3
""" This module is a definition of an Amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ This class represents an Amenity

        Attributes:
        name (str): The amenity’s name
    """
    name = ""
