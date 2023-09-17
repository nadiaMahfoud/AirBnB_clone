#!/usr/bin/python3
""" This module is a definition of a City class """
from models.base_model import BaseModel


class City(BaseModel):
    """ This class represents a City

        Attributes:
        state_id (str): The state’s id
        name (str): The city’s name
    """
    state_id = " "
    name = " "
