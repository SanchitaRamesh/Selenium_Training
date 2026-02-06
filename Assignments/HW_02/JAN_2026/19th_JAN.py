import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

ch_open = webdriver.ChromeOptions()
ch_open.add_experimental_option("detach", True)
driver = webdriver.Chrome(ch_open)


# Q1 Go to https://www.facebook.com/r.php?entry_point=login, select date, month and year
#
# driver.get("https://www.facebook.com/r.php?entry_point=login")
# time.sleep(2)
#
# day = driver.find_element("xpath", "//select[@id='day']")
# drop_box_day = Select(day)
# time.sleep(2)
# drop_box_day.select_by_value("24")
# time.sleep(2)
#
# month = driver.find_element("xpath", "//select[@id='month']")
# drop_box_month = Select(month)
# drop_box_month.select_by_index(4)
# time.sleep(2)
#
# year = driver.find_element("xpath", "//select[@id='year']")
# drop_box_year = Select(year)
# drop_box_year.select_by_value("1998")
# time.sleep(2)
# driver.close()

# Q2 Go to demo.html, select all the elements from the single-select listbox

# driver.get(r"C:\Users\User\PycharmProjects\Selenium_Training\html_files\demo_.html")
# time.sleep(2)
# single_drop_box = driver.find_element("xpath", "//select[@id='standard_cars']")
# select_all = Select(single_drop_box)
# time.sleep(2)
#
# all_options = select_all.options
#
# for option in all_options:
#     option_text_form = option.text
#     select_all.select_by_visible_text(option_text_form)
#     print(option_text_form)
#     time.sleep(2)
# driver.close()

# Q3 Go to demo.html, select all the checkboxes using find_elements
# driver.get(r"C:\Users\User\PycharmProjects\Selenium_Training\html_files\demo_.html")
# time.sleep(2)
#check_boxes = driver.find_elements("xpath", "//input[@type='checkbox']")
# for all in check_boxes:
#     all.click()
#     time.sleep(2)
# driver.close()

# OR

# check_boxes = driver.find_elements("xpath", "//table[@name='selenium']//input[@type='checkbox']")
# for box in check_boxes:
#     box.click()
#     time.sleep(1)
# driver.quit()

# Q4 Go to https://www.irctc.co.in/nget/train-search, handle the calender

# driver.get("https://www.irctc.co.in/nget/train-search")
# wait = WebDriverWait(driver, 10)
# try:
#     wait.until(EC.element_to_be_clickable(("xpath", "//button[@type = 'submit'][1]"))).click()
# except:
#     pass
#
# driver.find_element("xpath","//p-calendar[@id='jDate']").click()
# def j_date(month,date):
#     while True:
#         try:
#             find_month = driver.find_element("xpath","//span[text()='January']")
#             find_year = driver.find_element("xpath","//span[text()='2026']")
#             # find_month=find_month.text
#             # find_year=find_year.text
#             # print(type(find_month))
#             # print(type(find_year))
#             # month_year = find_month+""+find_year


#             month_display = f"{find_month} {find_year}"
#
#             if month_display == month:
#                 date_xpath = f"//table[contains(@class,'ui-datepicker-calendar')]//a[text()='{date}']"
#                 driver.find_element("xpath", date_xpath)
#
#                 print(f"Successfully selected {date} {month_display}")
#                 break
#
#             # if month==month_year:
#             #     find_date = driver.find_element("xpath",f"//span[text()='{month}']/../../..//span[text()='{date}']").click()
#             #     break
#         except:
#             next_button = wait.until(EC.element_to_be_clickable(("xpath", "//a[contains(@class,'ui-datepicker-next')]")))
#             next_button.click()
# j_date("January 2026","21")
# time.sleep(3)
# driver.close()

######################################################3
# driver.get("https://www.irctc.co.in/nget/train-search")
# wait = WebDriverWait(driver, 10)
# try:
#     wait.until(EC.element_to_be_clickable(("xpath", "//button[@type = 'submit'][1]"))).click()
# except:
#     pass
# find_month = driver.find_element("xpath","//span[text()='May']")
# find_year = driver.find_element("xpath","//span[text()='2026']")
# find_month=find_month.text
# find_year=find_year.text
# print(type(find_month))
# print(type(find_year))

# Q5 Go to https://www.abhibus.com/, select the departure date

driver.get("https://www.abhibus.com/")
wait = WebDriverWait(driver, 5)

driver.find_element("xpath","//span[text()='Flights']").click()
time.sleep(3)
driver.find_element("xpath","//button[text()='Round Trip']").click()
time.sleep(3)
driver.find_element("xpath","(//input[@class='outline-none w-full bg-transparent placeholder:text-disabled pt-3 focus:caret-selection text-primary placeholder:opacity-0 focus:placeholder:opacity-100 font-medium text-lg !pt-5'])[1]").send_keys("Bengaluru")
time.sleep(3)
driver.find_element("xpath","(//input[@class='outline-none w-full bg-transparent placeholder:text-disabled pt-3 focus:caret-selection text-primary placeholder:opacity-0 focus:placeholder:opacity-100 font-medium text-lg !pt-5'])[1]").send_keys("California")
time.sleep(3)
driver.find_element("xpath","//p[@data-testid='departureDate']").click()
time.sleep(3)

def departure_date(month,day):
    while True:
        if month == "April 2026":
            driver.find_element("xpath",f"//span[text()='{day}']").clear()
            break
        else:
            driver.find_element("xpath","//button[@type='button'][3]").click()

departure_date("April 2026",2)