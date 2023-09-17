#!/usr/bin/python3
""" DEfinition of the Unittest module for ‘BaseModel’ class """

import json
import re
import os
import time
import uuid
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """ The following are the test cases for the Basemodel class """

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
        """ This is to test instantiation of BaseModel class"""

        # Create a BaseModel instance
        bm = BaseModel()

        # Assert that the instance is of the expected type
        self.assertEqual(
                str(type(bm)),
                "<class 'models.base_model.BaseModel'>"
                )

        # Assert that the instance is an instance of BaseModel
        self.assertIsInstance(bm, BaseModel)

        # Assert that the instance's type is a subclass of BaseModel
        self.assertTrue(issubclass(type(bm), BaseModel))

    def test_init_no_args(self):
        """ This is to test __init__ with no arguments"""
        self.clearStorageData()

        # Check that trying to create an instance with no args raises an error
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        error_msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), error_msg)

    def test_init_many_args(self):
        """This is to test __init__ with many arguments."""
        self.clearStorageData()

        # Create a list of arguments
        args = [arg for arg in range(10)]

        # Create a BaseModel instance with many arguments
        bm = BaseModel(*args)

    def test_attributes(self):
        """This is totest attributes value for instance of a BaseModel class"""

        # Get the attributes for the BaseModel class
        attrs = storage.attributes()["BaseModel"]

        # Create a BaseModel instance
        obj = BaseModel()

        # Check if the instance has the expected attributes & their typesmatch
        for attr_name, attr_type in attrs.items():
            self.assertTrue(hasattr(obj, attr_name))
            self.assertEqual(type(getattr(obj, attr_name, None)), attr_type)

    def test_datetime_created(self):
        """This is to test if updated_at & created_at
        are current at creation"""

        # Get the current date and time
        current_time = datetime.now()

        # Create a BaseModel instance
        bm = BaseModel()

        # Calculate the time difference between updated_at and created_at
        time_diff = bm.updated_at - bm.created_at

        # Check that the time difference is within an acceptable range
        self.assertTrue(abs(time_diff.total_seconds()) < 0.01)

        # Calculate the time difference between created_at and the current date
        time_diff = bm.created_at - current_time

        # Check that the time difference is within an acceptable range
        self.assertTrue(abs(time_diff.total_seconds()) < 0.1)

    def test_id(self):
        """This is to test for unique user ids."""

        # Create a list of BaseModel IDs
        id_list = [BaseModel().id for _ in range(1000)]

        # Check that all IDs in the list are unique
        self.assertEqual(len(set(id_list)), len(id_list))

    def test_save(self):
        """This is to test the public instance method save()."""

        # Create a BaseModel instance
        bm = BaseModel()

        # Sleep to create a time gap
        time.sleep(0.5)

        # Get the current date and time
        current_time = datetime.now()

        # Call the save() method
        bm.save()

        # Calculate the time difference between updated_at and the current date
        time_diff = bm.updated_at - current_time

        # Check that the time difference is within an acceptable range
        self.assertTrue(abs(time_diff.total_seconds()) < 0.01)

    def test_str(self):
        """This is to test for __str__ method."""

        # Create a BaseModel instance
        bm = BaseModel()

        # Define a regular expression pattern to match the str representation
        regex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")

        # Match the string representation against the pattern
        result = regex.match(str(bm))

        # Check that the match is not None
        self.assertIsNotNone(result)

        # Check that the first group in the match is "BaseModel"
        self.assertEqual(result.group(1), "BaseModel")

        # Check that the second group in the match is the BaseModel's ID
        self.assertEqual(result.group(2), bm.id)

        # Extract 3rdgroup and replace single quotes with
        # double quotes for JSON compatibility

        str_data = result.group(3)
        str_data = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", str_data)
        data = json.loads(str_data.replace("'", '"'))

        # Create a dictionary from the BaseModel's __dict__
        # & format date attributes
        obj_data = bm.__dict__.copy()
        obj_data["created_at"] = repr(obj_data["created_at"])
        obj_data["updated_at"] = repr(obj_data["updated_at"])

        # Check that the data from the string representation matches
        # the BaseModel's attributes

        self.assertEqual(data, obj_data)

    def test_to_dict(self):
        """This is to test the public instance method to_dict()."""

        # Create a BaseModel instance
        bm = BaseModel()

        # Set some attributes
        bm.name = "ModelName"
        bm.age = 25

        # Convert the BaseModel instance to a dictionary
        data = bm.to_dict()

        # Check that the dictionary contains the expected data
        self.assertEqual(data["id"], bm.id)
        self.assertEqual(data["__class__"], type(bm).__name__)
        self.assertEqual(data["created_at"], bm.created_at.isoformat())
        self.assertEqual(data["updated_at"], bm.updated_at.isoformat())
        self.assertEqual(data["name"], bm.name)
        self.assertEqual(data["age"], bm.age)

    def test_to_dict_no_args(self):
        """This is to test to_dict() with no arguments."""
        self.clearStorageData()

        # Check that trying to call to_dict() with no arguments raises an error
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        error_msg = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), error_msg)

    def test_to_dict_excess_args(self):
        """This is to test to_dict() with too many arguments."""
        self.clearStorageData()

        # Check that trying to call to_dict()
        # with too many args raises an error
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, 98)
        error_msg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), error_msg)

    def test_instantiate_kwargs(self):
        """This is to test instantiation with **kwargs."""

        # Create a BaseModel instance
        model = BaseModel()

        # Set some attributes
        model.extra_info = "ExtraInfo"
        model.rating = 5

        # Convert the BaseModel instance to a dictionary
        model_json = model.to_dict()

        # Create a new BaseModel instance from the dictionary
        new_model = BaseModel(**model_json)

        # Check that the attributes of the new instance
        # match the original instance
        self.assertEqual(new_model.to_dict(), model.to_dict())

    def test_instantiate_dict(self):
        """This is to test instantiation with **kwargs from custom dict."""

        # Create a custom dictionary with attributes
        custom_dict = {
                "__class__": "BaseModel",
                "updated_at": datetime(
                    2039, 18, 20, 43, 59, 59, 13579
                    ).isoformat(),
                "created_at": datetime.now().isoformat(),
                "id": uuid.uuid4(),
                "custom_attr": "CustomValue",
                "int_attr": 42,
                "float_attr": 3.1416
                }

        # Create a BaseModel instance using the custom dictionary
        obj = BaseModel(**custom_dict)

        # Check that the attributes of the instance match the custom dictionary
        self.assertEqual(obj.to_dict(), custom_dict)

    def test_save_storage(self):
        """This is to test that storage.save() is called from save()."""
        self.clearStorageData()

        # Create a BaseModel instance
        bm = BaseModel()

        # Call the save() method
        bm.save()

        # Create a key for the object in the storage format
        key = "{}.{}".format(type(bm).__name__, bm.id)

        # Create a dictionary with the object's data
        data = {key: bm.to_dict()}

        # Check that the file storage file exists
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))

        # Check that the data in the file matches the expected data
        with open(
                FileStorage._FileStorage__file_path, "r", encoding="utf-8"
                ) as f:
            self.assertEqual(len(f.read()), len(json.dumps(data)))
            f.seek(0)
            self.assertEqual(json.load(f), data)

    def test_save_no_args(self):
        """This is to test save() with no arguments."""
        self.clearStorageData()

        # Check that trying to call save() with no arguments raises an error
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        error_msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), error_msg)

    def test_save_excess_args(self):
        """This is to test save() with too many arguments."""
        self.clearStorageData()

        # Check that trying to call save() with too many args raises an error
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 98)
        error_msg = "save() takes 1 positional argument but 2 were given"


if __name__ == '__main__':
    unittest.main()
