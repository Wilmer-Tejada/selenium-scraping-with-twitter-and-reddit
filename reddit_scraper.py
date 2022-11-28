import chromedriver_autoinstaller
import os
import time
import zipfile

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()


def open_page(website):
    driver.get(website)
    driver.implicitly_wait(5)


def pick_subreddit(subreddit):
    target_name = driver.find_element(By.XPATH, '//*[@id="targetNameInput"]')
    target_name.send_keys(subreddit)
    driver.implicitly_wait(1)


def pick_section(category):
    section = driver.find_element(
        By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div/input"
    )
    section.send_keys(category)
    section.send_keys(Keys.RETURN)


def click_gifs_button():
    include_gifs = driver.find_element(
        By.XPATH, "/html/body/div/div[2]/div[3]/div[2]/div[2]/div[1]/div/div/div/label"
    )
    include_gifs.click()


def click_download():
    download_button = driver.find_element(By.XPATH, '//*[@id="downloadButton"]')
    download_button.click()

def download_memes(subreddit):
    open_page("https://redditdownloader.github.io/")
    pick_subreddit(subreddit)
    pick_section("Top (day)")
    click_gifs_button()
    click_download()

    # Wait until file is created and fully downloaded.
    download_path = "/Users/wilmertejada/Downloads/dankmemes_top.zip"
    while not os.path.exists(download_path):
        time.sleep(5)

    # Cut and paste file into directory, extract, then delete zip.
    os.rename(download_path, f"{subreddit}.zip")
    with zipfile.ZipFile(f"{subreddit}.zip", "r") as zip_ref:
        zip_ref.extractall("memes")
    os.remove(f"{subreddit}.zip")

if __name__ == "__main__":
    download_memes("dankmemes")
    download_memes("Memes_Of_The_Dank")
