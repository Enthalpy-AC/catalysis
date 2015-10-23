'''Module that defines all classes for objects.'''

import inspect
import re
import sys

from copy import deepcopy

import subobject_classes as sub_c

from catalysis_globals import Invalid, int_at_least, key_or_value
from catalysis_defaults import (charDict, evDict, musicDict, soundDict,
                                popupDict, placeDict)
from frame_library import reserved_names as reserved_names_prefix
from object_globals import JSONRow


class Profile(JSONRow):
    '''Class for a profile.'''

    attribute = "profiles"
    sub_set = {sub_c.CustomSprite}
    base_dict = charDict
    colon_dict = {"long": {}, "short": {}, "sprite": {"active": True},
                  "voice": {}, "icon": {}, "prefix": {}}
    base_exclude = {"icon", "prefix"}
    suffix_dicts = {}

    def __init__(self):
        self.data = self.chain_init({
            "long_name": "", "short_name": "", "description": "",
            "civil_status": "", "hidden": False, "base": "Inconnu", "icon": "",
            "custom_sprites": [], "voice": -1, "auto_place_position": "",
            "auto_place": "", "auto_colour": ""})
        self.character_prefix = False
        self.sprite_suffix = {}
        self.custom_suffix_list = []

    @property
    def key_to_method(self):
        '''Hashes attribute name to function.'''
        return {"long": self.new_long, "short": self.new_short, "description":
            self.new_descript, "metadata": self.new_civil, "hidden":
            self.set_hidden, "sprite": self.new_base, "icon": self.new_icon,
            "voice": self.set_voice, "base": self.base, "prefix":
            self.set_character_prefix, "suffix": self.set_suffixes}

    def base(self, base):
        '''Run base. Prefix, being dependent on whether sprite is already run,
        must be run separately.'''
        super(Profile, self).base(base)
        self.colon_redef("prefix", base)

    def new_long(self, name):
        '''Set the long name.'''
        self.data["long_name"] = name
        self.last_method = False

    def new_short(self, name):
        '''Set the short name.'''
        self.data["short_name"] = name
        self.last_method = False

    def new_descript(self, descript):
        '''Change the description.'''
        self.data["description"] = descript
        self.last_method = {"name": "description", "value": descript}

    def new_civil(self, civil):
        '''Change the civil status.'''
        self.data["civil_status"] = civil
        self.last_method = {"name": "metadata", "value": civil}

    def set_hidden(self, dummy):
        '''Toggle whether the profile is hidden.'''
        self.data["hidden"] = not self.data["hidden"]
        self.last_method = False

    def new_base(self, sprite, active=False):
        '''Set the base attribute, which controls the default icon and
        sprites. '''
        if active:
            self.data["base"] = sprite
        else:
            raise Invalid("attr name", "sprite")
        self.last_method = False

    def new_icon(self, url):
        '''Set the icon. This has no default value.'''
        self.data["icon"] = url
        self.last_method = False

    def set_voice(self, voice):
        '''Set the voice to the proper value from this dictionary.'''
        voice_dict = {"none": 0, "male": -1, "female": -2, "type": -3,
                      "auto": -4}
        self.data["voice"] = key_or_value(voice.lower(), voice_dict, "voice")
        self.last_method = False

    def set_character_prefix(self, prefix):
        '''Set a prefix for this sprite. Also perform validation.'''
        if not re.match(r'\w+$', prefix):
            raise Invalid("not word", "Prefix")
        if prefix in reserved_names_prefix:
            raise Invalid("keyword claim", "Prefix", prefix)
        self.character_prefix = prefix
        # If the base isn't null, find the matching character, and set
        # suffixes.
        if self.data["base"] != "Inconnu":
            for char in self.base_dict.values():
                if self.data["base"] == char["sprite"]:
                    self.sprite_suffix = deepcopy(char["suffix"])
        else:
            self.sprite_suffix = {}
        self.last_method = False

    def set_suffixes(self, suffix_list):
        '''Convert a list of suffixes into suffix settings. These include
        absolute settings (pose_descriptor: new_suffix) and relative
        settings (new_suffix - so this must go after the last suffix.)'''
        # If there's no set prefix, you can't use a suffix.
        if not self.character_prefix:
            raise Invalid("suffix no prefix")
        suffix_list = suffix_list.split(", ")
        index = 0
        for tag in suffix_list:
            # If it's specifying the sprite to suffix absolutely...
            if ": " in tag:
                sprite_long, sprite_short = tag.split(": ", 1)
                if sprite_long in self.sprite_suffix and (
                        re.match(r'\w+$', sprite_short)):
                    self.sprite_suffix[sprite_long] = sprite_short
                    index = self.sprite_suffix.keys().index(sprite_long) + 1
                elif sprite_long in self.sprite_suffix:
                    raise Invalid("not word", "Suffix " + sprite_short)
                else:
                    raise Invalid("unk sprite", sprite_long)
            # Otherwise, the sprite is the next one in the list.
            else:
                if not re.match(r'\w+$', tag):
                    raise Invalid("not word", "Suffix")
                # Get the object to bind to...
                try:
                    sprite_long = self.sprite_suffix.keys()[index]
                except IndexError:
                    raise Invalid("excess suffix", "Suffix " + tag)
                # ...then bind and update the index of the "next" attribute.
                self.sprite_suffix[sprite_long] = tag
                index += 1
        self.last_method = False

    def update_suffixes(self, validate_prefix=True):
        '''Update the list of suffixes, performing validation as needed.'''

        # Early-exit if there is no prefix. Otherwise, validate against
        # duplicates if needed. The prefix is now confirmed valid.
        if not self.character_prefix:
            return
        elif validate_prefix and self.character_prefix in self.suffix_dicts:
            raise Invalid("prefix dupl", self.character_prefix)

        # Combine our lists of suffixes, to validate suffix uniqueness.
        values_list = self.custom_suffix_list + self.sprite_suffix.values()
        # Ensure suffix uniqueness.
        for suffix in values_list:
            if not values_list.count(suffix) == 1:
                raise Invalid("suffix dupl", suffix)

        # Suffixes for custom sprites go 1, 2, 3, 4...
        current_suffix_dict = {suffix: self.custom_suffix_list.index(
            suffix) + 1 for suffix in self.custom_suffix_list}
        # ...but suffixes for built-ins go -1, -2, -3, -4
        current_suffix_dict.update(
            {suffix: - self.sprite_suffix.values().index(suffix) - 1
             for suffix in self.sprite_suffix.values()})

        # We can now add this to the dictionary of sprites.
        self.suffix_dicts[self.character_prefix] = {
            "id": self.data["id"], "suffix dict": current_suffix_dict,
            "short": self.data["short_name"]}


class Evidence(JSONRow):
    '''The class for evidence.'''

    attribute = "evidence"
    sub_set = {sub_c.Sound, sub_c.Image, sub_c.Text}
    base_dict = evDict
    colon_dict = {"name": {}, "icon": {"external": False}}

    def __init__(self):
        self.data = self.chain_init({
            "name": "", "description": "", "metadata": "", "hidden": False,
            "icon": "", "icon_external": False, "check_button_data": []})

    @property
    def key_to_method(self):
        '''Hashes attribute name to function.'''
        return {"name": self.new_name, "description": self.new_descript,
            "metadata": self.new_metadata, "hidden": self.set_hidden,
            "icon": self.new_icon, "base": self.base}

    def new_name(self, name):
        '''Change the name.'''
        self.data["name"] = name
        self.last_method = False

    def new_descript(self, descript):
        '''Change the description and mark this for line continuation.'''
        self.data["description"] = descript
        self.last_method = {"name": "description", "value": descript}

    def new_metadata(self, meta):
        '''Change the metadata and mark this for line continuation.'''
        self.data["metadata"] = meta
        self.last_method = {"name": "metadata", "value": meta}

    def set_hidden(self, dummy):
        '''Toggle hidden.'''
        self.data["hidden"] = not self.data["hidden"]
        self.last_method = False

    def new_icon(self, icon, external=True):
        '''Change the icon, marking it as external unless defined by
        double colon syntax.'''
        self.data["icon"] = icon
        self.data["icon_external"] = external
        self.last_method = False


class Place(JSONRow):
    '''The class for a place.'''

    attribute = "places"
    sub_set = {sub_c.ForegroundObject, sub_c.BackgroundObject}
    base_dict = placeDict
    colon_dict = {"path": {"external": False}, "name": {}}

    def __init__(self):
        self.data = self.chain_init({
            "name": "", "background": {
                "image": "", "external": False, "hidden": False},
            "positions": [], "background_objects": [],
            "foreground_objects": []})

    @property
    def key_to_method(self):
        '''Hashes attribute name to function.'''
        return {
            "name": self.new_name, "path": self.new_path, "base": self.base}

    def new_name(self, name):
        '''Change the name.'''
        self.data["name"] = name

    def new_path(self, argument, external=True):
        '''Change the path. Mark as external unless defined by
        double-colon syntax. If it is, get the foreground object
        if defined. Regardless, overwrite all foregrounds.'''
        if external:
            image = argument
            fgo = []
        else:
            image = argument["image"]
            fgo = deepcopy(argument.get("fgo", []))
        self.data["background"] = {"image": image, "external": external,
                                   "hidden": False}
        self.data["foreground_objects"] = fgo


class Music(JSONRow):
    '''Class for a music object.'''

    attribute = "music"
    base_dict = musicDict
    colon_dict = {"path": {"external": False}, "name": {}}

    def __init__(self):
        self.data = self.chain_init({
            "name": "", "path": "", "external": False, "volume": 100,
            "loop_start": 0})

    @property
    def key_to_method(self):
        '''Hashes attribute name to function.'''
        return {"name": self.new_name, "path": self.new_path,
            "volume": self.new_volume, "loop": self.new_loop_start,
            "base": self.base}

    def new_name(self, name):
        '''Change the name.'''
        self.data["name"] = name

    def new_path(self, path, external=True):
        '''Change the path, marking it as external unless defined by
        double-colon syntax.'''
        self.data["path"] = path
        self.data["external"] = external

    def new_volume(self, volume):
        '''Change the volume to an integer at least 1.'''
        self.data["volume"] = int_at_least(volume, 1, "Volume")

    def new_loop_start(self, loop_start):
        '''Set the loop start time to an integer at last 0.'''
        self.data["loop_start"] = int_at_least(
            loop_start, 0, "Loop start time")


class Sound(JSONRow):
    '''Class for a sound object.'''

    attribute = "sounds"
    base_dict = soundDict
    colon_dict = {"path": {"external": False}, "name": {}}

    def __init__(self):
        self.data = self.chain_init({
            "name": "", "path": "", "external": False, "volume": 100})

    @property
    def key_to_method(self):
        '''Hashes attribute name to function.'''
        return {"name": self.new_name, "path": self.new_path,
            "volume": self.new_volume, "base": self.base}

    def new_name(self, name):
        '''Change the name.'''
        self.data["name"] = name

    def new_path(self, path, external=True):
        '''Change the path. Mark as external unless set by double colon
        syntax.'''
        self.data["path"] = path
        self.data["external"] = external

    def new_volume(self, volume):
        '''Change the volume to an integer at least 1.'''
        self.data["volume"] = int_at_least(volume, 1, "Volume")


class Popup(JSONRow):
    '''Class for a popup object.'''

    attribute = "popups"
    base_dict = popupDict
    colon_dict = {"path": {"external": False}, "name": {}}

    def __init__(self):
        self.data = self.chain_init({
            "name": "", "path": "", "external": False})

    @property
    def key_to_method(self):
        '''Hashes attribute name to function.'''
        return {"name": self.new_name, "path": self.new_path,
            "base": self.base}

    def new_name(self, name):
        '''Change the name.'''
        self.data["name"] = name

    def new_path(self, path, external=True):
        '''Change the path. Mark as external, unless set by double-colon
        syntax.'''
        self.data["path"] = path
        self.data["external"] = external

reserved_names = {n[0] for n in inspect.getmembers(
    sys.modules[__name__], predicate=inspect.isclass)}
