#!/usr/bin/python3
"""Definition of the BaseModel class."""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """ This class represents the Base model for all the classes
    in project 0x00. AirBnB clone - The console """

    def __init__(self, *args, **kwargs):
        """ Initialization of a new Base
            Args:
                *args: A list of arguments
                **kwargs: dictionary of the key values arguments
        """
        if kwargs is not None and kwargs != {}:
            for arg_name in kwargs:
                if arg_name == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif arg_name == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[arg_name] = kwargs[arg_name]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """This method returns an official string representation"""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """This method updates the public instance attribute ‘updated_at’ """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """THis method returns a dictionary with all keys/values of __dict__"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict
