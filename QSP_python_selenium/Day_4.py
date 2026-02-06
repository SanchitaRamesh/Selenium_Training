############################# 17/12/2025 ###########################
import time
from selenium import webdriver
# c_driver = webdriver.Chrome()
# time.sleep(5)

# e_driver = webdriver.Edge()
# time.sleep(5)

# f_driver = webdriver.Firefox()
# time.sleep(5)

# c_stay_opened = webdriver.ChromeOptions()
# c_stay_opened.add_experimental_option("detach", True)
# c_driver = webdriver.Chrome(c_stay_opened)

# e_stay_opened = webdriver.EdgeOptions()
# e_stay_opened.add_experimental_option("detach", True)
# e_driver = webdriver.Edge(e_stay_opened)

#### Firefox does not close automatically, hence there is no need to use FirefoxOptions() #######

c_stay_opened = webdriver.ChromeOptions()
c_stay_opened.add_experimental_option("detach", True)
driver=webdriver.Chrome(c_stay_opened)

driver.get("https://www.google.com")
time.sleep(2)
driver.get("https://www.instagram.com/accounts/login/?hl=en")
time.sleep(3)

driver.maximize_window()
time.sleep(3)

# driver.minimize_window()
# time.sleep(3)

driver.back()
time.sleep(3)

driver.forward()
time.sleep(3)

driver.refresh()
time.sleep(2)

driver.close()