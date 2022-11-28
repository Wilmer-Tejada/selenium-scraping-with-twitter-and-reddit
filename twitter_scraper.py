import time
import chromedriver_autoinstaller
import os
import random
import schedule
import shutil

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def login(username, password):
    """
    A simple function which logs a user into Twitter using Selenium.

    Parameters
    ----------
    username : str
        Twitter username of an existing account.
    password : str
        Twitter password of an existing account.
    """

    # Chromedriver setup and launch
    driver.get("https://twitter.com/i/flow/login")
    driver.implicitly_wait(5)

    # Enter username
    # username = "TEST"
    username_field = driver.find_element(By.XPATH, "//input[@name='text']")
    username_field.send_keys(username)
    username_field.send_keys(Keys.RETURN)
    driver.implicitly_wait(1)

    # Sometimes twitter asks for you to re-enter usernames to catch bots.
    try:
        username_field = driver.find_element(By.XPATH, "//input[@name='text']")
        username_field.send_keys("danksdanky")
        username_field.send_keys(Keys.RETURN)
        driver.implicitly_wait(1)
    except:
        pass

        # Sleep again for 3 so password page can load then enter password
    password_field = driver.find_element(By.XPATH, "//input[@name='password']")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)

    time.sleep(2)


def load_tweet_page():
    """
        Loads tweet page and disables file upload pop up
    """
    driver.get("https://twitter.com/compose/tweet")

    # disable the OS file picker popup
    driver.execute_script(
        """
                    document.addEventListener('click', function(evt) {
                      if (evt.target.type === 'file')
                        evt.preventDefault();
                    }, true)
                    """
    )
    driver.implicitly_wait(2)


def post_meme(file_location):
    """
        Tweets meme given a certain file path and then deletes it.
    """
    # click upload image button
    upload_image_button = driver.find_element(
        By.XPATH, '//*[@aria-label="Add photos or video"]'
    )
    upload_image_button.click()
    driver.implicitly_wait(2)

    # Upload file
    driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(file_location)
    tweet_button = driver.find_element(By.XPATH, '//*[@data-testid="tweetButton"]')
    driver.implicitly_wait(3)
    tweet_button.click()

    # Delete file locally
    os.remove(file_location)
    driver.implicitly_wait(10)



def loop():
    meme_list = os.listdir("memes")
    meme_list[0]
    load_tweet_page()
    post_meme("/Users/wilmertejada/Desktop/Programming/Python/Twitter Meme Bot/memes/" + meme_list[0])

def purge_memes():
    shutil.rmtree("memes")
    os.system('python reddit_scraper.py')

if __name__ == "__main__":
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()

    # Enter your username and password below
    launch_login = login("dankydanks@protonmail.com", "O$GT8R574t3v")


    minute = random.randint(1,59)
    schedule.every().hour.at(f":{minute}").do(loop)
    schedule.every().day.at("10:30").do(purge_memes)

    schedule.every(10).seconds.do(loop)

    while True:
        schedule.run_pending()
        time.sleep(1)


