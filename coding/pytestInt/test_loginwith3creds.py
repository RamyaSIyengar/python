import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver

class Test_Login:

    txtbox_username_id = "email"
    txtbox_passwd_id = "pass"
    btn_submit_name = "login"

    def __init__(self, setup):
        self.driver = setup
        self.driver.get("https://www.facebook.com/")

    def test_login(self):
        self.driver.find_element(By.ID, self.txtbox_username_id )





