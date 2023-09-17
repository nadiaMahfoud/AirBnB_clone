#!/usr/bin/python3
""" DEfinition of the Unittest module for ‘Review’ class """

import json
import re
import os
import time
import unittest
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """The following are the test cases for the Review class """

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
        """ This is to test instantiation of "Review" class."""
        review = Review()
        self.assertEqual(str(type(user)), "<class 'models.review.Review'>")
        self.assertIsInstance(review, Review)
        self.assertTrue(issubclass(type(review), BaseModel))

    def test_attrs(self):
        """ This is to test the attributes of "Review" class."""
        attributes = storage.attributes()["Review"]
        review = Review()
        for attr_name, attr_type in attributes.items():
            self.assertTrue(hasattr(review, attr_name))
            self.assertEqual(type(getattr(review, attr_name, None)), attr_type)


if __name__ == "__main__":
    unittest.main()
