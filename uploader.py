# coding: UTF-8

'''Module to automate sending Catalysis data to AAO and opening the
browser.'''

# Adapted from code by Ferdielance.

import webbrowser
import time

from urllib.error import HTTPError

import mechanicalsoup

from catalysis_globals import get_file_name

DATA_FILENAME = "testData.txt"
DOMAIN = "http://aaonline.fr/"
SAVE_URL = DOMAIN + "save.php"
LOGIN_URL = DOMAIN + "forum/ucp.php?mode=login"
EDITOR_URL_BASE = DOMAIN + "editor.php?trial_id="
# NOTE: Your environment PATH variable must include the path to Firefox
# for this to work!

class Uploader(object):
    '''This class handles trial file upload.'''

    def __init__(self, upload_dict):
        self.browser = mechanicalsoup.StatefulBrowser()
        self.upload_dict = upload_dict
        self.upload()

    def login_aao(self):
        '''Log the MechanicalSoup browser into AAO. Because you cannot login twice,
        this function should only be called once per session.'''
        self.browser.open(LOGIN_URL)
        self.browser.select_form('#login')
        self.browser["username"] = self.upload_dict["username"]
        self.browser["password"] = self.upload_dict["password"]
        time.sleep(5) # PHPBB prohibits forms from being submitted as soon as they're created as a bot defense measure.
        result_page = self.browser.submit_selected()
        return len(result_page.soup.select("#username_logged_in")) > 0

    def upload_data(self):
        '''Upload trial data once logged in.'''
        self.browser.open(SAVE_URL)
        self.browser.select_form()
        self.browser["trial_id"] = str(self.upload_dict["trial_id"])

        file_location = get_file_name(DATA_FILENAME)

        with open(file_location, "r") as trial_file:
            trial_data = trial_file.read()

        self.browser["trial_contents"] = trial_data
        self.browser["trial_contents_length"] = len(trial_data)
        result_page = self.browser.submit_selected()

        if result_page.status_code == 200:
            return True
        else:
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
