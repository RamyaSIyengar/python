import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('')
driver.implicitly_wait(10)
driver.maximize_window()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://www.tizag.com/htmlT/htmlcheckboxes.php")
driver.implicitly_wait(10)
driver.maximize_window()


def is_element_present(how, what):
    try:
        return driver.find_element(how, what).is_displayed()
    except NoSuchElementException:
        return False


block = driver.find_element(By.XPATH, "/html/body/table[3]/tbody/tr[1]/td[2]/table/tbody/tr/td/div[4]")

checkboxes = block.find_elements(By.XPATH, "//input[@name='sports']")
print(len(checkboxes))
for check in checkboxes:
    check.click()

time.sleep(3)
