# coding: UTF-8

'''Module that parses the macro_data.txt file. Creates macros and handles
configuration of Catalysis.'''

import re
import sys

from catalysis_globals import (
    extract_data, int_at_least, Invalid, key_or_value, quote_replace,
    terminate)
from frame_library import reserved_names

file_name = "macro_data.txt"


class ObjectParser(object):
    '''This class actually parses the macro. Each method consists of parsing
    instructions for a state of the file, and then returns the new file
    state.'''

    def __init__(self):
        self.next_method = self.no_macro
        self.return_to = self.no_macro
        self.active_macro = []
        self.macro_dict = {}
        self.config_dict = {
            "autopause": "on", "autowrap": True, "autoquote": True, ".": "250",
            "!": "250", ",": "125", "-": "200", "?": "250", "...": "500",
            ";": "200", ":": "200", "startup": 0, "autoescape": set()
        }
        self.customization_dict = {
            "autoquote": {"on": True, "off": False},
            "autopause": {"on": "on", "legacy": "legacy", "off": False},
            "autowrap": {"on": True, "off": False},
            "startup": {
                "s": 0, "d": 1, "b": 2, "skip": 0, "during": 1, "before": 2}
            }

    def no_macro(self, line):
        '''Handle parsing while not inside a macro.'''
        if line == "CONFIG {":
            return self.config
        try:
            macro = re.match(r"(\w+)\s*\{$", line).group(1)
        except AttributeError:
            raise Invalid("unk line")
        if macro.lower() == "config":
            return self.config
        if macro in self.macro_dict:
            raise Invalid("ban duplicate", "Macro", macro)
        # You can't give a macro the same name as a frame action.
        if macro in reserved_names:
            raise Invalid("keyword claim", "Macro", macro)
        self.macro_dict[macro] = self.active_macro = []
        return self.in_macro

    def in_macro(self, line):
        '''Handle parsing while inside a macro.'''
        if line == "}":
            # Conceptualizes that there's no active_macro anymore.
            self.active_macro = []
            return self.no_macro
        else:
            # Add this line to the list of lines that the macro stands for.
            self.active_macro.append(line)
            return self.in_macro

    def config(self, line):
        '''Handle parsing while inside a configuration block.'''
        if line == "}":
            return self.no_macro
        try:
            attr, value = re.split(": ?", line, maxsplit=1)
            attr, value = attr.lower(), value.lower()
        except ValueError:
            raise Invalid("config colon")
        if attr not in self.config_dict:
            raise Invalid("config attr", attr)
        if attr in self.customization_dict:
            self.config_dict[attr] = key_or_value(
                value, self.customization_dict[attr], attr)
        elif attr == "autoescape":
            self.config_dict[attr].update(value.split())
        else:
            self.config_dict[attr] = int_at_least(
                value, 0, "Configuration attribute " + attr)
        return self.config

    def in_comment(self, line):
        '''Handles parsing inside a mutliline comment.'''
        if line.endswith("*/"):
            return self.return_to
        return self.in_comment

    def cleanup(self):
        '''Handle validation after parsing is completed.'''
        # Equivalent to if self.active_macro exists.
        if self.next_method != self.no_macro:
            raise Invalid("unclosed", "Macro")


def parse_file(macro_test):
    '''Open the file, for-loop over the lines, feed them to the parser,
    validate, and return the macros, configuration, and automation.'''
    # Careful! If macro_test == "", we stick with that.
    lines = extract_data(file_name) if macro_test is False else (
        macro_test.splitlines())
    parser = ObjectParser()
    for i, line in enumerate(lines, start=1):
        # Escape stylized quotes with ASCII quotes if set to do so.
        line = line.strip()
        if not line:
            continue
        if parser.config_dict["autoquote"]:
            line = re.sub("‘|’|“|”", quote_replace, line)
        if line.startswith("/*") and parser.next_method != parser.in_comment:
            parser.return_to = parser.next_method
            parser.next_method = parser.in_comment(line)
        elif line.startswith("//"):
            pass
        else:
            try:
                parser.next_method = parser.next_method(line)
            except Invalid:
                print(sys.exc_info()[1].message.format(
                    "line {}".format(i), file_name))
                if Invalid.err_count >= Invalid.max_err:
                    terminate()
    try:
        if lines:
            parser.cleanup()
    except Invalid:
        print(sys.exc_info()[1].message.format("end of file", file_name))
        terminate()

    if Invalid.err_count:
        terminate()

    parser.config_dict["…"] = parser.config_dict.pop("...")
    return parser.macro_dict, parser.config_dict
