#!/usr/bin/python3
""" This module defines the HBNB console and serves as
the command interpreter's entry point """

import json
import cmd
import re
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ THis is the command interpreter class """
    prompt = "(hbnb) "

    def default(self, input_line):
        """ This is the catch-all method for processing user commands."""
        # This method is called when an unrecognized command is entered.
        # It serves as a fallback to capture and process commands that are
        # not explicitly handled by other methods.

        # Call the _precmd method to preprocess and potentially transform
        # the user's input before passing it to the command interpreter.
        result = self._precmd(input_line)
        # Return the result of _precmd, which may be empty str/modified cmd
        return result

    def _precmd(self, input_line):
        """THis method intercepts commands to test for class.syntax()"""
        # This private method is used to intercept & preprocess user commands
        # It analyzes thestructure of the user's input using regularexpression
        # and extracts relevant information.

        # Use regular expressions to analyze the structure of the user's input
        re_match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", input_line)
        if not re_match:
            # If the input doesn't match the expected pattern, return it as its
            return input_line

        # Extract components of the command
        class_name = re_match.group(1)
        method = re_match.group(2)
        args = re_match.group(3)

        # Is there ‘unique id’ , ‘optional attribute’ or ‘dictionary’
        arg_uid_match = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if arg_uid_match:
            uid = arg_uid_match.group(1)
            dict_or_attr = arg_uid_match.group(2)
        else:
            uid = args
            dict_or_attr = False

        val_attr = ""
        if method == "update" and dict_or_attr:
            # Handle the case when 'update' includes a dictionary
            dict_match = re.search('^({.*})$', dict_or_attr)
            if dict_match:
                self.update_dict(class_name, uid, dict_match.group(1))
                return ""

            # Handle the case when 'update' includes attribute-value pairs
            val_attr_match = re.search(
                    '^(?:"([^"]*)")?(?:, (.*))?$', dict_or_attr)
            if val_attr_match:
                val_attr = (val_attr_match.group(
                    1) or "") + " " + (val_attr_match.group(2) or "")

        # Construct a modified command string for execution
        mod_cmd = method + " " + class_name + " " + uid + " " + val_attr
        # Call the command interpreter with the modified command
        self.onecmd(mod_cmd)

        # Return the modified command string (or empty str if processed)
        return mod_cmd

    def update_dict(self, class_name, uid, input_dict):
        """This is a helper method for update() with a dictionary."""
        json_str = input_dict.replace("'", '"')
        up_dict = json.loads(json_str)

        if not class_name:
            print("** class name missing **")
        elif class_name not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            instance_key = "{}.{}".format(class_name, uid)
            if instance_key not in storage.all():
                print("** no instance found **")
            else:
                class_attributes = storage.attributes()[class_name]
                for attribute, new_value in up_dict.items():
                    if attribute in class_attributes:
                        new_value = class_attributes[attribute](new_value)
                    setattr(storage.all()[instance_key], attribute, new_value)
                storage.all()[instance_key].save()

    def do_create(self, input_line):
        """ This method creates an instance """
        if input_line == " " or input_line is None:
            print("** class name missing **")
        elif input_line not in storage.classes():
            print("** class doesn't exist **")
        else:
            new = storage.classes()[input_line]()
            new.save()
            print(new.id)

    def do_EOF(self, input_line):
        """ This method handles the ‘End Of File’ character."""
        print()
        return True

    def do_quit(self, input_line):
        """ This method exits the program."""
        return True

    def emptyline(self):
        """ This method does not do anything on “ENTER”."""
        pass

    def do_show(self, input_line):
        """This method prints the string representation of an instance"""
        if input_line == "" or input_line is None:
            print("** class name missing **")
        else:
            tokens = input_line.split(' ')
            if tokens[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(tokens) < 2:
                print("** instance id missing **")
            else:
                instance_key = "{}.{}".format(tokens[0], tokens[1])
                if instance_key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[instance_key])

    def do_destroy(self, input_line):
        """This method deletes an instance based on the class name and id"""
        if input_line == "" or input_line is None:
            print("** class name missing **")
        else:
            tokens = input_line.split(' ')
            if tokens[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(tokens) < 2:
                print("** instance id missing **")
            else:
                instance_key = "{}.{}".format(tokens[0], tokens[1])
                if instance_key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[instance_key]
                    storage.save()

    def do_all(self, input_line):
        """This method prints all string representations of all instances."""
        if input_line != "":
            tokens = input_line.split(' ')
            if tokens[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                instance_list = [str(obj) for key, obj in storage.all().items()
                                 if type(obj).__name__ == tokens[0]]
                print(instance_list)
        else:
            all_instances = [str(obj) for key, obj in storage.all().items()]
            print(all_instances)

    def do_count(self, input_line):
        """This method counts the instances of a class."""
        tokens = input_line.split(' ')
        if not tokens[0]:
            print("** class name missing **")
        elif tokens[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matching_instances = [
                    k for k in storage.all() if k.startswith(
                        tokens[0] + '.')]
            print(len(matching_instances))

    def do_update(self, input_line):
        """This method updates an instance by adding or updating attributes."""
        if input_line == "" or input_line is None:
            print("** class name missing **")
            return

        ptrn = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        pattern_match = re.search(ptrn, input_line)
        class_name = pattern_match.group(1)
        uid = pattern_match.group(2)
        attr = pattern_match.group(3)
        val = pattern_match.group(4)
        if not pattern_match:
            print("** class name missing **")
        elif class_name not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            instance_key = "{}.{}".format(class_name, uid)
            if instance_key not in storage.all():
                print("** no instance found **")
            elif not attr:
                print("** attribute name missing **")
            elif not val:
                print("** value missing **")
            else:
                val_convert = None
                if not re.search('^".*"$', val):
                    if '.' in val:
                        val_convert = float
                    else:
                        val_convert = int
                else:
                    val = val.replace('"', '')
                attributes = storage.attributes()[class_name]
                if attr in attributes:
                    val = attributes[attr](val)
                elif val_convert:
                    try:
                        val = val_convert(val)
                    except ValueError:
                        pass
                setattr(storage.all()[instance_key], attr, val)
                storage.all()[instance_key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
