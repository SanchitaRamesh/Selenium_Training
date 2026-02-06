##################### 14/01/2026 #################3
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

ch_open = webdriver.ChromeOptions()
ch_open.add_experimental_option("detach",True)
driver = webdriver.Chrome(ch_open)

mouse_operations = ActionChains(driver)

driver.get("https://www.myntra.com")

parent_window=driver.current_window_handle

home = driver.find_element('xpath',"//a[text()='Home'][1]").click()
mouse_operations.move_to_element(home).perform()
time.sleep(2)

driver.find_element('xpath', '//a[text()="Festive Decor"]').click()
time.sleep(2)

driver.find_element('xpath', '//h4[@class="product-product"]').click()      ## opens in a new tab
time.sleep(2)

handles = driver.window_handles
print(handles)      ## [parent_handle, child_handle]

for handle in handles:
    driver.switch_to.window(handle)     ## switching the driver to new tab/window
    if 'nestasia' in driver.current_url:
        driver.find_element('xpath', '//div[text()="ADD TO BAG"]').click()
        time.sleep(2)

## switching back to the parent_window
driver.switch_to.window(parent_window)
time.sleep(2)

## clicking on another element
driver.find_element('xpath', '(//h4[@class="product-product"])[2]').click()     ## opens in new tab

## initialize window_handles
handles2 = driver.window_handles
print(handles2)         ## [parent_handle, child_handle, child2]

for handle in handles2:
    driver.switch_to.window(handle)
    if 'backdropon' in driver.current_url:
        driver.find_element('xpath', '//div[text()="ADD TO BAG"]').click()


