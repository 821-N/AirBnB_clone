#!/usr/bin/python3
""" console file """

import cmd


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

    def help_quit(self):
        """ help_quit -

            Prints out basic usage of the
            Quit command
        """
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """ help_EOF -

            Prints out basic usage of the
            EOF command
        """
        print("EOF command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop(HBNBCommand().intro_prompt)
