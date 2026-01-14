#!/usr/bin/python3
"""
Entry point of the command interpreter.
"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand interpreter for AirBnB project.
    """
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel, "User": User, "State": State,
        "City": City, "Amenity": Amenity, "Place": Place, "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Does nothing upon receiving an empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a class, saves it, and prints the id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        obj_list = []
        if not args:
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if obj.__class__.__name__ == args[0]:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        
        obj = storage.all()[key]
        attr_name = args[2]
        attr_val = args[3].strip('"')
        
        # Simple type casting
        try:
            if attr_name in obj.__class__.__dict__:
                v_type = type(obj.__class__.__dict__[attr_name])
                setattr(obj, attr_name, v_type(attr_val))
            else:
                setattr(obj, attr_name, attr_val)
        except Exception:
            setattr(obj, attr_name, attr_val)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()