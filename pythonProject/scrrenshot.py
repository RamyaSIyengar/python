import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com/")
driver.maximize_window()

# driver.save_screenshot("img.png")
# driver.get_screenshot_as_file(os.getcwd()+"\\file.png")

# to take screenshot of particular element
logo = driver.find_element(By.XPATH, "//img[@alt='Google']")
# logo.screenshot("logo.png")

driver.get_screenshot_as_png() # in ascii code we need to decode
