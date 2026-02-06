################################# 12/01/2026 ###########################
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ch_open = webdriver.ChromeOptions()
ch_open.add_experimental_option("detach",True)
driver = webdriver.Chrome(ch_open)

# driver.get("https://testautomationpractice.blogspot.com/")
#
# driver.find_element('xpath','//button[text()="Confirmation Alert"]').click()
# alert_ = driver.switch_to.alert
# time.sleep(2)
# alert_.accept()
# time.sleep(3)
#
# driver.find_element('xpath','//button[text()="Confirmation Alert"]').click()
# time.sleep(2)
# alert_.dismiss()
# time.sleep(3)
#
# driver.find_element('xpath','//button[text()="Prompt Alert"]').click()
# time.sleep(2)
# alert_.send_keys("Jeon Sanchita Ramesh")
# alert_.accept()
# time.sleep(3)
# driver.close()
######################################################################################

# driver.get("https://testautomationpractice.blogspot.com/")
# driver.find_element('xpath','//button[text()="Confirmation Alert"]').click()
# def alerts(user_inp):
#     alert = driver.switch_to.alert
#     if user_inp=='accept':
#         alert.accept()
#     elif user_inp=='dismiss':
#         alert.dismiss()
# alerts("accept")
# time.sleep(5)
# driver.find_element('xpath','//button[text()="Confirmation Alert"]').click()
# alerts("dismiss")
# time.sleep(5)
# driver.close()

#######################################################################################

driver.get("https://testautomationpractice.blogspot.com/")
# path=(r'C:\Users\User\PycharmProjects\Selenium_Training\html_files\demo.html')
# driver.find_element('id', 'singleFileInput').send_keys(path)
# time.sleep(8)
# driver.close()

path_1 =(r"C:\Users\User\PycharmProjects\Selenium_Training\html_files\demo.html")
path_2 =(r"C:\Users\User\PycharmProjects\Selenium_Training\html_files\loading.html")
driver.find_element('id', 'multipleFilesInput').send_keys(f'{path_1}\n {path_2}')
time.sleep(8)
driver.close()