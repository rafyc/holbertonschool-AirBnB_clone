#!/usr/bin/python3
"""
Unit tests for the FileStorage class.
"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import unittest
import models
import os


class TestAttr(unittest.TestCase):
    """
    This class provides tests with attributes of the class FilesStorage
    """

    def test_attributes_assignement(self):
        self.assertIn("_FileStorage__objects", FileStorage.__dict__)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIn("_FileStorage__file_path", FileStorage.__dict__)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)


class TestNew(unittest.TestCase):
    """Class that tests the new method within file storage"""

    def test_key(self):
        """Test with different types of class"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        b1 = BaseModel()
        b1.save()
        dico = models.storage.all()
        self.assertEqual(type(dico[f"BaseModel.{str(b1.id)}"]), type(b1))


class TestMethods(unittest.TestCase):
    """
    Tests for the all method of the file_storage.py.
    """

    def test_instance_is_created(self):
        """Test type of the istance"""
        f1 = FileStorage()
        self.assertEqual(type(f1), FileStorage)

    def test_type_dict(self):
        """Test if the return value is a dict"""
        self.assertEqual(type(models.storage.all()), dict)

    def tests_with_empty_obj(self):
        """Empty obj"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        self.assertEqual(models.storage.all(), {})

    def test_with_one_obj(self):
        """Test with one object"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        b1 = BaseModel()
        b1.save()
        self.assertEqual(len(models.storage.all()), 1)

    def tests_multiple_obj(self):
        """Test with mult obj"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        b2 = BaseModel()
        b3 = BaseModel()
        b2.save()
        b3.save()
        self.assertEqual(len(models.storage.all()), 2)

    def tests_different_types(self):
        """Test with kind of type"""
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


class ReloadMethod(unittest.TestCase):
    """Class Testing the reload method"""

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
        """Check if keys are in storage.all()."""
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
        self.assertIn(f"BaseModel.{b1.id}", obj)
        self.assertIn(f"User.{u1.id}", obj)
        self.assertIn(f"State.{s1.id}", obj)
        self.assertIn(f"Place.{p1.id}", obj)
        self.assertIn(f"City.{c1.id}", obj)
        self.assertIn(f"Amenity.{a1.id}", obj)


class TestSave(unittest.TestCase):
    """Tests the save method"""

    def test_jsonfile_create(self):
        """Check if Json file has been created"""
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
        """Test if save methos write in Json file"""
        dico = models.storage.all().copy()
        for k, v in dico.items():
            del models.storage.all()[k]
        models.storage.save()
        self.assertEqual(os.path.getsize("file.json"), 2)
        s1 = State()
        s1.save()
        self.assertGreater(os.path.getsize("file.json"), 2)

    def test_save_after_del(self):
        """Test if save methos write in Json file"""
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

    def test_save_into_json(self):
        """Check if the keys are inside the Json file."""
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
            self.assertIn(f"BaseModel.{b1.id}", text)
            self.assertIn(f"User.{u1.id}", text)
            self.assertIn(f"State.{s1.id}", text)
            self.assertIn(f"Place.{p1.id}", text)
            self.assertIn(f"City.{c1.id}", text)
            self.assertIn(f"Amenity.{a1.id}", text)
            self.assertIn(f"Review.{r1.id}", text)


if __name__ == '__main__':
    unittest.main()
