import json
import shutil
import os
import time
from createLinks import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Instagram:
    '''A class to represent an Instagram bot
    
    Attributes
    ----------
        username : str
            the username of the Instagram account
        password : str
            the password of the Instagram account
        base_url : str
            the base url of the Instagram website
        bot : WebDriver
            the WebDriver instance
        username_for_scrape : str
            the username of the Instagram account to be scraped
        timer_for_scrape : int
            the time in seconds to wait before scraping the Instagram account
    
    Methods
    -------
        createFilesJson()
            Create JSON files for followers, followings, iDontFollowBack, and dontFollowMeBack
        createFilesTxt()
            Create text files for followers, followings, iDontFollowBack, and dontFollowMeBack
        removeFiles()
            Remove all .json and .txt files from the current directory
        selectData()
            Select the file type to view
        moveData()
            Move the data.json file to the current directory
        scrape()
            Scrape the Instagram account
        login()
            Login to the Instagram account
        '''
    def __init__(self, username, password, username_for_scrape, timer_for_scrape):
        '''Constructs all the necessary attributes for the Instagram object
        '''
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.bot = webdriver.Chrome()
        self.username_for_scrape = username_for_scrape
        self.timer_for_scrape = timer_for_scrape
        self.login()
    
    def createFilesJson(self):
        '''Create JSON files for followers, followings, iDontFollowBack, and dontFollowMeBack
        '''
        # Create JSON files for followers, followings, iDontFollowBack, and dontFollowMeBack
        current_directory = os.path.dirname(os.path.abspath(__file__))

        input_file_name = "data.json"
        input_file_path = os.path.join(current_directory, input_file_name)

        output_file_name = self.username_for_scrape + "followers.json"
        output_file_path = os.path.join(current_directory, output_file_name)
        
        with open(input_file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            
        followers = data.get('data', {}).get('followers', [])
        
        with open(output_file_path, "w", encoding="utf-8") as json_file:
            json.dump(followers, json_file, indent=2, ensure_ascii=False)
            
        print("File 'followers.json' created successfully")

        output_file_name = self.username_for_scrape + "followings.json"
        output_file_path = os.path.join(current_directory, output_file_name)
        
        with open(input_file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            
        following = data.get('data', {}).get('followings', [])
        
        with open(output_file_path, "w", encoding="utf-8") as json_file:
            json.dump(following, json_file, indent=2, ensure_ascii=False)
            
        print("File 'followings.json' created successfully")

        output_file_name = self.username_for_scrape + "iDontFollowBack.json"
        output_file_path = os.path.join(current_directory, output_file_name)
        
        with open(input_file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            
        i_dont_follow_back = data.get('data', {}).get('iDontFollowBack', [])
        
        with open(output_file_path, "w", encoding="utf-8") as json_file:
            json.dump(i_dont_follow_back, json_file, indent=2, ensure_ascii=False)
            
        print("File 'iDontFollowBack.json' created successfully")

        output_file_name = self.username_for_scrape + "dontFollowMeBack.json"
        output_file_path = os.path.join(current_directory, output_file_name)
        
        with open(input_file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        dont_follow_me_back = data.get('data', {}).get('dontFollowMeBack', [])

        with open(output_file_path, "w", encoding="utf-8") as json_file:
            json.dump(dont_follow_me_back, json_file, indent=2, ensure_ascii=False)
            
        print("File 'dontFollowMeBack.json' created successfully")

    def createFilesTxt(self):
        '''Create text files for followers, followings, iDontFollowBack, and dontFollowMeBack
        '''
        # Create text files for followers, followings, iDontFollowBack, and dontFollowMeBack
        current_directory = os.path.dirname(os.path.abspath(__file__))

        input_file_name = "data.json"
        input_file_path = os.path.join(current_directory, input_file_name)

        output_file_name = self.username_for_scrape + "followers.txt"
        output_file_path = os.path.join(current_directory, output_file_name)
        
        with open(input_file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            
        followers = data.get('data', {}).get('followers', [])
        
        with open(output_file_path, "w", encoding="utf-8") as txt_file:
            for follower in followers:
                txt_file.write(str(follower) + "\n")
                txt_file.write("\n")
                
        print("File 'followers.txt' created successfully")

        output_file_name = self.username_for_scrape + "followings.txt"
        output_file_path = os.path.join(current_directory, output_file_name)
        
        with open(input_file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            
        following = data.get('data', {}).get('followings', [])
        
        with open(output_file_path, "w", encoding="utf-8") as txt_file:
            for follower in following:
                txt_file.write(str(follower) + "\n")
                txt_file.write("\n")
                
        print("File 'followings.txt' created successfully")

        output_file_name = self.username_for_scrape + "iDontFollowBack.txt"
        output_file_path = os.path.join(current_directory, output_file_name)
        
        with open(input_file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            
        i_dont_follow_back = data.get('data', {}).get('iDontFollowBack', [])
        
        with open(output_file_path, "w", encoding="utf-8") as txt_file:
            for follower in i_dont_follow_back:
                txt_file.write(str(follower) + "\n")
                txt_file.write("\n")
                
        print("File 'iDontFollowBack.txt' created successfully")

        output_file_name = self.username_for_scrape + "dontFollowMeBack.txt"
        output_file_path = os.path.join(current_directory, output_file_name)
        
        with open(input_file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            
        dont_follow_me_back = data.get('data', {}).get('dontFollowMeBack', [])
        
        with open(output_file_path, "w", encoding="utf-8") as txt_file:
            for follower in dont_follow_me_back:
                txt_file.write(str(follower) + "\n")
                txt_file.write("\n")
                
        print("File 'dontFollowMeBack.txt' created successfully")

        with open (input_file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            
        #copiar tudo para um txt
        output_file_name = self.username_for_scrape + "data.txt"
        output_file_path = os.path.join(current_directory, output_file_name)
        
        with open(output_file_path, "w", encoding="utf-8") as txt_file:
            txt_file.write("Followers: \n")
            for follower in data.get('data', {}).get('followers', []):
                txt_file.write(str(follower) + "\n")
                txt_file.write("\n")
                
            txt_file.write("\Followings: \n")
            for follower in data.get('data', {}).get('following', []):
                txt_file.write(str(follower) + "\n")
                txt_file.write("\n")
                
            txt_file.write("\nIDontFollowBack: \n")
            for follower in data.get('data', {}).get('iDontFollowBack', []):
                txt_file.write(str(follower) + "\n")
                txt_file.write("\n")
                
            txt_file.write("\nDontFollowMeBack: \n")
            for follower in data.get('data', {}).get('dontFollowMeBack', []):
                txt_file.write(str(follower) + "\n")
                txt_file.write("\n")
                
        os.remove(input_file_path)
        print("File 'data.txt' created successfully")

    def removeFiles(self):
        '''Remove all .json and .txt files from the current directory'''
        # Remove all .json and .txt files from the current directory
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        # Remove all .json files in the directory
        for file in os.listdir(current_directory):
            if file.endswith(".json"):
                file_path = os.path.join(current_directory, file)
                os.remove(file_path)
                
        # Remove all .txt files in the directory
        for file in os.listdir(current_directory):
            if file.endswith(".txt"):
                file_path = os.path.join(current_directory, file)
                os.remove(file_path)
                     
    def selectData(self):    
        '''Select the file type to view''' 
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        script_file_path = os.path.join(current_directory, "script.js")
        
        print("Select the file type to view: ")
        print("1 - JSON")
        print("2 - TXT")
        print("0 - Quit")

        while True:
            file_option = int(input("Enter the desired option: "))
            
            if file_option == 0:
                break
            
            elif file_option == 1:
                self.createFilesJson()
                break
            
            elif file_option == 2:
                self.createFilesTxt()
                break
            
            else:
                print("Invalid option")        
                
        while True:
            link_option = int(input("Create a file with user profile links? (1 - Yes / 2 - No): "))

            if link_option == 1:
                if file_option == 1:
                    instagram_links_generator = CreateLinksJson(self.username_for_scrape)
                    instagram_links_generator.__init__(self.username_for_scrape)
                    break

                elif file_option == 2:
                    instagram_links_generator = CreateLinksTxt(self.username_for_scrape)
                    instagram_links_generator.__init__(self.username_for_scrape)
                    break

            elif link_option == 2:
                break

            else:  
                print("Invalid option")
            
        with open(script_file_path, "r") as js_file:
            js_code = js_file.read()
            js_code = js_code.replace(self.username_for_scrape, "cuardido")
            
        with open(script_file_path, "w") as js_file:
            js_file.write(js_code)          
        
    def moveData(self):
        '''Move the data.json file to the current directory'''
        # Specify the original file path and the new destination file path
        download_directory = os.path.join(os.path.expanduser("~"), "Downloads")
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        input_file_name = "data.json"
        input_file_path = os.path.join(download_directory, input_file_name)
        
        output_file_name = "data.json"
        output_file_path = os.path.join(current_directory, output_file_name)
        
        # Move the file to the new destination
        shutil.move(input_file_path, output_file_path)
        
        self.selectData()
        
    def scrape(self):
        '''Scrape the Instagram account'''
        self.bot.get('https://www.instagram.com/' + self.username_for_scrape + '/')
        
        time.sleep(5)
        
        self.removeFiles()
        
        current_directory = os.path.dirname(os.path.abspath(__file__))
        input_file_name = "script.js"
        input_file_path = os.path.join(current_directory, input_file_name)
        
        with open(input_file_path, "r") as js_file:
            js_code = js_file.read()

        self.bot.execute_script(js_code)
        
        time.sleep(self.timer_for_scrape)

        # Close the WebDriver
        self.bot.close()
        
        self.moveData()
        
    def login(self):
        '''Login to the Instagram account'''
        self.bot.get(self.base_url)
        
        enter_username = WebDriverWait(self.bot, 20).until(
        expected_conditions.presence_of_element_located((By.NAME, 'username')))
        
        enter_username.send_keys(self.username)
        
        enter_password = WebDriverWait(self.bot, 20).until(
        expected_conditions.presence_of_element_located((By.NAME, 'password')))
        
        enter_password.send_keys(self.password)
        
        enter_password.send_keys(Keys.RETURN)
        
        time.sleep(5)
        
        self.scrape()