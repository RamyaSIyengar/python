import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://www.wikipedia.org/")

e = driver.find_element(By.ID, 'searchLanguage')
element = Select(e)
allOptions = element.options
all = driver.find_elements(By.XPATH, "//select[@id=\"searchLanguage\"]/option")
i = 1
for op in allOptions:
    print(i, op.text)
    i += 1

for o in all:
    print(o.text, "-", o.get_attribute("Lang"))

links = driver.find_elements(By.TAG_NAME, "a")
print("No of links in the wikipedia page", len(links))

for link in links:
    print(f'link text- {link.text} link URL-{link.get_attribute("href")}')

# when you want to select a particular section element first target on the section and in that find the element

block_footer = driver.find_element(By.TAG_NAME, "footer")
footer_links = block_footer.find_elements(By.TAG_NAME, "a")
for flink in footer_links:
    print(flink.get_attribute("href"), flink.text)

# to get a first link
print(footer_links.__getitem__(0).text)

driver.close()

