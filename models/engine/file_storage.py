#!/usr/bin/python3
""" This module is a definition of a FileStorage class."""
import os
import datetime
import json


class FileStorage:
    """ This class represents the class for storing and retrieving data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ This method returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """This method sets in __objects the obj with <obj class name>.id"""
        obj_key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """This method serializes __objects to JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            serialized_obj = {
                    key: value.to_dict()
                    for key, value in FileStorage.__objects.items()
            }
            json.dump(serialized_obj, f)

    def classes(self):
        """This method returns a valid classes dict &their respective refr"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """ This method reloads the objects that have been stored """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            serialized_obj = json.load(f)
            serialized_obj = {
                    key: self.classes()[value["__class__"]](**value)
                    for key, value in serialized_obj.items()
            }
            FileStorage.__objects = serialized_obj

    def attributes(self):
        """This method returns valid attributes & their types for class name"""
        base_model_attrs = {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime
                }

        user_attrs = {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
                }

        state_attrs = {
                "name": str
                }

        city_attrs = {
                "state_id": str,
                "name": str
                }

        amenity_attrs = {
                "name": str
                }

        place_attrs = {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list
                }

        review_attrs = {
                "place_id": str,
                "user_id": str,
                "text": str
                }

        attributes = {
                "BaseModel": base_model_attrs,
                "User": user_attrs,
                "State": state_attrs,
                "City": city_attrs,
                "Amenity": amenity_attrs,
                "Place": place_attrs,
                "Review": review_attrs
                }
        return attributes
