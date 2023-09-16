#!/usr/bin/python3
""" DEfinition of the Unittest module for ‘State’ class """

import json
import re
import os
import time
import unittest
from models.base_model import BaseModel
from models.state import State
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """ The following are the test cases for the State class"""

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
        """ This is to test instantiation of "State" class."""
        state = State()
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")
        self.assertIsInstance(state, State)
        self.assertTrue(issubclass(type(state), BaseModel))

    def test_attrs(self):
        """ This is to test the attributes of "State" class."""
        attributes = storage.attributes()["State"]
        state = State()
        for attr_name, attr_type in attributes.items():
            self.assertTrue(hasattr(state, attr_name))
            self.assertEqual(type(getattr(state, attr_name, None)), attr_type)


if __name__ == "__main__":
    unittest.main()
