'''Module to automate sending Catalysis data to AAO and opening the
browser.'''

# Adapted from code by Ferdielance.

DATA_FILENAME = "/testData.txt"
SAVE_URL = "http://aceattorney.sparklin.org/save.php"
LOGIN_URL = "http://aceattorney.sparklin.org/forum/ucp.php?mode=login"
EDITOR_URL_BASE = "http://aceattorney.sparklin.org/editor.php?trial_id="
# Upon successful login.
TEXT_ON_SUCCESSFUL_LOGIN_PAGE = "latest post"
# NOTE: Your environment PATH variable must include the path to Firefox
# for this to work!
MY_BROWSER = "firefox"

import re
import mechanize
from mechanize._mechanize import FormNotFoundError
import webbrowser
from urllib2 import HTTPError

br = mechanize.Browser()

def login_aao(upload_dict):
    '''Log the Mechanize browser into AAO. Because you cannot login twice,
    this function should only be called once per session.'''
    br.open(LOGIN_URL)
    try:
        br.select_form(nr=0)
    except FormNotFoundError:
        print "Couldn't find login form on login page."
    br["username"] = upload_dict["username"]
    br["password"] = upload_dict["password"]
    logged_in = br.submit()
    logged_in_html = logged_in.read()
    # Check if the user has logged in by looking for the phrase
    # "latest post", which appears on successful login.
    match = re.search(TEXT_ON_SUCCESSFUL_LOGIN_PAGE, logged_in_html)
    return match != None

def upload_data(directory, upload_dict):
    '''Upload trial data once logged in.'''
    br.open(SAVE_URL)
    br.select_form(nr=0)
    br["trial_id"] = str(upload_dict["trial_id"])
    with open(directory + DATA_FILENAME, "r") as trial_file:
        trial_data = trial_file.read()
    br["trial_contents"] = trial_data
    # Fill out the hidden "trial_contents_length" field. AAO automates it,
    # but mechanize can't work with the JS, so we need to handle it manually.
    br.find_control("trial_contents_length").readonly = False
    # Inclusion of \r could possibly create an inconsistency here.
    # Catalysis code should have purged all of these.
    br["trial_contents_length"] = str(len(trial_data))
    try:
        br.submit()
    except HTTPError:
        print "Could not submit trial data - do you have the correct trial ID?"

# Open the browser with editor.
# Note: This requires an AAO login with Firefox, not the mechanize Browser.
# At bare minimum, Firefox needs the necessary cookies.
def open_browser(upload_dict):
    '''Open the editor.'''
    browser_controller = webbrowser.get(MY_BROWSER)
    browser_controller.open(EDITOR_URL_BASE + str(upload_dict["trial_id"]))

def upload(directory, upload_dict):
    '''Login, upload the data, and open the case in-editor.'''
    if login_aao(upload_dict):
        print "Login successful."
    else:
        print "Unable to login to AAO."

    upload_data(directory, upload_dict)
    print(
        "Complete! If you are logged into Firefox on AAO, we will now open"
        "this in the editor.")
    try:
        open_browser(upload_dict)
    except webbrowser.Error:
        pass
