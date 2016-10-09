# coding: UTF-8

'''Module that parses the macro_data.txt file. Creates macros and handles
configuration of Catalysis.'''

import sys

from catalysis_globals import extract_data, int_at_least, Invalid, terminate

file_name = "selector.txt"

def parse_file():
    '''Parses the selector file.'''
    lines = extract_data(file_name)
    try:
        if len(lines) != 10:
            raise Invalid("selector length")
    except Invalid:
        print(sys.exc_info()[1].message.format(
            "end of file", file_name))
        terminate()
    try:
        for i, string in enumerate([
                "USERNAME:", "PASSWORD:", "DIRECTORY:", "TRIAL_ID:",
                "MAX_ERRORS:"]):
            if string != lines[2*i]:
                raise Invalid("selector", string)
    except Invalid:
        print(sys.exc_info()[1].message.format(
            "line {}".format(2*i+1), file_name))
        terminate()
    try:
        max_err = int_at_least(lines[9], 1, "Maximum errors allowable")
    except Invalid:
        print(sys.exc_info()[1].message.format("line 10", file_name))
        terminate()
    return lines[5], {
        "username": lines[1], "password": lines[3],
        "trial_id": lines[7]
    }, max_err

