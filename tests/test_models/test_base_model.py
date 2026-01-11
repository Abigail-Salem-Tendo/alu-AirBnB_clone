#!/user/bin/python3
"""Testing file for the BaseModel class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """This is a testcase class that inherits from unittest.TestCase"""
    def setUp(self):
        """setting up the object for test"""
        self.base_model = BaseModel()

    def test_id_generation(self):
        """test for id generation"""
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at(self):
        """test for the created_at attribute"""
        self.assertIsNotNone(self.base_model.created_at)
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        """test for the updated_at attribute"""
        self.assertIsNotNone(self.base_model.updated_at)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save(self):
        """
        test for the save method by getting the initial value of updated_at,
        then calling the save method and checking if the save method updated
        the variable
        """
        first_updated_at = self.base_model.updated_at
        self.base_model.save()
        second_updated_at = self.base_model.updated_at
        self.assertNotEqual(first_updated_at, second_updated_at)

    def test_to_dict(self):
        """test for the to_dict method of the BaseModel class"""
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(
            obj_dict['__class__'], 'BaseModel')
        self.assertEqual(
            obj_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(
            obj_dict['updated_at'], self.base_model.updated_at.isoformat())

    def test__str__(self):
        """test for __str__ of the BaseModel class"""
        actual_output = str(self.base_model)
        self.assertEqual(
            actual_output,
            f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}")

if __name__ == "__main__":
    unittest.main()