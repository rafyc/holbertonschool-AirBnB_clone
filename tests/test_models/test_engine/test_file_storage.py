#!/usr/bin/python3
"""
This module contains unit tests for the class FileStorage.
"""


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from datetime import datetime
import unittest
import models
import json
import uuid
import os


class TestAttributes(unittest.TestCase):
    """
    This class provides tests with attributes of the class FilesStorage
    """
    def test_attributes_assignement(self):
        self.assertIn("_FileStorage__objects", FileStorage.__dict__)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIn("_FileStorage__file_path", FileStorage.__dict__)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)


class TestAllMethod(unittest.TestCase):
    """
    This class provides tests for the all method.
    """
    def test_instance_filestorage(self):
        """Test create a FileStorage instance"""
        f1 = FileStorage()
        self.assertEqual(type(f1), FileStorage)

    def test_type_return_value(self):
        """Test the type of the return value"""
        self.assertEqual(type(models.storage.all()), dict)

    def tests_none_objects(self):
        """Test all without objects"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        self.assertEqual(models.storage.all(), {})

    def tests_one_objects(self):
        """Test with one object"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        b1 = BaseModel()
        b1.save()
        self.assertEqual(len(models.storage.all()), 1)

    def tests_more_than_one_objects(self):
        """Test with more than one object"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        b2 = BaseModel()
        b3 = BaseModel()
        b2.save()
        b3.save()
        self.assertEqual(len(models.storage.all()), 2)

    def tests_all_types(self):
        """Test with all types of class"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        b1 = BaseModel()
        b1.save()
        u1 = User()
        u1.save()
        p1 = Place()
        p1.save()
        r1 = Review()
        r1.save()
        c1 = City()
        c1.save()
        a1 = Amenity()
        a1.save()
        s1 = State()
        s1.save()
        self.assertEqual(len(models.storage.all()), 7)

    def test_key(self):
        """Test the value of the key when the new method is called"""
        """Test with all types of class"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        b1 = BaseModel()
        b1.save()
        dico = models.storage.all()
        self.assertEqual(type(dico["BaseModel." + str(b1.id)]), type(b1))


class TestSaveMethod(unittest.TestCase):
    """Class that tests the save method"""

    def test_jsonfile_creation(self):
        """Test if the json file has been created"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        os.remove("file.json")
        self.assertEqual(os.path.exists("file.json"), False)
        b1 = BaseModel()
        b1.save()
        self.assertEqual(os.path.exists("file.json"), True)

    def test_if_jsonfile_is_filled(self):
        """Test if the save method fills the json file"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        self.assertEqual(os.path.getsize("file.json"), 2)
        s1 = State()
        s1.save()
        self.assertGreater(os.path.getsize("file.json"), 2)

    def test_save_after_del(self):
        """Test if the save method fills the json file"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        u1 = User()
        p1 = Place()
        u1.save()
        p1.save()
        self.assertGreater(os.path.getsize("file.json"), 2)
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        self.assertEqual(os.path.getsize("file.json"), 2)

    def test_save_in(self):
        """Test if the keys are in the json file."""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        b1 = BaseModel()
        u1 = User()
        s1 = State()
        p1 = Place()
        c1 = City()
        a1 = Amenity()
        r1 = Review()
        b1.save()
        u1.save()
        s1.save()
        p1.save()
        c1.save()
        a1.save()
        r1.save()
        text = ""
        with open("file.json", "r", encoding="utf-8") as f:
            text = f.read()
            self.assertIn("BaseModel." + b1.id, text)
            self.assertIn("User." + u1.id, text)
            self.assertIn("State." + s1.id, text)
            self.assertIn("Place." + p1.id, text)
            self.assertIn("City." + c1.id, text)
            self.assertIn("Amenity." + a1.id, text)
            self.assertIn("Review." + r1.id, text)


class TestReloadMethod(unittest.TestCase):
    """Class that tests the reload method"""

    def test_reload_type(self):
        """Test the reload method"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        u1 = User()
        u1.save()
        models.storage.reload()
        dico = models.storage.all()
        for k, v in dico.items():
            self.assertEqual(type(dico[k]), type(u1))

    def test_reload_in(self):
        """test if the keys are in storage.all()."""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        b1 = BaseModel()
        u1 = User()
        s1 = State()
        p1 = Place()
        c1 = City()
        a1 = Amenity()
        r1 = Review()
        b1.save()
        u1.save()
        s1.save()
        p1.save()
        c1.save()
        a1.save()
        r1.save()
        models.storage.reload()
        obj = models.storage.all()
        self.assertIn("BaseModel." + b1.id, obj)
        self.assertIn("User." + u1.id, obj)
        self.assertIn("State." + s1.id, obj)
        self.assertIn("Place." + p1.id, obj)
        self.assertIn("City." + c1.id, obj)
        self.assertIn("Amenity." + a1.id, obj)
        self.assertIn("Review." + r1.id, obj)


if __name__ == '__main__':
    unittest.main()
