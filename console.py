#!/usr/bin/python3
import cmd
import sys
import models
"""Console module for Holberton bnb data management
"""


class hbnb(cmd.Cmd):
    """Class to create console
    """
    prompt = '(hbnb) '
    obj = models.storage.all()
    file = None  # maybe remove

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, arg):
        '''Exits the program'''
        return True

    def emptyline(self):
        '''Prevents repeat of previous input'''
        pass

    def do_create(self, arg):
        '''Creates a new instance of BaseModel, save to JSON file'''
        args = arg.split()
        new_class = ['BaseModel', 'Amenity', 'City', 'Place', 'Review',
                     'State', 'User']
        if len(args) < 1:
            print('** class name missing **')
        else:
            if args[0] in new_class:
                if args[0] == 'BaseModel':
                    new = models.BaseModel()
                if args[0] == 'Amenity':
                    new = models.Amenity()
                if args[0] == 'City':
                    new = models.City()
                if args[0] == 'Place':
                    new = models.Place()
                if args[0] == 'Review':
                    new = models.Review()
                if args[0] == 'State':
                    new = models.State()
                if args[0] == 'User':
                    new = models.User()
                new.save()
                print('{}'.format(new.id))

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        new_class = ['BaseModel', 'Amenity', 'City', 'Place', 'Review',
                     'State', 'User']
        args = arg.split()

        if (len(args) == 0):
            print('** class name is missing **')
        elif args[0] not in new_class:
            print('** class doesn''t exist **')
        elif (len(args) < 2):
            print('** instance id missing **')
        else:
            if args[0] in new_class:
                models.storage.reload()
                new_dict = models.storage.all()
                if args[1] not in new_dict:
                    print('** no instance found **')
                for key in new_dict:
                    if args[0] in str(new_dict[key]):
                        if args[1] in new_dict.keys():
                            print(new_dict[args[1]])
                            break

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id,'''\
            '''saves to JSON file'''
        new_class = ['BaseModel', 'Amenity', 'City', 'Place', 'Review'
                     'State', 'User']
        args = arg.split()

        if (len(args) == 0):
            print('** class name is missing **')
        elif args[0] not in new_class:
            print('** class doesn''t exist **')
        elif (len(args) < 2):
            print('** instance id missing **')
        else:
            if args[0] in new_class:
                models.storage.reload()
                new_dict = models.storage.all()
                if args[1] not in new_dict:
                    print('** not instance found **')
                else:
                    if args[1] in new_dict.keys():
                        if args[0] in str(new_dict[args[1]]):
                            del new_dict[args[1]]
                            models.storage.save()

    def do_all(self, arg):
        """Prints string representation of all instances based,"""\
            """ or not, on the class name."""
        new_class = ['BaseModel', 'Amenity', 'City', 'Place', 'Review',
                     'State', 'User']
        our_list = []
        args = arg.split()

        if len(args) > 0:
            if args[0] in new_class:
                for i in self.obj.keys():
                    if self.obj[i].__class__.__name__ == args[0]:
                        our_list.append(str(self.obj[i]))
                print(our_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        '''Updates an instance based on the class name and id'''\
            '''by adding or updating attribute, saves to JSON file'''
        new_class = ['BaseModel', 'Amenity', 'City', 'Place', 'Review',
                     'State', 'User']
        args = arg.split()

        if len(args) == 0:
            print('** class name is missing **')
        elif len(args) < 2:
            print('** instance id missing **')
        elif len(args) < 4:
            print('** value missing **')
        elif args[1] not in self.obj:
            print('** no instance found **')
        else:
            class_name = args[0]
            user_id = args[1]
            attribute_name = args[2]
            attribute_value = args[3]
            if class_name in new_class:
                (self.obj[user_id]).__dict__[attribute_name] = attribute_value
                models.storage.save()
            else:
                print('** class doesn''t exist **')

if __name__ == '__main__':
    hbnb().cmdloop()
