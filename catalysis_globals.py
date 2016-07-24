# coding: UTF-8

'''Generic functions used by several modules. Primarily data validation.'''

import os
import sys

class Invalid(Exception):
    '''Exception that triggers upon invalid data.'''
    def __init__(self, err_code, *args):
        super(Invalid, self).__init__(err_code)
        err_msg = err_dict[err_code].format(*args)
        # Escape all braces in the error code, so format doesn't break.
        err_msg = err_msg.replace("{", "{{").replace("}", "}}")
        self.message = "Error on {} of {}: " + err_msg


def terminate():
    '''Close the program, waiting for user input if run from executable.'''
    if getattr(sys, 'frozen', False):
        print("Press enter to continue.")
        # Input can't have an argument, due to the codec.
        input()
    # This must have its default value of 0 for autotesting to work.
    sys.exit()


def get_file_name(file_name):
    '''Return the name of the file, making corrections for the
	Py2Exe handling of file locations.'''
    if getattr(sys, 'frozen', False):
        directory = os.path.dirname(sys.executable)
        return os.path.join(directory, file_name)
    return file_name


def quote_replace(match):
    '''Replace smart quotes with ASCII quotes.'''
    return {"‘": "'", "’": "'", "“": '"', "”": '"'}[match.group()]


def extract_data(file_name):
    '''Return the lines of the target file.'''
    input_file = get_file_name(file_name)
    try:
        with open(input_file, "r", encoding="utf-8-sig") as opened_file:
            return opened_file.read().splitlines()
    except UnicodeDecodeError:
        print(("Encoding for {} unknown. Please convert your files to UTF-8 " +
               "encoding before continuing.").format(file_name))
    except IOError:
        print("Ensure {} exists in this folder.".format(file_name))
    terminate()


def list_to_n_gen(target_list, mod, msg=""):
    '''Convert a flat list to a generator of n-length tuples. Raise an error if
    there aren't enough elements to convert fully.'''
    remainder = len(target_list) % mod
    if remainder:
        raise Invalid("implicit tuple", mod, msg, remainder, mod - remainder)
    else:
        target_list = [iter(target_list)] * mod
        return zip(*target_list)


def key_or_value(value, dictionary, word, or_value=False):
    '''Return the value from dictionary. If or_value, return value if it's
    a dictionary key. If neither work, send an error.'''
    try:
        return dictionary[value]
    except KeyError:
        if or_value and value in dictionary.values():
            return value
        else:
            raise Invalid("bad key", value, word)


def is_object(possible_object, target_set, item_name, object_dict):
    '''Return the object with the given handle, and validate that the value
    for attribute is in target_set. Sample use: converting a handle to
    a piece of evidence or profile.'''
    try:
        target_object = object_dict[possible_object]
    except KeyError:
        raise Invalid("unk obj", possible_object)
    if target_object.attribute not in target_set:
        raise Invalid("type in set", item_name, ", ".join(target_set))
    return target_object


def find_subobject(seek_attributes, place, target):
    '''Search the given place's seek_attributes attributes for an item with
    a name attribute of target. Seeks a place's foreground or background
    object.'''
    for attr in seek_attributes:
        for item in place[attr]:
            if item["name"] == target:
                return (attr, item["id"])
    raise Invalid("missing subobj", target)


def validate_int(value, name):
    '''Validate that the value is an integer, using name in the error
    message. Return the integer.'''
    try:
        return int(value)
    except ValueError:
        raise Invalid("int", name)


def int_at_least(value, target, name):
    '''Validate that value is an integer at least target, using name in the
    error message. Return the integer.'''
    value = validate_int(value, name)
    if value < target:
        raise Invalid("min", name, target)
    else:
        return value


err_dict = {
    "anc dupl": "Anchor {} is already in use.",
    "anc unset": "{} anchor {} is not set.",
    "arg missing": "{} not provided.",
    "attr name":  "{} is not a valid attribute name.",
    "attr val": "{} is not a valid attribute value.",
    "ban duplicate": "{} name {} is used twice.",
    "bad arg num": "Command {} does not have the proper number of arguments.",
    "bad context": "A command {} must be {}one of: {}.",
    "bad exam type": "Received point command {}, instead of one of: {}.",
    "bad exp number": (
        "Argument {} received {} pieces of an expression instead of {}."
    ),
    "bad global arg num": "{} arguments not taken.",
    "bad key": "{} is not a valid {} keyword.",
    "bad shape": "You can only examine with poly, rect, or circle, not {}.",
    "ban manual": "{} must not be called manually.",
    "ban on merge": "You cannot use {} on a merged frame.",
    "ban obj name": (
        "Objects cannot be given the name of a kind of object. Remove or " +
        "rename {}."
    ),
    "block open": (
        "The trial has ended with a cross-examination or investigation " +
        "still open."
    ),
    "circle 3": "circle needs 3 arguments after the shape.",
    "config attr": "Configuration attribute {} is invalid.",
    "config colon": "A configuration line must have ': ' exactly once.",
    "defaults unsupported": "This (sub)object has no default values.",
    "enforce scene": "Command {} can only be run in an investigation.",
    "excess press": (
        "Tried to start more press conversations than pressable statements."
    ),
    "excess suffix": "{} has exceeded the number of available sprites.",
    "exp dependency": (
        "Tried to specify a regular object without specifying a regular " +
        "place."
    ),
    "expected_new_obj": "Expected initiation of a new object.",
    "global action only": (
        "Received multiple arguments for a command that only has globals."
    ),
    "implicit tuple": (
        "Expected a multiple of {} arguments{}. Remove {} or add {}."
    ),
    "inadequate press": (
        "Tried to {} when {} press conversation(s) need to be written."
    ),
    "in obj": "Line not recognized. Currently in an object.",
    "int": "{} must be an integer.",
    "keyword claim": "{} name {} is a keyword name.",
    "min": "{} must be at least {}.",
    "missing locks": (
        "Scene number {} does not have psyche-locks, so the psyche-lock " +
        "button cannot be manipulated."
    ),
    "mult char no place": (
        "You can only define one character on a frame with no defined place."
    ),
    "missing subobj": "Subobject with name {} not found.",
    "mult char pos": (
        "Detected characters with the same position on this frame."
    ),
    "mult contra": "Tried to make {} contradictory twice.",
    "mult pos": "Tried to use position {} twice.",
    "mult pres": "Tried to make {} presentable twice.",
    "not word": "{} may only have letters, numbers, and underscores.",
    "no close brace": "Failed to spot closing brace for argument {}.",
    "no continuation": "Line continuation syntax not supported here.",
    "no default attr": "{} does not support double colon syntax.",
    "no exp": (
        "Attempted to use an expression for an action that does not permit" +
        " them. See the argument for {}."
    ),
    "no parent obj": "Subobjects need a parent object.",
    "num": "{} must be a number.",
    "obj subobj forbid": "Subobject {} cannot be used in object {}.",
    "parent obj dne": "Parent object {} not found.",
    "place post char": (
        "Place cannot be defined after characters are defined."
    ),
    "poly 6": "poly needs at least 6 arguments after the shape.",
    "poly pair": "poly needs pairs of coordinates.",
    "pre char": "There must be a character before {} can be set.",
    "pre place": "{} can only be run after a place is defined.",
    "prefix dupl": "The suffix {} is not unique.",
    "rect 4": "rect needs 4 arguments after the shape.",
    "rect to quad 4": (
        "Arguments 4 and 5 must be greater than arguments 2 and 3, " +
        "respectively."
    ),
    "schema fail": "Ran out of schema arguments at term {}.{}",
    "selector": "selector.txt expected this line to be {}.",
    "selector length": "selector.txt must have eight lines.",
    "subobj dne": "Subobject {} not recognized.",
    "suffix dupl": "The suffix {} is not unique.",
    "suffix no prefix": "Attempted to set a suffix before setting a prefix.",
    "terminal merge": "Attempted to merge the last frame into the next frame.",
    "type in set": "{}'s type must be one of: {}.",
    "unescaped brace": (
        "An unexpected, unescaped brace was found for " +
        "argument {}."
    ),
    "unk anc type": "Anchor type {} is not recognized.",
    "unk line": "Line not recognized. Check for typos.",
    "unk obj": "{} is not a recognized object.",
    "unk pre": "{} is not a recognized prefix.",
    "unk sprite": "{} is not a recognized longform sprite.",
    "unk suff": "{} is not a recognized suffix for prefix {}.",
    "unclosed": "{} not closed.",
    "valid fail": (
        "Critical error! Context validation has failed. {} permitted while " +
        "in {}. Please notify Enthalpy."
    ),
    "$ syntax": (
        "Expression argument {} contained an odd number of unescaped $ " +
        "symbols."
    ),
    ": syntax": "Expression argument {} had an unexpected syntactic colon."
}
