import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://jqueryui.com/droppable/")
driver.implicitly_wait(1)
driver.maximize_window()

iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

src = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")
act = ActionChains(driver)
# act.drag_and_drop(src, target).perform()
act.drag_and_drop_by_offset(source=src, yoffset=200, xoffset=200).perform()
time.sleep(1)
