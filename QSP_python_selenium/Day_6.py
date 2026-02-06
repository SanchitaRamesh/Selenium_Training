############################## 19/12/2025 #################
import time
from selenium import webdriver

c_open = webdriver.ChromeOptions()
c_open.add_experimental_option("detach",True)

driver=webdriver.Chrome(c_open)

# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# # username = driver.find_element("id" , "idToken1")
# # password = driver.find_element("id" , "idToken2")
# # print(username)  # prints address of that web element
# # print(password)  # prints address of that web element
#
# # username.send_keys("standard_user")
# # password.send_keys("secret_sauce")
#
# # though correct ,in the above process, it is not advisable to store the data in a variable each and every user.
# # hence we follow the below
#
# driver.find_element("id" , "name").send_keys("Sanchita")
# time.sleep(2)
# driver.find_element("id" , "email").send_keys("sanrashi@gmail.com")
# time.sleep(2)
# driver.find_element("id" , "phone").send_keys("1234567891")
# time.sleep(2)
# driver.find_element("id" , "textarea").send_keys("007,Samsung City,Hannamdong,seoul,South Korea")
# time.sleep(2)
# driver.find_element("id" , "female").click()
# time.sleep(2)
# driver.find_element("id" , "friday").click()
# time.sleep(3)
# driver.close()

#-------------------------------------------------------------------------------------------------------------------

driver.get("https://www.saucedemo.com/")
time.sleep(2)

driver.find_element("id","user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element("id","password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element("id","login-button").click()
time.sleep(5)
driver.find_element("id","add-to-cart-sauce-labs-fleece-jacket").click()
time.sleep(2)
driver.find_element("id","add-to-cart-sauce-labs-bolt-t-shirt").click()
time.sleep(2)
driver.find_element("id","add-to-cart-test.allthethings()-t-shirt-(red)").click()
time.sleep(2)
driver.find_element("id","add-to-cart-sauce-labs-backpack").click()
time.sleep(2)
driver.find_element("class name","shopping_cart_link").click()
time.sleep(2)
driver.find_element("id","remove-sauce-labs-backpack").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.find_element("id","add-to-cart-sauce-labs-onesie").click()
time.sleep(4)
driver.find_element("class name","shopping_cart_link").click()
time.sleep(2)
driver.find_element("id","checkout").click()
time.sleep(2)
# driver.find_element("id","cancel").click()
# time.sleep(2)
# driver.find_element("class name","shopping_cart_link").click()
# time.sleep(2)
# driver.find_element("id","checkout").click()
# time.sleep(2)
driver.find_element("id","first-name").send_keys("Jeon")
time.sleep(2)
driver.find_element("id","last-name").send_keys("Jungkook")
time.sleep(2)
driver.find_element("id","postal-code").send_keys("560070")
time.sleep(2)
driver.find_element("id","continue").click()
time.sleep(2)
driver.find_element("id","finish").click()
time.sleep(2)
driver.find_element("id","back-to-products").click()
time.sleep(2)
driver.find_element("id","react-burger-menu-btn").click()
time.sleep(3)
driver.find_element("id","logout_sidebar_link").click()
time.sleep(3)
driver.close()