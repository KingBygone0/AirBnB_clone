#!/usr/bin/python3
"""Test cases for the City Class."""

import unittest
import os
from datetime import datetime
from models.city import City
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_city_inherits_from_base_model(self):
        self.assertIsInstance(self.city, BaseModel)

    def test_city_attributes(self):
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_city_attributes_default_values(self):
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_city_attributes_assignment(self):
        self.city.state_id = "NY"
        self.city.name = "New York"
        self.assertEqual(self.city.state_id, "NY")
        self.assertEqual(self.city.name, "New York")

    def test_city_str_representation(self):
        self.assertEqual(str(self.city), "[City] ({}) {}"
                         .format(self.city.id, self.city.__dict__))


if __name__ == '__main__':
    unittest.main()
