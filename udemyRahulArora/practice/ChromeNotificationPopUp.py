import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

"""
We have to create an object of this ChromeOptions class and apply the 
addArguments method on it. The parameter --disable-notifications is 
passed as a parameter to this method. Finally, this information is 
sent to the ChromeDriver.
"""

options = webdriver.ChromeOptions()
# option.add_argument("--disable-notifications")

pref = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", pref)
# options.add_argument("--headless")  # Run in headless mode

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


driver.implicitly_wait(1)
driver.get("https://www.justdial.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# closing a popup inside a website

try:
    popup = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"__next\"]/div/section/div[3]/div/img")))
    closeButton = popup.find_element(By.XPATH, "//span[@class='jsx-43611f4a9c2537c5 floatbanner_close jdicon']")
    closeButton.click()
except Exception as e:
    # print("element is not clickable")
    print(f"error occurred {e}")



time.sleep(5)