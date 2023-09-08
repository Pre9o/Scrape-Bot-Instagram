import botInstagram
import getpass
import os


def main():
    print("Bem vindo ao bot do Instagram")
    print("Deseja executar o bot ou apenas deletar os arquivos .json e .txt?")
    print("1 - Executar o bot / 2 - Deletar os arquivos / 0 - Sair")
    
    while True:
        program_option = int(input("Digite a opção desejada: "))
        
        if program_option == 0:
            break
        
        elif program_option == 1:
            break
        
        elif program_option == 2:
            botInstagram.Instagram.removeFiles(program_option)
            return
        
        else:
            print("Opção inválida")
    
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
        
    botInstagram.Instagram(username, password, username_for_scrape)
    
    with open(input_file_path, "r") as js_file:
        js_code = js_file.read()
        js_code = js_code.replace(username_for_scrape, "cuardido")
        
    with open(input_file_path, "w") as js_file:
        js_file.write(js_code)
    
main()