#!/user/bin/python3
"""Testing file for the BaseModel class"""
import unittest
from models.place import Place


class TestUserModel(unittest.TestCase):
    """This is a testcase class that inherits from unittest.TestCase"""
    def setUp(self):
        """setting up the object for test"""
        self.place_model = Place()

    def test_instance(self):
        self.assertIsInstance(self.place_model, Place)

    def test_name(self):
        self.assertIsInstance(self.place_model.name, str)
        self.assertEqual(self.place_model.name, "")
        self.place_model.name = "KMJ"
        self.assertEqual(self.place_model.name, "KMJ")

    def test_user_id(self):
        self.assertIsInstance(self.place_model.user_id, str)
        self.assertEqual(self.place_model.user_id, "")
        self.place_model.user_id = "1234"
        self.assertEqual(self.place_model.user_id, "1234")

    def test_city_id(self):
        self.assertIsInstance(self.place_model.city_id, str)
        self.assertEqual(self.place_model.city_id, "")
        self.place_model.city_id = "5678"
        self.assertEqual(self.place_model.city_id, "5678")

    def test_desc(self):
        self.assertIsInstance(self.place_model.description, str)
        self.assertEqual(self.place_model.description, "")
        self.place_model.description = "hello world"
        self.assertEqual(self.place_model.description, "hello world")

    def test_rooms(self):
        self.assertIsInstance(self.place_model.number_rooms, int)
        self.assertEqual(self.place_model.number_rooms, 0)
        self.place_model.number_rooms = 34
        self.assertEqual(self.place_model.number_rooms, 34)

    def test_bathrooms(self):
        self.assertIsInstance(self.place_model.number_bathrooms, int)
        self.assertEqual(self.place_model.number_bathrooms, 0)
        self.place_model.number_bathrooms = 34
        self.assertEqual(self.place_model.number_bathrooms, 34)

    def test_guest(self):
        self.assertIsInstance(self.place_model.max_guest, int)
        self.assertEqual(self.place_model.max_guest, 0)
        self.place_model.max_guest = 50
        self.assertEqual(self.place_model.max_guest, 50)

    def test_price(self):
        self.assertIsInstance(self.place_model.price_by_night, int)
        self.assertEqual(self.place_model.price_by_night, 0)
        self.place_model.price_by_night = 5000
        self.assertEqual(self.place_model.price_by_night, 5000)

    def test_latitude(self):
        self.assertIsInstance(self.place_model.latitude, float)
        self.assertEqual(self.place_model.latitude, 0.0)
        self.place_model.latitude = 34.0
        self.assertEqual(self.place_model.latitude, 34.0)

    def test_longitude(self):
        self.assertIsInstance(self.place_model.longitude, float)
        self.assertEqual(self.place_model.longitude, 0.0)
        self.place_model.longitude = 54.0
        self.assertEqual(self.place_model.longitude, 54.0)

    def test_amenity_ids(self):
        self.assertIsInstance(self.place_model.amenity_ids, list)
        self.assertEqual(self.place_model.amenity_ids, [])
        self.place_model.amenity_ids = ["1", "2", "3"]
        self.assertEqual(self.place_model.amenity_ids, ["1","2","3"])

if __name__ == "__main__":
    unittest.main()