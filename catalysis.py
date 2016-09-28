# coding: UTF-8

'''This module runs Catalysis by calling classes from other modules.'''

import codecs
import json
import sys
import traceback

import catalysis_globals
import frame_parser
import object_parser
import macro_parser
import uploader
import upload_parser

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# If there are three argument variables, we're in test mode. Accept the data.
try:
    __, macro_test, obj_test, frame_test = sys.argv
    test_mode = True
except ValueError:
    macro_test, obj_test, frame_test = False, False, False
    test_mode = False

print("Beginning catalysis.\n")

try:
    if not test_mode:
        catalysis_globals.directory, upload_dict, max_err = (
         	  upload_parser.parse_file())
        catalysis_globals.Invalid.max_err = max_err
    else:
        catalysis_globals.directory = "test_lib"
    macro_dict, config_dict = macro_parser.parse_file(macro_test)
    template, suffix_dicts, object_dict = (
        object_parser.parse_file(config_dict, obj_test))
    json_data = frame_parser.parse_file(
        template, suffix_dicts, object_dict, macro_dict, config_dict,
        frame_test)
    json_data = json.dumps(json_data, separators=(',', ':'))
except SystemExit:
    sys.exit()
except:
    print(
        "Unknown error observed! Please send your documents to Enthalpy, "
        "especially err.txt, which has been automatically created."
    )
    error_file = catalysis_globals.get_file_name("err.txt")
    with open(error_file, "w") as f:
        traceback.print_exc(file=f)
    catalysis_globals.terminate()

# Write data to file.
output_file = catalysis_globals.get_file_name("testData.txt")
open(output_file, "w").write('//Definition//Def6\n' + json_data)

if not test_mode:
    try:
        upload_dict["trial_id"] = int(upload_dict["trial_id"])
    except ValueError:
        print("Choosing not to upload data...")
    else:
        print((
            "Choosing to upload data to trial {}. Press enter to " +
            "continue.").format(upload_dict["trial_id"]))
        print("If this was not the trial ID you wanted, close Catalysis.")
        # Due to the codec, you need a bytestring here.
        input()
        uploader.upload(upload_dict)

print("Catalysis complete!")
catalysis_globals.terminate()
