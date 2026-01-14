#!/usr/bin/python3
"""
Entry point for the AirBnB console.
This module contains the HBNBCommand class.
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

# Dictionary of available classes
classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the AirBnB console.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program (Ctrl+D)
        """
        print()
        return True

    def emptyline(self):
        """Does nothing when an empty line is entered.
        """
        pass

    def do_create(self, arg):
        """Creates a new instance of a class, saves it, and prints the id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            obj = classes[args[0]]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
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
        """Deletes an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
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
        """Prints all string representation of all instances.
        """
        args = arg.split()
        objs = storage.all()
        if args and args[0] not in classes:
            print("** class doesn't exist **")
            return
        
        obj_list = []
        for key in objs:
            if not args or objs[key].__class__.__name__ == args[0]:
                obj_list.append(str(objs[key]))
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
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
        
        # Logic to set attribute
        setattr(storage.all()[key], args[2], args[3].strip('"'))
        storage.all()[key].save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()