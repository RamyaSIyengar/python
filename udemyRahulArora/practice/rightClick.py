import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://deluxe-menu.com/popup-mode-sample.html")
driver.implicitly_wait(1)
driver.maximize_window()


wait = WebDriverWait(driver, 10)
src = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='dmD2']/following-sibling::p/img")))
act = ActionChains(driver)
act.context_click(src).perform()
productInfo = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[@id='dm2m1i1tdT']")))
act.move_to_element(productInfo).perform()
feature = driver.find_element(By.XPATH, "//*[@id=\"dm2m2i0tdT\"]")
act.move_to_element(feature).click().perform()

time.sleep(1)