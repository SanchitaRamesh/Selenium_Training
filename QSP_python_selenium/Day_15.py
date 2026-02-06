##################### 09/01/2026 ######################
import time
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ch_open = webdriver.ChromeOptions()
ch_open.add_experimental_option('detach',True)
driver = webdriver.Chrome(ch_open)

wait = WebDriverWait(driver, 50)

# driver.get("https://www.saucedemo.com/")
# driver.find_element('id',"user-name").send_keys("standard_user")
# driver.find_element('id','password').send_keys("secret_sauce")
# driver.find_element('id','login-button').click()
# time.sleep(5)
# try:
#     wait.until(EC.visibility_of_element_located(('xpath','//span[text()="Products"]')))
#     print("login was successful")
# except:
#     print("login was not successful")
# driver.close()
#####################################################3
# try:
#     wait.until(EC.url_contains("inventory"))
#     print("login was successful")
# except:
#     print("login was not successful")
# driver.close()
######################################################
# try:
#     wait.until(EC.visibility_of_element_located(('xpath','//div[contains(text(),"Swag Labs")]')))
#     print("login was successful")
# except:
#     print("login was not successful")
# driver.close()
######################################################
# try:
#     wait.until(EC.visibility_of_element_located(('xpath','//button[contains(text(),"Open Menu")]')))
#     print("login was successful")
# except:
#     print("login was not successful")
# driver.close()
######################################################
# try:
#     wait.until(EC.visibility_of_element_located(('xpath','//option[contains(text(),"Name (A to Z)")]/..')))
#     print("login was successful")
# except:
#     print("login was not successful")
# driver.close()
#####################################################
# try:
#     wait.until(EC.visibility_of_element_located(('xpath','//button[text()="Add to cart"]')))
#     print("login was successful")
# except:
#     print("login was not successful")
# driver.close()
############################################################
############################################################

driver.get("file:///C:/Users/User/Downloads/progressbar.html")
time.sleep(2)
driver.find_element('xpath','//button[text()="Click Me"]').click()
try:
    wait.until(EC.visibility_of_element_located(('xpath','//div[text()="100%"]')))
    driver.find_element('xpath','//button[text()="Click Me"]').click()
    print("successful")
except:
    print("ERROR!!!!!")
#print("successful")
# driver.close()