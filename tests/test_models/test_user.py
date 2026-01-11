#!/usr/bin/python3
"""test file for user class"""

import unittest
from models.user import User

class TestUserModel(unittest.TestCase):
    """creating a testcase class that inherits from unittest.TestCase"""
    def setUp(self):
        """setting up the object for testing"""
        self.user_model = User()

    def test_instance(self):
        self.assertIsInstance(self.user_model, User)

    def test_first_name(self):
        self.assertIsInstance(self.user_model.first_name, str)
        self.assertEqual(self.user_model.first_name, "")
        self.user_model.first_name = "KMJ"
        self.assertEqual(self.user_model.first_name, "KMJ")

    def test_last_name(self):
        self.assertIsInstance(self.user_model.last_name, str)
        self.assertEqual(self.user_model.last_name, "")
        self.user_model.last_name = "JMK"
        self.assertEqual(self.user_model.last_name, "JMK")

    def test_email(self):
        self.assertIsInstance(self.user_model.email, str)
        self.assertEqual(self.user_model.email, "")
        self.user_model.email = "kmj@alueducation.com"
        self.assertEqual(self.user_model.email, "kmj@alueducation.com")

    def test_password(self):
        self.assertIsInstance(self.user_model.password, str)
        self.assertEqual(self.user_model.password, "")
        self.user_model.password = "1234"
        self.assertEqual(self.user_model.password, "1234")

if __name__ == "__main__":
    unittest.main()