#################### 20/01/2026 ###################
#in cmd prompt : C:\Users\User>pip install openpyxl
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
# from openpyxl import Workbook
# workbook = Workbook()
# worksheet = workbook.active
# worksheet.title = "Critical_information"
# worksheet.cell['A1'] = "Sl.No"
# worksheet.cell['A2'] = "First Name"
# worksheet.cell['A3'] = "Last Name"
# worksheet.cell['A4'] = "Address"
# worksheet.cell['A5'] = "City"
#################################################
# data_list =[['Name','Age','Birth place','Status','Residing City','Spouse Name','Children','name'],
#     ['Jeon Jungkook','31','Busan','Married','Seoul','Sanchita Ramesh','1','Jeon Sara'],
#     ['Sanchita Ramesh','30','Bengaluru','Married','Seoul','Jeon Jungkook','1','Jeon Sara'],
#     ['Jeon Sara','1','Seoul','Unmarried','Seoul','N/A','N/A','N/A']
# ]
#
# for data in data_list:
#     worksheet.append(data)
# workbook.save('Family_card.xlsx')
#
# workbook.save(r'C:\Users\User\PycharmProjects\Selenium_Training\Excel_Files\Family_Survey.xlsx')

ch_open = webdriver.ChromeOptions()
ch_open.add_experimental_option("detach", True)
driver = webdriver.Chrome(ch_open)

driver.get("https://testautomationpractice.blogspot.com/")

#//table[@name="BookTable"]//tr[2]//td[1]

# for j in range(2,8):
#     for k in range(1,5):
#         result = driver.find_element("xpath",f"//table[@name='BookTable']//tr[{j}]//td[{k}]")
#         print(result.text)

# for j in range(2, 8):
#     row_data = []  # Initialize an empty list for the current row
#
#     # Iterate through columns (from column 1 to 4)
#     for k in range(1, 5):
#         result = driver.find_element("xpath", f"//table[@name='BookTable']//tr[{j}]//td[{k}]")
#         row_data.append(result.text)  # Add cell text to the row list
#
#     # Print the full list for the current row
#     print(row_data)
#
# driver.quit()

appended_table_list = []

for j in range(2, 8):
    row_data = []
    for k in range(1, 5):
        result = driver.find_element("xpath", f"//table[@name='BookTable']//tr[{j}]//td[{k}]")
        row_data.append(result.text)

    # 2. Append the current row list into the master list
    appended_table_list.append(row_data)

# 3. Print the final result (this will print all lists one behind the other)
print(appended_table_list)