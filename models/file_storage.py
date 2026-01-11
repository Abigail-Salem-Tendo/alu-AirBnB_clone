#!/usr/bin/python3
"""FileStorage class"""
import json
# from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review


class FileStorage:
    """Serializes instances to JSON and deserializes back"""

    __file_path = "file.json"
    __objects = {}

    # classes = {
    #     "BaseModel": BaseModel,
    #     "User": User,
    #     "State": State,
    #     "City": City,
    #     "Amenity": Amenity,
    #     "Place": Place,
    #     "Review": Review
    # }

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, "w") as f:
            json.dump(
                {k: v.to_dict() for k, v in self.__objects.items()},
                f
            )

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                objs = json.load(f)
                for key, value in objs.items():
                    cls = self.classes[value["__class__"]]
                    FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
