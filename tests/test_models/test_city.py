#!/usr/bin/python3
""" DEfinition of the Unittest module for ‘City’ class """

import json
import re
import os
import time
import unittest
from models.base_model import BaseModel
from models.city import City
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """ The following are the test cases for the City class"""

    def setUp(self):
        """ This is for setting up test methods."""
        pass

    def tearDown(self):
        """This is for tearing down test methods."""
        self.clearStorageData()
        pass

    def clearStorageData(self):
        """ This is for resetting FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiate(self):
        """ This is to test instantiation of 'City' class"""
        city = City()
        self.assertEqual(str(type(city)), "<class 'models.city.City'>")
        self.assertIsInstance(city, City)
        self.assertTrue(issubclass(type(city), BaseModel))

    def test_attrs(self):
        """ This is to test the attributes of "City" class."""
        attributes = storage.attributes()["City"]
        city = City()
        for attr_name, attr_type in attributes.items():
            self.assertTrue(hasattr(city, attr_name))
            self.assertEqual(type(getattr(city, attr_name, None)), attr_type)


if __name__ == "__main__":
    unittest.main()
