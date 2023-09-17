#!/usr/bin/python3
""" DEfinition of the Unittest module for ‘Amenity’ class """

import json
import re
import os
import time
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """ The following are the test cases for the Amenity class"""

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
        """ This is to test instantiation of "Amenity" class."""
        amenity = Amenity()
        self.assertEqual(str(type(user)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(issubclass(type(amenity), BaseModel))

    def test_attrs(self):
        """ This is to test the attributes of "Amenity" class."""
        attributes = storage.attributes()["Amenity"]
        amenity = Amenity()
        for attr_name, attr_type in attributes.items():
            self.assertTrue(hasattr(amenity, attr_name))
            self.assertEqual(
                    type(getattr(amenity, attr_name, None)),
                    attr_type
                    )


if __name__ == "__main__":
    unittest.main()
