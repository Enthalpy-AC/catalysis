# coding: UTF-8

'''Module that parses the frame_data.txt file. Creates and fills frames.'''

import re
import sys
import Tkinter as tk
import tkFont

import frame_library

from catalysis_defaults import validation_dict
from catalysis_globals import extract_data, Invalid, terminate, quote_replace

file_name = "/frame_data.txt"


class FrameParser(object):
    '''This class actually parses the frames. The functions here are less
    conceptually unified, but more hierarchical.'''

    def __init__(self, template, suffix_dicts, obj_dict,
                 macro_dict, config_dict):
        # Activate Tkinter, used for word wrapping.
        self.root = tk.Tk()
        self.font = tkFont.Font(family="PW Extended", size=-12)
        self.next_method = self.init_frame
        self.executor = frame_library.Library(template, suffix_dicts, obj_dict)
        self.glyph_dict = {}
        self.escape_dict = {}
        self.line_queue = [""]
        self.macro_dict = macro_dict
        self.config_dict = config_dict
        for punctuation in {".", "!", ",", "-", "?", "…", ";", ":"}:
            # 0's vanish.
            if self.config_dict[punctuation]:
                self.escape_dict[punctuation] = "[#{}]".format(
                    self.config_dict[punctuation])

    def blank(self):
        '''Tell the parser to expect initiation of a new frame, and handle
        the queue of lines to wrap. Run on blank lines.'''
        if self.executor.frame["merged_to_next"]:
            self.line_queue.append("")
        else:
            self.word_wrap()
            self.line_queue = [""]
        return self.init_frame

    def init_frame(self, line):
        '''Ensure a frame can be created here, make a frame, and process the
        requested command. Run when the previous line was blank.'''
        func = self.executor.make_frame
        self.validate_context(func)
        func()
        return self.command_process(line)

    def command_process(self, line, macro=False):
        '''Split the line into a list of commands and arguments, and then run
        it. If the line ends with a colon, expect dialogue. Otherwise, expect a
        new command and do some data valdiation.'''
        def func(match):
            r'''Function that handles escaping of comma-space, curly brackets
            and newline. Syntactical "{" are matched with "$", while "}" are 
            removed. Due to expression syntax and the dialogue command, 
            \ escape may not be safe.'''
            match = match.group(1)
            # Match \\ so they don't interfere with matching.
            # It may not be safe to treat them as an escaped \ yet.
            return {", ": "\n", r"\\": r"\\", "\\, ": ", ",
                    "\\{":"{", "\\}":"}", "{":"$", "}":""}[match]

        # Split at a comma-space and preserves escape characters,
        # but replaces non-escaped "{" and "}" with "$" and "" respectively.
        command_list = re.sub(r"(\\\\|\\, |, |\\{|\\}|{|})",
                              func, line).split("\n")
        # Seek a terminal colon, being wary of the possibility of escape.
        colon_match = re.search(r"(\\)*:$", command_list[-1])
        start_dialogue = False
        if colon_match:
            if colon_match.group(1) and len(colon_match.group(1)) % 2:
                # Colon escaped. Remove the escaping slash.
                command_list[-1] = command_list[-1][:-2] + command_list[-1][-1]
            else:
                # Colon not escaped. Remove it, and mark dialogue to start.
                start_dialogue = True
                command_list[-1] = command_list[-1][:-1]

        self.command(command_list)

        # If the command is run as part of a macro, it can't end a frame.
        if macro:
            return

        # Dialogue isn't set to start - we still expect commands.
        if not start_dialogue:
            return self.command_process
        # Dialogue is set to start - validate current places and positions.
        else:
            pos_list = [n["position"] for n in (
                self.executor.frame["characters"])]
            # Check if positions are duplicated...
            # If no place is set, there is only one available position,
            # so a repeat position means multiple characters.'''
            if len(pos_list) > len(set(pos_list)):
                if self.executor.frame["place"]:
                    raise Invalid("mult char pos")
                raise Invalid("mult char no place")
            return self.dialogue

    def command(self, command_list):
        '''Run the command in the sequence:
        command->macro->sprite->speaker.'''

        def underscore_purge(match):
            '''Remove terminal underscores.'''
            slash, score = match.groups()
            if score:
                return slash[:-1] + score if len(slash) % 2 else slash
            else:
                return slash if slash else ""

        # Convert the first word to a functional name.
        lead_word = command_list.pop(0).strip().replace(r"\\", "\\")


        # Assuming it's a Catalysis frame function, we need to transform the
        # camelCase to an underscore_version.
        func_name = re.sub(
            "([A-Z]+)", lambda match: "_" + match.group(1).lower(), lead_word)
        # The if checks if it is, in fact, a frame function.
        if func_name in frame_library.method_names:
            func = getattr(self.executor, func_name)
            self.validate_context(func)
            # Purge terminal underscores.
            command_list = [re.sub(
                r"(\\*)(_)$", underscore_purge, x) for x in command_list]
            # If we're free to replace backslashes now, do so.
            if not hasattr(func, "delay_sub"):
                command_list = [re.sub(r"\\\\", r"\\", x) for x in (
                    command_list)]
            try:
                func(*command_list)
                return
            except TypeError:  # Caution! Also catches unexpected TypeErrors.
                raise Invalid("bad arg num", lead_word)

        # Neither macros not characters should have been fragmented.
        if command_list:
            raise Invalid("unk line")
        # Assume it's a macro.
        try:
            for macro_line in self.macro_dict[lead_word]:
                self.command_process(macro_line, True)
            return
        except KeyError:
            pass

        # Assume it's prefix.suffix
        try:
            prefix, suffix = re.match(r"(\w+)\.(\w+)$", lead_word).groups()
        except AttributeError:
            pass
        else:
            func = self.executor.set_sprite
            self.validate_context(func)
            func(prefix, suffix)
            return

        # Assume it's just a prefix. Failing this, it's an error.
        try:
            prefix = re.match(r"(\w+)$", lead_word).group(1)
        except AttributeError:
            raise Invalid("unk line")
        else:
            func = self.executor.speaker_id
            self.validate_context(func)
            try:
                func(self.executor.suffix_dicts[prefix]["id"])
            except KeyError:
                raise Invalid("unk line", prefix)

    def comment(self, line):
        '''Return to init_frame if the comment ends.
        Otherwise you're still in the comment.'''
        if line.endswith("*/"):
            return self.init_frame
        return self.comment

    def dialogue(self, line):
        '''Ensure dialogue is permissible, handle pauses, word wrap, and
        add to text_content.'''
        func = self.executor.dialogue
        self.validate_context(func)
        self.line_queue[-1] += (line + '\n')
        return self.dialogue

    def cleanup(self):
        '''Cleanup actions to be run when the parser ends. Run blank again
        to word wrap, run anchor replacements, and do some validation.
        Then, end tKinter.'''

        # Run end-frame processing.
        self.blank()

        def list_wrap(*args):
            '''Function to get the value from a series of trial keys.'''
            item = self.executor.trial
            for key in args:
                item = item[key]
            return item

        # Do all anchor replacement.
        for key, value in self.executor.anc_dict.iteritems():

            def func(match):
                '''Function that returns the entry in the proper value dict
                for this match. Used for strng replacement.'''
                try:
                    return str(value["value"][match.group(1)])
                except KeyError:
                    raise Invalid("anc unset", key, match.group(1))

            for dest in value["destination"]:
                # The array or dict containing the replacement target.
                nonscalar = list_wrap(*dest[:-1])
                # The current value of the replacement target.
                string = list_wrap(*dest)
                # xpr replacement targets are separate by newlines.
                if string.startswith("xpr="):
                    nonscalar[dest[-1]] = re.sub("\n(.*)\n", func, string)
                # val replacement targets are everything after the val.
                elif string.startswith("val="):
                    nonscalar[dest[-1]] = re.sub("(?<=val=)(.*)", func, string)
                # And other replacment targets are the full value.
                else:
                    try:
                        nonscalar[dest[-1]] = value["value"][string]
                    except KeyError:
                        raise Invalid("anc unset", key, string)

        # Validate all prior assertions that psyche-lock sequences exist.
        for dest in self.executor.check_locks:
            string = list_wrap(*dest)
            if string.startswith("val="):
                target = int(string[4:])
                if not self.executor.trial["scenes"][target]["dialogues"][
                        0]["locks"]:
                    raise Invalid("missing locks", target)

        # Ensure that we're not expecting another frame.
        if self.executor.location:
            raise Invalid("block open")
        if self.executor.frame["merged_to_next"]:
            raise Invalid("terminal merge")

    def validate_context(self, command):
        '''Validate context. For example, some functions should never be
        called manually, should never be called on merged frames, or should
        only be called in a scene. This function validates this.'''

        # Define variables to be used in validation.
        name = re.sub(
            "_(.)", lambda match: match.group(1).upper(), command.__name__)
        location = self.executor.location
        dict_fragment = validation_dict[location]
        merged = self.executor.frame["merged_to_next"] or (
            command == self.executor.merge)
        try:
            merge_lock = "not merged" in self.executor.frame[
                "action_parameters"]["context"]
        except (KeyError, TypeError):
            merge_lock = False
        merge_lock = merge_lock or hasattr(command, "merge_lock")

        # Validate the command can be called manually, isn't scene-only,
        # doesn't have a merge problem, and isn't overriding an acton.
        if hasattr(command, "no_manual"):
            raise Invalid("ban manual", name)
        if hasattr(command, "scene_only") and (
                not self.executor.location.startswith("sce")):
            raise Invalid("enforce scene", name)
        if hasattr(command, "action") and self.executor.frame[
                "action_name"]:
            raise Invalid("one action", name)
        if merged and merge_lock:
            raise Invalid("ban on merge", name)

        # Validate the command is acceptable in this location.
        use_default = dict_fragment["use_default"]
        custom = dict_fragment["custom"]
        if use_default:
            default_if_applicable = not hasattr(command, "special")
            block_rule = "a generally usable command or "
        else:
            default_if_applicable = False
            block_rule = ""
        if not (default_if_applicable or name in custom):
            location_term = "after {}".format(location) if location else (
                "outside of special blocks")
            raise Invalid("bad context", location_term, block_rule,
                          ", ".join(custom))

        # Some commands have different permissible functions after makeFrame.
        # Change location, if necessary, to reflect this.
        if location in {"ceStatement", "sceMain"} and name == "makeFrame":
            self.executor.location += " and makeFrame"

    def word_wrap(self):
        '''The first part of this program turns our string into a series
        of (tag, length) tuples, where each tuple represents a different
        functional unit.

        WARNING! This is by far the most sensitive and complicated code in
        the program. Please do not make any changes without understanding
        the operation of the entire function.'''

        def get_length(text):
            '''Function that returns length for a string. Used only for a word
            or sequence of spaces. Subpixel rendering causes inconsistent
            pixel counts across machines if more than one character is
            measured at a time.'''
            return sum([self.glyph_dict.setdefault(
                n, self.font.measure(n)) for n in text])

        def escape(match):
            '''Handles pausing and escape characters. group(1) is the optional
            escape character, and group 2 is the symbol.'''
            if match.group(1):
                return match.group(2)
            try:
                return match.group(2) + self.escape_dict[match.group(2)]
            except KeyError:
                # Ellipsis case.
                if match.group(2) == len(match.group(2)) * "." and len(
                        match.group(2)) > 1:
                    return match.group(2) + self.escape_dict.get("…", "")
                else:
                    return match.group(2)

        words = []
        other = []
        for text in self.line_queue:
            # Split between AAO open/close tags, newlines, and other spaces.
            fragment_list = re.split(r'(\[#[^\]]*\]|\[/#]|[ \t\f\v]+|\n)',
                                     text[:-1])
            # The words go in one dictionary...
            words += [(x, get_length(x)) for x in fragment_list[::2]]
            # ...and everything else goes in the other.
            # \n's length is undefined, but it doesn't make a difference.
            other += [(x, get_length(x)) if x[0].isspace() else (x, 0) for (
                x) in fragment_list[1::2]]
            # words is one element longer than other. We'll add another
            # element to make them pair up, and to mark where the frame
            # breaks off.
            other.append(('BREAK', 0))

        # If autopause is set, add pauses where applicable.
        if self.config_dict["autopause"]:
            temp_words = []
            found_last = False
            # Loop over each word in the list, from last to first. This...
            for tag, length in reversed(words):
                # ...means the first word in our loop is the last word
                # and hence needs no pauses. found_last handles this.
                if found_last:
                    tag = re.sub(r'(\\)?(\.+|\\|,|-|\?|!|…|;|:)',
                                 escape, tag)
                # The last word /could/ be null, if, say, it ends with a close
                # tag. If so, don't mark it as the last tag. It's the word in
                # front of it we want to pause-exempt.
                elif tag:
                    found_last = True
                temp_words.append((tag, length))
            words = temp_words[::-1]

        # Combine the words and other dict again, purging any nulls.
        sequence = [item for pair in zip(words, other) for item in pair if (
            item != ('', 0))]
        total = 0
        wrapped_sequence = []

        # If autowrapping is enabled, loop over each term in the sequence.
        if self.config_dict["autowrap"]:
            for tag, length in sequence:
                # If the width would exceed the maximum with the new tag, or
                # the new tag is a newline, time to wrap!
                if total + length > 244 or tag == "\n":
                    # Delete the last space, if there is one.
                    if wrapped_sequence and wrapped_sequence[-1][0].isspace():
                        del wrapped_sequence[-1]
                    # And now append a newline and reset the total.
                    wrapped_sequence.append(("\n", 0))
                    total = 0
                    # Is the tag a space or newline? If so, wrapped_sequence
                    # and tag are how we want them, so continue.
                    if tag.isspace():
                        continue
                # Add the current term to the list, and update the width.
                wrapped_sequence.append((tag, length))
                total += length
        else:
            wrapped_sequence = sequence

        frame_text = [""]
        # Segment the list based on frame breaks, ignoring the terminal break
        # so as not to create a frame with blank text.
        for (tag, length) in wrapped_sequence[:-1]:
            if tag == "BREAK" and length == 0:
                # Interpret this as a new frame.
                frame_text.append("")
            else:
                # Add the tag to the contents for the new frame.
                frame_text[-1] += tag
        target_index = self.executor.frame["id"]
        frames = self.executor.trial["frames"]

        # And finally load each segment into frames, starting from the last.
        while frame_text:
            frames[target_index]["text_content"] += frame_text.pop()
            target_index -= 1


    def terminate(self):
        '''Close out of Tkinter and then terminate.'''
        self.root.after_idle(self.root.destroy)
        self.root.mainloop()
        terminate()


def parse_file(directory, template, suffix_dicts, object_dict, macro_dict,
               config_dict, frame_test):
    '''Open the file, for-loop over the lines, feed them to the parser,
    validate, and return the trial.'''
    lines = extract_data(directory + file_name) if frame_test is False else (
        frame_test.splitlines())
    parser = FrameParser(template, suffix_dicts, object_dict, macro_dict,
                         config_dict)
    # Replace stylized quotes with ASCII quotes if set to do so.
    if parser.config_dict["autoquote"]:
        lines = [re.sub("‘|’|“|”", quote_replace, line) for line in lines]
    for i, line in enumerate(lines, start=1):
        if not line:
            # A blank line means to expect a new frame.
            parser.next_method = parser.blank()
        elif line.startswith("//") and parser.next_method == parser.init_frame:
            # Ignore single-line comments.
            pass
        elif line.startswith("/*") and parser.next_method == parser.init_frame:
            # Mutliline comments trigger the comment state, but in case it's
            # a one-line multiline comment, call to comment.
            parser.next_method = parser.comment(line)
        else:
            # If all else fails, go with whatever the current state is.
            try:
                parser.next_method = parser.next_method(line)
            except Invalid:
                print sys.exc_info()[1].message.format(
                    "line {}".format(i), file_name)
                parser.terminate()
    try:
        if lines:
            parser.cleanup()
    except Invalid:
        print sys.exc_info()[1].message.format("end of file", file_name)
        parser.terminate()

    # Clear tkinter, even if the frame_data is blank.
    parser.root.after_idle(parser.root.destroy)
    parser.root.mainloop()
    return parser.executor.trial
