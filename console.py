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

    intro_prompt = '(hbnb) help\n' \
        '\n' \
        'Documented commands (type help <topic>):\n' \
        '========================================\n' \
        'EOF  help  quit\n'

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

    def do_show(self, arg):
        """ do_show -

            Prints the string representation of an
            instance base on the class name and id
        """
        if len(arg) is 0:
            print("**class name missing**")
            return


    def do_quit(self, arg):
        """ do_quit -

            Quits the console when Quit is
            input into the console
        """
        return True

    def do_EOF(self, arg):
        """ de_EOF -

            Quits the console when EOF is
            input into the console
        """
        return True

    # ----- Documentation/help commands -----

    def help_update(self):
        """ help_update -

           prints ouf the basic usage
           and description of the
           update command
        """

        print("\nUpdates an instance based on the class name")
        print("and id by adding or update an attribute")
        attrib = "1234-1234-1234 email \"aibnb@holbertonschool.com\""
        print("-\nUsage: (hbnb) update Basemodel {}\n".format(attrib))

    def help_all(self):
        """ help_all -

            prints out the basic usage
            and description of the
            all command
        """
        print("\nPrints all string representation of all instances")
        print("based or not on the class name")
        print("-\nUsage: (hbnb) all BaseModel")
        print("or (hbnb) all\n")


    def help_destroy(self):
        """ help_destroy -

            prints out the basic usage
            and description of the
            destroy command
        """
        print("\nDeletes an instance based on the class name")
        print("and id (saves change to into the JSON file")
        print("-\nUsage: destroy BaseModel 1234-1234-1234\n")

    def help_show(self):
        """ help_show -

            prints out the basic usage
            and description of the
            show command
        """
        print("\nPrints the string representation of an instance")
        print("based on the class name and id")
        print("-\nUsage: (hbnb) show BaseModel 1234-1234-1234\n")

    def help_create(self):
        """ help_create -

            prints out basic usage of
            the create command
        """
        print("\nCreates a new instance of BaseModel,")
        print("saves it (to the JSON file) and prints the id.")
        print("- \nUsage: (hbnb) create BaseModel\n")

    def help_quit(self):
        """ help_quit -

            Prints out basic usage of the
            Quit command
        """
        print("\nQuit command to exit the program")
        print("Usage: (hbnb) quit\n")

    def help_EOF(self):
        """ help_EOF -

            Prints out basic usage of the
            EOF command
        """
        print("\nEOF command to exit the program")
        print("Usage: (hbnb) EOF\n")

    # ----- Overrides n various other useful stuff ----

    def emptyline(self):
        """ emptyline -

            this function just overrides the
            predefined emptyline function. The
            override prevents the console from
            running the previous command entered
            when the user inputs a blank line
        """

        return ""

if __name__ == '__main__':
    HBNBCommand().cmdloop(HBNBCommand().intro_prompt)
