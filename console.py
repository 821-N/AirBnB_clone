#!/usr/bin/python3
""" console file """

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

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

            print(new_bmodel.id)
        else:
            print("** class doesn't exist **")


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

    # ----- Documentation/help commands -----

    # ----- Overrides n various other useful stuff ----

    def parse_arg(self, arg):
        """ parse_arg -

            This is used to seperate arguments
            into seperate sections of an array.
            Arguments are seperated by spaces
            and string arguments by double quotes
        """
        pass

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
