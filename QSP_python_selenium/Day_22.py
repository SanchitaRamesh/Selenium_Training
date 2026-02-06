##################### 21/01/2026 ####################
import xlrd
import time
from selenium import webdriver
from openpyxl import Workbook

# workbook = Workbook()
# worksheet = workbook.active
#
#
# data_list =[['Name','Age','Birth place','Status','Residing City','Spouse Name','Children','name'],
#     ['Jeon Jungkook','31','Busan','Married','Seoul','Sanchita Ramesh','1','Jeon Sara'],
#     ['Sanchita Ramesh','30','Bengaluru','Married','Seoul','Jeon Jungkook','1','Jeon Sara'],
#     ['Jeon Sara','1','Seoul','Unmarried','Seoul','N/A','N/A','N/A']
# ]
# worksheet.title = "Family_Info"
# for data in data_list:
#     worksheet.append(data)
# workbook.save('Family_Info.xlsx')
#
# file = workbook.save(r'C:\Users\User\PycharmProjects\Selenium_Training\Excel_Files\Family_Info.xlsx')
# path = r'C:\Users\User\PycharmProjects\Selenium_Training\Excel_Files\Family_Info.xlsx'
#
# open = xlrd.open_workbook(path)
#
# sheet = open.sheet_by_name("Family_Info")
#
# rows = sheet.get_rows()
#
# header = next(rows)
# for row in rows:
#     print([cell.value for cell in row])
#     print(row)
#
#############################################################################################################

#path =r"C:\Users\User\PycharmProjects\Selenium_Training\Excel_Files\Demo.xlsx"

#path = r"C:\Users\User\PycharmProjects\Selenium_Training\Excel_Files\reg_data.xlsx"

ch_open = webdriver.ChromeOptions()
ch_open.add_experimental_option('detach',True)
driver = webdriver.Chrome(ch_open)

# def read_excel_data(sheet_name):
#     workbook = xlrd.open_workbook(path)
#     open = xlrd.open_workbook(path)
#     sheet = open.sheet_by_name(sheet_name)
#     rows =sheet.get_rows()
#     header = next(rows)
#     dict ={}
#     for row in rows:
#         dict[row[0].value] = row[3].value
#     return dict
#     print(dict)
# result = read_excel_data('reg')

# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Register"]').click()
# time.sleep(2)
# driver.find_element('id', 'gender-female').click()
# time.sleep(2)
# driver.find_element('id', 'FirstName').send_keys(result['fname'])
# time.sleep(2)
# driver.find_element('id','LastName').send_keys(result['lname'])
# time.sleep(2)
# driver.find_element('id', 'Email').send_keys(result['email_id'])
# time.sleep(2)
# driver.find_element('id', 'Password').send_keys(result['pwd'])
# time.sleep(2)
# driver.find_element('id', 'ConfirmPassword').send_keys(result['confirm_pwd'])
# time.sleep(2)
# driver.find_element('id', 'register-button').click()
# time.sleep(2)
#
# driver.close()


#######################################################

def read_excel_data(sheet_name,path):
    #workbook = xlrd.open_workbook(path)
    open = xlrd.open_workbook(path)
    sheet = open.sheet_by_name(sheet_name)
    rows =sheet.get_rows()
    header = next(rows)
    dict ={}
    for row in rows:
        dict[row[0].value] = row[3].value
    return dict
    print(dict)
result = read_excel_data('reg',r"C:\Users\User\PycharmProjects\Selenium_Training\Excel_Files\reg_data.xlsx")

driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)

driver.find_element('xpath', '//a[text()="Register"]').click()
time.sleep(2)
driver.find_element('id', 'gender-female').click()
time.sleep(2)
driver.find_element('id', 'FirstName').send_keys(result['fname'])
time.sleep(2)
driver.find_element('id','LastName').send_keys(result['lname'])
time.sleep(2)
driver.find_element('id', 'Email').send_keys(result['email_id'])
time.sleep(2)
driver.find_element('id', 'Password').send_keys(result['pwd'])
time.sleep(2)
driver.find_element('id', 'ConfirmPassword').send_keys(result['confirm_pwd'])
time.sleep(2)
driver.find_element('id', 'register-button').click()
time.sleep(2)

driver.close()