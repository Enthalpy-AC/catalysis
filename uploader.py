# coding: UTF-8

'''Module to automate sending Catalysis data to AAO and opening the
browser.'''

# Adapted from code by Ferdielance.

import webbrowser

from urllib.error import HTTPError

import mechanicalsoup

from catalysis_globals import get_file_name

DATA_FILENAME = "testData.txt"
DOMAIN = "http://aaonline.fr/"
SAVE_URL = DOMAIN + "save.php"
LOGIN_URL = DOMAIN + "forum/ucp.php?mode=login"
EDITOR_URL_BASE = DOMAIN + "editor.php?trial_id="
# This text is scanned for to check if the login is successful.
# When accessed by MechanicalSoup, AAO assumes we want French text.
TEXT_ON_SUCCESSFUL_LOGIN_PAGE = "Vous êtes à présent connecté"
# NOTE: Your environment PATH variable must include the path to Firefox
# for this to work!

class Uploader(object):
    '''This class handles trial file upload.'''

    def __init__(self, upload_dict):
        self.browser = mechanicalsoup.Browser()
        self.upload_dict = upload_dict
        self.upload()

    def login_aao(self):
        '''Log the Mechanize browser into AAO. Because you cannot login twice,
        this function should only be called once per session.'''
        login_page = self.browser.get(LOGIN_URL)
        login_form = login_page.soup.form
        login_form.find(id="username")["value"] = self.upload_dict["username"]
        login_form.find(id="password")["value"] = self.upload_dict["password"]
        logged_in = self.browser.submit(login_form, LOGIN_URL)
        # Check if the user has logged in by looking for the phrase
        # "latest post", which appears on successful login.
        return TEXT_ON_SUCCESSFUL_LOGIN_PAGE in logged_in.soup.get_text()

    def upload_data(self):
        '''Upload trial data once logged in.'''
        save_page = self.browser.get(SAVE_URL)
        save_form = save_page.soup.form
        save_form.find("input", {"name": "trial_id"})['value'] = str(
            self.upload_dict["trial_id"])

        file_location = get_file_name(DATA_FILENAME)

        with open(file_location, "r") as trial_file:
            trial_data = trial_file.read()
        save_form.find("textarea", {"name": "trial_contents"}).insert(
            0, trial_data)
        # Fill the hidden "trial_contents_length" field. AAO automates it, but
        # mechanize can't work with the JS, so we need to handle it manually.
        save_form.find("input", {"name": "trial_contents_length"})[
            "readonly"] = False
        # Inclusion of \r could possibly create an inconsistency here.
        # Catalysis should have purged all of these.
        save_form.find("input", {"name": "trial_contents_length"})[
            "value"] = len(trial_data)
        try:
            self.browser.submit(save_form, SAVE_URL)
            return True
        except HTTPError:
            print("Could not submit trial data. Check your trial ID.")
            return False

    # Open the trial in-editor, if logged into AAO on the default browser.
    def open_browser(self):
        '''Open the editor.'''
        browser_controller = webbrowser.get()
        browser_controller.open(
            EDITOR_URL_BASE + str(self.upload_dict["trial_id"]))

    def upload(self):
        '''Login, upload the data, and open the case in-editor.'''
        if not self.login_aao():
            print("Unable to login to AAO. Aborting auto-upload. Check your "
                  "password and username.")
            return

        print("Login successful.")

        if self.upload_data():
            print("Complete! We will open the case with your default browser, "
                  "if you are logged into AAO on it.")
            try:
                self.open_browser()
            except webbrowser.Error:
                pass
