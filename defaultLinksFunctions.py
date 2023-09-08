import json
import os


class defaultLinksFuncionsToTxt:
    def __init__(self, input_file_path, temp_file_path, base_url):
        self.input_file_path = input_file_path
        self.temp_file_path = temp_file_path
        self.base_url = base_url
        self.generate_links_txt()
        self.replace_input_file_txt()
        
    
    def generate_links_txt(self):
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
                        temp_file.write("\n")  # Adiciona a linha em branco
                else:
                    temp_file.write(line)
                    temp_file.write("\n")  # Adiciona a linha em branco

    def replace_input_file_txt(self):
        os.replace(self.temp_file_path, self.input_file_path)
            
            
            
class defaultLinksFuncionsToJson:
    def __init__(self, input_file_path, temp_file_path, base_url):
        self.input_file_path = input_file_path
        self.temp_file_path = temp_file_path
        self.base_url = base_url
        self.generate_links_json()
        self.replace_input_file_json()
        
    def generate_links_json(self):
        with open(self.input_file_path, "r", encoding="utf-8") as file_json:
            with open(self.temp_file_path, "w", encoding="utf-8") as temp_file:
                data = json.load(file_json)
                for user in data:
                    link = self.base_url + "/" + user["username"]
                    user["link"] = link
                json.dump(data, temp_file, indent=4)
                            
    def replace_input_file_json(self):
        os.replace(self.temp_file_path, self.input_file_path)
        