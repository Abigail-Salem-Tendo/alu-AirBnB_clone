#!/user/bin/python3
"""Testing file for the State class"""
import unittest
from models.state import State


class TestBaseModel(unittest.TestCase):
    """This is a testcase class that inherits from unittest.TestCase"""
    def setUp(self):
        """setting up the object for test"""
        self.state_model = State()

    def test_instance(self):
        self.assertIsInstance(self.state_model, State)

    def test_name(self):
        self.assertIsInstance(self.state_model.name, str)
        self.assertEqual(self.state_model.name, "")
        self.state_model.name = "KMJ"
        self.assertEqual(self.state_model.name, "KMJ")

if __name__ == "__main__":
    unittest.main()