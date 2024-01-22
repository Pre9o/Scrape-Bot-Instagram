import os
from defaultLinksFunctions import *

class CreateLinksTxt:
    '''This class is used to create the links for the txt files. It uses the defaultLinksFunctions.py file to create the links.
    The links are created in the current directory of the file. The links are created in the following format:
    username + followers.txt
    username + followings.txt
    username + dontFollowMeBack.txt
    username + iDontFollowBack.txt
    '''
    def __init__(self, username_for_scrape):
        '''This function is used to initialize the class. It takes the username of the account that is going to be scraped.
        It also takes the base url of the instagram website and the current directory of the file.
        It also calls the functions to generate the links for the txt files.
        '''
        self.username_for_scrape = username_for_scrape
        self.base_url = "https://www.instagram.com"
        self.current_directory = os.path.dirname(os.path.abspath(__file__))

        self.generateLinksFollowers()
        self.generateLinksFollowings()
        self.generateLinksDontFollowMeBack()
        self.generateLinksIDontFollowBack()

    def generateLinksFollowers(self):
        '''This function is used to generate the links for the followers.txt file. It takes the username of the account that is going to be scraped.
        It also takes the base url of the instagram website and the current directory of the file.
        It calls the defaultLinksFuncionsToTxt function from the defaultLinksFunctions.py file to generate the links.
        It also takes the input file name and path and the temp file name and path.
        The input file name and path are the name and path of the file that is going to be used to generate the links.
        The temp file name and path are the name and path of the file that is going to be used to store the links.
        '''
        self.input_file_name = self.username_for_scrape + "followers.txt"
        self.input_file_path = os.path.join(self.current_directory, self.input_file_name)
        self.temp_file_name = self.username_for_scrape + "followers_temp.txt"
        self.temp_file_path = os.path.join(self.current_directory, self.temp_file_name)

        defaultLinksFuncionsToTxt(self.input_file_path, self.temp_file_path, self.base_url)

    def generateLinksFollowings(self):
        '''This function is used to generate the links for the followings.txt file. It takes the username of the account that is going to be scraped.
        It also takes the base url of the instagram website and the current directory of the file.
        It calls the defaultLinksFuncionsToTxt function from the defaultLinksFunctions.py file to generate the links.
        It also takes the input file name and path and the temp file name and path.
        The input file name and path are the name and path of the file that is going to be used to generate the links.
        The temp file name and path are the name and path of the file that is going to be used to store the links.
        '''
        self.input_file_name = self.username_for_scrape + "followings.txt"
        self.input_file_path = os.path.join(self.current_directory, self.input_file_name)
        self.temp_file_name = self.username_for_scrape + "followings_temp.txt"
        self.temp_file_path = os.path.join(self.current_directory, self.temp_file_name)

        defaultLinksFuncionsToTxt(self.input_file_path, self.temp_file_path, self.base_url)

    def generateLinksDontFollowMeBack(self):
        '''This function is used to generate the links for the dontFollowMeBack.txt file. It takes the username of the account that is going to be scraped.
        It also takes the base url of the instagram website and the current directory of the file.
        It calls the defaultLinksFuncionsToTxt function from the defaultLinksFunctions.py file to generate the links.
        It also takes the input file name and path and the temp file name and path.
        The input file name and path are the name and path of the file that is going to be used to generate the links.
        The temp file name and path are the name and path of the file that is going to be used to store the links.
        '''
        self.input_file_name = self.username_for_scrape + "dontFollowMeBack.txt"
        self.input_file_path = os.path.join(self.current_directory, self.input_file_name)
        self.temp_file_name = self.username_for_scrape + "dontFollowMeBack_temp.txt"
        self.temp_file_path = os.path.join(self.current_directory, self.temp_file_name)

        defaultLinksFuncionsToTxt(self.input_file_path, self.temp_file_path, self.base_url)

    def generateLinksIDontFollowBack(self):
        '''This function is used to generate the links for the iDontFollowBack.txt file. It takes the username of the account that is going to be scraped.
        It also takes the base url of the instagram website and the current directory of the file.
        It calls the defaultLinksFuncionsToTxt function from the defaultLinksFunctions.py file to generate the links.
        It also takes the input file name and path and the temp file name and path.
        The input file name and path are the name and path of the file that is going to be used to generate the links.
        The temp file name and path are the name and path of the file that is going to be used to store the links.
        '''
        self.input_file_name = self.username_for_scrape + "iDontFollowBack.txt"
        self.input_file_path = os.path.join(self.current_directory, self.input_file_name)
        self.temp_file_name = self.username_for_scrape + "iDontFollowBack_temp.txt"
        self.temp_file_path = os.path.join(self.current_directory, self.temp_file_name)

        defaultLinksFuncionsToTxt(self.input_file_path, self.temp_file_path, self.base_url)
      
class CreateLinksJson:
    '''This class is used to create the links for the json files. It uses the defaultLinksFunctions.py file to create the links.
    The links are created in the current directory of the file. The links are created in the following format:
    username + followers.json
    username + followings.json
    username + dontFollowMeBack.json
    username + iDontFollowBack.json
    '''
    def __init__(self, username_for_scrape):
        self.username_for_scrape = username_for_scrape
        self.base_url = "https://www.instagram.com"
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        
        self.generateLinksFollowers()
        self.generateLinksFollowings()
        self.generateLinksDontFollowMeBack()
        self.generateLinksIDontFollowBack()

    def generateLinksFollowers(self):
        '''This function is used to generate the links for the followers.json file. It takes the username of the account that is going to be scraped.
        It also takes the base url of the instagram website and the current directory of the file.
        It calls the defaultLinksFuncionsToJson function from the defaultLinksFunctions.py file to generate the links.
        It also takes the input file name and path and the temp file name and path.
        The input file name and path are the name and path of the file that is going to be used to generate the links.
        The temp file name and path are the name and path of the file that is going to be used to store the links.
        '''
        self.input_file_name = self.username_for_scrape + "followers.json"
        self.input_file_path = os.path.join(self.current_directory, self.input_file_name)
        self.temp_file_name = self.username_for_scrape + "followers_temp.json"
        self.temp_file_path = os.path.join(self.current_directory, self.temp_file_name)

        defaultLinksFuncionsToJson(self.input_file_path, self.temp_file_path, self.base_url)

    def generateLinksFollowings(self):
        '''This function is used to generate the links for the followings.json file. It takes the username of the account that is going to be scraped.
        It also takes the base url of the instagram website and the current directory of the file.
        It calls the defaultLinksFuncionsToJson function from the defaultLinksFunctions.py file to generate the links.
        It also takes the input file name and path and the temp file name and path.
        The input file name and path are the name and path of the file that is going to be used to generate the links.
        The temp file name and path are the name and path of the file that is going to be used to store the links.
        '''
        self.input_file_name = self.username_for_scrape + "followings.json"
        self.input_file_path = os.path.join(self.current_directory, self.input_file_name)
        self.temp_file_name = self.username_for_scrape + "followings_temp.json"
        self.temp_file_path = os.path.join(self.current_directory, self.temp_file_name)

        defaultLinksFuncionsToJson(self.input_file_path, self.temp_file_path, self.base_url)

    def generateLinksDontFollowMeBack(self):
        '''This function is used to generate the links for the dontFollowMeBack.json file. It takes the username of the account that is going to be scraped.
        It also takes the base url of the instagram website and the current directory of the file.
        It calls the defaultLinksFuncionsToJson function from the defaultLinksFunctions.py file to generate the links.
        It also takes the input file name and path and the temp file name and path.
        The input file name and path are the name and path of the file that is going to be used to generate the links.
        The temp file name and path are the name and path of the file that is going to be used to store the links.
        '''
        self.input_file_name = self.username_for_scrape + "dontFollowMeBack.json"
        self.input_file_path = os.path.join(self.current_directory, self.input_file_name)
        self.temp_file_name = self.username_for_scrape + "dontFollowMeBack_temp.json"
        self.temp_file_path = os.path.join(self.current_directory, self.temp_file_name)

        defaultLinksFuncionsToJson(self.input_file_path, self.temp_file_path, self.base_url)

    def generateLinksIDontFollowBack(self):
        '''This function is used to generate the links for the iDontFollowBack.json file. It takes the username of the account that is going to be scraped.
        It also takes the base url of the instagram website and the current directory of the file.
        It calls the defaultLinksFuncionsToJson function from the defaultLinksFunctions.py file to generate the links.
        It also takes the input file name and path and the temp file name and path.
        The input file name and path are the name and path of the file that is going to be used to generate the links.
        The temp file name and path are the name and path of the file that is going to be used to store the links.
        '''
        self.input_file_name = self.username_for_scrape + "iDontFollowBack.json"
        self.input_file_path = os.path.join(self.current_directory, self.input_file_name)
        self.temp_file_name = self.username_for_scrape + "iDontFollowBack_temp.json"
        self.temp_file_path = os.path.join(self.current_directory, self.temp_file_name)

        defaultLinksFuncionsToJson(self.input_file_path, self.temp_file_path, self.base_url)
    