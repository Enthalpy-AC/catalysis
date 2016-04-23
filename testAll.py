# coding: UTF-8

import os
import unittest
import json
import subprocess

from catalysis_globals import err_dict

class TestCase(unittest.TestCase):
        
    maxDiff = None
    filename = ""
    folder = ""
        
    def catalyze(self, macro, obj, frame):
        return subprocess.check_output(["python", "catalysis.py", macro, obj, frame]).splitlines()[-1]
        
    def returnFile(self, filename="test_lib/testData.txt"):
        with open(filename) as g:
            header, data = g.read().splitlines()
            assert header == r"//Definition//Def6"
            return json.loads(data)

    def checkError(self, msg, macro="", obj="", frame =""):
        '''Run the program, and assert that it raised the expected error.
        Error is encoded as (line number or "end of file", error key from
        catalysis_globals, any necessary arguments)'''
        location = "line {}".format(msg[0]) if isinstance(msg[0], int) else msg[0]
        msg = err_dict[msg[1]].format(*msg[2:])
        self.assertEqual(self.catalyze(macro, obj, frame), "Error on {} of {}: {}".format(location, self.filename, msg))

    def checkFile(self, filename, macro="", obj="", frame=""):
        '''Run the program, assert that it worked, and compare the result file
        with the file with name filename in the target folder.'''
        self.assertEqual(self.catalyze(macro, obj, frame), "Catalysis complete!")
        self.assertDictEqual(self.returnFile("test_lib/{}/{}.txt".format(self.folder, filename)), self.returnFile())

class ObjectErrors(TestCase):
    
    filename = "/object_data.txt"
        
class MacroErrors(TestCase):
    filename = "/macro_data.txt"
        
class FrameErrors(TestCase):
    
    filename = "/frame_data.txt"

class ObjectCoreGrammar(ObjectErrors):

    folder = "object"

    def test_blank(self):
        self.checkFile("blank")

    def test_take_objects(self):
        self.checkError((1, "expected_new_obj"), obj="fail")

    def test_invalid_object(self):
        self.checkError((1, "unk line"), obj="plac {")
        
    def test_unclosed_object(self):
        self.checkError(("end of file", "unclosed", "Object"), obj="place {")

class ObjectPopups(ObjectErrors):
    
    folder = "object"
    
    def test_blank(self):
        self.checkFile("popup", obj="""Popup {
            }""")
        
    def test_popup_specific(self):
        self.checkFile("popup name", obj="""Popup My Popup {
        }""")
        
    def test_name(self):
        self.checkFile("popup name", obj="""Popup {
        name: My Popup
        }""")
        
    def test_place(self):
        self.checkFile("popup path", obj="""Popup {
        path: dummy place
        }""")
        
    def test_internal(self):
        self.checkFile("popup internal path", obj="""Popup {
        path:: objection
        }""")
        
    def test_base(self):
        self.checkFile("popup base", obj="""Popup {
        base: objection
        }""")

class ObjectSound(ObjectErrors):
    
    folder = "object"
    
    def test_blank(self):
        self.checkFile("sound", obj="""Sound {
        }""")

    def test_name(self):
        self.checkFile("sound name", obj="""Sound {
        name: My Sound
        }""")

    def test_path(self):
        self.checkFile("sound path", obj="""Sound {
        path: fake_sound
        }""")
        
    def test_path_internal(self):
        self.checkFile("sound internal path", obj="""Sound {
        path:: phoenix objection
        }""")
        
    def test_volume(self):
        self.checkFile("sound volume", obj="""Sound {
        volume: 1
        }""")

    def test_volume_int(self):
        self.checkError((2, "int", "Volume"), obj="""Sound {
        volume: 1.2""")

    def test_volume_pos(self):
        self.checkError((2, "min", "Volume", 1), obj="""Sound {
        volume: 0
        }""")
        
class ObjectMusic(ObjectErrors):
    
    folder = "object"
    
    def test_blank(self):
        self.checkFile("music", obj="""Music {
        }""")

    def test_name(self):
        self.checkFile("music name", obj="""Music {
        name: My Music
        }""")

    def test_path(self):
        self.checkFile("music path", obj="""Music {
        path: fake song
        }""")
        
    def test_path_internal(self):
        self.checkFile("music internal path", obj="""Music {
        path:: pw1
        }""")
        
    def test_volume(self):
        self.checkFile("music volume", obj="""Music {
        volume: 1
        }""")

    def test_volume_int(self):
        self.checkError((2, "int", "Volume"), obj="""Music {
        volume: 1.2""")

    def test_volume_pos(self):
        self.checkError((2, "min", "Volume", 1), obj="""Music {
        volume: 0""")
        
    def test_loop(self):
        self.checkFile("music volume", obj="""Music {
        volume: 1
        }""")

    def test_loop_int(self):
        self.checkError((2, "int", "Loop start time"), obj="""Music {
        loop: 1.2""")

    def test_loop_pos(self):
        self.checkError((2, "min", "Loop start time", 0), obj="""Music {
        loop: -1""")

class ObjectPlace(ObjectErrors):

    folder = "object"

    def test_blank(self):
        self.checkFile("place", obj="""Place {
        }""")

    def test_name(self):
        self.checkFile("place name", obj="""Place {
        name: My Place
        }""")

    def test_path(self):
        self.checkFile("place path", obj="""Place {
        path: My Place
        }""")

    def test_path_internal(self):
        self.checkFile("place internal path", obj="""Place {
        path:: aj lobby
        }""")

    def test_path_default(self):
        self.checkFile("place default path", obj="""Place {
        path:: aj judge
        }""")

class ObjectEvidence(ObjectErrors):
    
    folder = "object"
    
    def test_blank(self):
        self.checkFile("evidence", obj="""Evidence {
        }""")

    def test_name(self):
        self.checkFile("evidence name", obj="""Evidence {
        name: My Evidence
        }""")

    def test_descript(self):
        self.checkFile("evidence descript", obj="""Evidence {
        description: My Description
        }""")
        
    def test_descript_plus(self):
        self.checkFile("evidence descript plus", obj="""Evidence {
        description: My Description
        : Is on two lines.
        }""")
        
    def test_meta(self):
        self.checkFile("evidence meta", obj="""Evidence {
        metadata: My Metadata
        }""")
    def test_meta_blank(self):
        self.checkFile("evidence meta blank", obj="""Evidence {
        metadata: My Metadata
        :
        }""")

    def test_meta_full(self):
        self.checkFile("evidence meta full", obj="""Evidence {
        metadata: My Metadata
        : Is on multiple lines
        }""")

    def test_hide(self):
        self.checkFile("evidence hide", obj="""Evidence {
        hidden:
        }""")

    def test_unhide(self):
        self.checkFile("evidence unhide", obj="""Evidence {
        hidden:
        hidden: dummy
        }""")

    def test_icon_internal(self):
        self.checkFile("evidence internal icon", obj="""Evidence {
        icon:: badge
        }""")

    def test_icon_external(self):
        self.checkFile("evidence icon", obj="""Evidence {
        icon: my icon
        }""")

class ObjectProfiles(ObjectErrors):

    folder = "object"

    def test_blank(self):
        self.checkFile("profile", obj="""Profile {
        }""")

    def test_long(self):
        self.checkFile("profile long", obj="""Profile {
        long: Long Name
        }""")

    def test_short(self):
        self.checkFile("profile short", obj="""Profile {
        short: Short Name
        }""")

    def test_descript(self):
        self.checkFile("profile descript", obj="""Profile {
        description: Description
        }""")

    def test_descript_plus(self):
        self.checkFile("profile descript plus", obj="""Profile {
        description: Description
        :  New stuff
        }""")

    def test_civil(self):
        self.checkFile("profile civil", obj="""Profile {
        metadata: Civil Status
        }""")

    def test_civil_plus(self):
        self.checkFile("profile civil plus", obj="""Profile {
        metadata: Civil Status
        : New stuff
        }""")

    def test_hide(self):
        self.checkFile("profile hide", obj="""Profile {
        hidden:
        }""")

    def test_unhide(self):
        self.checkFile("profile unhide", obj="""Profile {
        hidden:
        hidden: dummy
        }""")

    def test_sprite(self):
        self.checkError((2, "attr name", "sprite"), obj="""Profile {
        sprite: dummy
        }""")

    def test_icon(self):
        self.checkFile("profile icon", obj="""Profile {
        icon: My Icon
        }""")

    def test_voice(self):
        self.checkFile("profile voice", obj="""Profile {
        voice: auto
        }""")

    def test_voice_crash(self):
        self.checkError((2, "bad key", "crash", "voice"), obj="""Profile {
            voice: crash
            }""")
        
    def test_prefix_crash(self):
        self.checkError((2, "not word", "Prefix"), obj="""Profile {
            prefix: crash please""")

    def test_reserved_prefix(self):
        self.checkError((2, "keyword claim", "Prefix", "dispEv"), obj="""Profile {
prefix: dispEv""")
        
    def test_prefix_dupl(self):
        self.checkError((9, "prefix dupl", "kumquat"), obj="""Profile {
sprite:: phoenix
prefix: kumquat
}

Profile {
sprite:: phoenix
prefix: kumquat
}""")
        
    def test_suffix_no_prefix(self):
        self.checkError((2, "suffix no prefix"), obj="""Profile {
suffix: crash""")
        
    def test_suffix_pos_word(self):
        self.checkError((4, "not word", "Suffix foo bar"), obj="""Profile {
sprite:: phoenix
prefix:: phoenix
suffix: normal: foo bar""")

    def test_suffix_pos_sprite(self):
        self.checkError((4, "unk sprite", "kumquat"), obj="""Profile {
sprite:: phoenix
prefix:: phoenix
suffix: kumquat: foo""")
        
    def test_suffix_rel_word(self):
        self.checkError((4, "not word", "Suffix"), obj="""Profile {
sprite:: phoenix
prefix:: phoenix
suffix: normal: foo, bar baz""")
        
    def test_suffix_rel_sprite(self):
        self.checkError((4, "excess suffix", "Suffix baz"), obj="""Profile {
sprite:: phoenix
prefix:: phoenix
suffix: superobject: foo, bar, baz""")

def test_suffix_dupl(self):
        self.checkError((8, "suffix dupl", "kumquat"), obj="""Profile {
prefix: a
suffix: kumquat
}

Profile {
prefix: b
suffix: kumquat
}""")


class ObjectBadSyntax(ObjectErrors):
    
    def test_grammar_in_object(self):
        self.checkError((2, "in obj"), obj="""Place {
            this is complete gibberish""")
        
    def test_fake_attr(self):
        self.checkError((2, "attr name", "nonsense"), obj="""Place {
            Nonsense: command""")
    
    def test_fake_base(self):
        self.checkError((2, "attr val", "Command"), obj="""Place {
            base: Command""")
        
    def test_fake_default_name(self):
        self.checkError((2, "attr name", "nonsense"), obj="""Place {
            Nonsense:: pw office""")
        
    def test_fake_default_value(self):
        self.checkError((2, "attr val", "objection"), obj="""Place {
            name:: objection""")
        
    def test_default_unsupported(self):
        self.checkError((2, "no default attr", "volume"), obj="""Music {
volume:: PW1""")
        
    def test_no_continuation(self):
        self.checkError((3, "no continuation"), obj="""Music {
name: Text
: Crash!""")
        
    def test_no_duplicate(self):
        self.checkError((3, "ban duplicate", "Object", "duplicate"), obj="""Music duplicate {
}
Profile duplicate {""")
        
    def test_no_bad_obj_name(self):
        self.checkError((1, "ban obj name", "Evidence"), obj="Profile Evidence {")
        
    def test_no_parent_obj(self):
        self.checkError((1, "no parent obj"), obj="foreground {")
        
    def test_missing_parent_obj(self):
        self.checkError((1, "parent obj dne", "test"), obj="test foreground {")
        
    def test_bad_subobject(self):
        self.checkError((4, "subobj dne", "fake"), obj="""Place object {
}

object fake {""")
        
    def test_invalid_subobj(self):
        self.checkError((4, "obj subobj forbid", "sound", "foo"), obj="""Place foo {
}

foo sound {""")
        
class ObjectComments(ObjectErrors):
    
    folder = "object"
    
    def test_inline_in_obj(self):
        self.checkFile("object inline comment out", obj="""// Comment!
Place {
}""")
        
    def test_inline_out_obj(self):
        self.checkFile("object inline comment in", obj= """Place {
// Comment!
}""")
        
    def test_block_in_obj(self):
        self.checkFile("object block comment out", obj="""/* Comment!*/
Place {
}""")
        
    def test_block_out_obj(self):
        self.checkFile("object block comment in", obj="""Place {
/* Comment!*/
}""")
        
    def test_block_block(self):
        self.checkFile("object block comment block", obj="""Place {
/* Comment!
Continues!. */
}""")
        
class ObjectForeBackGround(ObjectErrors):

    folder = "subobject"

    def test_foreground(self):
        self.checkFile("fg", obj="""Place My_Place {
path:: pw office
}

My_Place foreground {
}""")

    def test_foreground_2(self):
        self.checkFile("fg 2", obj="""Place My_Place {
path:: pw office
}

Place My_Place_2 {
path:: pw office
}

My_Place foreground {
}""")

    def test_background(self):
        self.checkFile("bg", obj="""Place My_Place {
path:: pw office
}

My_Place background {
}""")

    def test_hidden(self):
        self.checkFile("bg hide", obj="""Place My_Place {
path:: pw office
}

My_Place background {
hidden: dummy
}""")

    def test_unhidden(self):
        self.checkFile("bg unhide", obj="""Place My_Place {
path:: pw office
}

My_Place background {
hidden: dummy
hidden: dummy
}""")

    def test_x(self):
        self.checkFile("bg x", obj="""Place My_Place {
path:: pw office
}

My_Place background {
x: 100
}""")

    def test_x_int(self):
        self.checkError((6, "int", "x"), obj="""Place My_Place {
path:: pw office
}

My_Place background {
x: upupu""")

    def test_y(self):
        self.checkFile("bg y", obj="""Place My_Place {
path:: pw office
}

My_Place background {
y: -100
}""")

    def test_y_int(self):
        self.checkError((6, "int", "y"), obj="""Place My_Place {
path:: pw office
}

My_Place background {
y: upupu""")

    def test_name(self):
        self.checkFile("bg name", obj="""Place My_Place {
path:: pw office
}

My_Place background {
name: name
}""")

    def test_background_default(self):
        self.checkFile("bg internal path", obj="""Place My_Place {
path:: pw office
}

My_Place background {
path:: pw judge
}""")

    def test_background_path(self):
        self.checkFile("bg path", obj="""Place My_Place {
path:: pw office
}

My_Place background {
path: external
}""")
        
class ObjectEvidencePage(ObjectErrors):

    folder = "subobject"

    def test_ev_text(self):
        self.checkFile("ev text", obj="""Evidence My_Evidence {
}

My_Evidence text {
}""")

    def test_ev_image(self):
        self.checkFile("ev image", obj="""Evidence My_Evidence {
}

My_Evidence image {
}""")

    def test_ev_sound(self):
        self.checkFile("ev sound", obj="""Evidence My_Evidence {
}

My_Evidence sound {
}""")

    def test_ev_mult_obj(self):
        self.checkFile("ev mult obj", obj="""Evidence My_Evidence {
}

Evidence My_Second_Evidence {
}

My_Evidence text {
}""")

    def test_ev_mult_subobj(self):
        self.checkFile("ev mult subobj", obj="""Evidence My_Evidence {
}

My_Evidence text {
}

My_Evidence image {
}""")

    def test_ev_text_content(self):
        self.checkFile("ev text content", obj="""Evidence My_Evidence {
}

My_Evidence text {
content: Content
}""")

    def test_ev_image_content(self):
        self.checkFile("ev image content", obj="""Evidence My_Evidence {
}

My_Evidence image {
content: Content
}""")

    def test_ev_text_sound(self):
        self.checkFile("ev sound content", obj="""Evidence My_Evidence {
}

My_Evidence sound {
content: Content
}""")

    def test_ev_text_cont(self):
        self.checkFile("ev text cont", obj="""Evidence My_Evidence {
}

My_Evidence text {
content: Content
: More content
}""")

    def test_ev_image_cont(self):
        self.checkError((6, "no continuation"), obj="""Evidence My_Evidence {
}

My_Evidence image {
content: Content
: More content
}""")

    def test_ev_sound_cont(self):
        self.checkError((6, "no continuation"), obj="""Evidence My_Evidence {
}

My_Evidence sound {
content: Content
: More content
}""")
        
    def test_no_base_dict(self):
        self.checkError((5, "defaults unsupported"), obj="""Evidence kumquat {
}

kumquat image {
base:: upupu""")
        
class Object_Sprites(ObjectErrors):

    folder = "subobject"

    def test_sprite(self):
        self.checkFile("sprite", obj="""Profile My_Profile {
}

My_Profile sprite {
}""")
        
    def test_sprite_obj_mult(self):
        self.checkFile("sprite obj mult", obj="""Profile My_Profile {
}

Profile My_Second_Profile {
}

My_Profile sprite {
}""")
        
    def test_sprite_subobj_mult(self):
        self.checkFile("sprite subobj mult", obj="""Profile My_Profile {
}

My_Profile sprite {
}

My_Profile sprite {
}""")

    def test_sprite_name(self):
        self.checkFile("sprite name", obj="""Profile My_Profile {
}

My_Profile sprite {
name: Name
}""")

    def test_sprite_still(self):
        self.checkFile("sprite still", obj="""Profile My_Profile {
}

My_Profile sprite {
still: Still
}""")

    def test_sprite_talk(self):
        self.checkFile("sprite talk", obj="""Profile My_Profile {
}

My_Profile sprite {
talk: Talk
}""")
        
    def test_sprite_start(self):
        self.checkFile("sprite start", obj="""Profile My_Profile {
}

My_Profile sprite {
startup: Start
}""")
        
    def test_sprite_duration_min(self):
        self.checkFile("sprite duration min", obj="""Profile My_Profile {
}

My_Profile sprite {
duration: 0
}""")

    def test_sprite_duration(self):
        self.checkFile("sprite duration", obj="""Profile My_Profile {
}

My_Profile sprite {
duration: 1
}""")

    def test_sprite_duration_int(self):
        self.checkError((5, "int", "Duration"), obj="""Profile My_Profile {
}

My_Profile sprite {
duration: crash""")

    def test_sprite_duration_non_neg(self):
        self.checkError((5, "min", "Duration", "0"), obj="""Profile My_Profile {
}

My_Profile sprite {
duration: -1""")
            
    def test_sprite_suffix_word(self):
        self.checkError((5, "not word", "Suffix"), obj="""Profile My_Profile {
}

My_Profile sprite {
suffix: Not A Word
}""")

    def test_sprite_suffix_no_prefix(self):
        self.checkError((5, "suffix no prefix"), obj="""Profile My_Profile {
}

My_Profile sprite {
suffix: Word
}""")

class FrameCoreSpeakerGrammar(FrameErrors):

    folder = "frame"

    def test_sprite_syntax(self):
        self.checkFile("sprite syntax", obj="""Profile {
base: lisabasil
}""", frame="lb2.n")
        
    def test_speaker_syntax(self):
        self.checkFile("speaker syntax", obj="""Profile {
base: lisabasil
}""", frame="lb2")

    def test_speaker_spriteless(self):
        self.checkFile("speaker spriteless", obj="""Profile {
base: dougswallow
}""", frame="ds")

    def test_custom_sprite(self):
        self.checkFile("custom sprite", obj="""Profile foo {
base: dougswallow
}

foo sprite {
suffix: bar
}""", frame="ds.bar")

    def test_sprite_redefined_absolute(self):
        self.checkFile("custom suffix abs", obj="""Profile {
base: lisabasil
suffix: happy: foo
}""", frame="lb2.foo")
        
    def test_sprite_redefined_relative(self):
        self.checkFile("custom suffix rel", obj="""Profile {
base: lisabasil
suffix: foo
}""", frame="lb2.foo")
        
    def test_null(self):
        self.checkFile("null", frame="null")
        
    def test_speaker_dialogue(self):
        self.checkFile("speaker dialogue", obj="""Profile {
base: lisabasil
}""", frame="""lb2:
Online.""")
        
    def test_sprite_dialogue(self):
        self.checkFile("sprite dialogue", obj="""Profile {
base: lisabasil
}""", frame="""lb2.n:
Online.""")
        
    def test_null_dialogue(self):
        self.checkFile("null dialogue", frame="""null:
Online.""")
        
    def test_punctuate(self):
        self.checkFile("punctuate", frame="""null:
. ! , - ? ... ; .. : .""")
        
    def test_multi_char_no_place(self):
        self.checkError((2, "mult char no place"), obj="""Profile {
sprite:: Phoenix
prefix:: Phoenix
}

Profile {
sprite:: Maya
prefix:: Maya
}""", frame="""pw.n
may.n:""")
        
    def test_multi_char_place(self):
        self.checkError((3, "mult char pos"), obj="""Profile {
sprite:: Phoenix
prefix:: Phoenix
}

Profile {
sprite:: Maya
prefix:: Maya
}""", frame="""place, black
pw.n
may.n:""")

    def test_terminal_colon_escape(self):
        self.checkFile("colon escape", frame="speakerName, myTest\:")

    def test_bad_arg_num(self):
        self.checkError((1, "bad arg num", "merge"), frame="merge, upupu")

    def test_end_merge(self):
        self.checkError(("end of file", "terminal merge"), frame="merge")

    def test_unk_line_args(self):
        self.checkError((1, "unk line"), frame="fake, command")
        
    def test_unk_line_words(self):
        self.checkError((1, "unk line"), frame="fake command")
        
    def test_unk_line_word(self):
        self.checkError((1, "unk line"), frame="fakecommand")

class Word_Wrap(FrameErrors):

    folder = "word wrap"

    def test_basic(self):
        self.checkFile("basic", frame="""null:
This is my testing of the word wrap functionality. If it works as intended, I will be quite happy.""")
        
    def test_end_pause(self):
        self.checkFile("end pause", frame="""null:
This is dialogue.[#200]""")

    def test_wordwrap_splitline(self):
        self.checkFile("splitline", frame="""null:
iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii think this many i is a very bad idea""")
        
    def test_wordwrap_silent(self):
        self.checkFile("silent", frame="""null:
This is [#dhigilsgilssststdststgtitstht] fake.""")
        
    def test_wordwrap_overlimit(self):
        self.checkFile("over limit", frame="""null:
iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii i think this many i is a very bad idea""")
        
    def test_wordwrap_underlimit(self):
        self.checkFile("under limit", frame="""null:
iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii i think this many i is a very bad idea""")
        
    def test_wordwrap_overlimit_merge(self):
        self.checkFile("over limit merge", frame="""merge:
iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii

null:
 i think this many i is a bad idea""")
        
    def test_wordwrap_underlimit_merge(self):
        self.checkFile("under limit merge", frame="""merge:
iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii

null:
 i think this many i is a bad idea""")
        
    def test_wordwrap_break(self):
        self.checkFile("linebreak", frame="""null:
It would've restored public trust in
the courts and the jurors' verdicts 
would've been just and sensible.""")
        
    def test_delete_term_ellipsis(self):
        self.checkFile("ellipsis", frame="""null:
I see…""")
        
    def test_delete_term_four(self):
        self.checkFile("four period", frame="""null:
I see....""")

class Frame_Commands(FrameErrors):
    
    folder = "frame"
    
    def test_popup(self):
        self.checkFile("popup", obj="""Popup Foo {
}""", frame="popup, Foo")
        
    def test_indent(self):
        self.checkError((1, "unk line"), obj="""Popup Foo {
}""", frame="    popup, Foo")
        
    def test_popup_no_word(self):
        self.checkFile("popup no word", obj="""Popup Foo Bar {
}""", frame="popup, Foo Bar")
        
    def test_popup_escape(self):
        self.checkFile("popup escape name", obj="""Popup Foo, Bar {
}""", frame="popup, Foo\, Bar")

    def test_popup_not_obj(self):
        self.checkError((1, "unk obj", "Foo"), frame="popup, Foo")
        
    def test_popup_not_popup(self):
        self.checkError((1, "type in set", "Popup to display", "popups"), obj="""Place Foo {
}""", frame="popup, Foo")
        
    def test_music(self):
        self.checkFile("music", obj="""Music Foo {
}""", frame="music, Foo")
        
    def test_music_kill(self):
        self.checkFile("music kill", obj="""Music Foo {
}""", frame="music")
        
    def test_music_error(self):
        self.checkError((1, "type in set", "Music to play", "music"), obj="""Place Foo {
}""", frame="music, Foo")
        
    def test_sound(self):
        self.checkFile("sound", obj="""Sound Foo {
}""", frame="sound, Foo")
        
    def test_sound_error(self):
        self.checkError((1, "type in set", "Sound to play", "sounds"), obj="""Place Foo {
}""", frame="sound, Foo")
        
    def test_place(self):
        self.checkFile("place", obj="""Place Foo {
}""", frame="place, Foo")

    def test_place_default(self):
        self.checkFile("place default", frame="place")

    def test_place_builtin(self):
        self.checkFile("place default", frame="place, black")

    def test_place_error(self):
        self.checkError((1, "bad key", "Foo", "place"), obj="""Popup Foo {
}""", frame="place, Foo")
        
    def test_place_post_char(self):
        self.checkError((2, "place post char"), obj="""Profile {
base: Phoenix
}""", frame="""pw.n
place, black""")
        
    def test_place_position(self):
        self.checkFile("place position", frame="place, black, left")
        
    def test_place_position_error(self):
        self.checkError((1, "bad key", "kumquat", "position"), frame="place, black, kumquat")
        
    def test_wait(self):
        self.checkFile("wait", frame="wait, 10")
        
    def test_wait_int_error(self):
        self.checkError((1, "int", "Wait time"), frame="wait, kumquat")
        
    def test_wait_min_error(self):
        self.checkError((1, "min", "Wait time", 0), frame="wait, -1")
        
    def test_hide(self):
        self.checkFile("hide", frame="hide")
        
    def test_unhide(self):
        self.checkFile("unhide", frame="""hide
hide""")
        
    def test_merge(self):
        self.checkFile("merge", frame="""merge

null""")
        
    def test_unmerge(self):
        self.checkFile("unmerge", frame="""merge
merge""")
        
    def test_erase(self):
        self.checkFile("erase", frame="erase")
        
    def test_unerase(self):
        self.checkFile("unerase", frame="""erase
erase""")

    def test_erase_override(self):
        self.checkFile("erase override", obj="""Profile {
sprite:: angelstarr
prefix:: angelstarr
}""", frame="""erase
erase
place, aj lobby
as.n""")

    def test_scroll(self):
        self.checkFile("scroll", frame="scroll")
        
    def test_unscroll(self):
        self.checkFile("unscroll", frame="""scroll
scroll""")
        
    def test_speed(self):
        self.checkFile("speed", frame="speed, 1.5")
        
    def test_speed_num_error(self):
        self.checkError((1, "num", "Typing speed"), frame="speed, kumquat")
        
    def test_speed_min_error(self):
        self.checkError((1, "min", "Typing speed", 0), frame="speed, -1")
        
    def test_blip(self):
        self.checkFile("blip", frame="blip, t")

    def test_blip_error(self):
        self.checkError((1, "bad key", "kumquat", "blip"), frame="blip, kumquat")
        
    def test_mirror(self):
        self.checkFile("mirror", obj="""Profile {
sprite:: Phoenix
prefix:: Phoenix
}""", frame="""pw.n
mirror""")

    def test_unmirror(self):
        self.checkFile("unmirror", obj="""Profile {
sprite:: Phoenix
prefix:: Phoenix
}""", frame="""pw.n
mirror
mirror""")
        
    def test_mirror_bug(self):
        self.checkError((1, "pre char", "mirror"), frame="mirror")

    def test_color_num(self):
        self.checkFile("color num", frame="color, 23A15F")

    def test_color_word(self):
        self.checkFile("color word", frame="color, red")
        
    def test_sync(self):
        self.checkFile("sync", obj="""Profile {
sprite:: Phoenix
prefix:: Phoenix
}""", frame="""pw.n
sync, k""")

    def test_sync_key_error(self):
        self.checkError((2, "bad key", "kumquat", "sync"), obj="""Profile {
base: Phoenix
}""", frame="""pw.n
sync, kumquat""")
        
    def test_sync_no_char(self):
        self.checkError((1, "pre char", "sync"), frame="sync, k")

    def test_startup(self):
        self.checkFile("startup", obj="""Profile {
sprite:: Phoenix
prefix:: Phoenix
}""", frame="""pw.yes
startup, during""")
        
    def test_startup_key_error(self):
        self.checkError((2, "bad key", "kumquat", "startup"), obj="""Profile {
base: Phoenix
}""", frame="""pw.yes
startup, kumquat""")
        
    def test_startup_no_char(self):
        self.checkError((1, "pre char", "startup"), frame="startup, during")
        
    def test_cPos_no_place(self):
        self.checkError((1, "pre place", "cPos"), frame="cPos, c")
        
    def test_cPos_key_error(self):
        self.checkError((3, "bad key", "kumquat", "character position"), obj="""Profile {
base: Phoenix
}""", frame="""place, black
pw.yes
cPos, kumquat""")
        
    def test_cPos_no_char(self):
        self.checkError((2, "pre char", "character position"), frame="""place, black
cPos, c""")
        
    def test_cPos_valid(self):
        self.checkFile("cPos valid", obj="""Profile {
sprite:: angelstarr
prefix:: angelstarr
}""", frame="""place, black
as.n
cPos, l""")
        
    def test_position_override(self):
        self.checkFile("camera override", obj="""Profile {
sprite:: angelstarr
prefix:: angelstarr
}""", frame="""place, black, center
as.n
cPos, l""")
        
    def test_position_setting(self):
        self.checkFile("camera speaker", obj="""Profile {
base: edgeworth
}

Profile {
base: phoenix
}""", frame="""place, aj bench
pw.n
cPos, l
me.n
cPos, r
pw.desk""")
    
    def test_pPos_no_place(self):
        self.checkError((2, "pre place", "pPos"), frame="""place, black
pPos, a""")
        
    def test_pPos_key_error(self):
        self.checkError((1, "bad key", "kumquat", "place position"), frame="pPos, kumquat")
        
    def test_pPos(self):
        self.checkFile("pPos", frame="pPos, n")

    def test_speaker_name(self):
        self.checkFile("speaker name", frame="speakerName, foo")
        
    def test_speakerId_unk(self):
        self.checkFile("speakerId unk", frame="speakerId, ?")
        
    def test_speakerId_null(self):
        self.checkFile("speakerId null", frame="speakerId")
        
    def test_speakerId(self):
        self.checkFile("speakerId", obj="""Profile my_test{
}""", frame="speakerId, my_test")
        
    def test_speakerId_error(self):
        self.checkError((1, "type in set", "Speaker", "profiles"), obj="""Evidence my_test{
}""", frame="speakerId, my_test")

    def test_speaker_override_fail(self):
        self.checkFile("speaker override fail", obj="""Profile {
sprite:: Phoenix
prefix:: Phoenix
}""", frame="""speakerId
pw.n""")
        
    def test_speaker_override(self):
        self.checkFile("speaker override", obj="""Profile {
sprite:: Phoenix
prefix:: Phoenix
}""", frame="""place, black
speakerId
pw.n""")

    def test_sprite_unk_pre(self):
        self.checkError((1, "unk pre", "kumquat"), frame="set_sprite, kumquat, fraud")
        
    def test_sprite_unk_suff(self):
        self.checkError((1, "unk suff", "kumquat", "pw"), obj="""Profile {
sprite:: Phoenix
prefix:: Phoenix
}""", frame="set_sprite, pw, kumquat")
    
    def test_sprite_new(self):
        self.checkFile("sprite new", obj="""Profile {
sprite:: Phoenix
prefix:: Phoenix
}""", frame="set_sprite, pw, n")
    
    def test_sprite_old(self):
        self.checkFile("sprite old", obj="""Profile {
sprite:: Phoenix
prefix:: Phoenix
}""", frame="""pw.yes
set_sprite, pw, n""")

    def test_make_frame(self):
        self.checkFile("manual make", frame="make_frame")
        
    def test_manual_dialogue(self):
        self.checkFile("manual dialogue", frame="dialogue, This, they say, is the end.\\\\\\")

class Cross_Examination_Tests(FrameErrors):
    
    folder = "cross"
    
    def test_minimal_cross(self):
        self.checkFile("basic", frame="""ceStart
assist
ceEnd""")
        
    def test_statement_skip(self):
        self.checkFile("skip", frame="""ceStart
ceStatement, skip

assist
ceEnd""")
        
    def test_statement_press(self):
        self.checkFile("press", frame="""ceStart
ceStatement

assist
press
ceEnd""")
        
    def test_statement_fail(self):
        self.checkFile("fail", frame="""ceStart
assist
fail
ceEnd""")
        
    def test_statement_mult(self):
        self.checkFile("mult statement", frame="""ceStart
ceStatement

ceStatement, skip

ceStatement

assist
press
press
fail
ceEnd""")
        
    def test_statement_dialogue(self):
        self.checkFile("dialogue", frame="""ceStart
ceStatement:
Text!

ceStatement, skip:
Lovely text!

ceStatement:
Way better than that dialogue!

assist
null:
Have some dialogue!

press
null:
Fresh dialogue.

press
null:
Good dialogue.

fail
null:
Just wrote it this morning!

ceEnd""")
        
    def test_cross_full(self):
        self.checkFile("full", obj="""Profile {
base: Phoenix
}

Popup obj {
base: Objection
}

Music pursuit {
base: aj11a
}""", frame="""ceStart
ceStatement
color, green:
Text!

ceStatement, skip
place, black:
Lovely text!

ceStatement
blip, f:
Way better than that dialogue!

assist
speed, 4:
Have some dialogue!

press
popup, obj:
Fresh dialogue.

press
pw.n:
Good dialogue.

fail
music, pursuit:
Just wrote it this morning!

ceEnd""")
        
    def test_non_manual(self):
        self.checkError((1, "ban manual", "assistEnd"), frame="assistEnd")
        
    def test_cross_command_error(self):
        self.checkError((1, "bad context", "outside of special blocks", "a generally usable command or ", "ceStart, sceIntro"), frame="assist")
        
    def test_cross_context_error(self):
        self.checkError((2, "bad context", "after ceStart", "", "ceStatement, assist"), frame="""ceStart
press""")
        
    def test_end_error(self):
        self.checkError(("end of file", "block open"), frame="""ceStart
assist""")
        
    def test_fail_inad_press_fail(self):
        self.checkError((5, "inadequate press", "start fail conversation", 1), frame="""ceStart
ceStatement

assist
fail""")

    def test_over_press(self):
        self.checkError((6, "excess press"), frame="""ceStart
ceStatement

assist
press
press""")

    def test_end_inad_press_endce(self):
        self.checkError((5, "inadequate press", "end cross examination", 1), frame="""ceStart
ceStatement

assist
ceEnd""")

    def test_contra_err(self):
        self.checkError((3, "type in set", "Contradictory item", "profiles, evidence"), obj="""Popup obj {
}""", frame="""ceStart
ceStatement
contra, obj, objectionable""")
            
    def test_contra_mult_err(self):
        self.checkError((4, "mult contra", "kumquat"), obj="""Profile kumquat {
}""", frame="""ceStart
ceStatement
contra, kumquat, objectionable
contra, kumquat, fake""")
            
    def test_no_contra_anc(self):
        self.checkError(("end of file", "anc unset", "frame", "objectionable"), obj="""Profile obj {
}

Profile kumquat {
}""", frame="""ceStart
ceStatement
contra, obj, objectionable
contra, kumquat, objectionable""")
            
    def test_contra_cross(self):
        self.checkFile("contra", obj="""Profile contradictory {
}""", frame="""ceStart
ceStatement, skip

ceStatement, skip
contra, contradictory, explain

assist
ceEnd
anc, explain""")

class Investigation_Tests(FrameErrors):

    folder = "scene"

    def test_sce_basic(self):
        self.checkFile("basic", frame="""sceIntro
sceMain

sceTalk
scePres
sceExam
sceMove""")

    def test_sce_named(self):
        self.checkFile("named", frame="""sceIntro, Test Place
sceMain

sceTalk
scePres
sceExam
sceMove""")
        
    def test_sce_hidden(self):
        self.checkFile("hidden", frame="""sceIntro, Test Place, False
sceMain

sceTalk
scePres
sceExam
sceMove""")
        
    def test_sce_talk(self):
        self.checkFile("talk", frame="""sceIntro
sceMain

sceTalk
sceTalkConvo
scePres
sceExam
sceMove""")

    def test_sce_talk_named(self):
        self.checkFile("talk titled", frame="""sceIntro
sceMain

sceTalk
sceTalkConvo, My Title
scePres
sceExam
sceMove""")
        
    def test_sce_talk_hidden(self):
        self.checkFile("talk hidden", frame="""sceIntro
sceMain

sceTalk
sceTalkConvo, My Title, hide
scePres
sceExam
sceMove""")
        
    def test_sce_pres(self):
        self.checkFile("present", obj="""Profile Present_Me {
}""", frame="""sceIntro
sceMain

sceTalk
scePres
scePresConvo, Present_Me
sceExam
sceMove""")
        
    def test_sce_exam_custom_place(self):
        self.checkFile("exam custom", obj="""Profile Present_Me {
}

Place New_Place {
base: pw office
}""", frame="""sceIntro
sceMain

sceTalk
scePres
scePresConvo, Present_Me
sceExam, New_Place
sceMove""")
        
    def test_sce_exam_default_place(self):
        self.checkFile("exam default", frame="""sceIntro
sceMain

sceTalk
scePres
sceExam, black
sceMove""")
        
    def test_sce_exam_polygon(self):
        self.checkFile("exam poly", obj="""Place New_Place {
path:: pw lobby
}""", frame="""sceIntro
sceMain

sceTalk
scePres
sceExam, New_Place
sceExamConvo, poly, 1, 15, 40, 194, 249, 137
sceMove""")

    def test_sce_exam_rect(self):
        self.checkFile("exam rect", obj= """Place New_Place {
path:: pw lobby
}""", frame="""sceIntro
sceMain

sceTalk
scePres
sceExam, New_Place
sceExamConvo, rect, 35, 128, 217, 182
sceMove""")
        
    def test_sce_exam_circ(self):
        self.checkFile("exam circ", obj="""Place New_Place {
path:: pw lobby
}""", frame="""sceIntro
sceMain

sceTalk
scePres
sceExam, New_Place
sceExamConvo, circle, 86, 28, 92
sceMove""")
        
    def test_sce_move(self):
        self.checkFile("move null", obj="""Place New_Place {
path:: pw lobby
}""", frame="""sceIntro
sceMain, my_Scene

sceTalk
scePres
sceExam, New_Place
sceExamConvo, circle, 86, 28, 92
sceMove, my_Scene, _""")
        
    def test_sce_move_2(self):
        self.checkFile("move under", frame="""sceIntro
sceMain, my_Scene

sceTalk
scePres
sceExam
sceMove, my_Scene, __""")
            
    def test_sce_locks(self):
        self.checkFile("locks", obj="""Profile Present_Me {
}""", frame="""sceIntro
sceMain

sceTalk
scePres
scePresConvo, Present_Me
sceLocks
sceExam
sceMove""")
        
    def test_sce_locks_hide(self):
        self.checkFile("locks hide", frame="""sceIntro
sceMain

sceTalk
scePres
sceLocks, not_digit
sceExam
sceMove""")
        
    def test_sce_locks_actual(self):
        self.checkFile("locks actual",  frame="""sceIntro
sceMain

sceTalk
scePres
sceLocks, -2, 135, 64, 85
sceExam
sceMove""")
        
    def test_sce_locks_hide_actual(self):
        self.checkFile("locks hide actual", frame="""sceIntro
sceMain

sceTalk
scePres
sceLocks, not_digit, -2, 135, 64, 85
sceExam
sceMove""")
        
    def test_sce_custom_main(self):
        self.checkFile("custom main", frame="""sceIntro
sceMain
place, black, left

sceTalk
scePres
sceExam
sceMove""")
        
    def test_custom_talk(self):
        self.checkFile("custom talk", frame="""sceIntro
sceMain

sceTalk
sceTalkConvo:
Have some dialogue.

color, green:
Great dialogue.

scePres
sceExam
sceMove""")
        
    def test_custom_present(self):
        self.checkFile("custom present", obj="""Profile Present_Me {
}""", frame="""sceIntro
sceMain

sceTalk
scePres
scePresConvo, Present_Me:
Have some dialogue.

color, green:
Great dialogue.

sceExam
sceMove""")

    def test_custom_examine(self):
        self.checkFile("custom exam", obj="""Place My_Place {
path:: pw lobby
}""", frame="""sceIntro
sceMain

sceTalk
scePres
sceExam, My_Place
sceExamConvo, circle, 86, 28, 92:
Have some dialogue.

color, green:
Great dialogue.

sceMove""")
        
    def test_custom_locks(self):
        self.checkFile("custom locks", frame="""sceIntro
sceMain

sceTalk
scePres
sceLocks:
Have some dialogue.

color, green:
Great dialogue.

sceExam
sceMove""")

    def test_same_anc_error(self):
        self.checkError((10, "anc dupl", "kumquat"), frame="""sceIntro
sceMain, kumquat

sceTalk
scePres
sceExam
sceMove

sceIntro
sceMain, kumquat""")
        
    def test_dupl_pres(self):
        self.checkError((7, "mult pres", "kumquat"), obj="""Evidence kumquat {
}""", frame="""sceIntro
sceMain

sceTalk
scePres
scePresConvo, kumquat
scePresConvo, kumquat""")
        
    def test_not_presentable(self):
        self.checkError((6, "type in set", "Item to present", "profiles, evidence"), obj="""Place kumquat {
}""", frame="""sceIntro
sceMain

sceTalk
scePres
scePresConvo, kumquat""")
        
    def test_lock_arg_nums(self):
        self.checkError((6, "implicit tuple", 2, "", 1, 1), frame="""sceIntro
sceMain

sceTalk
scePres
sceLocks, 10""")
        
    def test_lock_arg_word_first(self):
        self.checkError((6, "int", "Arguments to sceLocks after the optional hidden"), frame="""sceIntro
sceMain

sceTalk
scePres
sceLocks, 10, 20, kumquat, 30""")
        
    def test_lock_arg_word_second(self):
        self.checkError((6, "int", "Arguments to sceLocks after the optional hidden"), frame="""sceIntro
sceMain

sceTalk
scePres
sceLocks, 10, 20, 30, kumquat""")
        
    def test_fake_exam_place(self):
        self.checkError((6, "bad key", "kumquat", "place"), obj="""Popup kumquat {
}""", frame="""sceIntro
sceMain

sceTalk
scePres
sceExam, kumquat""")
        
    def test_fake_shape(self):
        self.checkError((7, "bad shape", "kumquat"), obj="""Popup kumquat {
}""", frame="""sceIntro
sceMain

sceTalk
scePres
sceExam
sceExamConvo, kumquat""")
        
    def test_poly_no_args(self):
        self.checkError((7, "poly pair"), obj="""Popup kumquat {
}""", frame="""sceIntro
sceMain

sceTalk
scePres
sceExam
sceExamConvo, poly, 1, 2, 3, 4, 5""")
        
    def test_poly_less_six(self):
        self.checkError((7, "poly 6"), frame="""sceIntro
sceMain

sceTalk
scePres
sceExam
sceExamConvo, poly, 1, 2, 3, 4""")
        
    def test_circ_not_3(self):
        self.checkError((7, "circle 3"), frame="""sceIntro
sceMain

sceTalk
scePres
sceExam
sceExamConvo, circle, 1, 2, 3, 4""")
        
    def test_rect_not_4(self):
        self.checkError((7, "rect 4"), frame="""sceIntro
sceMain

sceTalk
scePres
sceExam
sceExamConvo, rect, 1, 2, 3""")
        
    def test_rect_quad_4(self):
        self.checkError((7, "rect to quad 4"), frame="""sceIntro
sceMain

sceTalk
scePres
sceExam
sceExamConvo, rect, 3, 4, 1, 2""")
        
    def test_rect_negative(self):
        self.checkError((7, "min", "All arguments after polygon shape", 0), frame="""sceIntro
sceMain

sceTalk
scePres
sceExam
sceExamConvo, rect, 1, -2, 3, 4""")
        
    def test_move(self):
        self.checkError((7, "implicit tuple", 2, "", 1, 1), frame="""sceIntro
sceMain

sceTalk
scePres
sceExam
sceMove, one_item""")


class Anchors_Exp_Pack(FrameErrors):
    
    folder = "action"
    
    def test_bad_pack(self):
        self.checkError((2, "bad exp number", 1, 1, 2), frame="""dispEv
{1}""")
        
    def test_no_close(self):
        self.checkError((2, "no close brace", "kumquat"), frame="""dispEv
{1, kumquat""")
        
    def test_unescaped_brace_exp(self):
        self.checkError((2, "unescaped brace", "{kumquat"), frame="""dispEv
{1, {kumquat}""")
        
    def test_unescaped_brace(self):
        self.checkError((2, "unescaped brace", "kumquat}"), frame="""dispEv
kumquat}""")
    
    def test_var_def(self):
        self.checkError((2, "schema fail", 2, ""), frame="""varDef
1""")
    
    def test_global_excess(self):
        self.checkError((1, "bad global arg num", 2), frame="setOver, my_anc, other_anc, additional_anc")
    
    def test_single_marker(self):
        self.checkError((2, "$ syntax", "$1"), frame="""dispEv
{$1, 2}, {3}""")
        
    def test_exp_anchor(self):
        self.checkFile("anchor expression", frame="""setOver, {$my_over$}

anc, my_over""")

    # Uses the same file as above.
    def test_pack_unicode(self):
        self.checkFile("anchor expression", frame=u"""setOver, {$my_över$}

anc, my_över""")

    def test_exterior_colon(self):
        self.checkError((2, ": syntax", "kumquat:"), frame="""varDef
{kumquat:}, 2""")
        
    def test_double_colon(self):
        self.checkError((2, ": syntax", "$frame: anc: hor$"), frame="""varDef
{$frame: anc: hor$}, 2""")
        
    def test_unk_anc_type(self):
        self.checkError(("end of file", "unk anc type", "failure"), frame="""varDef
{$failure: anchor$}, 2""")
        
    def test_anc_unset(self):
        self.checkError(("end of file", "anc unset", "evidence", "anchor"), frame="""varDef
{$evidence: anchor$}, 2""")

    def test_colon_var_break(self):
        self.checkError((2, ": syntax", "12:34"), frame="""varDef
12:34, 5""")

    def test_colon_var(self):
        self.checkFile("colon var", frame="""varDef
12\:34, 5""")

    def test_cat_var_var(self):
        self.checkFile("catalysis var var", obj="""Evidence Badge {
}""", frame="""varDef
is_badge_revealed, evidence_is_revealed('preuve'\, $evidence: Badge$)""")

    def test_cat_var_exp(self):
        self.checkFile("catalysis var exp", obj="""Evidence Badge {
}""", frame="""varDef
is_badge_revealed, {evidence_is_revealed('preuve'\, $evidence: Badge$)}""")

    def test_colon_terminate(self):
        self.checkFile("colon terminate", frame="""varDef
foo, bar:

null:
Start dialogue.""")

class CR_GameFlow_Action(FrameErrors):
    
    folder = "action"
    
    def test_dispEv_keypos(self):
        self.checkFile("dispEv normal profile", obj="""Profile my_ev{
}""", frame="""dispEv
my_ev, tr""")
        
    def test_dispEv_valpos(self):
        self.checkFile("dispEv normal ev", obj="""Evidence my_ev{
}""", frame="""dispEv
my_ev, tr
my_ev, bottomleft""")
        
    def test_dispEv_bad_item(self):
        self.checkError((2, "type in set", "Item to display", "profiles, evidence"), obj="""Place my_ev{
}""", frame="""dispEv
my_ev, tr""")
        
    def test_dispEv_bad_pos(self):
        self.checkError((2, "bad key", "tru", "evidence position"), obj="""Evidence my_ev{
}""", frame="""dispEv
my_ev, tru""")
        
    def test_dispEv_rep_pos(self):
        self.checkError((3, "mult pos", "topright"), obj="""Evidence my_ev{
}

Profile my_ev2{
}""", frame="""dispEv
my_ev, tr
my_ev2, topright""")
        
    def test_dispEv_expression_mode(self):
        self.checkFile("dispEv exp", obj="""Evidence my_ev{
}""", frame="""dispEv
{my_arg, my_second_arg},{my_third_arg}
my_ev, tr""")

    def test_hideEv_keypos(self):
        self.checkFile("hideEv normal profile", obj="""Profile my_ev{
}""", frame="""hideEv
my_ev""")
        
    def test_hideEv_bad_item(self):
        self.checkError((2, "type in set", "Item to hide", "profiles, evidence"), obj="""Place my_ev{
}""", frame="""hideEv
my_ev""")
        
    def test_hideEv_expression_mode(self):
        self.checkFile("hideEv exp", obj="""Profile my_ev{
}""", frame="""hideEv
{my_arg, my_second_arg}
my_ev""")
        
    def test_revEv_keypos(self):
        self.checkFile("revEv normal profile", obj="""Profile my_ev{
}""", frame="""revEv
my_ev""")
        
    def test_over_normal(self):
        self.checkFile("setOver normal", frame="""setOver, my_anc

anc, my_anc""")
        
    def test_over_exp(self):
        self.checkFile("setOver exp", frame="setOver, {my_anc}")
        
    def test_proceed_normal(self):
        self.checkFile("proceed normal", frame="""proceed, my_anc

anc, my_anc""")

    def test_proceed_merged(self):
        self.checkError((2, "ban on merge", "proceed"), frame="""merge
proceed, foo""")

    def test_hideFrame_normal(self):
        self.checkFile("hideFrame normal", frame="""hideFrame
my_anc
my_other_anc

anc, my_anc

anc, my_other_anc""")
        
    def test_hideFrame_exp(self):
        self.checkFile("hideFrame exp", frame="""hideFrame
{my_anc}
{my_other_anc}""")
        
    def test_revealFrame_normal(self):
        self.checkFile("revealFrame normal", frame="""revealFrame
my_anc
my_other_anc

anc, my_anc

anc, my_other_anc""")
        
    def test_end_nothing(self):
        self.checkFile("end game nothing", frame="gameOver, end")
        
    def test_end_next(self):
        self.checkFile("end game next", frame="gameOver, next, var")
        
    def test_end_another(self):
        self.checkFile("end game another", frame="gameOver, another, full, 2, 10")
        
    def test_end_expression(self):
        self.checkFile("end game exp", frame="gameOver, {1}, {4}, {2}, {3}")
        
    def test_end_missing_next(self):
        self.checkError((1, "arg missing", "Data to transfer"), frame="gameOver, next")
            
    def test_end_bad_key(self):
        self.checkError((1, "bad key", "kumquat", "target part"), frame="gameOver, kumquat")

    def test_end_bad_key_exp(self):
        self.checkError((1, "bad key", "kumquat", "target part"), frame="gameOver, kumquat, {2}, {3}, {4}")
        
    def test_end_missing_key(self):
        self.checkError((1, "arg missing", "Target part"), frame="gameOver, another, 2, _, full")

    def test_action_overwrite(self):
        self.checkError((2, "global action only", "dispEv"), frame="""proceed, foo
dispEv
kumquat""")

class CR_GameEnv(FrameErrors):

    folder = "action"

    def test_hideObj_fg(self):
        self.checkFile("hide object fg", obj="""Place my_place {
}

my_place Foreground {
name: my_obj
}""", frame="""hideObj
my_place, my_obj""")

    def test_hideObj_bg(self):
        self.checkFile("hide object bg", obj="""Place my_place {
}

my_place Background {
name: my_obj
}""", frame="""hideObj
my_place, my_obj""")

    def test_hideObj_exp(self):
        self.checkFile("hide object exp", frame="""hideObj
{1}, {2, 3}""")
        
    def test_revObj_exp(self):
        self.checkFile("reveal object exp", obj="""Place street {
}""", frame="""revObj
{$street$}, {'foreground', 'object'\:}""")

    def test_hideObj_mixed_err(self):
        self.checkError((2, "exp dependency"), obj="""Place my_place {
}

my_place Background {
name: my_obj
}""", frame="""hideObj
{1}, my_obj""")

    def test_hideObj_not_place(self):
        self.checkError((2, "bad key", "my_place", "place"), obj="""Popup my_place {
}""", frame="""hideObj
my_place, my_obj""")

    def test_hideObj_default(self):
        self.checkFile("hide object default", frame="""hideObj
aj judge, filler""")

    def test_hideObj_fake_sub(self):
        self.checkError((2, "missing subobj", "kumquat"), obj="""Place my_place {
}

my_place Foreground {
name: my_obj
}""", frame="""hideObj
my_place, kumquat""")

    def test_hideSce_norm(self):
        self.checkFile("hide scene normal", frame="""sceIntro
sceMain, my_sce

sceTalk
scePres
sceExam
sceMove
hideSce, my_sce""")
        
    def test_hideSce_exp(self):
        self.checkFile("hide scene exp", frame="""sceIntro
sceMain, my_sce

sceTalk
scePres
sceExam
sceMove
hideSce, {1, 2}""")
        
    def test_revSce_norm(self):
        self.checkFile("reveal scene normal", frame="""sceIntro
sceMain, my_sce

sceTalk
scePres
sceExam
sceMove
revSce, my_sce""")

    def test_hideIntro_norm(self):
        self.checkFile("hide intro normal", frame="""sceIntro
sceMain, my_sce

sceTalk
scePres
sceExam
sceMove
hideIntro, my_sce""")
        
    def test_hideIntro_exp(self):
        self.checkFile("hide intro exp", frame="""sceIntro
sceMain, my_sce

sceTalk
scePres
sceExam
sceMove
hideIntro, {1, 2, 3, 4}""")
        
    def test_revIntro_norm(self):
        self.checkFile("reveal intro normal", frame="""sceIntro
sceMain, my_sce

sceTalk
scePres
sceExam
sceMove
revIntro, my_sce""")

    def test_hideTalk_norm(self):
        self.checkFile("hide talk normal", frame="""sceIntro
sceMain, my_sce

sceTalk
sceTalkConvo, _, _, talk_anc
scePres
sceExam
sceMove
hideTalk, talk_anc""")
        
    def test_revTalk_exp(self):
        self.checkFile("reveal talk exp", frame="""sceIntro
sceMain, my_sce

sceTalk
sceTalkConvo, _, _, talk_anc
scePres
sceExam
sceMove
revTalk, {1, 2, 3, 4, 5, 6}""")

    def test_revTalk_norm(self):
        self.checkFile("reveal talk normal", frame="""sceIntro
sceMain, my_sce

sceTalk
sceTalkConvo, _, _, talk_anc
scePres
sceExam
sceMove
revTalk, talk_anc""")

    def test_hidePsyB_norm(self):
        self.checkFile("hide psy button normal", frame="""sceIntro
sceMain, my_sce

sceTalk
scePres
sceLocks
sceExam
sceMove
hidePsyButton, my_sce""")
        
    def test_revPsyB_norm(self):
        self.checkFile("reveal psy button normal", frame="""sceIntro
sceMain, my_sce

sceTalk
scePres
sceLocks
sceExam
sceMove
revPsyButton, my_sce""")
        
    def test_revPsyB_err(self):
        self.checkError(("end of file", "missing locks", 1), frame="""sceIntro
sceMain, my_sce

sceTalk
scePres
sceExam
sceMove
revPsyButton, my_sce""")

class Locks_Health(FrameErrors):

    folder = "action"

    def test_hidePsy(self):
        self.checkFile("hide psy", frame="""sceIntro
hidePsy

sceMain

sceTalk
scePres
sceLocks
sceExam
sceMove""")
        
    def test_revPsy(self):
        self.checkFile("reveal psy", frame="""sceIntro
revPsy

sceMain, my_sce

sceTalk
scePres
sceLocks
sceExam
sceMove""")
        
    def test_hideOutPsy_err(self):
        self.checkError((1, "enforce scene", "hidePsy"), frame="hidePsy")

    def test_breakPsy_null(self):
        self.checkFile("break psy null", frame="""sceIntro
breakPsy, null_case

sceMain, my_sce

sceTalk
scePres
sceLocks
sceExam
sceMove""")

    def test_breakPsy_val(self):
        self.checkFile("break psy val", frame="""sceIntro
breakPsy
1

sceMain, my_sce

sceTalk
scePres
sceLocks, 10, 20
sceExam
sceMove""")
        
    def test_breakPsy_mixed(self):
        self.checkFile("break psy mixed", frame="""sceIntro
breakPsy
1
{1, 2, 3, 4, 5}

sceMain, my_sce

sceTalk
scePres
sceLocks, 10, 20
sceExam
sceMove""")
        
    def test_breakPsy_not_in_scene(self):
        self.checkError((1, "enforce scene", "breakPsy"), frame="breakPsy")
        
    def test_setHealth(self):
        self.checkFile("set health", frame="setHealth, 10")
        
    def test_redHealth(self):
        self.checkFile("reduce health", frame="redHealth, {10}")
        
    def test_flashHealth(self):
        self.checkFile("flash health", frame="flashHealth, 10")
        
    def test_incHealth(self):
        self.checkFile("increase health", frame="incHealth, {10}")
        
    def test_setHealthErr(self):
        self.checkError((1, "int", "Health"), frame="setHealth, kumquat")
        
    def test_flashHealthErr(self):
        self.checkError((1, "int", "Health"), frame="flashHealth, kumquat")

class Variables(FrameErrors):

    folder = "action"
    
    def test_playerIn_norm(self):
        self.checkFile("playerIn norm", frame="""playerIn
foo, s, true""")
        
    def test_playerIn_pass(self):
        self.checkFile("playerIn pass", frame="""playerIn
foo, float, _""")
        
    def test_playerIn_mixed(self):
        self.checkFile("playerIn mixed", frame="""playerIn
foo, f, true
{1}, {2}, _""")
        
    def test_playerIn_bad_type(self):
        self.checkError((2, "bad key", "kumquat", "type"), frame="""playerIn
foo, kumquat, true""")

    def test_varDef_norm(self):
        self.checkFile("varDef norm", frame="""varDef
foo, bar""")
        
    def test_varDef_exp(self):
        self.checkFile("varDef exp", frame="""varDef
foo, bar
{1}, {2}""")
        
    def test_exp_var(self):
        self.checkFile("expTest var", frame="""expTest, var, foo, my_anc
alpha, my_anc

anc, my_anc""")
        
    def test_exp_exp(self):
        self.checkFile("expTest exp", frame="""expTest, expression, foo, my_anc
alpha, my_anc

anc, my_anc""")
        
    def test_exp_expr_mode(self):
        self.checkFile("expTest expr mode", frame="""expTest, expression, foo, my_anc
alpha, my_anc
{1}, {2}

anc, my_anc""")
        
    def test_exp_expr_global(self):
        self.checkFile("expTest expr global", frame="""anc, my_anc
expTest, {alpha}, 2, 3, my_anc""")
        
    def test_exp_unk(self):
        self.checkError((1, "bad key", "kumquat", "variable"), frame="expTest, kumquat, 1, 2")
        
    def test_condit_norm(self):
        self.checkFile("condit norm", frame="""condit, my_anc
expr, my_anc

anc, my_anc""")
    
    def test_condit_exp(self):
        self.checkFile("condit exp", frame="""condit, my_anc
expr, my_anc
{1}, {2}

anc, my_anc""")

class Input(FrameErrors):
    
    folder = "action"
    
    def test_choice(self):
        self.checkFile("choice normal", frame="""choice
Your Choice, my_anc

anc, my_anc""")
        
    def test_choice_exp(self):
        self.checkFile("choice exp", frame="""choice
Your Choice, my_anc
{1}, {2}

anc, my_anc""")
        
    def test_choice_scene(self):
        self.checkFile("choice scene", frame="""sceIntro
choice
Your Choice, my_anc

sceMain

sceTalk
scePres
sceExam
sceMove
anc, my_anc""")

    def test_choice_lock(self):
        self.checkFile("choice locks", frame="""sceIntro
sceMain

sceTalk
scePres
sceLocks
choice, sealed
Your Choice, my_anc

sceExam
sceMove
anc, my_anc""")

    def test_askEv(self):
        self.checkFile("askEv normal", obj="""Evidence my_ev {
}""", frame="""askEv, all, my_anc
my_ev, my_anc

anc, my_anc""")
        
    def test_askEv_exp(self):
        self.checkFile("askEv exp", obj="""Evidence my_ev {
}""", frame="""askEv, {a}, {b}
my_ev, my_anc
{1, 2}, {3}

anc, my_anc""")
        
    def test_askEv_scene(self):
        self.checkFile("askEv scene", obj="""Evidence my_ev {
}""", frame="""sceIntro
askEv, all, my_anc
my_ev, my_anc

sceMain

sceTalk
scePres
sceExam
sceMove
anc, my_anc""")

    def test_askEv_lock(self):
        self.checkFile("askEv locks", obj="""Evidence my_ev {
}""", frame="""sceIntro
sceMain

sceTalk
scePres
sceLocks
askEv, sealed, all, my_anc
my_ev, my_anc

sceExam
sceMove
anc, my_anc""")

    def test_askEv_lock_error(self):
        self.checkError((7, "schema fail", 3, " An extra argument for the back button is required."), obj="""Evidence my_ev {
}""", frame="""sceIntro
sceMain

sceTalk
scePres
sceLocks
askEv, sealed, all""")
        
    def test_askEv_keyerr(self):
        self.checkError((1, "bad key", "kumquat", "Permissible evidence"), frame="""askEv, kumquat, my_anc
my_ev, my_anc""")
        
    def test_askEv_badobj(self):
        self.checkError((2, "type in set", "Item to present", "profiles, evidence"), obj="""Place my_ev {
}""", frame="""askEv, all, my_anc
my_ev, my_anc""")

    def test_point_exam_custom_place(self):
        self.checkFile("point exam custom", obj="""Place New_Place {
}""", frame="""point, New_Place, my_anc

anc, my_anc""")
        
    def test_point_exam_default_place(self):
        self.checkError((1, "bad key", "black", "place"), frame="""point, black, my_anc

anc, my_anc""")
        
    def test_point_exam_polygon(self):
        self.checkFile("point exam poly", obj="""Place New_Place {
}""", frame="""point, New_Place, my_anc
region, poly, 1, 15, 40, 194, 249, 137, my_anc

anc, my_anc""")
        
    def test_point_exam_rect(self):
        self.checkFile("point exam rect", obj="""Place New_Place {
}""", frame="""point, New_Place, my_anc
region, rect, 35, 128, 217, 182, my_anc

anc, my_anc""")
        
    def test_point_exam_circ(self):
        self.checkFile("point exam circ", obj="""Place New_Place {
}""", frame="""point, New_Place, my_anc
region, circle, 86, 28, 92, my_anc

anc, my_anc""")

    def test_fake_point_place(self):
        self.checkError((1, "bad key", "kumquat", "place"), frame="point, kumquat, my_anc")
        
    def test_fake_shape(self):
        self.checkError((2, "bad shape", "kumquat"), obj="""Place New_Place {
}""", frame="""point, New_Place, my_anc
region, kumquat, 1, 2, 3, 4, my_anc""")
        
    def test_poly_no_args(self):
        self.checkError((2, "poly pair"), obj="""Place New_Place {
}""", frame="""point, New_Place, my_anc
region, poly, 1, 2, 3, 4, 5, my_anc""")
        
    def test_poly_less_six(self):
        self.checkError((2, "poly 6"), obj="""Place New_Place {
}""", frame="""point, New_Place, my_anc
region, poly, 1, 2, 3, 4, my_anc""")
        
    def test_circ_not_3(self):
        self.checkError((2, "circle 3"), obj="""Place New_Place {
}""", frame="""point, New_Place, my_anc
region, circle, 1, 2, 3, 4, my_anc""")
        
    def test_rect_not_4(self):
        self.checkError((2, "rect 4"), obj="""Place New_Place {
}""", frame="""point, New_Place, my_anc
region, rect, 1, 2, 3, my_anc""")

    def test_rect_quad_4(self):
        self.checkError((2, "rect to quad 4"), obj="""Place New_Place {
}""", frame="""point, New_Place, my_anc
region, rect, 3, 4, 1, 2, my_anc""")

    def test_rect_negative(self):
        self.checkError((2, "min", "All arguments after polygon shape", 0), obj="""Place New_Place {
}""", frame="""point, New_Place, my_anc
region, rect, 1, -2, 3, 4, my_anc""")

    def test_point_expr(self):
        self.checkFile("point expr", frame="""point, {1}, {2}
region, {3}, {4}""")
        
    def test_point_one_arg(self):
        self.checkError((2, "bad arg num", "examination region selector"), frame="""point, {1}, {2}
region, {3}""")
        
    def test_point_scene(self):
        self.checkFile("point scene", obj="""Place New_Place {
}""", frame="""sceIntro
point, New_Place, my_anc
region, rect, 35, 128, 217, 182, my_anc

sceMain

sceTalk
scePres
sceExam
sceMove
anc, my_anc""")

    def test_point_lock(self):
        self.checkFile("point locks", obj="""Place New_Place {
}""", frame="""sceIntro
sceMain

sceTalk
scePres
sceLocks
point, sealed, New_Place, my_anc
region, rect, 35, 128, 217, 182, my_anc

sceExam
sceMove
anc, my_anc""")

    def test_point_object(self):
        self.checkFile("point object", obj="""Place My Place {
}

My Place foreground {
name: FGO
}""", frame="""point, My Place, my_anc
object, FGO, my_anc

anc, my_anc""")
        
#===============================================================================
# TODO: Uncomment this when AAO finally supports examining built-ins.
#     def test_point_object_default(self):
#         self.checkFile("point object default", frame="""point, aj court, my_anc
# object, null, my_anc
# 
# anc, my_anc""")
#===============================================================================

    def test_point_fake_object(self):
        self.checkError((2, "missing subobj", "kumquat"), obj="""Place My Place {
}

My Place foreground {
name: FGO
}""", frame="""point, My Place, my_anc
object, kumquat, my_anc""")

    def test_point_bad_type(self):
        self.checkError((2, "bad exam type", "kumquat", "region, object"), obj="""Place My Place {
}""", frame="""point, My Place, my_anc
kumquat, circle, 1, 2, 3, my_anc

anc, my_anc""")

class Macro_Tests(MacroErrors):
    
    folder = "macro"
    
    def test_fail_start(self):
        self.checkError((1, "unk line"), macro="""nonsense""")
        
    def test_fail_unclosed(self):
        self.checkError(("end of file", "unclosed", "Macro"), macro="""macro {""")
        
    def test_macro_syntax(self):
        self.checkFile("syntax", macro="""macro {
}""")
        
    def test_macro_duplicate(self):
        self.checkError((4, "ban duplicate", "Macro", "myMacro"), macro="""myMacro {
}

myMacro {""")
        
    def test_macro_keyword(self):
        self.checkError((1, "keyword claim", "Macro", "merge"), macro="""merge {
}""")
        
    def test_macro(self):
        self.checkFile("function", macro="""obj {
music
wait, 9000
}""", frame="obj")
        
    def test_recursive_macro(self):
        self.checkFile("recursive", macro="""obj {
music
obj2
}

obj2 {
wait, 9000
}""", frame="obj")

    def test_macro_no_override_non_func(self):
        self.checkFile("no non func override", macro="""cross {
wait, 100
}""", frame="cross")

    def test_config_colon(self):
        self.checkError((2, "config colon"), macro="""CONFIG {
test""")
        
    def test_bad_config_attr(self):
        self.checkError((2, "config attr", "fake_attr"), macro="""CONFIG {
fake_attr: fake_value""")

    def test_non_int_pause(self):
        self.checkError((2, "int","Configuration attribute ."), macro="""CONFIG {
.: fake_value""")
        
    def test_negative_pause(self):
        self.checkError((2, "min", "Configuration attribute .", 0), macro="""CONFIG {
.: -1""")
        
    def test_autopause(self):
        self.checkFile("autopause", macro="""CONFIG {
autopause: 
}""", frame = """null:
Let's not pause. That's fine, isn't it? It'll be fantastic!""")
        
    def test_autowrap(self):
        self.checkFile("autowrap", macro="""CONFIG {
autowrap: 
}""", frame = """null:
Let's not pause. That's fine, isn't it? It'll be fantastic!""")
        
    def test_autoquote(self):
        self.checkFile("autoquote", macro="""CONFIG {
autoquote: 
}

test {
dialogue, ‘
}""", obj="""Popup {
path: ”
}""", frame = """test:
”""")
        
    def test_unauto(self):
        self.checkFile("unauto", macro="""CONFIG {
autowrap: 
autowrap: 
}""", frame = """null:
Let's not pause. That's fine, isn't it? It'll be fantastic!""")
        
    def test_0_pause(self):
        self.checkFile("0 pause", macro="""CONFIG {
.: 0 
}""", frame = """null:
Let's not pause. That's fine, isn't it? It'll be fantastic!""")
        
    def test_10_pause(self):
        self.checkFile("10 pause", macro="""CONFIG {
.: 10 
}""", frame = """null:
Let's not pause. That's fine, isn't it? It'll be fantastic!""")
        
    def test_four_period_pause(self):
        self.checkFile("four period", macro="""CONFIG {
...: 10 
}""", frame = """null:
The scent of fresh lemons.... Ah.""")
        
    def test_long_ellipsis(self):
        self.checkFile("ellipsis", macro="""CONFIG {
...: 10 
}""", frame = """null:
The scent of fresh lemons… Ah.""")
        
    def test_bad_startup(self):
        self.checkError((2, "bad key", "kumquat", "startup macro"), macro="""CONFIG {
startup: kumquat""")

    def test_startup(self):
        self.checkFile("startup first", macro="""CONFIG {
startup: before
}""", obj="""Profile {
sprite:: judgebrother
prefix:: judgebrother
}""", frame="""jb.yes""")

if __name__ == '__main__':

    unittest.main()
    os.remove("test_lib/testData.txt")
