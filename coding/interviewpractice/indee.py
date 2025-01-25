import time

from selenium import webdriver
from selenium.common import ElementNotInteractableException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Sign in to the Platform.
driver.get("https://indeedemo-fyc.watch.indee.tv/")
driver.maximize_window()
wait = WebDriverWait(driver, 15)
act = ActionChains(driver)

# attempt = 0
# while attempt < retries:
#     try:
#         element = self.find_element(by_locator)
#         self.scroll_into_view(element)
#         self.wait.until(EC.element_to_be_clickable(by_locator)).click()
#         return
#     except ElementClickInterceptedException:
#         print(f"Element click intercepted, retrying... (Attempt {attempt + 1} of {retries})")
#         time.sleep(1)  # Brief wait before retrying
#         attempt += 1
#     except Exception as e:
#         print(f"An error occurred while clicking the element: {e}")
#         break
# else:
#     raise Exception(f"Failed to click the element after {retries} attempts")

# 3. Switch to the 'Details' Tab:
# details = wait.until(EC.element_to_be_clickable())
# details.click()
# # wait for 5 - 10 seconds.
# time.sleep(5)
# videos = wait.until(EC.element_to_be_clickable((By.ID, "videosSection")))
# videos.click()
# play_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Play Video']")))
# play_btn.click()


# def set_volume(self, vol):
#
#     volume_slider = self.find_element(self.slider_xpath)
#     self.move_to_element(volume_slider)
#
#     # Calculate the offset for the volume slider based on the desired volume
#     slider_width = volume_slider.size['width']
#     volume_level = (vol / 100)
#
#     # Drag the volume slider to the desired volume level
#
#     # self.action.click_and_hold(volume_slider).move_by_offset(volume_level - (slider_width / 2), 0).release().perform()
#     time.sleep(1)  # Optional: wait to see the change on screen
# Set the video volume to 50% using JavaScript
# # driver.execute_script("arguments[0].volume = 0.5;", video)



    # # Allow the video to play for 10 seconds, then pause it.
    # time.sleep(10)
    # #
    # driver.switch_to.frame('video_player')
    # # ActionChains(driver).move_to_element(controlBar).perform()
    #
    # # pause = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='jw-reset jw-button-container']/div[1]")))
    # # driver.execute_script("window.scrollBy(0,100);")
    # # driver.execute_script("arguments[0].scrollIntoView(true)", pause)
    #
    # controlBar = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='jw-reset jw-button-container']")))
    #
    # # # pause.click()
    # # time.sleep(10)

    # # Locate all video element
    # # video = WebDriverWait(driver, 10).until(
    # #     EC.presence_of_all_elements_located((By.TAG_NAME, "video"))
    # # )
    # # driver.execute_script("document.querySelector('video').pause();")
    # #
    # # Wait for the "Continue Watching" dialog to appear and click it if present
    #
    # # driver.switch_to.default_content()
    # # try:
    # #     continue_watching_button = wait.until(
    # #         EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Continue Watching']"))
    # #     )
    # #     continue_watching_button.click()
    # #     print("Clicked 'Continue Watching'.")
    # # except TimeoutException:
    # #     print("No 'Continue Watching' dialog appeared.")
    # # time.sleep(5)
    # #
    # # # 7. Adjust Volume
    # # driver.switch_to.frame('video_player')
    # # volume = driver.find_element(By.XPATH, "//div[@aria-label='Mute button']")
    # # slider = driver.find_element(By.XPATH, "//div[@aria-label='Mute button']//div[@class='jw-knob jw-reset']")
    # # print(slider.location)
    # # # act.move_to_element(volume).move_to_element(slider).click().send_keys("50").perform()
    # # act.move_to_element(volume).drag_and_drop_by_offset(slider,0,50)
    # # print(slider.location)
    #
    # # Set the video volume to 50% using JavaScript
    # # driver.execute_script("arguments[0].volume = 0.5;", video)
    # # # Retrieve and print the volume to confirm
    # # current_volume = driver.execute_script("return arguments[0].volume;", video)
    # # print(f"Current video volume: {current_volume * 100}%")
    # # time.sleep(5)
    #
    # act.move_to_element(controlBar).perform()
    # setting = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Settings']")))
    # # driver.execute_script("arguments[0].scrollIntoView(true)", setting)
    # setting.click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, "//button[normalize-space()='480p']").click()
    #
    # time.sleep(2)
    #
    # # Verify the resolution by checking video width and height properties -480p
    # video = driver.find_element(By.TAG_NAME, "video")
    # video_width = driver.execute_script("return arguments[0].videoWidth;", video)
    # video_height = driver.execute_script("return arguments[0].videoHeight;", video)
    # print(f"Current video resolution: {video_width}x{video_height}")
    #
    # act.move_to_element(controlBar).perform()
    # setting = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Settings']")))
    # setting.click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, "//button[normalize-space()='720p']").click()
    #
    # time.sleep(2)
    # # Verify the resolution by checking video width and height properties-720p
    # video_width = driver.execute_script("return arguments[0].videoWidth;", video)
    # video_height = driver.execute_script("return arguments[0].videoHeight;", video)
    # print(f"after 720 video resolution: {video_width}x{video_height}")
    #
    # # # Verify initial resolution by checking video width and height properties (expected 480p)
    # # video = driver.find_element(By.TAG_NAME, "video")
    # # video_width = driver.execute_script("return arguments[0].videoWidth;", video)
    # # video_height = driver.execute_script("return arguments[0].videoHeight;", video)
    # # print(f"Initial video resolution: {video_width}x{video_height}")
    # #
    # # # Access and click settings using JavaScript to ensure interaction registers
    # # setting = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Settings']")))
    # # driver.execute_script("arguments[0].click();", setting)
    # # time.sleep(2)
    # #
    # # # Click on 720p resolution
    # # resolution_720p = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='720p']")))
    # # driver.execute_script("arguments[0].click();", resolution_720p)
    # # print("Attempted to change resolution to 720p.")
    # # time.sleep(5)  # Allow time for the resolution change to take effect
    # # #
    # # # Verify the resolution change by re-checking video width and height properties (expected 720p)
    # # video_width = driver.execute_script("return arguments[0].videoWidth;", video)
    # # video_height = driver.execute_script("return arguments[0].videoHeight;", video)
    # # print(f"Current video resolution after setting to 720p: {video_width}x{video_height}")
    # #
    # # # Additional validation to ensure it changed to 720p
    # # if video_width == 1280 and video_height == 720:  # 1280x720 is the typical resolution for 720p
    # #     print("Resolution successfully changed to 720p.")
    # # else:
    # #     print("Resolution did not change to 720p as expected.")
    # #
    # #
    #
    # # pause = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='jw-reset jw-button-container']/div[1]")))
    # # pause.click()
    #
    # video = driver.find_element(By.TAG_NAME, 'video')
    # driver.execute_script("document.querySelector('video').pause();")
    #
    # driver.switch_to.default_content()
    # back_btn = wait.until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go Back and continue playing video']")))
    # back_btn.click()
    #
    #


acc_code = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='access-code']")))
acc_code.send_keys("WVMVHWBS")

btn = wait.until(EC.element_to_be_clickable((By.NAME, "signIn")))
btn.click()

# 2. Navigate to the 'Test Automation Project':
All_title = wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='All Titles']")))
if All_title:
    try:
        tst_project = wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[normalize-space()='Test automation project']")))
        tst_project.click()
    except ElementNotInteractableException:
        print("Element not intercatable")



# 3. Switch to the 'Details' Tab:
# details = wait.until(EC.element_to_be_clickable((By.ID, "detailsSection")))
# details.click()
# # wait for 5 - 10 seconds.
# time.sleep(5)

videos = wait.until(EC.element_to_be_clickable((By.ID, "videosSection")))
videos.click()


play_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Play Video']")))
play_btn.click()
# Allow the video to play for 10 seconds, then pause it.
time.sleep(10)
#
# ActionChains(driver).move_to_element(controlBar).perform()

# pause = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='jw-reset jw-button-container']/div[1]")))
# driver.execute_script("window.scrollBy(0,100);")
# driver.execute_script("arguments[0].scrollIntoView(true)", pause)

# Locate all video elements
# videos = WebDriverWait(driver, 10).until(
#     EC.presence_of_all_elements_located((By.TAG_NAME, "video"))
# )
driver.switch_to.frame('video_player')
controlBar = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='jw-reset jw-button-container']")))

# video = driver.find_element(By.TAG_NAME, 'video')
# driver.execute_script("document.querySelector('video').pause();")
#
# # pause.click()
# time.sleep(10)
# Wait for the "Continue Watching" dialog to appear and click it if present

# driver.switch_to.default_content()
# try:
#     continue_watching_button = wait.until(
#         EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Continue Watching']"))
#     )
#     continue_watching_button.click()
#     print("Clicked 'Continue Watching'.")
# except TimeoutException:
#     print("No 'Continue Watching' dialog appeared.")
# time.sleep(5)
#
# # 7. Adjust Volume
# driver.switch_to.frame('video_player')
# volume = driver.find_element(By.XPATH, "//div[@aria-label='Mute button']")
# slider = driver.find_element(By.XPATH, "//div[@aria-label='Mute button']//div[@class='jw-knob jw-reset']")
# print(slider.location)
# # act.move_to_element(volume).move_to_element(slider).click().send_keys("50").perform()
# act.move_to_element(volume).drag_and_drop_by_offset(slider,0,50)
# print(slider.location)

# Set the video volume to 50% using JavaScript
# driver.execute_script("arguments[0].volume = 0.5;", video)
# # Retrieve and print the volume to confirm
# current_volume = driver.execute_script("return arguments[0].volume;", video)
# print(f"Current video volume: {current_volume * 100}%")
# time.sleep(5)

act.move_to_element(controlBar).perform()
setting = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Settings']")))
# driver.execute_script("arguments[0].scrollIntoView(true)", setting)
setting.click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[normalize-space()='480p']").click()

time.sleep(2)

# Verify the resolution by checking video width and height properties -480p
video = driver.find_element(By.TAG_NAME, "video")
video_width = driver.execute_script("return arguments[0].videoWidth;", video)
video_height = driver.execute_script("return arguments[0].videoHeight;", video)
print(f"Current video resolution: {video_width}x{video_height}")

act.move_to_element(controlBar).perform()
setting = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Settings']")))
setting.click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[normalize-space()='720p']").click()

time.sleep(2)
# Verify the resolution by checking video width and height properties-720p
video_width = driver.execute_script("return arguments[0].videoWidth;", video)
video_height = driver.execute_script("return arguments[0].videoHeight;", video)
print(f"after 720 video resolution: {video_width}x{video_height}")

# # Verify initial resolution by checking video width and height properties (expected 480p)
# video = driver.find_element(By.TAG_NAME, "video")
# video_width = driver.execute_script("return arguments[0].videoWidth;", video)
# video_height = driver.execute_script("return arguments[0].videoHeight;", video)
# print(f"Initial video resolution: {video_width}x{video_height}")
#
# # Access and click settings using JavaScript to ensure interaction registers
# setting = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Settings']")))
# driver.execute_script("arguments[0].click();", setting)
# time.sleep(2)
#
# # Click on 720p resolution
# resolution_720p = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='720p']")))
# driver.execute_script("arguments[0].click();", resolution_720p)
# print("Attempted to change resolution to 720p.")
# time.sleep(5)  # Allow time for the resolution change to take effect
# #
# # Verify the resolution change by re-checking video width and height properties (expected 720p)
# video_width = driver.execute_script("return arguments[0].videoWidth;", video)
# video_height = driver.execute_script("return arguments[0].videoHeight;", video)
# print(f"Current video resolution after setting to 720p: {video_width}x{video_height}")
#
# # Additional validation to ensure it changed to 720p
# if video_width == 1280 and video_height == 720:  # 1280x720 is the typical resolution for 720p
#     print("Resolution successfully changed to 720p.")
# else:
#     print("Resolution did not change to 720p as expected.")
#
#

# pause = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='jw-reset jw-button-container']/div[1]")))
# pause.click()

video = driver.find_element(By.TAG_NAME, 'video')
driver.execute_script("document.querySelector('video').pause();")

driver.switch_to.default_content()
back_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go Back and continue playing video']")))
back_btn.click()

time.sleep(10)
#
#
# Logout
logout_btn = wait.until(EC.element_to_be_clickable((By.ID, 'signOutSideBar')))
logout_btn.click()
time.sleep(2)



