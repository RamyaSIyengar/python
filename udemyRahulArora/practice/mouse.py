import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.way2automation.com/")
driver.implicitly_wait(1)
driver.maximize_window()

resources = driver.find_element(By.XPATH,"//div/div/div/div/div/div[1]/nav/div[1]/ul/li/a["
                                         "@class='menu-link']/child::span[text()='Resources']")
practice1 = driver.find_element(By.ID, "menu-item-27618")
action = ActionChains(driver)
action.move_to_element(resources).move_to_element(practice1).click().perform()


time.sleep(5)
