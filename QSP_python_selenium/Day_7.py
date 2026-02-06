########################## 23/12/2025 #################
import time
from selenium import webdriver

ch_open = webdriver.ChromeOptions()
ch_open.add_experimental_option('detach',True)
driver=webdriver.Chrome(ch_open)
driver.get("https://www.kushals.com/")
time.sleep(4)
driver.find_element('partial link text','Bangles').click()
time.sleep(4)
driver.find_element('partial link text','92.5 Silver').click()
time.sleep(3)
driver.close()