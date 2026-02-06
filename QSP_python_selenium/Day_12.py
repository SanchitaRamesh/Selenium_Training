################ 02/01/2026  #####################
import time
from time import sleep

from selenium import webdriver

ch_open = webdriver.ChromeOptions()
ch_open.add_experimental_option("detach", True)
driver = webdriver.Chrome(ch_open)

# driver.get("https://www.amazon.com/")
# time.sleep(3)
# footer_contents = driver.find_elements('xpath','//div[@class="navFooterVerticalRow navAccessibility"]//a')
# for content in footer_contents:
#     print(content.text)
#     #print(content)
# driver.close()

# driver.find_element('xpath' , '//input[@data-action-type="DISMISS"]').click()
# time.sleep(2)
# driver.find_element('xpath' , '(//span[text()="All"])[2]').click()
# time.sleep(2)
# left_menu = driver.find_elements('xpath' , '//div[@id="hmenu-content"]//a')
# for i in left_menu:
#     print(i.text)
# driver.close()

driver.get("https://www.myntra.com")
time.sleep(2)
driver.find_element('xpath' , '//input[@class="desktop-searchBar"]').send_keys('Adidas')
time.sleep(2)
driver.find_element('xpath', '//li[text()="Adidas Originals Shoes"]').click()
time.sleep(2)
about = driver.find_elements('xpath','//ul[@class="results-base"]//h4')
price = driver.find_elements('xpath','//ul[@class="results-base"]//div[@class="product-price"]//span')

for i , j in zip(about,price):
    print(i.text)
    print(j.text)
driver.close()

