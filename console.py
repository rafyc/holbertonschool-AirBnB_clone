#!/usr/bin/python3

"""
The entry point of the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class for the line-oriented command interpreters.

    Args:
        Cmd : built in class
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        quit()

    def do_EOF(self, arg):
        """Exits the program with <Ctrl+D>
        """
        quit()

    def empty_line(self):
        """Handles the emptyline"""
        pass

    # ----- basic hbnb commands -----


if __name__ == '__main__':
    HBNBCommand().cmdloop()
