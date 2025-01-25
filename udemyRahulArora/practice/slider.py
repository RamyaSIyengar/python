import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://jqueryui.com/slider/")
driver.implicitly_wait(1)
driver.maximize_window()

iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

main_slider = driver.find_element(By.ID, "slider")
slider = driver.find_element(By.XPATH, "//div[@id='slider']/span")

location = main_slider.location
size = main_slider.size
h, w = size['height'], size['width']
print(location, size)  # {'x': 8, 'y': 8} {'height': 14, 'width': 564}
print(h, w)  # 14 564
print(slider.location)  # {'x': -1, 'y': 4}
ActionChains(driver).drag_and_drop_by_offset(slider, w/2, 0).perform()
print(slider.location)  # {'x': 280, 'y': 4}
time.sleep(1)
