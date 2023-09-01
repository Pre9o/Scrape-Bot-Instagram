import json
import os

def generate_links(self):
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

def replace_input_file(self):
    os.replace(self.temp_file_path, self.input_file_path)

def create_links_txt(self):
    generate_links(self)
    replace_input_file(self)
    print("Done")
