import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, MoveTargetOutOfBoundsException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

try:
    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://jqueryui.com/resizable/")
    driver.implicitly_wait(1)
    driver.maximize_window()

    # Switch to the iframe containing the resizable element
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )
    driver.switch_to.frame(iframe)

    # Find the resizable element
    resizable_ele = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='resizable']/div[3]"))
    )

    # Adjust drag offsets to avoid moving out of bounds
    action = ActionChains(driver)
    action.drag_and_drop_by_offset(resizable_ele, 100, 100).perform()


except (NoSuchElementException, TimeoutException) as e:
    print(f"An error occurred: {e}")
finally:
    # Clean up by closing the driver
    driver.quit()
