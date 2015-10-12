# coding: UTF-8

'''This module runs Catalysis by calling classes from other modules.'''

import json
import catalysis_globals
import object_parser
import macro_parser
import frame_parser
import upload_parser
import os
import sys
import uploader


# If there are three argument variables, we're in test mode. Accept the data.
try:
    __, macro_test, obj_test, frame_test = sys.argv
    test_mode = True
except ValueError:
    macro_test, obj_test, frame_test = False, False, False
    test_mode = False

print "Beginning catalysis.\n"

try:
    if not test_mode:
        directory, upload_dict = upload_parser.parse_file()
    else:
        directory = "test_lib"
    macro_dict, config_dict, auto_dict = macro_parser.parse_file(
        directory, macro_test)
    template, suffix_dicts, object_dict = (
        object_parser.parse_file(directory, config_dict, obj_test))
    json_data = frame_parser.parse_file(
        directory, template, suffix_dicts, object_dict, macro_dict,
        config_dict, frame_test)
    json_data = json.dumps(json_data, separators=(',', ':'))
except SystemExit:
    sys.exit()
except:
    print "Unknown error observed! Please send your documents to Enthalpy."
    catalysis_globals.terminate()

# Get file even when the program is .exe.
output_file = directory + "/testData.txt"
if getattr(sys, 'frozen', False):
    output_file = os.path.join(os.path.dirname(sys.executable), output_file)

# Write the full information to the file.
open(output_file, "w").write('//Definition//Def6\n' + json_data)

if not test_mode:
    try:
        upload_dict["trial_id"] = int(upload_dict["trial_id"])
    except ValueError:
        print "Choosing not to upload data..."
    else:
        print ("Choosing to upload data to trial {}. Press any key to " +
		"continue.").format(
			upload_dict["trial_id"])
        raw_input(
			"Alternately, exit to abort uploading while keeping a valid " +
			"trial file.")
        uploader.upload(upload_dict)

print "Catalysis complete!"
catalysis_globals.terminate()
