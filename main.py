import botInstagram
import getpass
import os

# Time in function sleep that the bot will wait to scrape
timer_for_scrape = 15

def main():
    '''Main function.
    '''
    print("Welcome to the Instagram bot")
    print("Do you want to run the bot or just delete the .json and .txt files?")
    print("1 - Run the bot / 2 - Delete files / 0 - Quit")

    while True:
        program_option = int(input("Enter your choice: "))

        if program_option == 0:
            return
        elif program_option == 1:
            break
        elif program_option == 2:
            botInstagram.Instagram.removeFiles(program_option)
            return
        else:
            print("Invalid option")

    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    username_for_scrape = input("Enter the username you want to scrape: ")

    current_directory = os.path.dirname(os.path.abspath(__file__))

    input_file_name = "script.js"
    input_file_path = os.path.join(current_directory, input_file_name)

    # Modify the script.js file and set the desired username for scraping
    with open(input_file_path, "r") as js_file:
        js_code = js_file.read()
        js_code = js_code.replace("cuardido", username_for_scrape)

    with open(input_file_path, "w") as js_file:
        js_file.write(js_code)

    botInstagram.Instagram(username, password, username_for_scrape, timer_for_scrape)

    # Restore the script.js file to its original state
    with open(input_file_path, "r") as js_file:
        js_code = js_file.read()
        js_code = js_code.replace(username_for_scrape, "cuardido")

    with open(input_file_path, "w") as js_file:
        js_file.write(js_code)

if __name__ == "__main__":
    main()
