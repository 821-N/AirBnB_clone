#!/usr/bin/python3
""" console file """


import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.engine.file_storage import FileStorage
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class HBNBCommand(cmd.Cmd):
    """ HBNBCommand -

        The main class for the HBNB project
        console / command line thing. It uses CMD for its
        core functionality
    """

    prompt = '(hbnb) '

    file = None

    # ------ Commands ------

    def do_create(self, arg):
        """ do_create -

            Creates a new instance of BaseModel,
            saves it (To the JSON file) and prints
            the id
            Ex. create BaseModel
        """

        if len(arg) is 0:
            print("** class name missing **")
            return

        if arg == "BaseModel":
            new_bmodel = BaseModel()
            new_bmodel.save()
            storage.reload()
            print(new_bmodel.id)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        """

        arg = self.parse_arg(arg)

        if len(arg) < 1:
            print("** class name missing **")
            return

        class_in = arg[0]

        if (class_in != "User" and class_in != "Amenity" and
                class_in != "BaseModel" and class_in != "City" and
                class_in != "Place" and class_in != "Review" and
                class_in != "State"):
                    print("** class doesn't exist**")
                    return

        if (len(arg) > 0):
            id_in = arg[1]
        else:
            print("** instance id missing **")
            return

        if (len(arg) > 1):
            attrib_in = arg[2]
        else:
            print("** attribute name missing **")
            return

        if (len(arg) > 2):
            value_in = arg[3]
        else:
            print("** value missing **")
            return

    def do_show(self, arg):
        """Prints the string representation of an instance
        """
        arg = self.parse_arg(arg)

        if len(arg) == 0:
            print("** class name missing **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return

        class_in = arg[0]
        key_in = arg[1]

        is_class = False

        all_objs = storage.all()

        for index in all_objs.keys():
            if class_in in index.split(".")[0]:
                is_class = True
                if key_in in index.split(".")[1]:
                    print(str(all_objs[index]))
                    return

        if is_class is True:
            print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        """
        arg = self.parse_arg(arg)
        all_objs = storage.all()

        if len(arg) == 1:
            class_in = arg[0]

        for i in all_objs.keys():
            if len(arg) > 0:
                if class_in in i.split(".")[0]:
                    print(str(all_objs[i]))
                else:
                    print("** class doesn't exist **")
            else:
                print(str(all_objs[i]))

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """ de_EOF -

            Quits the console when EOF is
            input into the console
        """
        return True

    # ----- Overrides n various other useful stuff ----

    def parse_arg(self, arg):
        """ parse_arg -

            This is used to seperate arguments
            into seperate sections of an array.
            Arguments are seperated by spaces
            and string arguments by double quotes
        """
        if arg is not "":
            return arg.split(" ")
        return ""

    def emptyline(self):
        """ emptyline -

            this function just overrides the
            predefined emptyline function. The
            override prevents the console from
            running the previous command entered
            when the user inputs a blank line
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
