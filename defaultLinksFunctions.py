import json
import os

class defaultLinksFuncionsToTxt:
    '''This class adds links to the end of each line in the input file.
    The input file is a text file with one line per user. The line contains
    the user's username. The output file is a text file with one line per
    user. The line contains the user's username and a link to the user's
    profile page. The link is added to the end of the line.
    '''
    def __init__(self, input_file_path, temp_file_path, base_url):
        '''Initialize the class.
        input_file_path: The path to the input file.
        temp_file_path: The path to the temporary file.
        base_url: The base URL for the links.
        '''
        self.input_file_path = input_file_path
        self.temp_file_path = temp_file_path
        self.base_url = base_url
        self.generate_links_txt()
        self.replace_input_file_txt()
        
    def generate_links_txt(self):
        '''Read input file and write links to a temporary file.
        The input file is a text file with one line per user. The line
        contains the user's username. The output file is a text file with
        one line per user. The line contains the user's username and a link
        to the user's profile page. The link is added to the end of the line.
        '''
        # Read input file and write links to a temporary file
        with open(self.input_file_path, "r", encoding="utf-8") as file_txt:
            lines = file_txt.readlines()

        with open(self.temp_file_path, "w", encoding="utf-8") as temp_file:
            for line in lines:
                username_start = line.find("'username': '") + len("'username': '")
                if username_start >= 0:
                    username_end = line.find("'", username_start)
                    if username_end >= 0:
                        username = line[username_start:username_end]
                        link = self.base_url + "/" + username
                        line_with_link = line.rstrip() + f" Link: {link}\n"
                        temp_file.write(line_with_link)
                        temp_file.write("\n")  # Add a blank line
                else:
                    temp_file.write(line)
                    temp_file.write("\n")  # Add a blank line

    def replace_input_file_txt(self):
        '''Replace the input file with the temporary file.
        '''
        # Replace the input file with the temporary file
        os.replace(self.temp_file_path, self.input_file_path)
            
class defaultLinksFuncionsToJson:
    '''This class adds links to the input JSON file.
    The input file is a JSON file with one user per object. The object
    contains the user's username. The output file is a JSON file with one
    user per object. The object contains the user's username and a link to
    the user's profile page. The link is added to the object.
    '''
    def __init__(self, input_file_path, temp_file_path, base_url):
        '''Initialize the class.
        input_file_path: The path to the input file.
        temp_file_path: The path to the temporary file.
        base_url: The base URL for the links.
        '''
        self.input_file_path = input_file_path
        self.temp_file_path = temp_file_path
        self.base_url = base_url
        self.generate_links_json()
        self.replace_input_file_json()
        
    def generate_links_json(self):
        '''Read input JSON file, add links, and write to a temporary file.
        The input file is a JSON file with one user per object. The object
        contains the user's username. The output file is a JSON file with one
        user per object. The object contains the user's username and a link to
        the user's profile page. The link is added to the object.
        '''
        # Read input JSON file, add links, and write to a temporary file
        with open(self.input_file_path, "r", encoding="utf-8") as file_json:
            with open(self.temp_file_path, "w", encoding="utf-8") as temp_file:
                data = json.load(file_json)
                for user in data:
                    link = self.base_url + "/" + user["username"]
                    user["link"] = link
                json.dump(data, temp_file, indent=4)
                            
    def replace_input_file_json(self):
        '''Replace the input file with the temporary file.
        '''
        # Replace the input file with the temporary file
        os.replace(self.temp_file_path, self.input_file_path)
        