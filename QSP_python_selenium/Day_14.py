########################### 08/01/2026 ######################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ch_open = webdriver.ChromeOptions()
ch_open.add_experimental_option("detach", True)
driver = webdriver.Chrome(ch_open)

# driver.get(r'C:\Users\User\PycharmProjects\Selenium_Training\html_files\loading.html')
# time.sleep(3) # ElementNotInteractableException: Message: element not interactable
#
# '''
# 1. we get this exception when the element is present but not loaded yet.
# 2. selenium is trying to find the element even before the app is loaded.
# 3. time.sleep(10) wworks fine. everytime the app loading time cannot be guessed.
# 4. this is overcome in next concept ( implicite wait and explicite wait )'''
#
# driver.find_element("name", "fname").send_keys("Sanchita")
# time.sleep(1)
# driver.find_element("name", "lname").send_keys("Ramesh")
# driver.close()

###############################################################

# driver.implicitly_wait(10)
# '''
# 1. selenium implicitly/ automatically waits for 30 sec, for the page/ app to load.
# 2. if the page is loaded & webelement is detected by selenium within 10 seconds,the implicite wait stalls the wait time
#     and proceeds with the next step of testing.
# 3. here the implicit wait does not wait for the entire 30 seconds or the time we mention, to go to the next step
#     of locating other bweb elements.
# 4. we just have to mention implicite wait once. no need to reuse like time.sleep()
# 5. 30 seconds in max The default loading/ detecting time for webelement using (find_element,find_elements,any 8 loactors)
#     we can give more than 30, but even after 30 sec selenium didnt locate the webelement, we will get error/exception.
# '''
#
# driver.get(r'C:\Users\User\PycharmProjects\Selenium_Training\html_files\loading.html')
# driver.find_element("name", "fname").send_keys("Sanchita")
# time.sleep(1)
# driver.find_element("name", "lname").send_keys("Ramesh")
# driver.close()

###############################################################
wait = WebDriverWait(driver, 30)
'''
1. syncs the loading time of browser, app , web page etc
'''
driver.get(r'C:\Users\User\PycharmProjects\Selenium_Training\html_files\loading.html')
wait.until(EC.visibility_of_element_located(("xpath", '//div[contains(text(), "FirstName")]')))
'''
1. waits until this web element is loacted post loading
'''
driver.find_element("name", "fname").send_keys("Sanchita")
time.sleep(1)
driver.find_element("name", "lname").send_keys("Ramesh")
driver.close()