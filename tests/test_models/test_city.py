#!/user/bin/python3
"""Testing file for the City class"""
import unittest
from models.city import City


class TestUserModel(unittest.TestCase):
    """This is a testcase class that inherits from unittest.TestCase"""
    def setUp(self):
        """setting up the object for test"""
        self.city = City()

    def test_instance(self):
        self.assertIsInstance(self.city, City)

    def test_name(self):
        self.assertIsInstance(self.city.name, str)
        self.assertEqual(self.city.name, "")
        self.city.name = "kigali"
        self.assertEqual(self.city.name, "kigali")

    def test_state_id(self):
        self.assertIsInstance(self.city.state_id, str)
        self.assertEqual(self.city.state_id, "")
        self.city.state_id = "1234"
        self.assertEqual(self.city.state_id, "1234")

if __name__ == "__main__":
    unittest.main()