import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.flipkart.com/")
driver.maximize_window()

driver.find_element(By.NAME, "q").send_keys("iphone 15")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//ul[@class='_1sFryS _2x2Mmc _3ofZy1']/li[@class='_3D0G9a']")

print(len(results))
length_res = len(results)


if results:
    for res in results:
        print(res.text)
    driver.find_element(By.XPATH, "//ul[@class='_1sFryS _2x2Mmc _3ofZy1']/li[@class='_3D0G9a']["+str(length_res-2)+"]").click()






# for res in results:
#     print(res.text)
#
# with file("file.txt",'a')




    # Input: [1,2,3,[4,5],6,[7,8],9,10]
    # Output:[1,2,3,4,5,6,7,8,9,10]

    # arr = [1, 2, 3, [4, 5], 6, [7, 8], 9, 10]
    # a = []
    #
    # print(type(arr[0]))
    #
    # for i in range(len(arr)):
    #     if type(arr[i]) is int:
    #         a.append(arr[i])
    #     else:
    #         for j in arr[i]:
    #             a.append(j)
    #
    # print(a)
