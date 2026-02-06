######################### 16/01/2026 ######################3
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

ch_open = webdriver.ChromeOptions()
ch_open.add_experimental_option("detach", True)
driver = webdriver.Chrome(ch_open)

mouse_action = ActionChains(driver)
window_navigation = driver.current_window_handle

driver.get("https://www.linkedin.com")
time.sleep(2)

g_login = driver.find_element("xpath","//iframe[@title='Sign in with Google Button']")
driver.switch_to.frame(g_login)
time.sleep(2)

driver.switch_to.parent_frame()
time.sleep(2)

find_near_ele = driver.find_element("xpath","//h2[contains(text(),'Join your colleagues, classmates, and friends on LinkedIn')]")
mouse_action.scroll_to_element(find_near_ele)
time.sleep(2)

click_youtube = driver.find_element("xpath","//iframe[@title='Gayatri Iyer: In it to chase my dream | #InItTogether']")
driver.switch_to.frame(click_youtube)
time.sleep(2)

driver.find_element("xpath","//button[@title='Play']").click()
driver.switch_to.parent_frame()

driver.close()