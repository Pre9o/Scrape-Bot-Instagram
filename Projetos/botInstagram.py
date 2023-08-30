import getpass
import json
import shutil
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()

class Instagram:
    def __init__(self, username, password, username_for_scrape):
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.bot = driver
        self.username_for_scrape = username_for_scrape
        self.login()
        
    def removeFiles(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        input_file_name = "data.json"
        input_file_path = os.path.join(current_directory, input_file_name)
        
        output_file_name = "followers.json"
        output_file_path = os.path.join(current_directory, output_file_name)
        
        output_file_name = "following.json"
        output_file_path = os.path.join(current_directory, output_file_name)
        
        output_file_name = "iDontFollowBack.json"
        output_file_path = os.path.join(current_directory, output_file_name)
        
        output_file_name = "dontFollowMeBack.json"
        output_file_path = os.path.join(current_directory, output_file_name)
        
        if os.path.exists(input_file_path):
            os.remove(input_file_path)
        else:
            print("O arquivo não existe")
            
        if os.path.exists(output_file_path):
            os.remove(output_file_path)
        else:
            print("O arquivo não existe")
        
    def selectData(self):     
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        input_file_name = "data.json"
        input_file_path = os.path.join(current_directory, input_file_name)
                
        print("1 - Seguidores")
        print("2 - Seguindo")
        print("3 - Não sigo de volta")
        print("4 - Não me segue de volta")
        print("5 - Todos os dados")
        print("0 - Sair")        
        
        while True:
            option = int(input("Digite a opção desejada: "))
            
            if option == 0:
                break
                        
            elif option == 1:
                output_file_name = "followers.json"
                output_file_path = os.path.join(current_directory, output_file_name)
                
                with open(input_file_path, "r", encoding="utf-8") as json_file:
                    data = json.load(json_file)
                    
                followers = data.get('data', {}).get('followers', [])
                
                with open(output_file_path, "w", encoding="utf-8") as json_file:
                    json.dump(followers, json_file, indent=2, ensure_ascii=False)
                    
                print("Arquivo criado com sucesso")
        
            elif option == 2:
                output_file_name = "following.json"
                output_file_path = os.path.join(current_directory, output_file_name)
                
                with open(input_file_path, "r", encoding="utf-8") as json_file:
                    data = json.load(json_file)
                    
                following = data.get('data', {}).get('following', [])
                
                with open(output_file_path, "w", encoding="utf-8") as json_file:
                    json.dump(following, json_file, indent=2, ensure_ascii=False)
                    
                print("Arquivo criado com sucesso")
                            
            elif option == 3:
                output_file_name = "iDontFollowBack.json"
                output_file_path = os.path.join(current_directory, output_file_name)
                
                with open(input_file_path, "r", encoding="utf-8") as json_file:
                    data = json.load(json_file)
                    
                i_dont_follow_back = data.get('data', {}).get('iDontFollowBack', [])
                
                with open(output_file_path, "w", encoding="utf-8") as json_file:
                    json.dump(i_dont_follow_back, json_file, indent=2, ensure_ascii=False)
                    
                print("Arquivo criado com sucesso")
                
                            
            elif option == 4:
                output_file_name = "dontFollowMeBack.json"
                output_file_path = os.path.join(current_directory, output_file_name)
                
                with open(input_file_path, "r", encoding="utf-8") as json_file:
                    data = json.load(json_file)

                dont_follow_me_back = data.get('data', {}).get('dontFollowMeBack', [])

                with open(output_file_path, "w", encoding="utf-8") as json_file:
                    json.dump(dont_follow_me_back, json_file, indent=2, ensure_ascii=False)
                    
                print("Arquivo criado com sucesso")
                                        
            elif option == 5:
                print("O arquivo data.json contém todos os dados")
                
            else:
                print("Opção inválida")
                    
                
    def moveData(self):
        # Especifique o caminho do arquivo original e o novo caminho de destino
        download_directory = os.path.join(os.path.expanduser("~"), "Downloads")
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        input_file_name = "data.json"
        input_file_path = os.path.join(download_directory, input_file_name)
        
        output_file_name = "data.json"
        output_file_path = os.path.join(current_directory, output_file_name)
        
        # Mova o arquivo para o novo caminho de destino
        shutil.move(input_file_path, output_file_path)
        
        self.selectData()
        
        
    def scrape(self):
        self.bot.get('https://www.instagram.com/' + self.username_for_scrape + '/')
        
        time.sleep(5)
        
        self.removeFiles()
        
        current_directory = os.path.dirname(os.path.abspath(__file__))
        input_file_name = "script.js"
        input_file_path = os.path.join(current_directory, input_file_name)
        
        with open(input_file_path, "r") as js_file:
            js_code = js_file.read()

        self.bot.execute_script(js_code)
        
        time.sleep(30)

        #fechar o driver
        self.bot.close()
        
        self.moveData()
        
    def login(self):
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
        
def main():
    username = input("Digite seu nome de usuário: ")
    password = getpass.getpass("Digite sua senha: ")
    
    username_for_scrape = input("Digite o nome de usuário que deseja fazer o scrape: ")
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    input_file_name = "script.js"
    input_file_path = os.path.join(current_directory, input_file_name)

    #modificar o arquivo script.js e colocar o nome de usuário que deseja fazer o scrape
    with open(input_file_path, "r") as js_file:
        js_code = js_file.read()
        js_code = js_code.replace("cuardido", username_for_scrape)
        
    with open(input_file_path, "w") as js_file:
        js_file.write(js_code)
        
    Instagram(username, password, username_for_scrape)
    
    with open(input_file_path, "r") as js_file:
        js_code = js_file.read()
        js_code = js_code.replace(username_for_scrape, "cuardido")
        
    with open(input_file_path, "w") as js_file:
        js_file.write(js_code)
    
main()

    
                





        
        
        
        

        
    
        
        
    
    
        
        
    
    
    