'''Module of auxiliary functions used by multiple library functions.'''

import re

from catalysis_globals import Invalid

def expression_pack(arguments, global_schema=tuple(), mult_schema=tuple()):
    '''Returns a dictionary with global and multple keys. The global key
    consists of one unit, and multiple consists of a list of units. A unit is
    all the information needed to fill one 'section' of action_parameters.
    A unit consists of subunits, each of which stands for one GUI-selectable
    data point. A subunit is a list that starts with a prefix and then contains
    all the relevant data points. By definition, a val prefix will have one
    other data point, while a xpr prefix may have multiple.
    The schemas give the number of data points for each xpr-prefixed subunit
    in a unit.'''
    def repl_custom(match):
        '''Replace when Catalysis variables are allowed.'''
        return {r"\\": "\\", r"\$": "$", "$": "\n"}[match.group()]

    def repl_default(match):
        '''Replace when Catalysis variables are not allowed.'''
        return {r"\\": "\\", r"\$": "$"}[match.group()]

    def packer(schema, msg):
        '''Pack a list of arguments into a single unit.'''
        unit = []
        for i, subunit_len in enumerate(schema, start=1):
            subbed_args = []
            try:
                arg = arguments.pop(0)
                # If the arguments are in expression mode...
                if arg.startswith("$"):
                    # Make a list of all the arguments for this "phase."
                    active_args = [arg[1:]] + arguments[:subunit_len-1]
                    # Slicing doesn't raise errors, so we need to validate
                    # that all these arguments exist.
                    if len(active_args) != subunit_len:
                        raise IndexError
                    for arg in active_args:
                        # Handle $, \, and Catalysis variables.
                        tag = re.sub(r"\\\\|\\\$|\$", repl_custom, arg)
                        if tag.count("\n") % 2:
                            raise Invalid("$ syntax", arg)
                        subbed_args.append(tag)
                    # Prefix the argument list and add the subunit.
                    unit.append(["xpr"] + subbed_args)
                    del arguments[:subunit_len-1]
                # If the arguments are not in expression mode...
                else:
                    # Handle $ and \ escapes, and append a subdescriptor.
                    # The function will modify this if necessary.
                    arg = re.sub(r"\\\\|\\\$", repl_default, arg)
                    unit.append(["val", arg])
            except IndexError:
                raise Invalid("schema fail", msg, i)
        return unit

    arguments = list(arguments)
    arg_dict = {"global": [], "multiple": []}
    if global_schema:
        arg_dict["global"] = packer(global_schema, "global")
    if mult_schema:
        while arguments:
            arg_dict["multiple"].append(packer(mult_schema, "multiple"))
    elif arguments:
        # If there is no allowance for multiple arguments, and the global
        # arguments have been exhausted, the argument number is wrong.
        raise Invalid("bad global arg num", len(arguments))
    return arg_dict


def param(tup, i):
    '''Used to parse an expression_pack unit, which are in the format:
    [prefix, arg1, arg2, etc.]'''
    return tup[0] + "=" + str(tup[i])


def no_manual(func):
    '''Tells a function not to be called.
    See frame_parser.context_validator.'''
    func.no_manual = True
    return func


def merge_lock(func):
    '''Tells a function that it can't be used on a merged frame.
    See frame_parser.context_validator.'''
    func.merge_lock = True
    return func


def scene_only(func):
    '''Tells a function that it can only be called in a scene.
    See frame_parser.context_validator.'''
    func.scene_only = True
    return func


def special(func):
    '''Tells a function that it can't be used on a generic frame, and actions
    can't be used atop it. See frame_parser.context_validator.'''
    func.special = True
    return func


def delay_sub(func):
    '''Tells a function to delay argument substitution.
    See frame_parser.command.'''
    func.delay_sub = True
    return func


def action(func):
    '''Tells a function to ban its use if action_name is set and delay argument
    substitution. See frame_parser.context_validator and
    frame_parser.command.'''
    func.action = True
    func = delay_sub(func)
    return func
