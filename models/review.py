#!/usr/bin/python3
""" This module is a definition of a Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ This class represents a Review.

        Attributes:
        place_id (str): The place’s id
        user_id (str): The user’s id.
        text (str): The review’s text
    """
    place_id = ""
    user_id = ""
    text = ""
