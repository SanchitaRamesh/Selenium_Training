import time
from selenium import webdriver

ch_open = webdriver.ChromeOptions()
ch_open.add_experimental_option("detach", True)
driver = webdriver.Chrome(ch_open)


#Q1 wap to print the shoe name and shoe price of adidas original shoes in myntra
# driver.get("https://www.myntra.com/")
# time.sleep(2)
# driver.find_element('xpath' , '//input[@class="desktop-searchBar"]').send_keys('Adidas')
# time.sleep(2)
# driver.find_element('xpath', '//li[text()="Adidas Originals Shoes"]').click()
# product_varient = driver.find_elements('xpath','//ul[@class="results-base"]//h4')
# product_price = driver.find_elements('xpath','//ul[@class="results-base"]//div[@class="product-price"]//span')
# time.sleep(2)
# for i,j in zip(product_varient,product_price):
#     print(i.text)
#     print(j.text)
# driver.close()

#Q2 wap to print the colors available for adidas original shoes in https://www.myntra.com/
# driver.get("https://www.myntra.com/")
# time.sleep(2)
# driver.find_element('xpath' , '//input[@class="desktop-searchBar"]').send_keys('Adidas')
# time.sleep(2)
# driver.find_element('xpath', '//li[text()="Adidas Originals Shoes"]').click()
# time.sleep(2)
# driver.find_element('xpath','//div[@class="colour-more"]//span').click()
# time.sleep(2)
# colors = driver.find_elements('xpath', '//div[@class="vertical-filters-filters"][2]/ul//li')
# time.sleep(2)
# for i in colors:
#     print(i.text)
#     time.sleep(1)
# driver.close()

#Q3 wap to print the menu items of the items available in domino's pizza in https://www.zomato.com/bangalore/delivery
# driver.get("https://www.zomato.com/bangalore/restaurants")
# time.sleep(2)
# driver.find_element('xpath','//input[@class="sc-dBfaGr dyyfrm"]').send_keys("california")
# time.sleep(2)
# driver.find_element('xpath', '//p[text()="California Burrito"]').click()
# time.sleep(3)
# driver.find_element('xpath','//a[text()="Order Online"]').click()
# time.sleep(2)
# menu = driver.find_elements('xpath','//section[@class="sc-bZVNgQ iGYweR"]//div[2]//h4')
# for i in menu:
#     print(i.text)
#     time.sleep(1)
# driver.close()

#Q4 wap to fetch all the recommended movies in https://in.bookmyshow.com/
driver.get("https://in.bookmyshow.com/")
time.sleep(2)
driver.find_element('xpath','(//ul[@class="sc-p6ayv6-1 gOMCrp"]//p)[3]').click()
time.sleep(10)
driver.find_element('xpath','//div[text()="See All ›"]').click()
time.sleep(2)
recommendations = driver.find_elements('xpath','//div[@class="sc-7o7nez-0 elfplV"]')
time.sleep(10)
# driver.find_element('xpath','//div[@class="sc-lnhrs7-9 djvlvn"]').click()
# time.sleep(10)
# more_recommendations = driver.find_elements('xpath','//div[@class="sc-lnhrs7-1 jTlXHB"]//div[@class="sc-7o7nez-0 lkwOqB"]')
# time.sleep(10)
# for j in more_recommendations:
#     print(j.text)
#     time.sleep(10)
for i in recommendations:
     print(i.text)
     time.sleep(10)
driver.close()
#//div[@class="sc-lnhrs7-9 djvlvn"]