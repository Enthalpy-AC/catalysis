# coding: UTF-8

'''Module that defines all classes for subobjects, objects within profiles,
evidence, music, popups, places, and sounds.'''

import re

from abc import ABCMeta, abstractproperty

from object_globals import JSONClass
from catalysis_globals import Invalid, int_at_least, validate_int
from catalysis_defaults import objectDict

class CustomSprite(JSONClass):
    '''Class for a custom sprite.'''
    attribute = "custom_sprites"

    def __init__(self, parent_object):
        self.parent_object = parent_object
        parent_attr = self.parent_object.data[self.__class__.attribute]
        parent_attr.append({
            "id": len(parent_attr) + 1, "name": len(parent_attr) + 1,
            "talking": "", "still": "", "startup": "", "startup_duration": 0})
        self.data = parent_attr[-1]

    @property
    def key_to_method(self):
        '''Hashes attribute name to function.'''
        return {
            "name": self.new_name, "still": self.new_still,
            "talk": self.new_talk, "startup": self.new_start,
            "duration": self.set_duration, "suffix": self.set_suffix
        }

    def new_name(self, name):
        '''Property that defines the sprite's name.'''
        self.data["name"] = name

    def new_still(self, name):
        '''Property that defines the still sprite URL.'''
        self.data["still"] = name

    def new_talk(self, name):
        '''Property that defines the talking sprite URL.'''
        self.data["talking"] = name

    def new_start(self, name):
        '''Property that defines the startup sprite URL.'''
        self.data["startup"] = name

    def set_duration(self, duration):
        '''Property that defines the duration. Startup sprite unneeded'''
        self.data["startup_duration"] = int_at_least(duration, 0, "Duration")

    def set_suffix(self, suffix):
        '''Set the suffix for the custom sprite.'''
        if not re.match(r'\w+$', suffix):
            raise Invalid("not word", "Suffix")
        if not self.parent_object.character_prefix:
            raise Invalid("suffix no prefix")
        self.parent_object.custom_suffix_list.append(suffix)
        self.parent_object.update_suffixes(False)

class EvidenceCheck(JSONClass, metaclass=ABCMeta):
    '''Abstract class for a piece of evidence's suboject.'''

    attribute = "check_button_data"

    def __init__(self, parent_object):
        self.parent_object = parent_object
        parent_attr = self.parent_object.data[self.__class__.attribute]
        parent_attr.append({"type": self.type_var, "content": ""})
        self.data = parent_attr[-1]

    @abstractproperty
    def type_var(self):
        '''Abstract property standing in for the class attribute type_var.'''
        pass

    @property
    def key_to_method(self):
        '''Hashes attribute name to function.'''
        return {"content": self.new_content}

    def new_content(self, content):
        '''Method that sets the subobject's content. May be overridne.'''
        self.data["content"] = content

class Text(EvidenceCheck):
    '''Class representing a text check option in evidence.'''
    type_var = "text"

    def new_content(self, content):
        super(Text, self).new_content(content)
        self.last_method = {"name": "content", "value": content}


class Image(EvidenceCheck):
    '''Class representing an image check option in evidence.'''
    type_var = "image"


class Sound(EvidenceCheck):
    '''Class representing a sound check option in evidence.'''
    type_var = "sound"


class PlaceObject(JSONClass, metaclass=ABCMeta):
    '''Abstract class to create a place's foreground or background object.'''

    base_dict = objectDict
    colon_dict = {"name": {}, "path": {}}

    def __init__(self, parent_object):
        self.parent_object = parent_object
        parent_attr = self.parent_object.data[self.__class__.attribute]
        parent_attr.append({
            "id": len(parent_attr) + 1, "name": "", "image": "",
            "external": 1, "hidden": False, "x": 0, "y": 0})
        self.data = parent_attr[-1]

    @property
    def key_to_method(self):
        '''Hashes attribute name to function.'''
        return {
            "name": self.new_name, "path": self.new_path,
            "hidden": self.set_hidden, "x": self.set_x, "y": self.set_y,
            "base": self.base
        }

    def new_name(self, name):
        '''Propery that sets the foreground/background object's name.'''
        self.data["name"] = name

    def new_path(self, image, external=True):
        '''Property that defines the subobject's image. External is set by
        whether path is called by double-colon syntax.'''
        self.data["image"] = image
        self.data["external"] = external

    def set_hidden(self, dummy):
        '''Property that toggles the hidden option.'''
        self.data["hidden"] = not self.data["hidden"]

    def set_x(self, xcoord):
        '''Property that defines the x-coordinate.'''
        self.data["x"] = validate_int(xcoord, "x")

    def set_y(self, ycoord):
        '''Property that defines the y-coordinate.'''
        self.data["y"] = validate_int(ycoord, "y")


class ForegroundObject(PlaceObject):
    '''Class to create a foreground object.'''

    attribute = "foreground_objects"

class BackgroundObject(PlaceObject):
    '''Class to create a background object.'''

    attribute = "background_objects"
