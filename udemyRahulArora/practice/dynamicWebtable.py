from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/points-table-standings")
driver.implicitly_wait(1)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

rows = len(driver.find_elements(By.XPATH, "//tbody/tr"))
print(rows)
cols = len(driver.find_elements(By.XPATH, "//table/tr[1]/td"))
print(cols)

# printing a data from row2 col5
# try:
#     row2col5 = wait.until(EC.presence_of_element_located((By.XPATH, "//tbody[@class='ds-text-center']//tr[2]/td[5]")))
#     print(row2col5.text)
# except Exception as e:
#     print(f"an error occured {e}")


# for row in range(2, rows+1):
#     for col in range(1, cols+1):
#         xpath = f""


