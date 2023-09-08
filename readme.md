Scrape  Bot Instagram
================

This is a simple bot that scrapes Instagram followers and following. It uses a simple algorithm to find the followers that don't follow you back and the following that you don't follow back. It's a simple project that I made to learn how to use Selenium and Typescript. It's not perfect, but it works.

## How to use
1. Clone this repository
2. Install the dependencies with `pip install -r requirements.txt`
3. Install ChromeDriver from [here](https://chromedriver.chromium.org/downloads)
4. Run the script with `python main.py`
5. Enter your Instagram username, password and the username of the account you want to scrape (your username and password are not saved anywhere, they are only used to log in to Instagram)
6. Wait for the script to finish
7. Select the files option to see the results

## How it works
The script uses Selenium to open a browser and log in to Instagram. Then it goes to the profile of the account you want to scrape and scrolls down until it reaches the end of the followers/following list. Then it saves the list of followers/following in a file. After that, it compares the followers list with the following list and saves the results in one file called `data.json`, after that, you can select the files option to see the results.

## How to contribute
If you want to contribute to this project, you can fork this repository and make a pull request with your changes. If you find any bugs, you can open an issue and I'll try to fix it as soon as possible.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer
This project is not affiliated, associated, authorized, endorsed by, or in any way officially connected with Instagram, or any of its subsidiaries or its affiliates. The official Instagram website can be found at https://instagram.com. The name Instagram as well as related names, marks, emblems and images are registered trademarks of their respective owners. The use of any trade name or trademark is for identification and reference purposes only and does not imply any association with the trademark holder of their product brand. Instagram has a API that you can find [here](https://developers.facebook.com/docs/instagram-api/). This project uses Selenium to scrape Instagram, it's not the best way to do it, but it works.


