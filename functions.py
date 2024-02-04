from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from pytube import YouTube
from pytube.exceptions import AgeRestrictedError

def create_webdriver_instance():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")  
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("start-maximized")  
    chrome_options.add_argument("disable-infobars")  
    chrome_options.add_argument("--disable-extensions")  


    driver = webdriver.Chrome(options=chrome_options)
    return driver

def scroll_to_bottom(driver):
    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

        time.sleep(2)

        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def doownloadVideo(link, path):
    try:
        video = YouTube(link)
        video.streams.filter(res='720p').first().download(path)
        return 'Downloaded'
    except AgeRestrictedError as e:
        print(f"Error: Video {link} is age restricted. Skipping...")
        return 'Skipped due to age restriction'
    except Exception as e:
        print(f"An error occurred for video {link}: {e}")
        return 'Skipped due to an error'
