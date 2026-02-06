####################### 26/12/2025 ################
import time
from selenium import webdriver

ch_open = webdriver.ChromeOptions()
ch_open.add_experimental_option("detach",True)
driver = webdriver.Chrome(ch_open)

# driver.get('https://www.myntra.com/')
# time.sleep(2)

# driver.find_element('css selector' , 'a[data-group="men"]').click()
# time.sleep(2)
#
# driver.find_element('css selector' , 'a[data-group="women"]').click()
# time.sleep(2)
#
# driver.find_element('css selector' , 'class="desktop-userTitle"').click()
# time.sleep(2)
#
# driver.close()

driver.get('https://www.macys.com/')
time.sleep(2)

driver.find_element('xpath', 'html/body/div/div/header/div/div[3]/div/div/a').click()
time.sleep(2)

driver.find_element('xpath' , 'html/body/div[2]/div/div[6]/div/div/form/div[3]/div/div/input').send_keys('sanchita2415kaviya@gmail.com')
time.sleep(2)
driver.find_element('xpath' ,'html/body/div[2]/div/div[6]/div/div/form/div[3]/div[2]/div[1]/input').send_keys('JeonSanchita0124')
time.sleep(2)
# driver.find_element('xpath','html/body/div[2]/div/div[6]/div/div/form/div[3]/div[2]/div[1]/div/button').click()
# time.sleep(2)
driver.find_element('xpath' , 'html/body/div[2]/div/div[6]/div/div/form/button').click()
time.sleep(10)
driver.find_element('xpath' , 'html/body/div/div/header/nav/ul/li[2]').click()
time.sleep(2)
driver.find_element('xpath' , 'html/body/div/div/header/nav/ul/li[7]').click()
time.sleep(2)
driver.find_element('xpath', 'html/body/div/div/header/nav/ul/li[1]').click()
time.sleep(2)
driver.find_element('xpath', 'html/body/div/div/header/nav/ul/li[1]/button/span[2]').click()
time.sleep(2)
driver.find_element('xpath' , 'html/body/div/div/header/nav/div[15]/nav/div/div/div/div/div/section/ul/li[2]/a/span').click()
time.sleep(2)
driver.find_element('xpath', 'html/body/div[2]/div/header/div/div[3]/button/span').click()
time.sleep(2)
driver.find_element('xpath' , 'html/body/div/dialog[2]/div[2]/div/div/div/ul/li[1]/a').click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.find_element('xpath', 'html/body/div[2]/div/header/div/div[3]/button/span').click()
time.sleep(2)
driver.find_element('xpath' , 'html/body/div/dialog[2]/div[2]/div/div/div/ul/li[8]/a').click()
time.sleep(2)
driver.close()