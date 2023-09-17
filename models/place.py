#!/usr/bin/python3
""" This module is a definition of a Place class """
from models.base_model import BaseModel


class Place(BaseModel):
    """ This class represents place objects

        Attributes:
            city_id (str): The City id.
            user_id (str): The user’s id.
            name (str): The place’s name.
            description (str): The place’s description.
            number_rooms (int): Number of rooms in the place.
            number_bathrooms (int): Number of bathrooms available in the place
            max_guest (int): Max permissible number of guests for the place
            price_by_night (int): The nightly rental rate of the place
            latitude (float): Geographical latitude coordinate of the place
            longitude (float): Geographical longitude coordinate of the place.
            amenity_ids (list): List of IDs representing place's amenities
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
