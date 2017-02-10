#!/usr/bin/python3
import cmd
import sys
import models
"""Console module for holberton bnb data management
"""


class hbnb(cmd.Cmd):
    """Class to create console
    """
    prompt = '(hbnb) '
    obj = models.storage.all()
    file = None #maybe remove

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'Exits the program'
        return True

    def emptyline(self):
        'Prevents repeat of previous input'
        pass

    def do_create(self, arg):
        'Creates a new instance of BaseModel, save to JSON file'
        if 'BaseModel' in arg:
            new = models.BaseModel()
            print('{}'.format(new.id))

    def do_show(self, arg):
        'Prints the string representation of an instance' \
        ' based on the class name and id'
        if (len(arg.split()) == 0):
            print('** class name is missing **')
        elif 'BaseModel' not in arg: #fix, shouldn't be hardcoded
            print('** class doesn''t exist **')
        elif (len(arg.split()) < 2):
            print('** instance id missing **')
        elif arg.split()[1] not in self.obj:
            print('** no instance found **')
        else:
            print(self.obj[arg.split()[1]])

    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id, saves to JSON file'
        if (len(arg.split()) == 0):
            print('** class name is missing **')
        elif 'BaseModel' not in arg: #fix, shouldn't be hard coded
            print('** class doesn''t exist **')
        elif (len(arg.split()) < 2):
            print('** instance id missing **')
        elif arg.split()[1] not in self.obj:
            print('** no instance found **')
        else:
            del self.obj[arg.split()[1]]
            models.storage.save()

    def do_all(self, arg):
        'Prints all string representation of all instances' \
        'based or not on the class name.'
        if 'BaseModel' not in arg: #fix, shouldn't be hard coded
            print('** class doesn''t exist **')
        else:
            ourlist = []
            for i in self.obj.keys():
                if self.obj[i].__class__.__name__ == arg:
                    ourlist.append(str(self.obj[i]))
                else:
                    outlist.append(str(self.obj[i]))
            print(ourlist)

    def do_update(self, arg):
        'Updates an instance based on the class name and id ' \
        'by adding or updating attribute, saves to JSON file'
        if (len(arg.split()) == 0):
            print('** class name is missing **')
        elif 'BaseModel' not in arg: #fix, shouldn't be hard coded
            print('** class doesn''t exist **')
        elif (len(arg.split()) < 2):
            print('** instance id missing **')
        elif arg.split()[1] not in self.obj:
            print('** no instance found **')
        elif (len(arg.split()) < 4):
            print('** value missing **')
        else:
            clsname = arg.split()[2]
            clsvalue = arg.split()[3]
            (self.obj[arg.split()[1]]).__dict__[clsname] = clsvalue
            models.storage.save()

if __name__ == '__main__':
    hbnb().cmdloop()
