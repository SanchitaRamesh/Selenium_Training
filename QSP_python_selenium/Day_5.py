####################### 18/12/2025 ########################
import time

from selenium import webdriver
c_open=webdriver.ChromeOptions()
c_open.add_experimental_option("detach", True)
driver=webdriver.Chrome(c_open)

driver.get("https://www.myntra.com")
time.sleep(2)

driver.maximize_window()
time.sleep(3)

# current_url , name , title are getter methods (property methods).hence we do not call it like current_url() , name() etc.
print(driver.current_url)

print(driver.name)

print(driver.title)

# if path not mentioned, it will by default store in the current directory
# driver.save_screenshot("myntra.png")

# we use raw string (r) to avoid the escape sequences like \n , \t
driver.save_screenshot(r"C:\Users\User\PycharmProjects\Selenium_Training\screenshots\screenshot.png")

driver.close()
#------------------------------------------------
# to inspect:
# 1. right click on the web page >> inspect   OR
# 2. ctrl + shift + i    OR    ( when the right click on the webpage is disabled )
# 3. Fn + F12  ( when the right click on the webpage is disabled )
# 4. click on the left corner arrow >> and navigate to the web element we need to inspect >> click ... we get the tag
#  associated to the selected web element     OR
# 5. directly right click on the element >> inspect

# Note : 1. in HTML we have two types of tag, a tag that also has a closing tag , and tags that does notbhave a closing tag
#           <a> </a>    and <input> which does not have a closing tag
# 2. every tags will have attributes , text etc
# 3. atrributes contain attribute name and attribute value ( attribute name="attribute value")
# 4. any text that is between open tag and close tag is called text

# to aceess the web elements , we make use to web element methods - find_element and find_elements(used in complex case)
#   driver.find_element("locator name", "locator value")
#
#   we have 8 locators in python-selenium:  these will be used in place of locator name in the find_element()
#     1. id
#     2. name
#     3. class name
#     4. tag name
#     5. link text
#     6. partial link text
#     7. css selector
#     8. xpath