#!/usr/bin/python3
""" DEfinition of the Unittest module for ‘Place’ class """

import json
import re
import os
import time
import unittest
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):
    """The following are the test cases for the Place class """

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
        """ This is to test instantiation of "Place" class."""
        place = Place()
        self.assertEqual(str(type(place)), "<class 'models.place.Place'>")
        self.assertIsInstance(place, Place)
        self.assertTrue(issubclass(type(place), BaseModel))

    def test_attrs(self):
        """ This is to test the attributes of "Place" class."""
        attributes = storage.attributes()["Place"]
        place = Place()
        for attr_name, attr_type in attributes.items():
            self.assertTrue(hasattr(place, attr_name))
            self.assertEqual(type(getattr(place, attr_name, None)), attr_type)


if __name__ == "__main__":
    unittest.main()
