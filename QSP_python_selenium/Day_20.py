########################### 19/01/2026 #################
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

ch_open = webdriver.ChromeOptions()
ch_open.add_experimental_option("detach", True)
driver = webdriver.Chrome(ch_open)

driver.get(r'C:\Users\User\PycharmProjects\Selenium_Training\html_files\demo_.html')
time.sleep(2)

cars = driver.find_element('xpath', '//select[@id="standard_cars"]')
#select_obj = Select(cars)

## select_by_index
# select_obj.select_by_index(6)
# time.sleep(2)
# select_obj.select_by_index(3)
# time.sleep(2)
# select_obj.select_by_index(9)
# time.sleep(2)
#select_obj.select_by_index(100)     ## NoSuchElementException: Message: Could not locate element with index 100

##------------------------------------------------------------

# ## select_by_value
# select_obj.select_by_value('bmw')
# time.sleep(2)
# select_obj.select_by_value('jgr')
# time.sleep(2)
# select_obj.select_by_value('toy')

##------------------------------------------------------------

# ## select_by_visible_text
# select_obj.select_by_visible_text("Honda")
# time.sleep(2)
# select_obj.select_by_visible_text("Mercedes")
# time.sleep(2)
# select_obj.select_by_visible_text("Volvo")

########################################################################################################

'''     Multi-select listbox        '''

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\User\PycharmProjects\Selenium_Training\html_files\demo_.html')
# time.sleep(2)
#
# listbox = driver.find_element('xpath', '//select[@id="multiple_cars"]')
# select_obj = Select(listbox)

##------------------------------------------------------------------------------

## select_by_index
# select_obj.select_by_index(3)
# time.sleep(1)
# select_obj.select_by_index(4)
# time.sleep(1)
# select_obj.select_by_index(5)
# time.sleep(3)
# #
# # ## deselect_by_index
# select_obj.deselect_by_index(4)
# time.sleep(1)
# select_obj.deselect_by_index(3)
# time.sleep(1)
# select_obj.deselect_by_index(5)
# time.sleep(1)
# select_obj.deselect_by_index(6)

##------------------------------------------------------------------------------

# ## select_by_value
# select_obj.select_by_value("jgr")
# time.sleep(1)
# select_obj.select_by_value("merc")
# time.sleep(1)
# select_obj.select_by_value("nin")
# time.sleep(2)
#
# ## deselect_by_value
# select_obj.deselect_by_value('jgr')
# time.sleep(1)
# select_obj.deselect_by_value('nin')
# time.sleep(1)
# select_obj.deselect_by_value('merc')

##------------------------------------------------------------------------------

# ## select_by_visible_text
# select_obj.select_by_visible_text("Audi")
# time.sleep(1)
# select_obj.select_by_visible_text("Ford")
# time.sleep(1)
# select_obj.select_by_visible_text("BMW")
# time.sleep(2)
#
# ## deselect_by_visible_text
# select_obj.deselect_by_visible_text('Audi')
# time.sleep(1)
# select_obj.deselect_by_visible_text('Ford')
# time.sleep(1)
# select_obj.deselect_by_visible_text('BMW')


# ########################################################################################################
'''
is_multiple :   It is a property. It will check whether the listbox is multi-select or not
                Return True if it is multi-select listbox else None

                SYNTAX  :   select_obj.is_multiple
'''

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\User\PycharmProjects\Selenium_Training\html_files\demo_.html')
# time.sleep(2)
#
# listbox = driver.find_element('xpath', '//select[@id="multiple_cars"]')
# select_obj = Select(listbox)
# print(select_obj.is_multiple)       ## True
#
#
# cars = driver.find_element('xpath', '//select[@id="standard_cars"]')
# select_cars = Select(cars)
# print(select_cars.is_multiple)      ## None

###############################################################################################

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\User\PycharmProjects\Selenium_Training\html_files\demo_.html')
# time.sleep(2)
#
# listbox = driver.find_element('xpath', '//select[@id="multiple_cars"]')
# select_obj = Select(listbox)
#
# select_obj.select_by_index(8)
# time.sleep(1)
# select_obj.select_by_index(6)
# time.sleep(1)
# select_obj.select_by_index(2)
# time.sleep(1)

##------------------------------------------------------------------------------

'''     To get all the selected items   
all_selected_options    :   It is a property of Selenium’s Select class that returns a list of all currently selected options in a dropdown.
    We use it to, 
        To verify what options are selected.
        To print all selected values.
        To check multi-select dropdown selections.
        To confirm your selection operation worked correctly.
'''

# elements = select_obj.all_selected_options     ## list of web-elements     ## [wb1, wb2, wb3, wb4, wb5,..]
# for ele in elements:
#     print(ele.text)

##------------------------------------------------------------------------------

# # print(select_obj.first_selected_option)     ## web-element
# print(select_obj.first_selected_option.text)

##------------------------------------------------------------------------------

'''     
To deselect all the selected items
deselect_all()  :   It is a method of Selenium’s Select class used to remove all selected options from a multi-select dropdown.      
                    *   Works only for multi-select dropdown
                    *   Clears all selected options
                    *   Does NOT work for normal dropdowns
'''

# select_obj.deselect_all()


###############################################################################################

'''
options     :   options is a property of Selenium’s Select class.
                It returns a list of all option elements inside a <select> dropdown.
                options returns a list of WebElements.
                *   To get all items present in a dropdown
                *   To check dropdown count
'''

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\User\PycharmProjects\Selenium_Training\html_files\demo_.html')
# time.sleep(2)
#
# listbox = driver.find_element('xpath', '//select[@id="multiple_cars"]')
# select_obj = Select(listbox)
#
# all_elements = select_obj.options
# print(all_elements)         ## list of web-elements
#
# for ele in all_elements:
#     print(ele.text)


###############################################################################################

'''     Normal listboxes    '''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.irctc.co.in/nget/train-search')
# time.sleep(2)
# driver.find_element('xpath', '//button[text()="OK"]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//div[@role="button"])[1]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[text()="AC Chair car (CC)"]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//div[@role="button"])[2]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[text()="PREMIUM TATKAL"]').click()