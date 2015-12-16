'''Module of auxiliary functions used by multiple library functions.'''

import re

from catalysis_globals import Invalid
from functools import wraps

def expression_pack(arguments, schema, pad=False):
    '''Returns one unit. A unit is all the information needed to fill one
    'section' of action_parameters. A unit consists of subunits, each of which
    stands for one GUI-selectable data point. A subunit is a list that starts
    with a prefix and then contains all the relevant data points. By
    definition, a val prefix will have one other data point, while a xpr
    prefix may have multiple. The schemas give the number of data points for
    each xpr-prefixed subunit in a unit. arguments is a list/tuple of
    arguments to the action.'''
    def repl_custom(match):
        '''Replace when Catalysis variables are allowed.'''
        if match.group(0) in {"{", "}"}:
            raise Invalid("dummy")
        return {r"\\": "\\", r"\$": "$", "$": "\n", r"\}": "}",
                r"\{": "}"}[match.group()]

    def repl_default(match):
        '''Replace when Catalysis variables are not allowed.'''
        if match.group(0) in {"{", "}"}:
            raise Invalid("dummy")
        return {r"\\": "\\", r"\}": "}", r"\{": "{"}[match.group()]
    arguments = list(arguments)
    unit = []
    for i, subunit_len in enumerate(schema, start=1):
        subbed_args = []
        try:
            # The next argument is the next item in arguments, unless
            # arguments is empty, and we've set to "pad," in which case
            # it's an empty string. This is used for commands that have
            # omitted arguments, such as gameOver.
            arg = "" if pad and not arguments else arguments.pop(0)
            # If the arguments are in expression mode...
            if arg.startswith("{"):
                # Make a list of all the arguments for this "phase," removing
                # the { from the first argument.
                active_args = [arg[1:]] + arguments[:subunit_len-1]
                # Slicing doesn't raise errors, so we need to validate
                # that all these arguments exist.
                if len(active_args) != subunit_len:
                    raise Invalid(
                        "bad exp number", i, len(active_args), subunit_len)
                end_match = re.search(r"(\\)*\}$", active_args[-1][-1])
                if end_match and len(end_match.groups()) % 2:
                    # As expected, ends at an unescaped brace.
                    active_args[-1] = active_args[-1][:-1]
                else:
                    raise Invalid("no close brace", active_args[-1])
                for arg in active_args:
                    # Handle $, \, and Catalysis variables.
                    try:
                        tag = re.sub(
                            r"\\(\\|\$|\{, \})|\{|\}|\$", repl_custom, arg)
                    except Invalid:
                        raise Invalid("unescaped brace", arg)
                    if tag.count("\n") % 2:
                        raise Invalid("$ syntax", arg)
                    subbed_args.append(tag)
                # Prefix the argument list and add the subunit.
                unit.append(["xpr"] + subbed_args)
                del arguments[:subunit_len-1]
            # If the arguments are not in expression mode...
            else:
                # Handle $, {, } and \ escapes, and append a subdescriptor.
                # The function will modify this if necessary.
                try:
                    arg = re.sub(r"\\(\\|\{|\})|\{|\}", repl_default, arg)
                except Invalid:
                    raise Invalid("unescaped brace", arg)
                unit.append(["val", arg])
        except IndexError:
            raise Invalid("schema fail", i)
    if arguments:
        raise Invalid("bad global arg num", len(arguments))
    return unit


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


def action(arg={"type": "null"}):
    '''Tells a function to delay argument substitution, and set the parser's
    action_mult to the decorator argument. This "part" holds the decorator
    arguments.'''
    # Remember never to change a dictionary that's also a default value.
    def wrap(func):
        '''Hold the function being decorated.'''
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            '''The wrapped function is replaced with this. Set action_mult to
            arg, and then run the function.'''
            self = args[0]
            self.action_mult = arg
            return func(*args, **kwargs)
        wrapped_func = delay_sub(wrapped_func)
        return wrapped_func
    return wrap
