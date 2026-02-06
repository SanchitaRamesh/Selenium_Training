######################## 29/12/2025 ###################
import time
from selenium import webdriver

ch_open = webdriver.ChromeOptions()
ch_open.add_experimental_option('detach', True)

driver = webdriver.Chrome(ch_open)

driver.get("https://www.jiomart.com/?tab=groceries")
time.sleep(2)
driver.find_element('xpath','//button[text()="Enable Location"]').click()
time.sleep(2)
# driver.find_element('xpath','//button[text()="Select Location"]').click()
# driver.find_element("xpath",'//input[@enterkeyhint="search"]').send_keys("paneer")
# time.sleep(2)