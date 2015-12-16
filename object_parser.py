# coding: UTF-8

'''Module that parses the object_data.txt file. Creates objects and
subobjects.'''

import re
import sys

import object_classes
import subobject_classes as sub_c

from catalysis_globals import extract_data, Invalid, quote_replace, terminate

file_name = "/object_data.txt"


class ObjectParser(object):
    '''This class actually parses the macro. Each method consists of parsing
    instructions for a state of the file, and then returns the new file
    state.'''

    # Hashes subobject keyword to subobject class.
    subobject_dict = {
        "foreground": sub_c.ForegroundObject, "background":
        sub_c.BackgroundObject, "sound": sub_c.Sound, "image":
        sub_c.Image, "text": sub_c.Text, "sprite": sub_c.CustomSprite}

    def __init__(self, config_dict):
        self.active_object = False
        self.config_dict = config_dict
        self.next_method = self.no_object
        self.using_objects = {}
        self.return_to = self.no_object

    def no_object(self, line):
        '''Handles parsing while not inside an object.'''
        # Parse line as "word string(optional) {" else crash.
        try:
            object_type, name = re.match(
                r"(\w+)\s*(.+?)?\s*\{$", line).groups()
        except AttributeError:
            raise Invalid("expected_new_obj")
        # Assume it's calling an object. If that fails, move on.
        try:
            self.active_object = getattr(
                object_classes, object_type.capitalize())()
        except AttributeError:
            pass
        else:
            if name:
                # Validate the object names...
                if name in self.using_objects:
                    raise Invalid("ban duplicate", "Object", name)
                if name in object_classes.reserved_names:
                    raise Invalid("ban obj name", name)
                # Store the object name for later...
                self.using_objects[name] = self.active_object
                # And make the handle the name unless overriden...
                if object_type.capitalize() == "Profile":
                    self.active_object.redefine("long", name)
                    self.active_object.redefine("short", name)
                else:
                    self.active_object.redefine("name", name)
            return self.in_object
        # Assume subobject, so names have to be flipped
        # around, and the second word is mandatory.
        try:
            name, subobject = object_type, name.lower()
        except AttributeError:
            if object_type in self.subobject_dict:
                raise Invalid("no parent obj")
            else:
                raise Invalid("unk line")
        # Find the object it's a subobject of.
        try:
            base_object = self.using_objects[name]
        except KeyError:
            raise Invalid("parent obj dne", name)
        # Find the kind of subobject it's supposed to be.
        try:
            subobject_class = self.subobject_dict[subobject]
        except KeyError:
            raise Invalid("subobj dne", subobject)
        # Validate the current object permits this subobject.
        if subobject_class in base_object.sub_set:
            self.active_object = subobject_class(base_object)
        else:
            raise Invalid("obj subobj forbid", subobject, name)
        return self.in_object

    def in_object(self, line):
        '''Handle parsing for an object.'''
        # First, check if it's setting an attribute to an AAO built-in.
        try:
            attr, value = re.match(r"(\w+)::\s*(.*)$", line).groups()
        except AttributeError:
            pass
        else:
            self.active_object.colon_redef(attr, value)
            return self.in_object
        # Second, check if it's a standard command.
        # The below ? allows for blank attributes, to allow a blank line.
        try:
            attr, value = re.match(r"(\w+):\s*(.*)?$", line).groups("")
        except AttributeError:
            pass
        else:
            self.active_object.redefine(attr.lower(), value)
            return self.in_object
        # Third, check if it's closing the object.
        if line == "}":
            try:
                self.active_object.update_suffixes()
            except AttributeError:
                pass
            # Conceptualizes that there is no active_object anymore.
            self.active_object = False
            return self.no_object
        # Last, check for line continuation. If this fails, it's over.
        try:
            value = re.match(r":\s?(.*)?$", line).group(1)
            value = value if value else ""
        except AttributeError:
            raise Invalid("in obj")
        else:
            self.active_object.append(value)
            return self.in_object

    def in_comment(self, line):
        '''Handle parsing for a multiline comment.'''
        if line.endswith("*/"):
            return self.return_to
        return self.in_comment

    def cleanup(self):
        '''Handle validation after parsing is completed.'''
        # If we're expecting something in particular, there's a problem.
        # All objects should be closed.
        if self.next_method != self.no_object:
            raise Invalid("unclosed", "Object")


def parse_file(directory, config_dict, obj_test):
    '''Open the file, for-loop over the lines, feed them to the parser,
    validate, and return the trial, suffixes, and objects with a handle.'''
    # Careful! If macro_test == "", we stick with that.
    lines = extract_data(directory + file_name) if obj_test is False else (
        obj_test.splitlines())
    parser = ObjectParser(config_dict)
    # Escape stylized quotes with ASCII quotes if set to do so.
    if parser.config_dict["autoquote"]:
        lines = [re.sub("‘|’|“|”", quote_replace, line) for line in lines]
    for i, line in enumerate(lines, start=1):
        line = line.strip()
        if not line:
            continue
        if line.startswith("/*") and parser.next_method != parser.in_comment:
            parser.return_to = parser.next_method
            parser.next_method = parser.in_comment(line)
        elif line.startswith("//"):
            pass
        else:
            try:
                parser.next_method = parser.next_method(line)
            except Invalid:
                print sys.exc_info()[1].message.format(
                    "line {}".format(i), file_name)
                terminate()
    try:
        if lines:
            parser.cleanup()
    except Invalid:
        print sys.exc_info()[1].message.format("end of file", file_name)
        terminate()
    template = {
        "profiles": [0], "evidence": [0], "places": [0], "sounds": [0],
        "music": [0], "popups": [0], "cross_examinations": [0], "scenes": [0],
        "scenes_aai": [0], "frames": [0],
        "ui": {"base": "classic", "elements": []}
    }
    for row in {"Popup", "Sound", "Music", "Place", "Evidence", "Profile"}:
        active_obj = getattr(object_classes, row)
        template[active_obj.attribute] = active_obj.chain
    return template, object_classes.Profile.suffix_dicts, parser.using_objects
