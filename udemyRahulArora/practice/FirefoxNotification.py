import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

firefox_options = Options()
firefoxOptions = webdriver.FirefoxOptions()
# firefox_options.add_argument("--disable-notifications")
firefox_options.set_preference("dom.webnotifications.enabled", False)
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefoxOptions)

driver.get("https://www.justdial.com/")

windowsIDs = driver.window_handles  # to get windowId of all the windows so that we can switch
print(windowsIDs)
time.sleep(1)

driver.close()
