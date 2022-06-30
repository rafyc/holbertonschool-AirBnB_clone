#!/usr/bin/python3

"""
    Unittests for BaseModel
"""

import unittest
import os
import pycodestyle
from models.base_model import BaseModel
from datetime import datetime


class Test_Init(unittest.TestCase):
    """
    test for BaseModel
    """
    def test_id(self):
        """Test id type"""
        a = BaseModel()
        self.assertTrue(type(a.id) == str)

    def test_id_None(self):
        """Test id is not None"""
        a = BaseModel()
        self.assertIsNot(a.id, None)

    def test_id_unique(self):
        """Test id is unique"""
        a = BaseModel()
        b = BaseModel()
        self.assertIsNot(b.id, a.id)
    
    def test_id_length(self):
        """Test id length"""
        a = BaseModel()
        self.assertEqual(len(a.id), 36)

    def test_created_at(self):
        """Test created_at type"""
        a = BaseModel()
        self.assertEqual(type(a.created_at), datetime)
    
    def test_created_at_format(self):
        """Test created at regex"""
        a = BaseModel()
        self.assertRegex(str(a.created_at), '^\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}.\\d{6}')

    def test_update_at_format(self):
        """Test updated_at regex"""
        a = BaseModel()
        self.assertRegex(str(a.updated_at), '^\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}.\\d{6}')

    def test_kwargs(self):
        """test kwargs"""
        a = BaseModel()
        dict_a = a.to_dict()
        b = BaseModel(**dict_a)
        self.assertEqual(a.id, b.id)

    def test_kwargs_datetime(self):
        """test kwargs datetime"""
        a = BaseModel()
        dict_a = a.to_dict()
        b = BaseModel(**dict_a)
        self.assertRegex(str(b.updated_at), '^\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}.\\d{6}')

    def test_kwargs_class(self):
        """test kwargs class"""
        a = BaseModel()
        dict_a = a.to_dict()
        b = BaseModel(**dict_a)
        self.assertTrue(hasattr(b, '__class__'))
