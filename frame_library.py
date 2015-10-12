'''A module for a class containing functions to manipulate the trial data.'''

import functools
import inspect
import re

from catalysis_globals import (
    Invalid, list_to_n_tuple, key_or_value, is_object, validate_int,
    int_at_least, find_subobject)
from library_aux import (
    action, delay_sub, expression_pack, param, no_manual, merge_lock,
    scene_only, special)


class Library(object):
    '''Class that does the trial data manipulation.'''

    def __init__(self, JSON, suffix_dicts, object_dict):
        self.trial = JSON
        self.suffix_dicts = suffix_dicts
        self.object_dict = object_dict
        self.cross = self.trial["cross_examinations"][-1]
        self.scene = self.trial["scenes"][-1]
        self.statement_index = -1
        self.pressable_indices = []
        self.frame = {"merged_to_next": False, "action_parameters": {}}
        self.location = ""
        self.anc_dict = {x: {"destination": set(), "value": {}} for x in {
            "frames", "scenes", "talk", "talk_sce"}}
        self.scene_dia = {}
        self.check_locks = set()
        self.from_object_dict = functools.partial(
            is_object, object_dict=self.object_dict)
        self.from_object_dict.no_manual = True
        self.speaker_override = False

    def null(self):
        '''Dummy function to create a blank frame.'''
        pass

    def make_frame(self):
        '''Add a frame.'''
        # Yes, action_parameters is an array when blank, not a dict.
        self.trial["frames"].append({
            "id": len(self.trial["frames"]), "speaker_name": "",
            "speaker_use_name": False, "speaker_id": -3, "speaker_voice": -4,
            "sound": 0, "music": 0, "place": 0, "place_position": 0,
            "place_transition": 0, "characters": [],
            "characters_erase_previous": False, "popups": [],
            "action_name": "", "action_parameters": [],
            "text_colour": "white", "text_content": "", "text_speed": 1,
            "hidden": False, "wait_time": 0, "merged_to_next": False
        })
        self.frame = self.trial["frames"][-1]
        self.speaker_override = False

    @delay_sub
    def dialogue(self, *args):
        r'''Add dialogue. \ is escaped, and a terminal \ signifies a
        newline.'''
        original_line = ", ".join(args)
        match = re.search(r"\\*$", original_line)
        if match and len(match.group(0)) % 2:
            original_line = original_line[:-1]
            newline = "\n"
        else:
            newline = ""
        line = original_line.replace(r"\\", "\\")
        self.frame["text_content"] += (line + newline)

    def popup(self, name):
        '''Set a pop-up. The argument is the name of the pop-up.'''
        obj = self.from_object_dict(name, {"popups"}, "Popup to display")
        self.frame["popups"].append({
            "popup_id": obj.data["id"], "position": 0, "mirror_effect": False})

    def music(self, name=-1):
        '''Play a music track. Argument is the name in playerCommands.'''
        if name == -1:
            self.frame["music"] = -1
        else:
            obj = self.from_object_dict(name, {"music"}, "Music to play")
            self.frame["music"] = obj.data["id"]

    def sound(self, name):
        '''Play a sound. Argument is the name in playerCommands'''
        obj = self.from_object_dict(name, {"sounds"}, "Sound to play")
        self.frame["sound"] = obj.data["id"]

    def place(self, name=-1, position="center"):
        '''Set the place.'''
        if name == -1:
            self.frame["place"] = name
        else:
            try:
                obj = self.from_object_dict(
                    name, {"places"}, "Place to display"
                )
                self.frame["place"] = obj.data["id"]
            except Invalid:
                built_dict = {
                    "black": -1, "pw bench": -2, "pw judge": -6,
                    "pw counsel": -3, "pw court loud": -8,
                    "pw court silent": -9, "pw lobby": -10,
                    "pw det behind": -18, "pw det ahead": -19,
                    "aj bench": -12, "aj judge": -14, "aj counsel": -13,
                    "aj court loud": -15, "aj court silent": -16,
                    "aj lobby": -17, "aj det behind": -20,
                    "aj det ahead": -21, "power def": -4, "power pros": -5,
                    "gavel 1": -7, "gavel 3": -11
                }
                self.frame["place"] = key_or_value(name, built_dict, "place")
        if self.frame["characters"]:
            raise Invalid("place post char")
        pos_dict = {
            "c": -1, "l": -2, "r": -3, "l2": -4, "r2": -5, "ll": -6, "rl": -7,
            "lr": -8, "rr": -9, "lc": -10, "rc": -11, "center": -1,
            "left": -2, "right": -3, "AAI left": -4, "AAI right": -5,
            "left of left": -6, "right of left": -7, "left of right": -8,
            "right of right": -9, "left of center": -10, "right of center": -11
        }
        self.frame["place_position"] = key_or_value(
            position, pos_dict, "position")

    def wait(self, time):
        '''Set a wait in milliseconds. Argument is wait in miliseconds.'''
        self.frame["wait_time"] = int_at_least(time, 0, "Wait time")

    def hide(self):
        '''Hide a frame.'''
        self.frame["hidden"] = not self.frame["hidden"]

    def merge(self):
        '''Merge a frame with the one below.'''
        self.frame["merged_to_next"] = not self.frame["merged_to_next"]

    def erase(self):
        '''Erases previous characters.'''
        self.frame["characters_erase_previous"] = not self.frame[
            "characters_erase_previous"]

    def scroll(self):
        '''Established smooth scrolling.'''
        self.frame["place_transition"] = not self.frame["place_transition"]

    def speed(self, type_speed):
        '''Set the type-speed from the default of one.'''
        try:
            type_speed = float(type_speed)
        except ValueError:
            raise Invalid("num", "Typing speed")
        if type_speed < 0:
            raise Invalid("min", "Typing speed", 0)
        else:
            self.frame["text_speed"] = str(type_speed)

    def blip(self, keyword):
        '''Set the text blips. Takes the kind of blip as argument.'''
        blip_dict = {
            "n": 0, "m": -1, "f": -2, "t": -3, "a": -4, "none": 0, "male": -1,
            "female": -2, "type": -3, "auto": -4
        }
        self.frame["speaker_voice"] = key_or_value(keyword, blip_dict, "blip")

    def mirror(self):
        '''Activate the mirror effect.'''
        try:
            self.frame["characters"][-1]["mirror_effect"] = (
                not self.frame["characters"][-1]["mirror_effect"])
        except IndexError:
            raise Invalid("pre char", "mirror")

    def color(self, color_code):
        '''Set the color. Takes as argument the hex code or string.'''
        try:
            int(color_code, 16)
        except ValueError:
            pass
        else:
            color_code = "#" + color_code
        self.frame["text_colour"] = color_code

    def sync(self, keyword):
        '''Set the sync behavior. Sync, do not talk, keep talking, or auto.
        Works for last character. Assumes character already set.'''
        sync_dict = {"s": 0, "n": 1, "k": 2, "a": 3, "sync": 0,
                     "do not talk": 1, "keep talking": 2, "auto": 3}
        sync_number = key_or_value(keyword, sync_dict, "sync")
        try:
            self.frame["characters"][-1]["sync_mode"] = sync_number
        except IndexError:
            raise Invalid("pre char", "sync")

    def startup(self, keyword):
        '''Set the start-up behavior. Is the animation skipped, during,
        or before text?'''
        start_dict = {
            "s": 0, "d": 1, "b": 2, "skip": 0, "during": 1, "before": 2}
        start_number = key_or_value(keyword, start_dict, "startup")
        try:
            self.frame["characters"][-1]["startup_mode"] = start_number
        except IndexError:
            raise Invalid("pre char", "startup")

    def c_pos(self, keyword):
        '''Set the character position.'''
        pos_dict = {
            "c": -1, "l": -2, "r": -3, "l2": -4, "r2": -5, "ll": -6, "rl": -7,
            "lr": -8, "rr": -9, "lc": -10, "rc": -11, "center": -1,
            "left": -2, "right": -3, "AAI left": -4, "AAI right": -5,
            "left of left": -6, "right of left": -7, "left of right": -8,
            "right of right": -9, "left of center": -10,
            "right of center": -11
        }
        if not self.frame["place"]:
            raise Invalid("pre place", "cPos")
        pos_number = key_or_value(keyword, pos_dict, "character position")
        try:
            self.frame["characters"][-1]["position"] = pos_number
        except IndexError:
            raise Invalid("pre char", "character position")

    def p_pos(self, keyword):
        '''Set the place position. Automatic, no move, or align on
        centered. Only use if place not set.'''
        if self.frame["place"]:
            raise Invalid("pre place", "pPos")
        pos_dict = {
            "a": 0, "n": -101, "ac": -100, "auto": 0, "no move": -101,
            "align center": -100
        }
        self.frame["place_position"] = key_or_value(
            keyword, pos_dict, "place position")

    def speaker_name(self, name=""):
        '''Set a custom name for the present speaker. Takes speaker name as
        argument. With no argument, name will be the empty string.'''
        self.frame["speaker_name"] = name
        self.frame["speaker_use_name"] = True

    def speaker_id(self, speaker=""):
        '''Change the speaker ID to the ID, or null. With no argument,
        goes to null. With ???, turn to ???. Can take an integer argument if
        passed one by the special syntax.'''
        if not speaker:
            speaker = -3
        elif speaker == "?":
            speaker = -1
        elif not isinstance(speaker, int):
            active_object = self.from_object_dict(
                speaker, {"profiles"}, "Speaker")
            speaker = active_object.data["id"]
        self.frame["speaker_id"] = speaker
        # editor_frames_rows 996 forces this
        if not self.frame["speaker_use_name"]:
            if speaker == -1:
                self.frame["speaker_name"] = "???"
            elif speaker == -3:
                self.frame["speaker_name"] = ""
            else:
                self.frame["speaker_name"] = (
                    self.trial["profiles"][speaker]["short_name"])
        self.speaker_override = True

    def set_sprite(self, prefix, suffix):
        '''Sets the sprite with the given prefix and suffix.'''
        try:
            data = self.suffix_dicts[prefix]
        except KeyError:
            raise Invalid("unk pre", prefix)
        try:
            sprite_id = data["suffix dict"][suffix]
        except KeyError:
            raise Invalid("unk suff", suffix, prefix)
        if not self.speaker_override or not self.frame["place"]:
            self.frame["speaker_id"] = data["id"]
        for char in self.frame["characters"]:
            if char["profile_id"] == data["id"]:
                char["sprite_id"] = sprite_id
                break
        else:
            position = -1 if self.frame["place"] else 0
            self.frame["characters"].append({
                "profile_id": data["id"], "sprite_id": sprite_id,
                "sync_mode": 3, "startup_mode": 0, "position": position,
                "mirror_effect": False, "visual_effect_appears": 1,
                "visual_effect_appears_mode": 0,
                "visual_effect_disappears": 1,
                "visual_effect_disappears_mode": 0
            })

    @special
    def ce_start(self):
        '''Start a cross-examination. Structure is
        Testimony->Assistant->Press->Failure.'''
        self.location = "ceStart"
        self.frame["wait_time"] = 1
        self.frame["action_name"] = "CEStart"
        self.frame["action_parameters"] = {}
        ce_id = self.cross["id"] if self.cross else 0
        self.trial["cross_examinations"].append({
            "id": ce_id + 1, "start": self.frame["id"], "end": 0,
            "cocouncil_start": 0, "cocouncil_end": 0, "statements": [],
            "failure_conv_start": 0, "failure_conv_end": 0})
        self.cross = self.trial["cross_examinations"][-1]
        self.make_frame()

    @special
    def ce_statement(self, skip=False):
        '''Create a cross-examination statement.'''
        self.location = "ceStatement"
        self.statement_index += 1
        if not skip:
            self.pressable_indices.append(self.statement_index)
        self.frame["action_name"] = "CEStatement"
        self.frame["action_parameters"] = {
            "context": {"statement_desc": {
                "ce_id": "val="+str(self.cross["id"]), "statement_id":
                "val="+str(self.frame["id"])}}}
        self.cross["statements"].append({
            "id": self.frame["id"], "contradictions": [],
            "pressing_conv_start": 0, "pressing_conv_end": 0,
            "optional_conv_start": 0, "optional_conv_end": 0})

    @special
    def assist(self):
        '''Start an assistant conversation.'''
        self.statement_index = 0
        self.location = "assist"
        self.frame["wait_time"] = 1
        self.cross["cocouncil_start"] = self.frame["id"]
        self.frame["action_name"] = "CEPause"
        self.frame["action_parameters"] = {}
        self.make_frame()

    @no_manual
    def assist_end(self):
        '''End the assistant conversation.'''
        self.frame["wait_time"] = 1
        self.cross["cocouncil_end"] = self.frame["id"]
        self.frame["action_name"] = "CERestart"
        self.frame["action_parameters"] = {
            "context": {"ce_desc": "val="+str(self.cross["id"])}}
        self.make_frame()

    @special
    def press(self):
        '''Start a press conversation.'''
        try:
            # Run the end function for the last block.
            {"assist": self.assist_end, "press": self.press_end}[
                self.location]()
        except KeyError:
            raise Invalid("valid fail", "press", self.location)
        self.location = "press"
        self.frame["wait_time"] = 1
        try:
            index = self.pressable_indices[0]
        except IndexError:
            raise Invalid("excess press")
        self.cross["statements"][index]["pressing_conv_start"] = (
            self.frame["id"])
        self.frame["action_name"] = "CEPause"
        self.frame["action_parameters"] = {}
        self.make_frame()

    @no_manual
    def press_end(self):
        '''End a press conversation. Must be used before a new press
        conversation begins.'''
        index = self.pressable_indices.pop(0)
        self.frame["wait_time"] = 1
        self.cross["statements"][index]["pressing_conv_end"] = (
            self.frame["id"])
        self.cross["end"] = self.frame["id"]
        self.frame["action_name"] = "CEReturnAfter"
        self.frame["action_parameters"] = {
            "context": {"statement_desc": {
                "ce_id": "val="+str(self.cross["id"]), "statement_id":
                "val=" + str(self.cross["statements"][index]["id"])}}}
        self.make_frame()

    @special
    def fail(self):
        '''Start the cross-examination fail conversation.'''
        try:
            {"assist": self.assist_end, "press": self.press_end}[
                self.location]()
        except KeyError:
            raise Invalid("valid fail", "fail", self.location)
        self.location = "fail"
        if self.pressable_indices:
            raise Invalid(
                "inadequate press", "start fail conversation",
                len(self.pressable_indices))
        self.frame["wait_time"] = 1
        self.cross["failure_conv_start"] = self.frame["id"]
        self.frame["action_name"] = "CEPause"
        self.frame["action_parameters"] = {}
        self.make_frame()

    @no_manual
    def fail_end(self):
        '''End a fail conversation, and the cross-examination.'''
        self.frame["wait_time"] = 1
        self.cross["end"] = self.frame["id"]
        self.cross["failure_conv_end"] = self.frame["id"]
        self.frame["action_name"] = "CERestart"
        self.frame["action_parameters"] = {
            "context": {"ce_desc": "val="+str(self.cross["id"])}}
        self.make_frame()

    @special
    def ce_end(self):
        '''End the cross-examination'''
        self.cross["end"] = self.frame["id"]
        try:
            {"assist": self.assist_end, "press": self.press_end,
             "fail": self.fail_end}[self.location]()
        except KeyError:
            raise Invalid("valid fail", "ceEnd", self.location)
        if self.pressable_indices:
            raise Invalid(
                "inadequate press", "end cross examination",
                len(self.pressable_indices))
        self.location = ""

    @special
    def contra(self, item, dest_anc):
        '''Create a contradiction. Arguments are object to present and
        destination anchor.'''
        contra_ev = self.from_object_dict(
            item, {"profiles", "evidence"}, "Contradictory item")
        contras = self.cross["statements"][-1]["contradictions"]
        type_dict = {"type": contra_ev.attribute, "id": contra_ev.data["id"]}
        for contra in contras:
            if contra["contrad_elt"] == type_dict:
                raise Invalid("mult contra", item)
        self.anc_dict["frames"]["destination"].add((
            "cross_examinations", self.cross["id"], "statements",
            self.statement_index, "contradictions", len(contras),
            "destination"))
        contras.append({"contrad_elt": type_dict, "destination": dest_anc})

    def anc(self, point):
        '''Set an anchor. Point is the 'anchor phrase.' Anchor can be used in
        any frame with dialogue.'''
        if point in self.anc_dict["frames"]["value"]:
            raise Invalid("anc dupl", point)
        self.anc_dict["frames"]["value"][point] = self.frame["id"]

    @special
    def sce_intro(self, name="", hidden=False):
        '''Start the scene. Arguments are scene name and if hidden.
        This command writes multiple frames.'''
        self.location = "sceIntro"
        self.frame["wait_time"] = 1
        self.frame["action_name"] = "SceneStart"
        hidden = bool(hidden)
        sce_id = self.scene["id"] if self.scene else 0
        self.trial["scenes"].append({
            "id": sce_id + 1, "name": name, "hidden": hidden,
            "dialogues": [{
                "id": 1, "start": 0, "main": 0, "talk": 0, "present": 0, "end":
                0, "intro_start": 0, "intro_end": 0, "talk_topics": [],
                "present_conversations": [], "locks":None}],
            "current_dialogue": 1, "examinations": [],
            "current_examination": 1, "start": self.frame["id"],
            "move": 0, "end": 0, "move_list": []})
        self.scene = self.trial["scenes"][-1]
        self.frame["action_parameters"] = {"context": {"scene": {
            "scene_type": "val=scenes",
            "scene_id": "val="+str(self.scene["id"])}}}
        self.make_frame()
        self.frame["action_name"] = "GoTo"
        # Missing action_parameters is accounted for in sceMain.
        self.frame["wait_time"] = 1
        self.frame["hidden"] = 1
        self.scene = self.trial["scenes"][-1]
        self.scene_dia = self.scene["dialogues"][0]
        self.scene_dia["start"] = self.frame["id"]
        self.scene_dia["intro_start"] = self.frame["id"]
        self.make_frame()
        self.frame["action_name"] = "RevealFrame"
        self.frame["action_parameters"] = {"multiple": {"frame": [{
            "target": "val="+str(self.frame["id"]-1)}]}}
        self.frame["wait_time"] = 1
        self.make_frame()

    @special
    def sce_main(self, anc=""):
        '''Ends the introduction conversation and creates the scene
        interface.'''
        self.location = "sceMain"
        self.frame["action_name"] = "GoTo"
        # Missing action_parameters is accounted for after make_frame.
        self.frame["wait_time"] = 1
        self.scene_dia["intro_end"] = self.frame["id"]
        self.make_frame()
        self.scene_dia["main"] = self.frame["id"]
        self.trial["frames"][self.scene_dia["start"]][
            "action_parameters"] = (
                {"global": {"target": "val="+str(self.frame["id"])}})
        self.trial["frames"][self.scene_dia["intro_end"]][
            "action_parameters"] = (
                {"global": {"target": "val="+str(self.frame["id"])}})
        self.frame["action_name"] = "DialogueMenu"
        self.frame["action_parameters"] = {"context": {"dialogue": {
            "scene_type": "val=scenes",
            "scene_id": "val="+str(self.scene["id"]),
            "section_type": "val=dialogues", "section_id": "val=1"}}}
        if anc:
            if anc in self.anc_dict["scenes"]["value"]:
                raise Invalid("anc dupl", anc)
            self.anc_dict["scenes"]["value"][anc] = self.scene["id"]

    @special
    def sce_talk(self):
        '''Create the talk interface.'''
        self.location = "sceTalk"
        self.frame["action_name"] = "DialogueTalk"
        self.frame["action_parameters"] = {"context": {"dialogue": {
            "scene_type": "val=scenes",
            "scene_id": "val="+str(self.scene["id"]),
            "section_type": "val=dialogues", "section_id": "val=1"}}}
        self.scene_dia["talk"] = self.frame["id"]
        self.make_frame()

    @special
    def sce_talk_convo(self, title="", hidden=False, anc=""):
        '''Start a talk option. Arguments are title for option, and if hidden,
        and if anchor.'''
        if self.location == "sceTalkConvo":
            self.sce_talk_end()
        self.location = "sceTalkConvo"
        hidden = bool(hidden)
        talk_id = len(self.scene_dia["talk_topics"]) + 1
        self.scene_dia["talk_topics"].append({
            "start": self.frame["id"], "end": 0,
            "id": talk_id, "title": title,
            "hidden": hidden, "icon": 0})
        self.frame["wait_time"] = 1
        if anc:
            if anc in self.anc_dict["talk"]["value"]:
                raise Invalid("anc dupl", anc)
            self.anc_dict["talk"]["value"][anc] = talk_id
            self.anc_dict["talk_sce"]["value"][anc] = self.scene["id"]
        self.make_frame()

    @no_manual
    def sce_talk_end(self):
        '''End a talk option.'''
        self.frame["action_name"] = "GoTo"
        self.frame["action_parameters"] = {"global": {
            "target": "val="+str(self.scene_dia["talk"])}}
        self.scene_dia["talk_topics"][-1]["end"] = self.frame["id"]
        self.frame["wait_time"] = 1
        self.make_frame()

    @special
    def sce_pres(self):
        '''Start a present sequence.'''
        if self.location == "sceTalkConvo":
            self.sce_talk_end()
        self.location = "scePres"
        self.frame["action_name"] = "DialoguePresent"
        self.frame["action_parameters"] = {
            "context": {"dialogue": {
                "scene_type": "val=scenes",
                "scene_id": "val="+str(self.scene["id"]),
                "section_type": "val=dialogues", "section_id": "val=1"}}}
        self.scene_dia["present"] = self.frame["id"]
        self.make_frame()
        self.sce_pres_convo()

    @special
    def sce_pres_convo(self, evidence=""):
        '''Start an individual present. Takes name of evidence/profile as
        argument.'''
        self.location = "scePresConvo"
        if self.scene_dia["present_conversations"]:
            self.sce_pres_end()
            pres_ev = self.from_object_dict(
                evidence, {"profiles", "evidence"}, "Item to present")
            snippet = {"type": pres_ev.attribute, "id": pres_ev.data["id"]}
            for present in self.scene_dia["present_conversations"]:
                if present["elt"] == snippet:
                    raise Invalid("mult pres", evidence)
        else:
            snippet = None
        self.frame["wait_time"] = 1
        self.scene_dia["present_conversations"].append({
            "elt": snippet, "start": self.frame["id"], "end": 0})
        self.make_frame()

    @no_manual
    def sce_pres_end(self):
        '''End an individual present.'''
        self.frame["action_name"] = "GoTo"
        self.frame["action_parameters"] = {
            "global": {"target": "val="+str(self.scene_dia["present"])}}
        self.scene_dia["present_conversations"][-1]["end"] = (
            self.frame["id"])
        self.frame["wait_time"] = 1
        self.make_frame()

    @special
    def sce_locks(self, *argv):
        '''Start psyche-locks. Arguments are sequence of x and y, then
        (optional) hidden status.'''
        self.sce_pres_end()
        try:
            int(argv[0] if argv else "0")
            hidden = False
        except ValueError:
            argv = argv[1:]
            hidden = True
        self.location = "sceLocks"
        self.scene_dia["locks"] = {
            "start": self.frame["id"], "end": 0, "hidden": hidden,
            "locks_to_display": []}
        argv = list_to_n_tuple(
            argv, 2, " plus one for hidden" if hidden else "")
        err_msg = "Arguments to sceLocks after the optional hidden"
        for index, (x_coord, y_coord) in enumerate(argv):
            x_coord = validate_int(x_coord, err_msg)
            y_coord = validate_int(y_coord, err_msg)
            self.scene_dia["locks"]["locks_to_display"].append({
                "id": index+1, "type": "jfa_lock", "x": x_coord,
                "y": y_coord})
        self.frame["wait_time"] = 1
        self.make_frame()

    @special
    def sce_exam(self, place=0):
        '''Initialize examinations. Takes the place to examine as argument.
        Also ends psyche_locks.'''
        if self.location == "scePresConvo":
            self.sce_pres_end()
        elif self.location == "sceLocks":
            self.scene_dia["locks"]["end"] = self.frame["id"]
            self.frame["wait_time"] = 1
            self.frame["action_name"] = "LocksEnd"
            self.frame["action_parameters"] = {"context": {
                "parent_dialogue": {
                    "scene_type": "val=scenes", "scene_id":
                    "val="+str(self.scene["id"]),
                    "section_type": "val=dialogues", "section_id": "val=1"}}}
            self.make_frame()
        else:
            raise Invalid("valid fail", "sceExam", self.location)
        self.scene_dia["end"] = self.frame["id"]
        self.make_frame()
        if place:
            place = self.from_object_dict(
                place, {"places"}, "Place to examine")
            place = place.data["id"]
            # AAO does not support a pre-defined place here. See AAO Issue
            # 108. Replace this if suite with the comment below once fixed.
            # try:
            #    place = self.from_object_dict(
            #        place, {"places"}, "Place to examine")
            #    place = place.data["id"]
            # except Invalid:
            #    built_dict = {
            #        "black": -1, "pw bench": -2, "pw judge": -6,
            #        "pw counsel": -3, "pw court loud": -8,
            #        "pw court silent": -9, "pw lobby": -10,
            #        "pw det behind": -18, "pw det ahead": -19,
            #        "aj bench": -12, "aj judge": -14, "aj counsel": -13,
            #        "aj court loud": -15, "aj court silent": -16,
            #        "aj lobby": -17, "aj det behind":-20, "aj det ahead": -21,
            #        "power def": -4, "power pros": -5, "gavel 1": -7,
            #        "gavel 3": -11
            #    }
            #    place = key_or_value(place, built_dict, "place")
        else:
            place = 0
        self.frame["action_name"] = "ExaminationExamine"
        self.frame["action_parameters"] = {"context": {"examination": {
            "scene_type": "val=scenes",
            "scene_id": "val="+str(self.scene["id"]),
            "section_type": "val=examinations", "section_id": "val=1"}}}
        self.scene["examinations"].append({
            "id": 1, "start": self.frame["id"], "examine": self.frame["id"],
            "end": 0, "place": place, "examine_conversations": [],
            "deduce_conversations": [], "enable_deduction": False})
        self.make_frame()
        self.sce_exam_convo()

    @special
    def sce_exam_convo(self, shape="", *argv):
        '''Create the examination. Takes arguments for the area. You can only
        avoid arguments for the default.'''
        if self.location == "sceExamConvo":
            self.sce_exam_end()
            if shape == "poly":
                if len(argv) % 2:
                    raise Invalid("poly pair")
                if len(argv) < 6:
                    raise Invalid("poly 6")
            elif shape == "rect":
                if len(argv) != 4:
                    raise Invalid("rect 4")
                if not (int(argv[2]) > int(argv[0]) and (
                        int(argv[3]) > int(argv[1]))):
                    raise Invalid("rect to quad 4")
            elif shape == "circle":
                if len(argv) != 3:
                    raise Invalid("circle 3")
            else:
                raise Invalid("bad shape", shape)
            for coord in argv[1:]:
                int_at_least(coord, 0, "All arguments after polygon shape")
            exam_dict = {
                "start": self.frame["id"], "end": 0,
                "area": shape + ":" + ",".join(argv)}
        else:
            exam_dict = {"area": None, "start": self.frame["id"], "end": 0}
        self.location = "sceExamConvo"
        self.frame["wait_time"] = 1
        self.scene["examinations"][0]["examine_conversations"].append(
            exam_dict)
        self.make_frame()

    @no_manual
    def sce_exam_end(self):
        '''End the examination.'''
        self.scene["examinations"][0][
            "examine_conversations"][-1]["end"] = self.frame["id"]
        self.frame["action_name"] = "GoTo"
        self.frame["action_parameters"] = {
            "global": {"target": "val="+str(self.scene["examinations"][0][
                "start"])}}
        self.frame["wait_time"] = 1
        self.make_frame()

    @special
    def sce_move(self, *argv):
        '''Handle deduction frames, end the investigation block, and go into
        sceMove.'''
        self.sce_exam_end()
        self.location = ""
        self.frame["wait_time"] = 1
        dedu_dict = {"area": None, "elt": None, "start": self.frame["id"],
                     "end": 0}
        self.scene["examinations"][0]["deduce_conversations"].append(dedu_dict)
        self.make_frame()
        self.scene["examinations"][0]["deduce_conversations"][-1]["end"] = (
            self.frame["id"])
        self.frame["action_name"] = "GoTo"
        self.frame["action_parameters"] = {
            "global": {"target": "val="+str(
                self.scene["examinations"][0]["start"])}}
        self.frame["wait_time"] = 1
        self.make_frame()
        self.frame["wait_time"] = 1
        self.scene["examinations"][0]["end"] = self.frame["id"]
        self.make_frame()
        self.frame["action_name"] = "SceneMove"
        self.frame["action_parameters"] = {
            "context": {"scene": {"scene_type": "val=scenes", "scene_id":
                                  "val="+str(self.scene["id"])}}}
        self.scene["move"] = self.frame["id"]
        self.scene["end"] = self.frame["id"]
        object_list = list_to_n_tuple(argv, 2)
        for i, j in object_list:
            self.anc_dict["scenes"]["destination"].add((
                "scenes", self.scene["id"], "move_list",
                len(self.scene["move_list"]), "scene_id"))
            self.scene["move_list"].append({
                "scene_type": "scenes", "scene_id": i, "name_override": j})
        self.make_frame()

    @action
    def disp_ev(self, *argv):
        '''Display evidence. Arguments are evidence name and position as
        coded.'''
        def check_ev(item):
            '''Utility function to check if the item is a profile or
            evidence.'''
            return self.from_object_dict(
                item, {"profiles", "evidence"}, "Item to display")

        self.frame["action_name"] = "DisplayElements"
        self.frame["action_parameters"] = {"multiple": {"element": []}}
        pos_dict = {"a": "auto", "tr": "topright", "tl": "topleft",
                    "br": "bottomright", "bl": "bottomleft"}
        parsed_exp = expression_pack(argv, mult_schema=(2, 1))
        insert = self.frame["action_parameters"]["multiple"]["element"]
        for evidence, pos in parsed_exp["multiple"]:
            if evidence[0] == "val":
                place = check_ev(evidence[1])
                evidence = ("val", place.attribute, str(place.data["id"]))
            else:
                evidence[1] = re.sub(r"\n(.*)\n", (
                    lambda m: check_ev(m.group(1)).atribute), evidence[1])
                evidence[2] = re.sub(r"\n(.*)\n", (
                    lambda m: check_ev(m.group(1)).data["id"]), evidence[2])
            if pos[0] == "val":
                pos[1] = key_or_value(
                    pos[1], pos_dict, "evidence position", True)
            for ele in insert:
                if ele["position"] == param(pos, 1):
                    raise Invalid("mult pos", pos[1])
            insert.append({
                "element_desc": {
                    "type": param(evidence, 1), "id": param(evidence, 2)},
                "position": param(pos, 1)
            })

    @no_manual
    def set_unset_ev_helper(self, msg, *argv):
        '''Helper function for setting and unsetting evidence. Handles the
        action parameters.'''
        def check_ev(item):
            '''Utility function to check if the item is a profile or
            evidence.'''
            return self.from_object_dict(item, {"profiles", "evidence"}, msg)

        self.frame["action_parameters"] = {"multiple": {"element": []}}
        parsed_exp = expression_pack(argv, mult_schema=(2,))
        insert = self.frame["action_parameters"]["multiple"]["element"]
        for evidence, in parsed_exp["multiple"]:
            if evidence[0] == "val":
                place = check_ev(evidence[1])
                evidence = ("val", place.attribute, str(place.data["id"]))
            else:
                evidence[1] = re.sub(r"\n(.*)\n", (
                    lambda m: check_ev(m.group(1)).attribute), evidence[1])
                evidence[2] = re.sub(r"\n(.*)\n", (
                    lambda m: check_ev(m.group(1)).data["id"]), evidence[2])
            insert.append({"element_desc": {
                "type": param(evidence, 1), "id": param(evidence, 2)}})

    @action
    def hide_ev(self, *argv):
        '''Hide evidence. Argument is evidence name.'''
        self.frame["action_name"] = "HideElements"
        self.set_unset_ev_helper("Item to hide", *argv)

    @action
    def rev_ev(self, *argv):
        '''Reveal evidence. Argument is evidence name.'''
        self.frame["action_name"] = "RevealElements"
        self.set_unset_ev_helper("Item to display", *argv)

    @no_manual
    def over_proceed_helper(self, *argv):
        '''Helper function for game overs and proceed to frame. Handles the
        action parameters.'''
        parsed_exp = expression_pack(argv, global_schema=(1,))["global"][0]
        self.frame["action_parameters"] = {
            "context": {"not_merged": "val=true"},
            "global": {"target": param(parsed_exp, 1)}}
        self.anc_dict["frames"]["destination"].add((
            "frames", self.frame["id"], "action_parameters", "global",
            "target"
        ))

    @merge_lock
    @action
    def set_over(self, *argv):
        '''Make a game over redirect. Argument is an anchor.'''
        self.frame["action_name"] = "SetGameOver"
        self.over_proceed_helper(*argv)

    @merge_lock
    @action
    def proceed(self, *argv):
        '''Make a proceed command. Argument is an anchor.'''
        self.frame["action_name"] = "GoTo"
        self.over_proceed_helper(*argv)

    @no_manual
    def hide_reveal_frame_helper(self, *argv):
        '''Helper function for hiding and revealing frames. Handles the
        action parameters.'''
        self.frame["action_parameters"] = {"multiple": {"frame": []}}
        parsed_exp = expression_pack(argv, mult_schema=(1,))
        insert = self.frame["action_parameters"]["multiple"]["frame"]
        for frame, in parsed_exp["multiple"]:
            self.anc_dict["frames"]["destination"].add((
                "frames", self.frame["id"], "action_parameters", "multiple",
                "frame", len(insert), "target"))
            insert.append({"target": param(frame, 1)})

    @action
    def hide_frame(self, *argv):
        '''Hide a frame. Arguments are anchors.'''
        self.frame["action_name"] = "HideFrame"
        self.hide_reveal_frame_helper(*argv)

    @action
    def reveal_frame(self, *argv):
        '''Reveal a frame. Arguments are anchors.'''
        self.frame["action_name"] = "RevealFrame"
        self.hide_reveal_frame_helper(*argv)

    @merge_lock
    @action
    def game_over(self, dest, data="", part="", frame=""):
        '''End the game. First command tells which end state to go. If 'next'
        or 'another' end state, supply data-transfer type. If 'another,' also
        supply target part and frame IDs.'''
        self.frame["action_name"] = "GameOver"
        self.frame["action_parameters"] = {
            "context": {"not_merged": "val=true"}, "global": {"action": ""}}
        data_dict = {"none": "0", "var": "1", "full": "2"}
        parsed_exp = expression_pack(
            [dest, data, part, frame], (1, 1, 1, 1))["global"]
        insert = self.frame["action_parameters"]["global"]
        if all([x[0] == "val" for x in parsed_exp]) and (
                parsed_exp[0][1] != "another"):
            if parsed_exp[0][1] == "end":
                insert["action"] = "val=0"
            elif parsed_exp[0][1] == "next":
                parsed_exp = parsed_exp[1]
                if not parsed_exp[1]:
                    raise Invalid("arg missing", "Data to transfer")
                parsed_exp[1] = key_or_value(
                    parsed_exp[1], data_dict, "game over transfer data", True)
                insert["action"] = "val=1"
                insert["data_transfer"] = param(parsed_exp, 1)
            else:
                raise Invalid("bad key", parsed_exp[0][1], "target part")
        else:
            if parsed_exp[0][0] == "val" and parsed_exp[0][1] not in {
                    "end", "next", "another"}:
                raise Invalid("bad key", parsed_exp[0][1], "target part")
            else:
                proceed_dict = {"end": "0", "next": "1", "another": "2"}
                parsed_exp[0] = (parsed_exp[0][0], key_or_value(
                    parsed_exp[0][1], proceed_dict, "proceed", True))
            if not parsed_exp[1][1]:
                raise Invalid("arg missing", "Data to transfer")
            if not parsed_exp[2][1]:
                raise Invalid("arg missing", "Target part")
            if not parsed_exp[3][1]:
                raise Invalid("arg missing", "Target frame")
            if parsed_exp[1][0] == "val":
                parsed_exp[1][1] = key_or_value(
                    parsed_exp[1][1], data_dict, "game over transfer data",
                    True)
            insert["action"] = param(parsed_exp[0], 1)
            insert["data_transfer"] = param(parsed_exp[1], 1)
            insert["target_part"] = param(parsed_exp[2], 1)
            insert["target_frame"] = param(parsed_exp[3], 1)

    @no_manual
    def hide_rev_obj_helper(self, *argv):
        '''Helper function for revealing and hiding objects. Handles the
        action parameters.'''

        def place_replace(match):
            '''Replace place keywords with the place ID as needed.'''
            match = match.group(1)
            try:
                base_place = self.from_object_dict(
                    match, {"places"}, "Place with object")
                return str(base_place.data["id"])
            except Invalid:
                return str(key_or_value(match, built_dict, "place"))

        self.frame["action_parameters"] = {"multiple": {"object": []}}
        parsed_exp = expression_pack(argv, mult_schema=(1, 3))["multiple"]
        built_dict = {
            "pw bench": -2, "pw judge": -6, "pw det behind": -18,
            "aj bench": -12, "aj judge": -14, "aj det behind": -20}
        for place, subobj in parsed_exp:
            skip = False
            if place[0] == "val":
                # If the first place isn't an expression, seek from the
                # defined places, then the AAO built-ins.
                try:
                    base_place = self.from_object_dict(
                        place[1], {"places"}, "Place with object")
                    place[1] = base_place.data["id"]
                except Invalid:
                    place = ["val", key_or_value(
                        place[1], built_dict, "place")]
                    # Place is a built-in. Mark "skip" because the subobject
                    # needs no fixing.
                    subobj = ["val", place[1], "foreground_objects", 1]
                    skip = True
            else:
                # Otherwise, look for things that were between two newlines
                # and replace those.
                place[1] = re.sub(r"\n(.*)\n", place_replace, place[1])
            if subobj[0] == "val" and not skip:
                try:
                    layer, sub_id = find_subobject(
                        {"foreground_objects", "background_objects"},
                        base_place, subobj[1])
                except NameError:
                    raise Invalid("exp dependency")
                subobj[1] = place[1]
                subobj.append(layer)
                subobj.append(sub_id)
            elif not skip:
                subobj[1] = re.sub(r"\n(.*)\n", place_replace, subobj[1])
            self.frame["action_parameters"]["multiple"]["object"].append({
                "place_desc": param(place, 1),
                "object_desc": {
                    "place_id": param(subobj, 1), "layer": param(subobj, 2),
                    "id": param(subobj, 3)}})

    @action
    def hide_obj(self, *argv):
        '''Hide an object. Arguments are place name and object name.'''
        self.frame["action_name"] = "HideObject"
        self.hide_rev_obj_helper(*argv)

    @action
    def rev_obj(self, *argv):
        '''Reveal an object. Arguments are place name and object name.'''
        self.frame["action_name"] = "RevealObject"
        self.hide_rev_obj_helper(*argv)

    @no_manual
    def hide_rev_sce_helper(self, *argv):
        '''Helper function for revealing and hiding scenes. Handles the
        action parameters.'''
        scene = expression_pack(argv, global_schema=(2,))["global"][0]
        if scene[0] == "val":
            scene.insert(1, "scenes")
        self.frame["action_parameters"] = {
            "global": {
                "scene": {
                    "scene_type": param(scene, 1),
                    "scene_id": param(scene, 2)
                }
            }
        }
        self.anc_dict["scenes"]["destination"].add((
            "frames", self.frame["id"], "action_parameters", "global",
            "scene", "scene_id"))

    @action
    def hide_sce(self, *argv):
        '''Hide scene. Argument is scene anchor.'''
        self.frame["action_name"] = "HideScene"
        self.hide_rev_sce_helper(*argv)

    @action
    def rev_sce(self, *argv):
        '''Reveal scene. Argument is scene anchor.'''
        self.frame["action_name"] = "RevealScene"
        self.hide_rev_sce_helper(*argv)

    @no_manual
    def hide_rev_intro_helper(self, *argv):
        '''Helper function for revealing and hiding introduction
        conversations. Handles action parameters.'''
        parsed_exp = expression_pack(argv, global_schema=(6,))["global"][0]
        if parsed_exp[0] == "val":
            parsed_exp.insert(1, "scenes")
            parsed_exp += (parsed_exp[1:3] + ["dialogues", "1"])
        self.frame["action_parameters"] = {"global": {
            "scene": {"scene_type": param(parsed_exp, 1),
                      "scene_id": param(parsed_exp, 2)},
            "dialogue": {"scene_type": param(parsed_exp, 3),
                         "scene_id": param(parsed_exp, 4),
                         "section_type": param(parsed_exp, 5),
                         "section_id": param(parsed_exp, 6)}
            }}
        self.anc_dict["scenes"]["destination"].add((
            "frames", self.frame["id"], "action_parameters", "global",
            "scene", "scene_id"))
        self.anc_dict["scenes"]["destination"].add((
            "frames", self.frame["id"], "action_parameters", "global",
            "dialogue", "scene_id"))

    @action
    def hide_intro(self, *argv):
        '''Hide intro conversation. Takes scene anchor as argument.'''
        self.frame["action_name"] = "HideDialogueIntro"
        self.hide_rev_intro_helper(*argv)

    @action
    def rev_intro(self, *argv):
        '''Reveal intro conversation. Takes scene anchor as argument.'''
        self.frame["action_name"] = "RevealDialogueIntro"
        self.hide_rev_intro_helper(*argv)

    @no_manual
    def hide_rev_talk_helper(self, *argv):
        '''Helper function for hiding reveal and talk converstions. Handles
        the action parameters.'''
        talk = expression_pack(argv, global_schema=(12,))["global"][0]
        if talk[0] == "val":
            talk.insert(1, "scenes")
            talk += (talk[1:3] + ["dialogues", "1"])
            talk += (talk[-4:] + ["talk_topics", talk[2]])
        self.frame["action_parameters"] = {"global": {
            "scene": {
                "scene_type": param(talk, 1), "scene_id": param(talk, 2)},
            "dialogue": {
                "scene_type": param(talk, 3), "scene_id": param(talk, 4),
                "section_type": param(talk, 5), "section_id": param(talk, 6)},
            "talk_topic": {
                "scene_type": param(talk, 7), "scene_id": param(talk, 8),
                "section_type": param(talk, 9), "section_id": param(talk, 10),
                "conv_type": param(talk, 11), "conv_id": param(talk, 12)}}}
        self.anc_dict["talk_sce"]["destination"].add((
            "frames", self.frame["id"], "action_parameters", "global",
            "scene", "scene_id"))
        self.anc_dict["talk_sce"]["destination"].add((
            "frames", self.frame["id"], "action_parameters", "global",
            "dialogue", "scene_id"))
        self.anc_dict["talk_sce"]["destination"].add((
            "frames", self.frame["id"], "action_parameters", "global",
            "talk_topic", "scene_id"))
        self.anc_dict["talk"]["destination"].add((
            "frames", self.frame["id"], "action_parameters", "global",
            "talk_topic", "conv_id"))

    @action
    def hide_talk(self, *argv):
        '''Hide a talk conversation. Takes convo anchor as argument.'''
        self.frame["action_name"] = "HideTalkTopic"
        self.hide_rev_talk_helper(*argv)

    @action
    def rev_talk(self, *argv):
        '''Reveal a talk conversation. Takes convo anchor as argument.'''
        self.frame["action_name"] = "RevealTalkTopic"
        self.hide_rev_talk_helper(*argv)

    @no_manual
    def hide_rev_psy_button_helper(self, *argv):
        '''Helper functions for hiding and revealing the psyche-lock
        button. Handles action parameters.'''
        parsed_exp = expression_pack(argv, global_schema=(6,))["global"][0]
        if parsed_exp[0] == "val":
            parsed_exp.insert(1, "scenes")
            parsed_exp += (parsed_exp[1:3] + ["dialogues", "1"])
        self.frame["action_parameters"] = {
            "global": {"scene": {"scene_type": param(parsed_exp, 1),
                                 "scene_id": param(parsed_exp, 2)},
                       "dialogue": {"scene_type": param(parsed_exp, 3),
                                    "scene_id": param(parsed_exp, 4),
                                    "section_type": param(parsed_exp, 5),
                                    "section_id": param(parsed_exp, 6)}}}
        self.anc_dict["scenes"]["destination"].add((
            "frames", self.frame["id"], "action_parameters", "global",
            "scene", "scene_id"))
        self.anc_dict["scenes"]["destination"].add((
            "frames", self.frame["id"], "action_parameters", "global",
            "dialogue", "scene_id"))
        self.check_locks.add((
            "frames", self.frame["id"], "action_parameters", "global",
            "scene", "scene_id"))

    @action
    def hide_psy_button(self, *argv):
        '''Hide psyche-locks button. Takes scene anchor as argument.'''
        self.frame["action_name"] = "HideDialogueLocks"
        self.hide_rev_psy_button_helper(*argv)

    @action
    def rev_psy_button(self, *argv):
        '''Hide psyche-locks button. Takes scene anchor as argument.'''
        self.frame["action_name"] = "RevealDialogueLocks"
        self.hide_rev_psy_button_helper(*argv)

    @no_manual
    def hide_rev_psy_helper(self):
        '''Helper function for hiding and reveal psyche-locks. Handles the
        action parameters.'''
        self.frame["action_parameters"] = {"context": {"parent_dialogue": {
            "scene_type": "val=scenes",
            "scene_id": "val="+str(self.scene["id"]),
            "section_type": "val=dialogues", "section_id": "val=1"}}}

    @scene_only
    @action
    def hide_psy(self):
        '''Hide psyche-locks. Can only be used in investigation.'''
        self.frame["action_name"] = "LocksHide"
        self.hide_rev_psy_helper()

    @scene_only
    @action
    def rev_psy(self):
        '''Reveal psyche-locks. Can only be used in investigation.'''
        self.frame["action_name"] = "LocksShow"
        self.hide_rev_psy_helper()

    @scene_only
    @action
    def break_psy(self, *argv):
        '''Break a psyche-lock or psyche-locks. Argument is lock numbers.
        0 for automatic mode. Can only be used in investigation.'''
        argv = argv or ["0"]
        self.frame["action_name"] = "LocksBreak"
        parsed_exp = expression_pack(argv, mult_schema=(5,))["multiple"]
        self.frame["action_parameters"] = {
            "context": {"parent_dialogue": {
                "scene_type": "val=scenes",
                "scene_id": "val="+str(self.scene["id"]),
                "section_type": "val=dialogues", "section_id": "val=1"}},
            "multiple": {"lock": []}
        }
        for descript in parsed_exp:
            descript = descript[0]
            if descript[0] == "val":
                descript = [
                    descript[0], "scenes", str(self.scene["id"]),
                    "dialogues", "1", descript[1]]
            try:
                int(descript[5])
            except ValueError:
                descript[5] = "0"
            self.frame["action_parameters"]["multiple"]["lock"].append({
                "lock_desc": {
                    "scene_type": param(descript, 1),
                    "scene_id": param(descript, 2),
                    "section_type": param(descript, 3),
                    "section_id": param(descript, 4),
                    "lock_id": param(descript, 5)}})

    @no_manual
    def set_red_health_helper(self, *argv):
        '''Helper for setting and reducing health. Handles the action
        parameters.'''
        descript = expression_pack(argv, global_schema=(1,))["global"][0]
        if descript[0] == "val":
            validate_int(descript[1], "Health")
        self.frame["action_parameters"] = {
            "context": {"not_merged": "val=true"},
            "global": {"points": param(descript, 1)}}

    @merge_lock
    @action
    def set_health(self, *argv):
        '''Set health. Argument is the number.'''
        self.frame["action_name"] = "SetHealth"
        self.set_red_health_helper(*argv)

    @merge_lock
    @action
    def red_health(self, *argv):
        '''Reduce health. Argument is the number.'''
        self.frame["action_name"] = "ReduceHealth"
        self.set_red_health_helper(*argv)

    @no_manual
    def flash_inc_health_helper(self, *argv):
        '''Helper for flashing and increasing health. Handles action
        parameters.'''
        descript = expression_pack(argv, global_schema=(1,))["global"][0]
        if descript[0] == "val":
            validate_int(descript[1], "Health")
        self.frame["action_parameters"] = {
            "global": {"points": param(descript, 1)}}

    @action
    def flash_health(self, *argv):
        '''Flash health. Argument is the number.'''
        self.frame["action_name"] = "FlashHealth"
        self.flash_inc_health_helper(*argv)

    @action
    def inc_health(self, *argv):
        '''Increase health. Argument is the number.'''
        self.frame["action_name"] = "IncreaseHealth"
        self.flash_inc_health_helper(*argv)

    @no_manual
    def input_helper(self, global_schema, mult_schema, *argv):
        '''Helper for input player input functions. Handles parameter
        actions.'''
        if self.location == "sceLocks":
            # If we're in psyche locks, add a Back Button term.
            global_schema = (1,) + global_schema
            exp_parsed = expression_pack(argv, global_schema, mult_schema)
            parent_dialogue = {"scene_type": "val=scenes", "scene_id":
                               "val="+str(self.scene["id"]), "section_type":
                               "val=dialogues", "section_id": "val=1"}
            in_locks = "val=true"
            lock_tuple = exp_parsed["global"].pop(0)
            if lock_tuple[0] == "val":
                lock_tuple[1] = "true" if lock_tuple else "false"
        else:
            if self.location.startswith("sce"):
                parent_dialogue = {
                    "scene_type": "val=scenes",
                    "scene_id": "val="+str(self.scene["id"]),
                    "section_type": "val=dialogues", "section_id": "val=1"
                }
            else:
                parent_dialogue = "val=0"
            exp_parsed = expression_pack(
                argv, global_schema=global_schema, mult_schema=mult_schema)
            in_locks = "val=0"
            lock_tuple = ["val", "false"]
        self.frame["action_parameters"] = {
            "context": {"parent_dialogue": parent_dialogue, "in_locks":
                        in_locks, "not_merged": "val=true"},
            "global": {
                "locks_show_return": param(lock_tuple, 1)}, "multiple": {}}
        return exp_parsed

    @merge_lock
    @action
    def choice(self, *argv):
        '''Write a multiple choice prompt. Arguments are respectively text to
        display and anchor.'''
        self.frame["action_name"] = "MultipleChoices"
        exp_parsed = self.input_helper(tuple(), (1, 1), *argv)
        self.frame["action_parameters"]["multiple"]["answer"] = []
        insert = self.frame["action_parameters"]["multiple"]["answer"]
        for text, frame in exp_parsed["multiple"]:
            self.anc_dict["frames"]["destination"].add((
                "frames", self.frame["id"], "action_parameters",
                "multiple", "answer", len(insert), "answer_dest"))
            insert.append({
                "answer_text": param(text, 1), "answer_dest": param(frame, 1)})

    @merge_lock
    @action
    def ask_ev(self, *argv):
        '''Request evidence from player. Arguments are type lock, failure
        destination, then alternating object to present and failure
        location...'''
        def check_ev(item):
            '''Utility function to check if the item is a profile or
            evidence.'''
            return self.from_object_dict(
                item, {"profiles", "evidence"}, "Item to present")

        self.frame["action_name"] = "AskForEvidence"
        exp_parsed = self.input_helper((1, 1), (2, 1), *argv)
        lock, dest = exp_parsed["global"]
        if lock[0] == "val":
            lock[1] = key_or_value(
                lock[1], {"ev": "evidence", "pro": "profiles", "all": "all"},
                "Permissible evidence", True
            )
        snip = {"type_lock": param(lock, 1), "failure_dest": param(dest, 1)}
        self.frame["action_parameters"]["global"].update(snip)
        self.anc_dict["frames"]["destination"].add((
            "frames", self.frame["id"], "action_parameters", "global",
            "failure_dest"))
        self.frame["action_parameters"]["multiple"]["element"] = []
        insert = self.frame["action_parameters"]["multiple"]["element"]
        for ele, frame in exp_parsed["multiple"]:
            if ele[0] == "val":
                evi = check_ev(ele[1])
                ele = [ele[0], evi.attribute, evi.data["id"]]
            else:
                ele[1] = re.sub(r"\n(.*)\n", (
                    lambda m: check_ev(m.group(1)).atribute), ele[1])
                ele[2] = re.sub(r"\n(.*)\n", (
                    lambda m: check_ev(m.group(1)).data["id"]), ele[2])
            self.anc_dict["frames"]["destination"].add((
                "frames", self.frame["id"], "action_parameters", "multiple",
                "element", len(insert), "element_dest"
            ))
            insert.append({
                "element_desc": {"type": param(ele, 1), "id": param(ele, 2)},
                "element_dest": param(frame, 1)
            })

    @merge_lock
    @action
    def point(self, *argv):
        '''Call on the player to point to an area. Arguments are background,
        target frame ID, a region term, and a target frame anchor. A back
        button is prepended to the argument list if in a scene.'''

        def poly(pieces):
            '''Validate for a polygonal shape.'''
            if len(pieces) % 2:
                raise Invalid("poly pair")
            if len(pieces) < 6:
                raise Invalid("poly 6")

        def circle(pieces):
            '''Validate for a circular shape.'''
            if len(pieces) != 3:
                raise Invalid("circle 3")

        def rect(pieces):
            '''Validate for a rectangular shape.'''
            if len(pieces) != 4:
                raise Invalid("rect 4")
            if not (int(pieces[2]) > int(pieces[0]) and (
                    int(pieces[3]) > int(pieces[1]))):
                raise Invalid("rect to quad 4")

        self.frame["action_name"] = "PointArea"
        exp_parsed = self.input_helper((1, 1), (1, 1), *argv)
        place, frame = exp_parsed["global"]
        if place[0] == "val":
            try:
                place[1] = self.from_object_dict(
                    place[1], {"places"}, "Place to point at").data["id"]
            except Invalid:
                built_dict = {
                    "black": -1, "pw bench": -2, "pw judge": -6,
                    "pw counsel": -3, "pw court loud": -8,
                    "pw court silent": -9, "pw lobby": -10,
                    "pw det behind": -18, "pw det ahead": -19,
                    "aj bench": -12, "aj judge": -14, "aj counsel": -13,
                    "aj court loud": -15, "aj court silent": -16,
                    "aj lobby": -17, "aj det behind": -20,
                    "aj det ahead": -21, "power def": -4, "power pros": -5,
                    "gavel 1": -7, "gavel 3": -11
                }
                place[1] = key_or_value(place[1], built_dict, "place")
        snip = {"background": param(place, 1), "failure_dest": param(frame, 1)}
        self.frame["action_parameters"]["global"].update(snip)
        self.anc_dict["frames"]["destination"].add((
            "frames", self.frame["id"], "action_parameters", "global",
            "failure_dest"))
        self.frame["action_parameters"]["multiple"]["area"] = []
        insert = self.frame["action_parameters"]["multiple"]["area"]
        # Package argv into a set of tuples...
        for exam, frame in exp_parsed["multiple"]:
            if exam[0] == "val":
                pieces = exam[1].split(",")
                shape = pieces.pop(0)
                try:
                    {"poly": poly, "circle": circle, "rect": rect}[
                        shape](pieces)
                except KeyError:
                    raise Invalid("bad shape", shape)
                for coord in pieces[1:]:
                    int_at_least(coord, 0, "All arguments after polygon shape")
            self.anc_dict["frames"]["destination"].add((
                "frames", self.frame["id"], "action_parameters", "multiple",
                "area", len(insert), "area_dest"))
            insert.append({
                "area_def": param(exam, 1), "area_dest": param(frame, 1)})

    @merge_lock
    @action
    def player_in(self, *argv):
        '''Call on the player for input. Arguments are multiples of a type
        keyword, whether to use password mode, and the variable name.'''
        self.frame["action_name"] = "InputVars"
        exp_parsed = expression_pack(argv, mult_schema=(1, 1, 1))["multiple"]
        self.frame["action_parameters"] = {
            "context": {"not_merged": "val=true"}, "multiple": {"variable": []}
        }
        type_dict = {"s": "string", "w": "word", "f": "float"}
        for name, var_type, password in exp_parsed:
            if var_type[0] == "val":
                var_type[1] = key_or_value(
                    var_type[1], type_dict, "type", True)
            if password[0] == "val":
                password[1] = "true" if password[1] else "false"
            self.frame["action_parameters"]["multiple"]["variable"].append(
                {"var_name": param(name, 1), "var_type": param(var_type, 1),
                 "var_password": param(password, 1)})

    @action
    def var_def(self, *argv):
        '''Define a multiple of variables, with a series of names and
        values.'''
        self.frame["action_name"] = "DefineVars"
        exp_parsed = expression_pack(argv, mult_schema=(1, 1))["multiple"]
        self.frame["action_parameters"] = {"multiple": {"variable": []}}
        for name, val in exp_parsed:
            self.frame["action_parameters"]["multiple"]["variable"].append(
                {"var_name": param(name, 1), "var_value": param(val, 1)})

    @merge_lock
    @action
    def exp_test(self, *argv):
        '''Test an expression. The global sequence is whether a variable or
        expression is tested, then the variable to test, expression to test,
        and the failure anchor. If the first variable isn't an expression,
        skip the second or third argument - whichever doesn't matter. The
        multiples are a sequence of test values and anchors upon success.'''
        self.frame["action_name"] = "TestExprValue"
        global_schema = (1, 1, 1, 1) if argv[0].startswith("$") else (1, 1, 1)
        exp_parsed = expression_pack(argv, global_schema, mult_schema=(1, 1))
        glob_list = exp_parsed["global"]
        if glob_list[0][0] == "val":
            glob_list[0][1] = key_or_value(glob_list[0][1], {
                "exp": "expression", "var": "var_name"}, "variable", True)
            index = 2 if glob_list[0][1] == "var_name" else 1
            glob_list.insert(index, ["val", ""])
        snip = {
            "expr_type": param(glob_list[0], 1),
            "var_name": param(glob_list[1], 1),
            "expression": param(glob_list[2], 1),
            "failure_dest": param(glob_list[3], 1)
            }
        self.frame["action_parameters"] = {
            "context": {"not_merged": "val=true"}, "global": snip,
            "multiple": {"values": []}}
        self.anc_dict["frames"]["destination"].add((
            "frames", self.frame["id"],
            "action_parameters", "global", "failure_dest"))
        insert = self.frame["action_parameters"]["multiple"]["values"]
        for val, dest in exp_parsed["multiple"]:
            self.anc_dict["frames"]["destination"].add((
                "frames", self.frame["id"], "action_parameters",
                "multiple", "values", len(insert), "value_dest"))
            insert.append({
                "value": param(val, 1), "value_dest": param(dest, 1)})

    @merge_lock
    @action
    def condit(self, *argv):
        '''Evaluate conditions to redirect the player. The first argument is
        the failure frame anchor. Afterwards is a series of conditions and
        target frame anchors.'''
        self.frame["action_name"] = "EvaluateConditions"
        exp_parsed = expression_pack(argv, global_schema=(1,),
                                     mult_schema=(1, 1))
        self.frame["action_parameters"] = {
            "context": {"not_merged": "val=true"}, "global": {
                "failure_dest": param(exp_parsed["global"][0], 1)},
            "multiple": {"condition": []}}
        self.anc_dict["frames"]["destination"].add((
            "frames", self.frame["id"], "action_parameters", "global",
            "failure_dest"))
        insert = self.frame["action_parameters"]["multiple"]["condition"]
        for exp, frame in exp_parsed["multiple"]:
            self.anc_dict["frames"]["destination"].add((
                "frames", self.frame["id"], "action_parameters",
                "multiple", "condition", len(insert), "cond_dest"))
            insert.append(
                {"expression": param(exp, 1), "cond_dest": param(frame, 1)})

reserved_names = set()
method_names = set()
for n in inspect.getmembers(Library, predicate=inspect.ismethod):
    res_name = n[0]
    # Reserve the function names in underscore and camelCase mode.
    reserved_names.add(res_name)
    reserved_names.add(
        re.sub("_(.)", lambda match: match.group(1).upper(), res_name))
    # Now add the name to the list of method names. When I get an attribute
    # of the parser, I can compare against this to check if it is a method.
    method_names.add(n[0])
