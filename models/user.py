#!/usr/bin/python3
""" This module is a definition of a User class """
from models.base_model import BaseModel


class User(BaseModel):
    """ This class represents the User objects

        Attributes:
            email (str): The user’s email
            password (str): The user’s password.
            first_name (str): The user’s First name
            last_name (str): The user’s Last name
    """

    email = " "
    password = " "
    first_name = " "
    last_name = " "
