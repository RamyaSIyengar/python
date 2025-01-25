import time

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://accounts.google.com/")
driver.maximize_window()

driver.find_element(by=By.CSS_SELECTOR, value="#identifierId").send_keys("ramyaiyengar244@gmail.com")
driver.find_element(by=By.XPATH, value="//span[text()='Next']").click()
time.sleep(5)


