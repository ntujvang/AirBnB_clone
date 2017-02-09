#!/usr/bin/python3
import cmd, sys, models

class hbnb(cmd.Cmd):
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
        'Prints the string representation of an instance \
        based on the class name and id'
        if (len(arg.split()) == 0):
            print('** class name is missing **')
        elif 'BaseModel' not in arg:
            print('** class doesn''t exist **')
        elif (len(arg.split()) < 2):
            print('** instance id missing **')
        elif arg.split()[1] != self.obj.__class__.__name__: #not working correctly
            print('** no instance found **')
        else:
            print(self.obj) #not sure if this is working

if __name__ == '__main__':
    hbnb().cmdloop()
