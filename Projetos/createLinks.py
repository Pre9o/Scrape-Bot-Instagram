import json
import os
from defaultLinksFunctions import create_links_txt, create_links_json

class CreateLinksTxt:
    def __init__(self, username_for_scrape):
        self.username_for_scrape = username_for_scrape
        self.base_url = "https://www.instagram.com"
        self.current_directory = os.path.dirname(os.path.abspath(__file__))

        self.generateLinksFollowers()
        self.generateLinksFollowings()
        self.generateLinksDontFollowMeBack()
        self.generateLinksIDontFollowBack()

    def generateLinksFollowers(self):
        self.input_file_name = self.username_for_scrape + "followers.txt"
        self.input_file_path = os.path.join(self.current_directory, self.input_file_name)
        self.temp_file_name = self.username_for_scrape + "followers_temp.txt"
        self.temp_file_path = os.path.join(self.current_directory, self.temp_file_name)

        create_links_txt(self)

    def generateLinksFollowings(self):
        self.input_file_name = self.username_for_scrape + "followings.txt"
        self.input_file_path = os.path.join(self.current_directory, self.input_file_name)
        self.temp_file_name = self.username_for_scrape + "followings_temp.txt"
        self.temp_file_path = os.path.join(self.current_directory, self.temp_file_name)

        create_links_txt(self)

    def generateLinksDontFollowMeBack(self):
        self.input_file_name = self.username_for_scrape + "dontFollowMeBack.txt"
        self.input_file_path = os.path.join(self.current_directory, self.input_file_name)
        self.temp_file_name = self.username_for_scrape + "dontFollowMeBack_temp.txt"
        self.temp_file_path = os.path.join(self.current_directory, self.temp_file_name)

        create_links_txt(self)

    def generateLinksIDontFollowBack(self):
        self.input_file_name = self.username_for_scrape + "iDontFollowBack.txt"
        self.input_file_path = os.path.join(self.current_directory, self.input_file_name)
        self.temp_file_name = self.username_for_scrape + "iDontFollowBack_temp.txt"
        self.temp_file_path = os.path.join(self.current_directory, self.temp_file_name)

        create_links_txt(self)
      


class CreateLinksJson:
    def __init__(self, username_for_scrape):
        self.username_for_scrape = username_for_scrape
        self.base_url = "https://www.instagram.com"
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        
        self.generateLinksFollowers()
        self.generateLinksFollowings()
        self.generateLinksDontFollowMeBack()
        self.generateLinksIDontFollowBack()

    def generateLinksFollowers(self):
        self.input_file_name = self.username_for_scrape + "followers.json"
        self.input_file_path = os.path.join(self.current_directory, self.input_file_name)
        self.temp_file_name = self.username_for_scrape + "followers_temp.json"
        self.temp_file_path = os.path.join(self.current_directory, self.temp_file_name)

        create_links_json(self)

    def generateLinksFollowings(self):
        self.input_file_name = self.username_for_scrape + "followings.json"
        self.input_file_path = os.path.join(self.current_directory, self.input_file_name)
        self.temp_file_name = self.username_for_scrape + "followings_temp.json"
        self.temp_file_path = os.path.join(self.current_directory, self.temp_file_name)

        create_links_json(self)

    def generateLinksDontFollowMeBack(self):
        self.input_file_name = self.username_for_scrape + "dontFollowMeBack.json"
        self.input_file_path = os.path.join(self.current_directory, self.input_file_name)
        self.temp_file_name = self.username_for_scrape + "dontFollowMeBack_temp.json"
        self.temp_file_path = os.path.join(self.current_directory, self.temp_file_name)

        create_links_json(self)

    def generateLinksIDontFollowBack(self):
        self.input_file_name = self.username_for_scrape + "iDontFollowBack.json"
        self.input_file_path = os.path.join(self.current_directory, self.input_file_name)
        self.temp_file_name = self.username_for_scrape + "iDontFollowBack_temp.json"
        self.temp_file_path = os.path.join(self.current_directory, self.temp_file_name)

        create_links_json(self)
    