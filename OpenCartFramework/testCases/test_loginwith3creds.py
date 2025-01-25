import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# def setup():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     return driver

def data():

    dp = [('7090929039', 'R6i#24412'),('7090929031', 'R6i#24411'),('7090922039', 'R6i#22412')]

    return dp


class Test_Login:

    txtbox_username_id = "email"
    txtbox_passwd_id = "pass"
    btn_submit_name = "login"

    @pytest.mark.parametrize('user, passwd', data())
    def test_login(self, setup, user, passwd):
        self.driver = setup
        self.driver.get("https://www.facebook.com/")
        self.driver.find_element(By.ID, self.txtbox_username_id).send_keys(user)
        self.driver.find_element(By.ID, self.txtbox_passwd_id).send_keys(passwd)
        self.driver.find_element(By.NAME, self.btn_submit_name).click()






