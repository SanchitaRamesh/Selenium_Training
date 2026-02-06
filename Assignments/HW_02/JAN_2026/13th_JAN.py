 import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

ch_open = webdriver.ChromeOptions()
ch_open.add_experimental_option("detach",True)
driver = webdriver.Chrome(ch_open)

mouse_action = ActionChains(driver)

'''
1. loads fb page >> waits for 2 seconds >> enters data for first name >> waits for 1 second
2. clicks tab button >> waits for 1 seconds >> control moves to last name text box >> enters last name >> waits for 2 seconds
3. performs 2 back space actions one after the another >> waits for 2 seconds between both operations
'''
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@name="firstname"]').send_keys('Harry')
# time.sleep(1)
#
# mouse_action.send_keys(Keys.TAB).perform()
# time.sleep(1)
# mouse_action.send_keys('Potter').perform()
# time.sleep(2)
#
# mouse_action.send_keys(Keys.BACKSPACE).perform()
# time.sleep(2)
# mouse_action.send_keys(Keys.BACKSPACE).perform()

#driver.close()

'''
1. loads fb page >> waits for 2 seconds >> locate firstname & lastname elements in the web page
2. enters data for first name >> waits for 2 seconds >> performs ctrl+a ( select all ) in the firstname text box
3. control moves to last name text box >> performs ctrl+v ( paste )
'''
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# fname = driver.find_element('xpath', '//input[@name="firstname"]')
# lname = driver.find_element('xpath', '//input[@name="lastname"]')
#
# fname.send_keys('Harry')
# time.sleep(2)
#
# fname.send_keys(Keys.CONTROL + 'a')         ## select the data
# fname.send_keys(Keys.CONTROL + 'c')         ## copy the data
#
# mouse_action.send_keys(Keys.TAB).perform()        ## switching the control to last name
# lname.send_keys(Keys.CONTROL + 'v')         ## paste the data

'''
1. loads testautomationpractice page >> waits for 2 seconds
2. performs ctrl+a ( select all )
3. entire page gets selected ( from top to bottom ? ) >> performs control key operation
'''
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# mouse_action.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()

'''
1. loads testautomationpractice page >> waits for 2 seconds
2. locates the web element with attributes id="name" >> waits for 2 seconds
3. enters the data for name element 
'''
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# driver.find_element('xpath', '//input[@id="name"]').send_keys('Harry Potter')
# time.sleep(2)
# mouse_action.key_down(Keys.CONTROL).send_keys(Keys.BACKSPACE).key_up(Keys.CONTROL).perform()

'''
1. loads testautomationpractice page >> waits for 2 seconds
2. locates the web element with attributes id="name" >> waits for 2 seconds
3. performs shift+a ( results in entering/appending upper case A to the already existing data )
'''
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# driver.find_element('xpath', '//input[@id="name"]').send_keys('harry')
# time.sleep(2)
# mouse_action.key_down(Keys.SHIFT).send_keys('a').perform()

'''
1. loads testautomationpractice page >> waits for 2 seconds
2. locates the web element with attributes id="name" >> enters data for the name element >> waits for 2 seconds
3. performs tab operation >> directly enters data in the where the control is currently present(not checking for webelemnts)
   >> waits for 2 seconds
'''
driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)
driver.find_element('xpath', '//input[@id="name"]').send_keys('Harry Potter')
time.sleep(2)
mouse_action.send_keys(Keys.TAB).perform()
time.sleep(2)
mouse_action.send_keys('harry@gmail.com').perform()