#  sign in for both + and - two-sceanrios of new ts - adopt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#  positive scenario

def signIn_Credentials(username, passwd, error_msg1=None):

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://app.indee.tv/")

    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(passwd)
    driver.find_element(By.LINK_TEXT, "Sign in").click()

    if not error_msg1:
        assert driver.title == "indee"
    else:
        error_msg = driver.find_element()
        assert error_msg == error_msg1


if __name__ == "main":
    signIn_Credentials("username", "passwd")





