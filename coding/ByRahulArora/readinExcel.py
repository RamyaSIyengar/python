import openpyxl
from selenium.webdriver.support.wait import WebDriverWait
import XL_Utils

path = "C:\\Users\\soundarr\\Documents\\data.xlsx"

totalrows = XL_Utils.get_maxRow(filename=path, SheetName="Sheet4")
totalcol = XL_Utils.get_maxColumn(filename=path, SheetName="Sheet4")
print(totalrows, totalcol)

for row in range(2, totalrows+1):
    for col in range(1, totalcol+1):
        print(XL_Utils.get_cellData(filename=path,SheetName="Sheet4",row=row, col=col), end= ' ')
    print()

XL_Utils.set_cellData(path, "Sheet4", 6, 2, "admin120")
    # try:
    #     usr = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    #     passwd = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    # except TimeoutError:
    #     pass
    # usr.send_keys(username)
    # passwd.send_keys(password)
    # btn = driver.find_element(By.TAG_NAME, "button")
    # driver.execute_script("arguments[0].scrollIntoView(true)", btn)
    # btn.click()
    #
    # dashbd = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//h6[normalize-space()='Dashboard']")))
    # assert "Dashboard" in dashbd.text
    # print("In home page")
