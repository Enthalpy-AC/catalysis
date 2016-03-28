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

    def __init__(self, JSON, suffix_dicts, object_dict, config_dict):
        self.trial = JSON
        self.suffix_dicts = suffix_dicts
        self.object_dict = object_dict
        self.base_start = config_dict["startup"]
        self.cross = self.trial["cross_examinations"][-1]
        self.scene = self.trial["scenes"][-1]
        self.statement_index = -1
        self.pressable_indices = []
        self.frame = {"merged_to_next": False}
        self.location = ""
        self.action_mult = {}
        # talk and talk scene are separate! Each talk anchor needs a related
        # anchor for the scene, even if no global scene anchor has been made.
        self.anc_dict = {x: {"destination": set(), "value": {}} for x in {
            "frame", "scene", "talk", "talk scene", "evidence", "profile"}}
        for item, val in object_dict.iteritems():
            if val.attribute in {"profiles", "evidence"}:
                attr = "profile" if val.attribute == "profiles" else (
                    val.attribute)
                self.anc_dict[attr]["value"][item] = val.data["id"]
        self.scene_dia = {}
        self.check_locks = set()
        self.from_object_dict = functools.partial(
            is_object, object_dict=self.object_dict)
        self.from_object_dict.no_manual = True
        self.speaker_override = False
        self.camera_override = False
        self.erase_override = False

    @no_manual
    def check_ev(self, item):
        '''Utility function to check if the item is a profile or
        evidence.'''
        return self.from_object_dict(
            item, {"profiles", "evidence"}, self.action_mult["bad_ev_msg"])

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
        self.camera_override = False
        self.erase_override = False

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

    def place(self, name="black", position=False):
        '''Set the place.'''
        # If a position is given, disable characters implicitly changing it.
        if position:
            self.camera_override = True
        # Otherwise, mark the new position as center.
        else:
            position = "center"
        self.frame["place"] = self.place_exp(["val", name], kill_exp=True)[1]
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
        if not self.erase_override:
            self.frame["characters_erase_previous"] = True

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
        self.erase_override = True

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
        if not self.camera_override:
            self.frame["place_position"] = pos_number

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
            char = {
                "profile_id": data["id"], "sprite_id": sprite_id,
                "sync_mode": 3, "startup_mode": self.base_start,
                "position": position, "mirror_effect": False,
                "visual_effect_appears": 1,
                "visual_effect_appears_mode": 0,
                "visual_effect_disappears": 1,
                "visual_effect_disappears_mode": 0
            }
            self.frame["characters"].append(char)
        if not self.camera_override:
            self.frame["place_position"] = char["position"]

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
        self.anc_dict["frame"]["destination"].add((
            "cross_examinations", self.cross["id"], "statements",
            self.statement_index, "contradictions", len(contras),
            "destination"))
        contras.append({"contrad_elt": type_dict, "destination": dest_anc})

    def anc(self, point):
        '''Set an anchor. Point is the 'anchor phrase.' Anchor can be used in
        any frame with dialogue.'''
        if point in self.anc_dict["frame"]["value"]:
            raise Invalid("anc dupl", point)
        self.anc_dict["frame"]["value"][point] = self.frame["id"]

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
            if anc in self.anc_dict["scene"]["value"]:
                raise Invalid("anc dupl", anc)
            self.anc_dict["scene"]["value"][anc] = self.scene["id"]

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
            self.anc_dict["talk scene"]["value"][anc] = self.scene["id"]
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
        place = self.place_exp(
            ["val", place], kill_exp=True)[1] if place else 0
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
    def sce_exam_convo(self, *argv):
        '''Create the examination. Takes arguments for the area. You can only
        avoid arguments for the default.'''
        if self.location == "sceExamConvo":
            self.sce_exam_end()
            exam = self.exam_exp("val", list(argv))[1]
            exam_dict = {
                "start": self.frame["id"], "end": 0,
                "area": exam}
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
            self.anc_dict["scene"]["destination"].add((
                "scenes", self.scene["id"], "move_list",
                len(self.scene["move_list"]), "scene_id"))
            self.scene["move_list"].append({
                "scene_type": "scenes", "scene_id": i, "name_override": j})
        self.make_frame()

    @action({"type": "ev_pos", "bad_ev_msg": "Item to display"})
    def disp_ev(self):
        '''Display evidence. Arguments are evidence name and position as
        coded.'''
        self.frame["action_name"] = "DisplayElements"
        self.frame["action_parameters"] = {"multiple": {"element": []}}

    @action({"type": "ev", "bad_ev_msg": "Item to hide"})
    def hide_ev(self):
        '''Hide evidence. Argument is evidence name.'''
        self.frame["action_name"] = "HideElements"
        self.frame["action_parameters"] = {"multiple": {"element": []}}

    @action({"type": "ev", "bad_ev_msg": "Item to reveal"})
    def rev_ev(self):
        '''Reveal evidence. Argument is evidence name.'''
        self.frame["action_name"] = "RevealElements"
        self.frame["action_parameters"] = {"multiple": {"element": []}}

    @no_manual
    def over_proceed_helper(self, *argv):
        '''Helper function for game overs and proceed to frame. Handles the
        action parameters.'''
        frame, = expression_pack(argv, (1,))
        self.frame["action_parameters"] = {
            "context": {"not_merged": "val=true"},
            "global": {"target": param(frame, 1)}}
        self.frame_exp(("global", "target"))

    @merge_lock
    @action()
    def set_over(self, *argv):
        '''Make a game over redirect. Argument is an anchor.'''
        self.frame["action_name"] = "SetGameOver"
        self.over_proceed_helper(*argv)

    @merge_lock
    @action()
    def proceed(self, *argv):
        '''Make a proceed command. Argument is an anchor.'''
        self.frame["action_name"] = "GoTo"
        self.over_proceed_helper(*argv)

    @action({"type": "frame"})
    def hide_frame(self):
        '''Hide a frame. Arguments are anchors.'''
        self.frame["action_name"] = "HideFrame"
        self.frame["action_parameters"] = {"multiple": {"frame": []}}

    @action({"type": "frame"})
    def reveal_frame(self):
        '''Reveal a frame. Arguments are anchors.'''
        self.frame["action_name"] = "RevealFrame"
        self.frame["action_parameters"] = {"multiple": {"frame": []}}

    @merge_lock
    @action()
    def game_over(self, *argv):
        '''End the game. First command tells which end state to go. If 'next'
        or 'another' end state, supply data-transfer type. If 'another,' also
        supply target part and frame IDs.'''
        self.frame["action_name"] = "GameOver"
        self.frame["action_parameters"] = {
            "context": {"not_merged": "val=true"}, "global": {"action": ""}}
        data_dict = {"none": "0", "var": "1", "full": "2"}
        parsed_exp = expression_pack(argv, (1, 1, 1, 1), pad=True)
        insert = self.frame["action_parameters"]["global"]
        # If we don't need all four variables...
        if all([x[0] == "val" for x in parsed_exp]) and (
                parsed_exp[0][1] != "another"):
            # End the game now is simple!
            if parsed_exp[0][1] == "end":
                insert["action"] = "val=0"
            # But if we go to the next part, which data transfers over?
            elif parsed_exp[0][1] == "next":
                data = parsed_exp[1]
                if not data[1]:
                    raise Invalid("arg missing", "Data to transfer")
                data[1] = key_or_value(
                    data[1], data_dict, "game over transfer data", True)
                insert["action"] = "val=1"
                insert["data_transfer"] = param(data, 1)
            # Any other case is a problem in the script.
            else:
                raise Invalid("bad key", parsed_exp[0][1], "target part")
        # If we do need all four variables...
        else:
            # Let's rule out any bad types for the first argument...
            if parsed_exp[0][0] == "val" and parsed_exp[0][1] not in {
                    "end", "next", "another"}:
                raise Invalid("bad key", parsed_exp[0][1], "target part")
            # ...and handle the good types now, unless we're in advanced mode.
            elif parsed_exp[0][0] == "val":
                proceed_dict = {"end": "0", "next": "1", "another": "2"}
                parsed_exp[0] = (parsed_exp[0][0], key_or_value(
                    parsed_exp[0][1], proceed_dict, "proceed", True))
            # We expect all data, so let's make sure we have it.
            if not parsed_exp[1][1]:
                raise Invalid("arg missing", "Data to transfer")
            if not parsed_exp[2][1]:
                raise Invalid("arg missing", "Target part")
            if not parsed_exp[3][1]:
                raise Invalid("arg missing", "Target frame")
            # Convert the data-to-transfer to a number...
            if parsed_exp[1][0] == "val":
                parsed_exp[1][1] = key_or_value(
                    parsed_exp[1][1], data_dict, "game over transfer data",
                    True)
            # And now we fill the insertion dict!
            insert["action"] = param(parsed_exp[0], 1)
            insert["data_transfer"] = param(parsed_exp[1], 1)
            insert["target_part"] = param(parsed_exp[2], 1)
            insert["target_frame"] = param(parsed_exp[3], 1)

    @action({"type": "bg_obj"})
    def hide_obj(self):
        '''Hide an object. Arguments are place name and object name.'''
        self.frame["action_name"] = "HideObject"
        self.frame["action_parameters"] = {"multiple": {"object": []}}

    @action({"type": "bg_obj"})
    def rev_obj(self):
        '''Reveal an object. Arguments are place name and object name.'''
        self.frame["action_name"] = "RevealObject"
        self.frame["action_parameters"] = {"multiple": {"object": []}}

    @no_manual
    def hide_rev_sce_helper(self, *argv):
        '''Helper function for revealing and hiding scenes. Handles the
        action parameters.'''
        scene, = expression_pack(argv, (2,))
        scene = self.scene_exp(scene, ("global", "scene", "scene_id"))
        self.frame["action_parameters"] = {
            "global": {
                "scene": {
                    "scene_type": param(scene, 1),
                    "scene_id": param(scene, 2)
                }
            }
        }

    @action()
    def hide_sce(self, *argv):
        '''Hide scene. Argument is scene anchor.'''
        self.frame["action_name"] = "HideScene"
        self.hide_rev_sce_helper(*argv)

    @action()
    def rev_sce(self, *argv):
        '''Reveal scene. Argument is scene anchor.'''
        self.frame["action_name"] = "RevealScene"
        self.hide_rev_sce_helper(*argv)

    @no_manual
    def intro_helper(self, *argv):
        '''Helper function for setting introduction conversations. Handles
        action parameters.'''
        # It's perfectly safe to use expression_pack here, since this is
        # only ever called for global arguments, not multiple.
        dialogue, = expression_pack(argv, (4,))
        dialogue = self.dialogue_exp(
            dialogue, ("global", "scene", "scene_id"),
            ("global", "dialogue", "scene_id"))
        self.frame["action_parameters"] = {"global": {
            "scene": {"scene_type": param(dialogue, 1),
                      "scene_id": param(dialogue, 2)},
            "dialogue": {"scene_type": param(dialogue, 1),
                         "scene_id": param(dialogue, 2),
                         "section_type": param(dialogue, 3),
                         "section_id": param(dialogue, 4)}
            }}

    @action()
    def hide_intro(self, *argv):
        '''Hide intro conversation. Takes scene anchor as argument.'''
        self.frame["action_name"] = "HideDialogueIntro"
        self.intro_helper(*argv)

    @action()
    def rev_intro(self, *argv):
        '''Reveal intro conversation. Takes scene anchor as argument.'''
        self.frame["action_name"] = "RevealDialogueIntro"
        self.intro_helper(*argv)

    @no_manual
    def talk_helper(self, *argv):
        '''Helper function for hiding reveal and talk converstions. Handles
        the action parameters.'''
        talk, = expression_pack(argv, (6,))
        talk = self.talk_exp(talk,
                             ("global", "scene", "scene_id"),
                             ("global", "dialogue", "scene_id"),
                             ("global", "talk_topic", "scene_id"),
                             ("global", "talk_topic", "conv_id"))
        self.frame["action_parameters"] = {"global": {
            "scene": {
                "scene_type": param(talk, 1), "scene_id": param(talk, 2)},
            "dialogue": {
                "scene_type": param(talk, 1), "scene_id": param(talk, 2),
                "section_type": param(talk, 3), "section_id": param(talk, 4)},
            "talk_topic": {
                "scene_type": param(talk, 1), "scene_id": param(talk, 2),
                "section_type": param(talk, 3), "section_id": param(talk, 4),
                "conv_type": param(talk, 5), "conv_id": param(talk, 2)}}}

    @action()
    def hide_talk(self, *argv):
        '''Hide a talk conversation. Takes convo anchor as argument.'''
        self.frame["action_name"] = "HideTalkTopic"
        self.talk_helper(*argv)

    @action()
    def rev_talk(self, *argv):
        '''Reveal a talk conversation. Takes convo anchor as argument.'''
        self.frame["action_name"] = "RevealTalkTopic"
        self.talk_helper(*argv)

    @no_manual
    def hide_rev_psy_button_helper(self, *argv):
        '''Helper functions for hiding and revealing the psyche-lock
        button. Handles action parameters.'''
        self.intro_helper(*argv)
        self.check_locks.add((
            "frames", self.frame["id"], "action_parameters", "global",
            "scene", "scene_id"))

    @action()
    def hide_psy_button(self, *argv):
        '''Hide psyche-locks button. Takes scene anchor as argument.'''
        self.frame["action_name"] = "HideDialogueLocks"
        self.hide_rev_psy_button_helper(*argv)

    @action()
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
    @action()
    def hide_psy(self):
        '''Hide psyche-locks. Can only be used in investigation.'''
        self.frame["action_name"] = "LocksHide"
        self.hide_rev_psy_helper()

    @scene_only
    @action()
    def rev_psy(self):
        '''Reveal psyche-locks. Can only be used in investigation.'''
        self.frame["action_name"] = "LocksShow"
        self.hide_rev_psy_helper()

    @scene_only
    @action({"type": "lock"})
    def break_psy(self, break_now=False):
        '''Break a psyche-lock or psyche-locks. Argument is lock numbers.
        0 for automatic mode. Can only be used in investigation.'''
        self.frame["action_name"] = "LocksBreak"
        self.frame["action_parameters"] = {
            "context": {"parent_dialogue": {
                "scene_type": "val=scenes",
                "scene_id": "val="+str(self.scene["id"]),
                "section_type": "val=dialogues", "section_id": "val=1"}},
            "multiple": {"lock": []}
        }
        if break_now:
            self.lock_type("0")

    @no_manual
    def set_red_health_helper(self, *argv):
        '''Helper for setting and reducing health. Handles the action
        parameters.'''
        self.flash_inc_health_helper(*argv)
        self.frame["action_parameters"]["context"] = {
            "not_merged": "val=true"}

    @merge_lock
    @action()
    def set_health(self, *argv):
        '''Set health. Argument is the number.'''
        self.frame["action_name"] = "SetHealth"
        self.set_red_health_helper(*argv)

    @merge_lock
    @action()
    def red_health(self, *argv):
        '''Reduce health. Argument is the number.'''
        self.frame["action_name"] = "ReduceHealth"
        self.set_red_health_helper(*argv)

    @no_manual
    def flash_inc_health_helper(self, *argv):
        '''Helper for flashing and increasing health. Handles action
        parameters.'''
        descript, = expression_pack(argv, (1,))
        if descript[0] == "val":
            validate_int(descript[1], "Health")
        self.frame["action_parameters"] = {
            "global": {"points": param(descript, 1)}}

    @action()
    def flash_health(self, *argv):
        '''Flash health. Argument is the number.'''
        self.frame["action_name"] = "FlashHealth"
        self.flash_inc_health_helper(*argv)

    @action()
    def inc_health(self, *argv):
        '''Increase health. Argument is the number.'''
        self.frame["action_name"] = "IncreaseHealth"
        self.flash_inc_health_helper(*argv)

    @no_manual
    def input_helper(self, schema, *argv):
        '''Helper for player input functions. Handles parameter
        actions.'''
        if self.location.startswith("sce"):
            parent_dialogue = {
                "scene_type": "val=scenes",
                "scene_id": "val="+str(self.scene["id"]),
                "section_type": "val=dialogues", "section_id": "val=1"
            }
        else:
            parent_dialogue = "val=0"
        if self.location == "sceLocks":
            # If we're in psyche locks, add a Back Button term.
            exp_parsed = expression_pack(argv, schema, back=True)
            in_locks = "val=true"
            lock_tuple = exp_parsed.pop(0)
            if lock_tuple[0] == "val":
                lock_tuple[1] = "true" if lock_tuple[1] else "false"
        else:
            exp_parsed = expression_pack(argv, schema)
            in_locks = "val=0"
            lock_tuple = ["val", "false"]
        self.frame["action_parameters"] = {
            "context": {"parent_dialogue": parent_dialogue, "in_locks":
                        in_locks, "not_merged": "val=true"},
            "global": {
                "locks_show_return": param(lock_tuple, 1)}, "multiple": {}}
        return exp_parsed

    @merge_lock
    @action({"type": "answer"})
    def choice(self, *argv):
        '''Write a multiple choice prompt. Arguments are respectively text to
        display and anchor.'''
        self.frame["action_name"] = "MultipleChoices"
        self.input_helper(tuple(), *argv)
        self.frame["action_parameters"]["multiple"]["answer"] = []

    @merge_lock
    @action({"type": "ev_frame", "bad_ev_msg": "Item to present"})
    def ask_ev(self, *argv):
        '''Request evidence from player. Arguments are type lock, failure
        destination, then alternating object to present and failure
        location...'''
        self.frame["action_name"] = "AskForEvidence"
        lock, dest = self.input_helper((1, 1), *argv)
        if lock[0] == "val":
            lock[1] = key_or_value(
                lock[1], {"ev": "evidence", "pro": "profiles", "all": "all"},
                "Permissible evidence", True
            )
        snip = {"type_lock": param(lock, 1), "failure_dest": param(dest, 1)}
        self.frame["action_parameters"]["global"].update(snip)
        self.frame_exp(("global", "failure_dest"))
        self.frame["action_parameters"]["multiple"]["element"] = []

    @merge_lock
    @action({"type": "ambig_exam_frame"})
    def point(self, *argv):
        '''Call on the player to point to an area. Arguments are background,
        target frame ID, a region term, and a target frame anchor. A back
        button is prepended to the argument list if in a scene.'''
        self.frame["action_name"] = "PointArea"
        place, frame = self.input_helper((1, 1), *argv)
        # AAO doesn't support default places for this action yet. Remove
        # the built_dict kwarg when that gets fixed.
        # Only the GUI for point expressions isn't there. We can still use
        # the actual expressions, or Endless Nine wouldn't work. No need for
        # kill_exp.
        place = self.place_exp(place, built_dict={})
        self.frame["action_parameters"]["global"].update(
            {"background": param(place, 1), "failure_dest": param(frame, 1)})
        self.frame_exp(("global", "failure_dest"))
        self.frame["action_parameters"]["multiple"]["area"] = []

    @merge_lock
    @action({"type": "input"})
    def player_in(self):
        '''Call on the player for input. Arguments are multiples of a type
        keyword, whether to use password mode, and the variable name.'''
        self.frame["action_name"] = "InputVars"
        self.frame["action_parameters"] = {
            "context": {"not_merged": "val=true"}, "multiple": {"variable": []}
        }

    @action({"type": "var"})
    def var_def(self):
        '''Define a multiple of variables, with a series of names and
        values.'''
        self.frame["action_name"] = "DefineVars"
        self.frame["action_parameters"] = {"multiple": {"variable": []}}

    @merge_lock
    @action({"type": "val_dest"})
    def exp_test(self, *argv):
        '''Test an expression. The global sequence is whether a variable or
        expression is tested, then the variable to test, expression to test,
        and the failure anchor. If the first variable isn't an expression,
        skip the second or third argument - whichever doesn't matter. The
        multiples are a sequence of test values and anchors upon success.'''
        self.frame["action_name"] = "TestExprValue"
        global_schema = (1, 1, 1, 1) if argv[0].startswith("{") else (1, 1, 1)
        glob_list = expression_pack(argv, global_schema)
        if glob_list[0][0] == "val":
            glob_list[0][1] = key_or_value(glob_list[0][1], {
                "exp": "expression", "var": "var_name"}, "variable", True)
            index = 2 if glob_list[0][1] == "var_name" else 1
            glob_list.insert(index, ["val", ""])
        self.frame["action_parameters"] = {
            "context": {"not_merged": "val=true"}, "global": {
                "expr_type": param(glob_list[0], 1),
                "var_name": param(glob_list[1], 1),
                "expression": param(glob_list[2], 1),
                "failure_dest": param(glob_list[3], 1)
                },
            "multiple": {"values": []}}
        self.frame_exp(("global", "failure_dest"))

    @merge_lock
    @action({"type": "condit"})
    def condit(self, *argv):
        '''Evaluate conditions to redirect the player. The first argument is
        the failure frame anchor. Afterwards is a series of conditions and
        target frame anchors.'''
        self.frame["action_name"] = "EvaluateConditions"
        frame, = expression_pack(argv, (1,))
        self.frame["action_parameters"] = {
            "context": {"not_merged": "val=true"}, "global": {
                "failure_dest": param(frame, 1)},
            "multiple": {"condition": []}}
        self.frame_exp(("global", "failure_dest"))

    @no_manual
    def evidence_exp(self, evidence):
        '''Convert a tuple representing evidence from user-input to editor
        form.'''
        if evidence[0] == "val":
            item = self.check_ev(evidence[1])
            evidence = ("val", item.attribute, str(item.data["id"]))
        else:
            evidence[1] = re.sub(r"\n(.*)\n", (
                lambda m: self.check_ev(m.group(1)).attribute), evidence[1])
            evidence[2] = re.sub(r"\n(.*)\n", (
                lambda m: self.check_ev(m.group(1)).data["id"]), evidence[2])
        return evidence

    @no_manual
    def frame_exp(self, anc_terms):
        '''Add the specified frame location to the list of frames to
        replace.'''
        self.anc_dict["frame"]["destination"].add(
            ("frames", self.frame["id"], "action_parameters") + anc_terms)

    @no_manual
    def ev_pos_exp(self, pos, prev_ev):
        '''Convert a tuple representing evidence position from user-input
        to editor form.'''
        pos_dict = {"a": "auto", "tr": "topright", "tl": "topleft",
                    "br": "bottomright", "bl": "bottomleft"}
        if pos[0] == "val":
            pos[1] = key_or_value(
                pos[1], pos_dict, "evidence position", True)
        for ele in prev_ev:
            if ele["position"] == param(pos, 1):
                raise Invalid("mult pos", pos[1])
        return pos

    @no_manual
    def place_exp(self, place, built_dict=False, kill_exp=False):
        '''Convert a tuple represneting place from user-input to editor
        form.'''
        def place_replace(match):
            '''Replace place keywords with the place ID as needed.'''
            match = match.group(1)
            try:
                base_place = self.from_object_dict(
                    match, {"places"}, "dummy_string")
                return str(base_place.data["id"])
            except Invalid:
                return str(key_or_value(match, built_dict, "place"))

        # Redefine built_dict, taking care not to override {}.
        built_dict = {
            "black": -1, "pw bench": -2, "pw judge": -6, "pw counsel": -3,
            "pw court loud": -8, "pw court silent": -9, "pw lobby": -10,
            "pw det behind": -18, "pw det ahead": -19, "aj bench": -12,
            "aj judge": -14, "aj counsel": -13, "aj court loud": -15,
            "aj court silent": -16, "aj lobby": -17, "aj det behind": -20,
            "aj det ahead": -21, "power def": -4, "power pros": -5,
            "gavel 1": -7, "gavel 3": -11
        } if built_dict == False else built_dict

        if place[0] == "val":
            # If the place isn't an expression, seek from the defined places,
            # then the AAO built-ins with objects.
            try:
                base_place = self.from_object_dict(
                    place[1], {"places"}, "Place with object")
                place[1] = base_place.data["id"]
            # Check if it's an acceptable built-in place.
            except Invalid:
                place = ["val", key_or_value(
                    place[1], built_dict, "place")]
        elif kill_exp:
            raise Invalid("no exp", "place")
        else:
            # Parse Catalysis expressions immediately.
            place[1] = re.sub(r"\n(.*)\n", place_replace, place[1])
        return place

    @no_manual
    def bg_fg_obj_exp(self, bg_fg_obj, place, built_dict, got_id=False):
        '''Convert a tuple representing a background or foreground object from
        user-input to editor form.'''
        if not got_id:
            place = self.place_exp(place, built_dict)
        # If the object is an expression, no need to fix.
        if bg_fg_obj[0] != "val":
            return place, bg_fg_obj
        # It isn't possible to fix an expression's object.

        if place[0] != "val":
            raise Invalid("exp dependency")

        if place[1] > 0:
            active_place = self.trial["places"][place[1]]
            layer, sub_id = find_subobject(
                {"foreground_objects", "background_objects"}, active_place,
                bg_fg_obj[1])
            bg_fg_obj = ("val", layer, sub_id)
        else:
            bg_fg_obj = ("val", "foreground_objects", 1)

        return place, bg_fg_obj

    @no_manual
    def scene_exp(self, scene, anc_terms, talk=False):
        '''Convert a tuple representing a scene from user-input to
        editor form.'''
        anc_cat = "talk scene" if talk else "scene"
        if scene[0] == "val":
            scene.insert(1, "scenes")
        self.anc_dict[anc_cat]["destination"].add((
            "frames", self.frame["id"], "action_parameters") + anc_terms)
        return scene

    @no_manual
    def dialogue_exp(self, dialogue, anc_terms_sce, anc_terms_dia, talk=False):
        '''Convert a tuple representing dialogue from user-input to editor
        form.'''
        dialogue = self.scene_exp(dialogue, anc_terms_sce, talk)
        anc_cat = "talk scene" if talk else "scene"
        if dialogue[0] == "val":
            dialogue += ["dialogues", "1"]
        self.anc_dict[anc_cat]["destination"].add((
            "frames", self.frame["id"], "action_parameters") + anc_terms_dia)
        return dialogue

    @no_manual
    def talk_exp(self, talk, anc_sce, anc_dia, anc_talk_1, anc_talk_2):
        '''Convert a tuple representng a talk conversation from user-input
        to editor form.'''
        talk = self.dialogue_exp(talk, anc_sce, anc_dia, talk)
        if talk[0] == "val":
            # The scene anchor name is also the talk anchor name in val mode.
            talk += ["talk_topics", talk[2]]
        self.anc_dict["talk scene"]["destination"].add((
            "frames", self.frame["id"], "action_parameters") + anc_talk_1)
        self.anc_dict["talk"]["destination"].add((
            "frames", self.frame["id"], "action_parameters") + anc_talk_2)
        return talk

    @no_manual
    def lock_exp(self, descript):
        '''Convert a tuple representing a psyche-lock from user-input to
        editor form.'''
        if descript[0] == "val":
            descript = [
                descript[0], "scenes", str(self.scene["id"]),
                "dialogues", "1", descript[1]]
        try:
            int(descript[5])
        except ValueError:
            descript[5] = "0"
        return descript

    @no_manual
    def exam_exp(self, parse_instr, pieces):
        '''Convert a tuple representing a region to select from user-input to
        editor form.'''
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

        if parse_instr == "val":
            shape = pieces.pop(0)
            try:
                {"poly": poly, "circle": circle, "rect": rect}[
                    shape](pieces)
            except KeyError:
                raise Invalid("bad shape", shape)
            for coord in pieces:
                int_at_least(coord, 0, "All arguments after polygon shape")
            pieces = shape + ":" + ",".join(pieces)
        else:
            pieces = ",".join(pieces)

        return [parse_instr, pieces]

    @no_manual
    def ev_pos_type(self, *argv):
        '''Function to handle evidence and position tuples as multiple
        parameters.'''
        evidence, pos = expression_pack(argv, (2, 1))
        insert = self.frame["action_parameters"]["multiple"]["element"]
        evidence = self.evidence_exp(evidence)
        pos = self.ev_pos_exp(pos, insert)
        insert.append({
            "element_desc": {
                "type": param(evidence, 1), "id": param(evidence, 2)},
            "position": param(pos, 1)
        })

    @no_manual
    def ev_type(self, *argv):
        '''Function to handle evidence as a multiple parameter.'''
        evidence, = expression_pack(argv, (2,))
        insert = self.frame["action_parameters"]["multiple"]["element"]
        evidence = self.evidence_exp(evidence)
        insert.append({"element_desc": {
            "type": param(evidence, 1), "id": param(evidence, 2)}})

    @no_manual
    def frame_type(self, *argv):
        '''Function to handle frames as a multiple parameter.'''
        frame, = expression_pack(argv, (1,))
        insert = self.frame["action_parameters"]["multiple"]["frame"]
        self.frame_exp(("multiple", "frame", len(insert), "target"))
        insert.append({"target": param(frame, 1)})

    @no_manual
    def bg_obj_type(self, *argv):
        '''Function to handle place and place object tuples as multiple
        parameters.'''
        place, bg_fg_obj = expression_pack(argv, (1, 2))
        built_dict = {
            "pw bench": -2, "pw judge": -6, "pw det behind": -18,
            "aj bench": -12, "aj judge": -14, "aj det behind": -20}
        place, bg_fg_obj = self.bg_fg_obj_exp(bg_fg_obj, place, built_dict)
        self.frame["action_parameters"]["multiple"]["object"].append({
            "place_desc": param(place, 1),
            "object_desc": {
                "place_id": param(place, 1), "layer": param(bg_fg_obj, 1),
                "id": param(bg_fg_obj, 2)}})

    @no_manual
    def lock_type(self, *argv):
        '''Function to handle psyche-locks as a multiple parameter.'''
        descript, = expression_pack(argv, (5,))
        descript = self.lock_exp(descript)
        self.frame["action_parameters"]["multiple"]["lock"].append({
            "lock_desc": {
                "scene_type": param(descript, 1),
                "scene_id": param(descript, 2),
                "section_type": param(descript, 3),
                "section_id": param(descript, 4),
                "lock_id": param(descript, 5)}})

    @no_manual
    def answer_type(self, *argv):
        '''Function to handle multiple-choice answers as a multiple
        parameter.'''
        text, frame = expression_pack(argv, (1, 1))
        insert = self.frame["action_parameters"]["multiple"]["answer"]
        self.frame_exp(("multiple", "answer", len(insert), "answer_dest"))
        insert.append({
            "answer_text": param(text, 1), "answer_dest": param(frame, 1)})

    @no_manual
    def ev_frame_type(self, *argv):
        '''Function to handle evidence and frame pairs as a multiple
        parameter.'''
        ele, frame = expression_pack(argv, (2, 1))
        insert = self.frame["action_parameters"]["multiple"]["element"]
        ele = self.evidence_exp(ele)
        self.frame_exp(("multiple", "element", len(insert), "element_dest"))
        insert.append({
            "element_desc": {"type": param(ele, 1), "id": param(ele, 2)},
            "element_dest": param(frame, 1)
        })

    @no_manual
    def ambig_exam_frame_type(self, *argv):
        '''Function to handle examination and frame pairs as a multiple
        parameter. Examination items can be either objects or regions.'''
        # Validate that there are enough arguments for the procedure to work.
        if len(argv) < 3:
            raise Invalid("bad arg num", "examination region selector")
        # The first and last args are special, but the rest are parsed as one.
        exam_type = argv[0]
        fixed_args = [','.join(argv[1:-1]), argv[-1]]
        exam, frame = expression_pack(fixed_args, (1, 1))
        insert = self.frame["action_parameters"]["multiple"]["area"]
        items = exam[1].split(",")
        if exam_type.lower() == "region":
            exam = self.exam_exp(exam[0], items)
            exam = param(exam, 1)
        elif exam_type.lower() == "object":
            prefix, place_id = self.frame["action_parameters"]["global"][
                "background"].split("=", 1)
            _, exam = self.bg_fg_obj_exp(
                exam, [prefix, int(place_id)], {}, True)
            exam = {"place_id": self.frame["action_parameters"]["global"][
                "background"], "layer": param(exam, 1),
                    "id": param(exam, 2)}
        else:
            raise Invalid("bad exam type", exam_type, "region, object")
        self.frame_exp(("multiple", "area", len(insert), "area_dest"))
        insert.append({
            "area_def": exam, "area_dest": param(frame, 1)})

    @no_manual
    def input_type(self, *argv):
        '''Function to handle player input as a multiple parameter.'''
        type_dict = {"s": "string", "w": "word", "f": "float"}
        name, var_type, password = expression_pack(argv, (1, 1, 1))
        if var_type[0] == "val":
            var_type[1] = key_or_value(
                var_type[1], type_dict, "type", True)
        if password[0] == "val":
            password[1] = "true" if password[1] else "false"
        self.frame["action_parameters"]["multiple"]["variable"].append(
            {"var_name": param(name, 1), "var_type": param(var_type, 1),
             "var_password": param(password, 1)})

    @no_manual
    def var_type(self, *argv):
        '''Function to handle variable definitions as a multiple parameter.'''
        name, val = expression_pack(argv, (1, 1))
        self.frame["action_parameters"]["multiple"]["variable"].append(
            {"var_name": param(name, 1), "var_value": param(val, 1)})

    @no_manual
    def val_dest_type(self, *argv):
        '''Function to handle value, destination pairs for input as a multiple
        parameter.'''
        val, dest = expression_pack(argv, (1, 1))
        insert = self.frame["action_parameters"]["multiple"]["values"]
        self.frame_exp(("multiple", "values", len(insert), "value_dest"))
        insert.append({"value": param(val, 1), "value_dest": param(dest, 1)})

    @no_manual
    def condit_type(self, *argv):
        '''Function to handle expression, destination pairs as a multiple
        parameter.'''
        exp, frame = expression_pack(argv, (1, 1))
        insert = self.frame["action_parameters"]["multiple"]["condition"]
        self.frame_exp(("multiple", "condition", len(insert), "cond_dest"))
        insert.append(
            {"expression": param(exp, 1), "cond_dest": param(frame, 1)})


    @no_manual
    def null_type(self, *argv):
        '''Function to raise an error when multiple arguments are given for
        an action that has no multiple arguments.'''
        raise Invalid("global action only")

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
