#!/usr/bin/python3

"""
    Unittests for BaseModel
"""

import unittest
import os
import pycodestyle
from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4


class Test_Init(unittest.TestCase):
    """
    test for BaseModel
    """
    def test_id(self):
        """Test id type"""
        base = BaseModel()
        self.assertTrue(type(base.id) == str)

    def test_id_None(self):
        """Test id is not None"""
        base = BaseModel()
        self.assertIsNot(base.id, None)

    def test_id_unique(self):
        """Test id is unique"""
        base = BaseModel()
        base2 = BaseModel()
        self.assertIsNot(base2.id, base.id)
    
    def test_id_length(self):
        """Test id length"""
        base = BaseModel()
        self.assertEqual(len(base.id), 36)

    def test_created_at(self):
        """Test created_at type"""
        base = BaseModel()
        self.assertEqual(type(base.created_at), datetime)
    
    def test_created_at_format(self):
        """Test created at regex"""
        base = BaseModel()
        self.assertRegex(str(base.created_at), '^\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}.\\d{6}')

    def test_update_at_format(self):
        """Test updated_at regex"""
        base = BaseModel()
        self.assertRegex(str(base.updated_at), '^\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}.\\d{6}')

    def test_kwargs(self):
        """test kwargs"""
        base = BaseModel()
        dict_a = base.to_dict()
        base2 = BaseModel(**dict_a)
        self.assertEqual(base.id, base2.id)

    def test_kwargs_datetime(self):
        """test kwargs datetime"""
        base = BaseModel()
        dict_a = base.to_dict()
        base2 = BaseModel(**dict_a)
        self.assertRegex(str(base2.updated_at), '^\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}.\\d{6}')

    def test_kwargs_class(self):
        """test kwargs class"""
        base = BaseModel()
        dict_a = base.to_dict()
        base2 = BaseModel(**dict_a)
        self.assertTrue(hasattr(base2, '__class__'))

class Test_BaseModel_Init(unittest.TestCase):
    """test the instantiation"""

    def test_name_class(self):
        """test the class name"""
        base = BaseModel()
        self.assertEqual(base.__class__.__name__, "BaseModel")

    def test_base_id_str(self):
        """test id str"""
        base = BaseModel()
        self.assertIsInstance(base.id, str)

    def test_base_id_unique(self):
        """test unique id"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_id_length(self):
        """test the lenght of the id"""
        base = BaseModel()
        self.assertEqual(len(base.id), 36)

    def test_create_type_datetime(self):
        """test if created at"""
        base = BaseModel()
        self.assertEqual(type(base.created_at), datetime)

    def test_different_created(self):
        """test if created_at change each time executed"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.created_at, base2.created_at)

    def test_update_type_datetime(self):
        """test the type of updated_at"""
        base = BaseModel()
        self.assertEqual(type(base.updated_at), datetime)

    def test_different_created_updated(self):
        """test if updated_at change each time executed"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.created_at, base2.updated_at)

    def test_different_updated(self):
        """test if updated_at change each time executed"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.updated_at, base2.updated_at)


class Test_BaseModel_Str(unittest.TestCase):
    """test the str method"""

    def test_representation_class_name_and_id(self):
        """test the str representation"""
        base = BaseModel()
        base.id = 123
        self.assertTrue("[BaseModel] (123)", base.__str__)

    def test_representation_updated_at(self):
        """test if update_at is True"""
        base = BaseModel()
        self.assertTrue('updated_at' in str(base), True)

    def test_representation_created_at(self):
        """test if created_at is True"""
        base = BaseModel()
        self.assertTrue('created_at' in str(base), True)



class TestBaseModelSave(unittest.TestCase):
    """test the save method"""

    def test_name_base_model(self):
        """test the save method with name"""
        obj = BaseModel()
        obj.name = "Houssem"
        obj.save()
        self.assertEqual(obj.name, "Houssem")

    def test_my_number_base_model(self):
        """test the save method with number"""
        obj = BaseModel()
        obj.num = 1234
        obj.save()
        self.assertEqual(obj.num, 1234)

    def test_save_update(self):
        """test if changes of update are saved"""
        obj = BaseModel()
        obj.num = 1
        date1 = obj.updated_at
        obj.save()
        obj.num = 2
        date2 = obj.updated_at
        obj.save()
        self.assertNotEqual(date1, date2)

    def test_save_updates_file(self):
        """test the information are really saved in the file"""
        base = BaseModel()
        base.save()
        with open("file.json", "r", encoding="utf-8") as f:
            self.assertIn("BaseModel." + base.id, f.read())


class Test_BaseModel_To_Dict(unittest.TestCase):
    """test the to_dict method"""

    def test_dictionary_return(self):
        """test the to_dict method"""
        base = BaseModel()
        my_dict = base.to_dict()
        self.assertEqual(type(my_dict), dict)

    def test_create_dictionary(self):
        """test if the function to_dict work"""
        base = BaseModel()
        self.assertEqual(type(base.__dict__), dict)

    def test_compare_dictionary_type(self):
        """test if our dictionary is same as the __dict__"""
        base = BaseModel()
        self.assertEqual(type(base.__dict__), type(base.to_dict()))

    def test_correct_keys(self):
        base = BaseModel()
        self.assertIn("id", base.to_dict())
        self.assertIn("created_at", base.to_dict())
        self.assertIn("updated_at", base.to_dict())
        self.assertIn("__class__", base.to_dict())


if __name__ == '__main__':
    unittest.main()
