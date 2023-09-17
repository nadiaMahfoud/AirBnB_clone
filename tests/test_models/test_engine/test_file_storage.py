#!/usr/bin/python3
""" DEfinition of the Unittest module for ‘FileStorage’ class """

import json
import re
import os
import time
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ The following are the test cases for the FileStorage class """

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

    def test_storage_init(self):
        """ This is to test the instantiation of storage Class."""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_init_empty_args(self):
        """This is to test __init__ with no args."""
        self.clearStorageData()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        expected_error_msg = (
                "descriptor '__init__' of 'object' object needs an argument"
                )
        self.assertEqual(str(e.exception), expected_error_msg)

    def test_init_excess_args(self):
        """This is to test __init__ with many arguments."""
        self.clearStorageData()
        with self.assertRaises(TypeError) as e:
            instance = FileStorage(*range(10))
        expected_error_msg = "object() takes no parameters"
        self.assertEqual(str(e.exception), expected_error_msg)

    def test_attrs(self):
        """This is to test class_attributes"""
        self.clearStorageData()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def test_storage_init(self):
        """ This is to test the instantiation of storage Class."""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_init_empty_args(self):
        """This is to test __init__ with no args."""
        self.clearStorageData()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        expected_error_msg = (
                "descriptor '__init__' of 'object' object needs an argument"
                )
        self.assertEqual(str(e.exception), expected_error_msg)

    def test_init_excess_args(self):
        """This is to test __init__ with many arguments."""
        self.clearStorageData()
        with self.assertRaises(TypeError) as e:
            instance = FileStorage(*range(10))
        expected_error_msg = "object() takes no parameters"
        self.assertEqual(str(e.exception), expected_error_msg)

    def test_attrs(self):
        """This is to test class_attributes"""
        self.clearStorageData()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def helper_test_all_method(self, class_name):
        """This is to test 'all()' method for a given class_name.
            Args:
            class_name (str): The name of the class to be tested.
            """
        # Reset the storage
        self.clearStorageData()

        # Ensure the storage is initially empty
        self.assertEqual(storage.all(), {})
        # Create an instance of the specified class, add it to storage,
        # and check if it exists in the storage
        obj = storage.classes()[class_name]()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], obj)

        # Test cases for various classes using the helper method

        def test_all_for_base_model(self):
            """This is to test 'all()' method for the BaseModel class."""
            self.helper_test_all_method("BaseModel")

        def test_all_for_user(self):
            """This is to test 'all()' method for the User class."""
            self.helper_test_all_method("User")

        def test_all_for_state(self):
            """This is to test 'all()' method for the State class."""
            self.helper_test_all_method("State")

        def test_all_for_city(self):
            """This is to test 'all()' method for the City class."""
            self.helper_test_all_method("City")

        def test_all_for_amenity(self):
            """This is to test 'all()' method for the Amenity class."""
            self.helper_test_all_method("Amenity")

        def test_all_for_place(self):
            """This is to test 'all()' method for the Place class."""
            self.helper_test_all_method("Place")

        def test_all_for_review(self):
            """This is to test 'all()' method for the Review class."""
            self.helper_test_all_method("Review")

        def helper_to_all_many(self, class_name):
            """This is to test 'all()' with many objects for a given class_name
                Args:
                    class_name (str): The name of the class to be tested
                    """
            # Reset the storage
            self.clearStorageData()

            # Ensure the storage is initially empty
            self.assertEqual(storage.all(), {})

            class_obj = storage.classes()[class_name]
            objects = [class_obj() for _ in range(1000)]
            [storage.new(obj) for obj in objects]

            # Check if the number of objects matches the number in storage
            self.assertEqual(len(objects), len(storage.all()))

            for obj in objects:
                key = "{}.{}".format(type(obj).__name__, obj.id)

                # Check if each object exists in storage and is equal
                self.assertTrue(key in storage.all())
                self.assertEqual(storage.all()[key], obj)

        # Test cases for various classes using the helper
        # method “helper_to_all_many”

        def test_all_many_base_model(self):
            """This is to test 'all()' with many objects for BaseModel."""
            self.helper_to_all_many("BaseModel")

        def test_all_many_user(self):
            """This is to test 'all()' with many objects for User."""
            self.helper_to_all_many("User")

        def test_all_many_state(self):
            """This is to test 'all()' with many objects for State."""
            self.helper_to_all_many("State")

        def test_all_many_city(self):
            """This is to test 'all()' with many objects for City."""
            self.helper_to_all_many("City")

        def test_all_many_amenity(self):
            """This is to test 'all()' with many objects for Amenity."""
            self.helper_to_all_many("Amenity")

        def test_all_many_place(self):
            """This is to test 'all()' with many objects for Place."""
            self.helper_to_all_many("Place")

        def test_all_many_review(self):
            """This is to test 'all()' with many objects for Review."""
            self.helper_to_all_many("Review")

        # Test case for all() with no arguments

        def test_all_empty(self):
            """This is to test all() with no arguments."""

            # Reset the storage
            self.clearStorageData()

            # Ensure that calling all() with no arguments raises a TypeError
            with self.assertRaises(TypeError) as e:
                storage.all()

            # Verify the error message
            expected_error_msg = (
                    "all() missing 1 required positional argument: 'self'"
                    )
            self.assertEqual(str(e.exception), expected_error_msg)

        # Test case for all() with too many arguments

        def test_all_too_many(self):
            """This is to test all() with too many arguments."""
            # Reset the storage
            self.clearStorageData()

            # Ensure that calling all() with too many arguments
            # raises a TypeError
            with self.assertRaises(TypeError) as e:
                storage.all(self, 98)

            # Verify the error message
            expected_error_msg = (
                    "all() takes 1 positional argument but 2 were given"
                    )
            self.assertEqual(str(e.exception), expected_error_msg)

            # Helper method for testing new() method for a given class_name

        def helper_test_new_method(self, class_name):
            """This is to test 'new()' method for a given class_name.

                Args:
                    class_name (str): The name of the class to be tested.
                    """

            # Reset the storage
            self.clearStorageData()

            class_obj = storage.classes()[class_name]
            obj = class_obj()
            storage.new(obj)
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.assertTrue(key in FileStorage._FileStorage__objects)
            self.assertEqual(FileStorage._FileStorage__objects[key], obj)

            # Helper method for testing new() method for a given class_name

        def helper_test_new_method(self, class_name):
            """This is to test 'new()' method for a given class_name.

            Args:
            class_name (str): The name of the class to be tested.
            """
            # Reset the storage
            self.clearStorageData()

            class_obj = storage.classes()[class_name]
            obj = class_obj()
            storage.new(obj)
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.assertTrue(key in FileStorage._FileStorage__objects)
            self.assertEqual(FileStorage._FileStorage__objects[key], obj)

        # Test cases for various classes using the helper method

        def test_new_for_base_model(self):
            """This is to test 'new()' method for BaseModel."""
            self.helper_test_new_method("BaseModel")

        def test_new_for_user(self):
            """This is to test 'new()' method for User."""
            self.helper_test_new_method("User")

        def test_new_for_state(self):
            """This is to test 'new()' method for State."""
            self.helper_test_new_method("State")

        def test_new_for_city(self):
            """This is to test 'new()' method for City."""
            self.helper_test_new_method("City")

        def test_new_for_amenity(self):
            """This is to test 'new()' method for Amenity."""
            self.helper_test_new_method("Amenity")

        def test_new_for_place(self):
            """This is to test 'new()' method for Place."""
            self.helper_test_new_method("Place")

        def test_new_for_review(self):
            """This is to test 'new()' method for Review."""
            self.helper_test_new_method("Review")

        # Test case for new() method with no arguments

        def test_new_empty(self):
            """This is to test new() with no arguments."""
            self.clearStorageData()
            with self.assertRaises(TypeError) as e:
                storage.new()
            expected_error_msg = (
                    "new() missing 1 required positional argument: 'obj'"
                    )
            self.assertEqual(str(e.exception), expected_error_msg)

        # Test case for new() method with too many arguments

        def test_new_too_many(self):
            """This is to test new() with too many arguments."""
            self.clearStorageData()
            base_model_obj = BaseModel()
            with self.assertRaises(TypeError) as e:
                storage.new(base_model_obj, 98)
            expected_error_msg = (
                    "new() takes 2 positional arguments but 3 were given"
                    )
            self.assertEqual(str(e.exception), expected_error_msg)

        # Helper method for testing save() method for a given class_name

        def helper_test_save_method(self, class_name):
            """Helper method for testing save() method
            for a given class_name."""

            self.clearStorageData()
            class_obj = storage.classes()[class_name]
            obj = class_obj()
            storage.new(obj)
            key = "{}.{}".format(type(obj).__name__, obj.id)
            storage.save()
            self.assertTrue(
                    os.path.isfile(FileStorage._FileStorage__file_path)
                    )

            # Create a dictionary representing the object's data
            object_data = {key: obj.to_dict()}
            with open(
                    FileStorage._FileStorage__file_path,
                    "r", encoding="utf-8"
                    ) as f:
                self.assertEqual(len(f.read()), len(json.dumps(object_data)))
                f.seek(0)
                self.assertEqual(json.load(f), object_data)

        # Test cases for various classes using the helper method

        def test_save_for_base_model(self):
            """This is to test 'save()' method for BaseModel."""
            self.helper_test_save_method("BaseModel")

        def test_save_for_user(self):
            """This is to test 'save()' method for User."""
            self.helper_test_save_method("User")

        def test_save_for_state(self):
            """This is to test 'save()' method for State."""
            self.helper_test_save_method("State")

        def test_save_for_city(self):
            """This is to test 'save()' method for City."""
            self.helper_test_save_method("City")

        def test_save_for_amenity(self):
            """This is to test 'save()' method for Amenity."""
            self.helper_test_save_method("Amenity")

        def test_save_for_place(self):
            """This is to test 'save()' method for Place."""
            self.helper_test_save_method("Place")

        def test_save_for_review(self):
            """This is to test 'save()' method for Review."""
            self.helper_test_save_method("Review")

        # Test case for save() method with no arguments

        def test_save_empty(self):
            """This is to test save() with no arguments."""
            self.clearStorageData()
            with self.assertRaises(TypeError) as e:
                storage.save()
            expected_error_msg = (
                    "save() missing 1 required positional argument: 'self'"
                    )
            self.assertEqual(str(e.exception), expected_error_msg)

        # Test case for save() method with too many arguments

        def test_save_too_many(self):
            """This is to test save() with too many arguments."""
            self.clearStorageData()
            base_model_obj = BaseModel()
            with self.assertRaises(TypeError) as e:
                storage.save(base_model_obj, 98)
            expected_error_msg = (
                    "save() takes 1 positional argument but 2 were given"
                    )
            self.assertEqual(str(e.exception), expected_error_msg)

        # Helper method for testing reload() method for a given class_name

        def helper_test_reload_method(self, class_name):
            """Helper method for testing reload() method
            for a given class_name
            Args:
            class_name (str): The name of the class to be tested.
            """
            # Reset the storage and reload to ensure a clean state
            self.clearStorageData()
            storage.reload()

            # Ensure that the internal objects dictionary is empty
            self.assertEqual(FileStorage._FileStorage__objects, {})

            # Create an instance of the specified class, add it to storage,
            # and save the data to the file
            class_obj = storage.classes()[class_name]
            obj = class_obj()
            storage.new(obj)
            key = "{}.{}".format(type(obj).__name__, obj.id)
            storage.save()

            # Reload the data from the file
            storage.reload()

            # Verify that the reloaded object's data matches
            # original object's data
            self.assertEqual(obj.to_dict(), storage.all()[key].to_dict())

        # Test cases for various classes using the helper method

        def test_reload_for_base_model(self):
            """This is to test 'reload()' method for BaseModel."""
            self.helper_test_reload_method("BaseModel")

        def test_reload_for_user(self):
            """This is to test 'reload()' method for User."""
            self.helper_test_reload_method("User")

        def test_reload_for_state(self):
            """This is to test 'reload()' method for State."""
            self.helper_test_reload_method("State")

        def test_reload_for_city(self):
            """This is to test 'reload()' method for City."""
            self.helper_test_reload_method("City")

        def test_reload_for_amenity(self):
            """This is to test 'reload()' method for Amenity."""
            self.helper_test_reload_method("Amenity")

        def test_reload_for_place(self):
            """This is to test 'reload()' method for Place."""
            self.helper_test_reload_method("Place")

        def test_reload_for_review(self):
            """This is to test 'reload()' method for Review."""
            self.helper_test_reload_method("Review")

        def helper_test_reload_mismatch(self, class_name):
            """This is to test reload() method for class_name
            with a mismatched attribute.
            Args:
            class_name (str): The name of the class to be tested.
            """
            # Reset the storage and reload to ensure a clean state
            self.clearStorageData()
            storage.reload()

            # Ensure that the internal objects dictionary is empty
            self.assertEqual(FileStorage._FileStorage__objects, {})

            # Create an instance of the specified class, add it to storage,
            # and save the data to the file
            class_obj = storage.classes()[class_name]
            obj = class_obj()
            storage.new(obj)
            key = "{}.{}".format(type(obj).__name__, obj.id)
            storage.save()

            # Modify an attribute of the object,
            # reload the data from the file,
            # verify that the reloaded data does not match the modified object
            obj.name = "ModifiedName"
            storage.reload()
            self.assertNotEqual(obj.to_dict(), storage.all()[key].to_dict())

        # Test cases for various classes using the helper method

        def test_reload_mismatch_for_base_model(self):
            """This is to test reload() method with a mismatched attribute
            for BaseModel."""
            self.helper_test_reload_mismatch("BaseModel")

        def test_reload_mismatch_for_user(self):
            """This is to test reload() method with a mismatched attribute
            for User."""
            self.helper_test_reload_mismatch("User")

        def test_reload_mismatch_for_state(self):
            """This is to test reload() method with a mismatched attribute
            for State."""
            self.helper_test_reload_mismatch("State")

        def test_reload_mismatch_for_city(self):
            """This is to test reload() method with a mismatched attribute
            for City."""
            self.helper_test_reload_mismatch("City")

        def test_reload_mismatch_for_amenity(self):
            """This is to test reload() method with a mismatched attribute
            for Amenity."""
            self.helper_test_reload_mismatch("Amenity")

        def test_reload_mismatch_for_place(self):
            """This is to test reload() method with a mismatched attribute
            for Place."""
            self.helper_test_reload_mismatch("Place")

        def test_reload_mismatch_for_review(self):
            """This is to test reload() method with a mismatched attribute
            for Review."""
            self.helper_test_reload_mismatch("Review")

        # Test case for reload() with no arguments

        def test_reload_mismatch_empty(self):
            """This is to test reload() with no arguments."""
            self.clearStorageData()
            with self.assertRaises(TypeError) as e:
                FileStorage.reload()
            expected_error_msg = (
                    "reload() missing 1 required positional argument: 'self'"
                    )
            self.assertEqual(str(e.exception), expected_error_msg)

        # Test case for reload() with too many arguments

        def test_reload_mismatch_too_many(self):
            """This is to test reload() with too many arguments."""
            self.clearStorageData()
            with self.assertRaises(TypeError) as e:
                FileStorage.reload(self, "additional_arg")
            expected_error_msg = (
                    "reload() takes 1 positional argument but 2 were given"
                    )
            self.assertEqual(str(e.exception), expected_error_msg)


if __name__ == '__main__':
    unittest.main()
