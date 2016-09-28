# coding: UTF-8

'''Module to automate sending Catalysis data to AAO and opening the
browser.'''

# Adapted from code by Ferdielance.

import webbrowser

from urllib.error import HTTPError

import mechanicalsoup

from catalysis_globals import get_file_name

DATA_FILENAME = "testData.txt"
SAVE_URL = "http://aceattorney.sparklin.org/save.php"
LOGIN_URL = "http://aceattorney.sparklin.org/forum/ucp.php?mode=login"
EDITOR_URL_BASE = "http://aceattorney.sparklin.org/editor.php?trial_id="
# This text is scanned for to check if the login is successful.
# When accessed by MechanicalSoup, AAO assumes we want French text.
TEXT_ON_SUCCESSFUL_LOGIN_PAGE = "Vous êtes à présent connecté"
# NOTE: Your environment PATH variable must include the path to Firefox
# for this to work!

br = mechanicalsoup.Browser()

def login_aao(upload_dict):
    '''Log the Mechanize browser into AAO. Because you cannot login twice,
    this function should only be called once per session.'''
    login_page = br.get(LOGIN_URL)
    login_form = login_page.soup.form
    login_form.find(id="username")["value"] = upload_dict["username"]
    login_form.find(id="password")["value"] = upload_dict["password"]
    logged_in = br.submit(login_form, LOGIN_URL)
    # Check if the user has logged in by looking for the phrase
    # "latest post", which appears on successful login.
    return TEXT_ON_SUCCESSFUL_LOGIN_PAGE in logged_in.soup.get_text()

def upload_data(upload_dict):
    '''Upload trial data once logged in.'''
    save_page = br.get(SAVE_URL)
    save_form = save_page.soup.form
    save_form.find("input", {"name": "trial_id"})['value'] = str(
    	   upload_dict["trial_id"])

    file_location = get_file_name(DATA_FILENAME)

    with open(file_location, "r") as trial_file:
        trial_data = trial_file.read()
    save_form.find("textarea", {"name": "trial_contents"}).insert(
    	   0, trial_data)
    # Fill out the hidden "trial_contents_length" field. AAO automates it,
    # but mechanize can't work with the JS, so we need to handle it manually.
    save_form.find("input", {"name": "trial_contents_length"})["readonly"] = (
    	   False)
    # Inclusion of \r could possibly create an inconsistency here.
    # Catalysis should have purged all of these.
    save_form.find("input", {"name": "trial_contents_length"})["value"] = len(
    	   trial_data)
    try:
        br.submit(save_form, SAVE_URL)
        return True
    except HTTPError:
        print("Could not submit trial data. Check your trial ID.")
        return False

# Open the browser with editor, if logged into Firefox on AAO.
def open_browser(upload_dict):
    '''Open the editor.'''
    browser_controller = webbrowser.get()
    browser_controller.open(EDITOR_URL_BASE + str(upload_dict["trial_id"]))

def upload(upload_dict):
    '''Login, upload the data, and open the case in-editor.'''
    if not login_aao(upload_dict):
        print("Unable to login to AAO. Aborting auto-upload. Check your "
        	     "password and username.")
        return

    print("Login successful.")

    if upload_data(upload_dict):
        print("Complete! We will open the case with your default browser, "
        	     "if you are logged into AAO on it.")
        try:
            open_browser(upload_dict)
        except webbrowser.Error:
            pass
