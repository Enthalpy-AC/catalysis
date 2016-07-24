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
    directory = ""
    if not test_mode:
        directory, upload_dict = upload_parser.parse_file()
    else:
        directory = "test_lib"
    directory += "/"
    macro_dict, config_dict = macro_parser.parse_file(directory, macro_test)
    template, suffix_dicts, object_dict = (
        object_parser.parse_file(directory, config_dict, obj_test))
    json_data = frame_parser.parse_file(
        directory, template, suffix_dicts, object_dict, macro_dict,
        config_dict, frame_test)
    json_data = json.dumps(json_data, separators=(',', ':'))
except SystemExit:
    sys.exit()
except:
    print(
        "Unknown error observed! Please send your documents to Enthalpy, "
        "especially err.txt, which has been automatically created."
    )
    error_file = catalysis_globals.get_file_name(directory + "/err.txt")
    error_file = open(error_file, "w")
    error_file.write(str(sys.exc_info()[0]) + "\n")
    traceback.print_tb(sys.exc_info()[2], file=error_file)
    catalysis_globals.terminate()

# Write data to file.
output_file = catalysis_globals.get_file_name(directory + "/testData.txt")
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
        uploader.upload(directory, upload_dict)

print("Catalysis complete!")
catalysis_globals.terminate()
