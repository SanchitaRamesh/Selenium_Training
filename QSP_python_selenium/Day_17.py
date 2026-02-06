###############################3 13/01/2026 ##############################
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

ch_open = webdriver.ChromeOptions()
ch_open.add_experimental_option("detach",True)
driver = webdriver.Chrome(ch_open)

#driver.get("https://testautomationpractice.blogspot.com/")

mouse_action = ActionChains(driver)

# hover = driver.find_element("xpath",'//button[text()="Confirmation Alert"]')
# mouse_action.click(hover).perform()
# time.sleep(3)
# driver.close()

# double_cl = driver.find_element("xpath",'//label[text()="Name:"]')
# mouse_action.double_click(double_cl).perform()
# time.sleep(5)
# driver.close()

# right_click = driver.find_element('xpath', '//h2[text()="Tabs"]')
# mouse_action.context_click(right_click).perform()
# time.sleep(5)
# driver.close()

''' python code ( used only for vertical scrolling ) '''
# driver.get('https://www.myntra.com/')
# scroll_down = driver.find_element('xpath', '//p[text()=" USEFUL LINKS "]')
# mouse_action.scroll_to_element(scroll_down).perform()
# time.sleep(5)
# driver.close()

''' Java script  ( can be used for both horizontal and veritcal scrolling ) '''
# driver.get('https://www.myntra.com/')
# scroll_down = driver.find_element('xpath', '//p[text()=" USEFUL LINKS "]')
# driver.execute_script("arguments[0].scrollIntoView();", scroll_down)
# time.sleep(5)
# driver.close()

''' scroll till end and back to top of page in one go (operation of end key in keyboard)'''
# driver.get('https://www.myntra.com/')
# ac_obj.send_keys(Keys.END).perform()
# ac_obj.send_keys(Keys.HOME).perform()
# time.sleep(5)
# driver.close()

''' same using java script '''
# driver.get('https://www.myntra.com/')
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
# time.sleep(5)
# driver.close()

''' Scrolling by pixels '''
# driver.get('https://www.myntra.com/')
# driver.execute_script("window.scrollBy(0, 500);")
# driver.execute_script("window.scrollBy(0, -500);")
# time.sleep(5)
# driver.close()

''' drag and drop '''
# driver.get('https://testautomationpractice.blogspot.com/')
# ele = driver.find_element('xpath', '//h2[text()="SVG Elements"]')
# ac_obj.scroll_to_element(ele).perform()
# draggable_ele = driver.find_element('xpath', '//div[@id="draggable"]')
# droppable_ele = driver.find_element('xpath', '//div[@id="droppable"]')
# ac_obj.drag_and_drop(draggable_ele, droppable_ele).perform()
# time.sleep(5)
# driver.close()

''' SLIDER '''
# driver.get('https://testautomationpractice.blogspot.com/')
# ele = driver.find_element('xpath', '//h2[text()="SVG Elements"]')
# ac_obj.scroll_to_element(ele).perform()
# slider = driver.find_element('xpath', '//div[@id="slider-range"]/span[1]')
# ac_obj.click_and_hold(slider).move_by_offset(100, 0).release().perform()
# ac_obj.click_and_hold(slider).move_by_offset(-100, 0).release().perform()
# time.sleep(5)
# driver.close()

