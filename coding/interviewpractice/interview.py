# arr [1,2,3,4,5,6,7,8,9,10]
#  if n=3, output_list = [3,6,9]
#  if n=4, output = [4,8]

arr = [1,2,3,4,5,6,7,8,9,10]
n = 4
l=[]

for i in range(1,len(arr)):
    if i % n ==0:
        l.append(i)

print(l)


# --------------------------ALTEMETRIC

# https://www.linkedin.com/home
# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.implicitly_wait(10)
#
# driver.get("https://www.linkedin.com/home")
# driver.maximize_window()
#
# driver.find_element(By.LINK_TEXT, "Sign in with email").click()
# time.sleep(2)
#
# #
# # driver.execute_script("argument[0].scrolIntoView();", element)
#
#
# # ----------------------------
#
# string = 'dasara festival'
#
# ch = 'as'
#
# count = 0
#
# s= ''
# # for i in string:
# #     if i == ch[0] and i == ch[1]:
# #
# # for i in range(len(string)-1):
# #     if len(ch) ==1:
# #     if string[i]+string[i+1] == ch:
# #         count+=1
#
#
#
# print(count)
