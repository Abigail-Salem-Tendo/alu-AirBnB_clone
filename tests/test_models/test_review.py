#!/user/bin/python3
"""Testing file for the review class"""
import unittest
from models.review import Review


class TestUserModel(unittest.TestCase):
    """This is a testcase class that inherits from unittest.TestCase"""
    def setUp(self):
        """setting up the object for test"""
        self.review_model = Review()

    def test_instance(self):
        self.assertIsInstance(self.review_model, Review)

    def test_text(self):
        self.assertIsInstance(self.review_model.text, str)
        self.assertEqual(self.review_model.text, "")
        self.review_model.text = "burger"
        self.assertEqual(self.review_model.text, "burger")

    def test_user_id(self):
        self.assertIsInstance(self.review_model.user_id, str)
        self.assertEqual(self.review_model.user_id, "")
        self.review_model.user_id = "1234"
        self.assertEqual(self.review_model.user_id, "1234")

    def test_place_id(self):
        self.assertIsInstance(self.review_model.place_id, str)
        self.assertEqual(self.review_model.place_id, "")
        self.review_model.place_id = "5678"
        self.assertEqual(self.review_model.place_id, "5678")

if __name__ == "__main__":
    unittest.main()