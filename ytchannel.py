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
import os
from functions import *

directory = input("What will this directory be named?")

channel = input("What channel are we downloading? ")

parent_dir = "C:\\Open Source\\yt transcription"

path = os.path.join(parent_dir,directory)

driver = create_webdriver_instance()

driver.get(f'https://www.youtube.com/@{channel}/videos')

scroll_to_bottom(driver)

links = driver.find_elements(By.CSS_SELECTOR, 'a.yt-simple-endpoint.style-scope.ytd-rich-grid-media')

hrefs = [link.get_attribute('href') for link in links]

complete_hrefs = [href for href in hrefs if href is not None]

for href in complete_hrefs:
    print(href)
    result = doownloadVideo(href, path)
    print(f"{href}: {result}")


print("Total number of links:", len(complete_hrefs))

time.sleep(3)

driver.quit()