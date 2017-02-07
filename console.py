#!/usr/bin/python3
import cmd, sys

class hbnb(cmd.Cmd):
    prompt = '(hbnb) '
    file = None #maybe remove

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'Exits the program'
        return True

if __name__ == '__main__':
    hbnb().cmdloop()
