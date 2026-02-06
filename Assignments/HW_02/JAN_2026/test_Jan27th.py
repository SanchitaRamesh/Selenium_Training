####################### 27/01/2026 ##################
import time
import xlrd
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_excel_data():
    path = r"C:\Users\User\PycharmProjects\Selenium_Training\Excel_Files\Id_pwd.xlsx"
    open_wb = xlrd.open_workbook(path)
    sheet = open_wb.sheet_by_name("cred")
    rows = sheet.get_rows()
    next(rows)  # Skipping the header (userid, password)

    data_list = []
    for row in rows:
        # row[0] is Column A (User), row[1] is Column B (Password)
        user = row[0].value
        pwd = row[1].value
        data_list.append((user, pwd))

    return data_list


@pytest.mark.parametrize("username, password", get_excel_data())
def test_login(username, password):
    ch_open = webdriver.ChromeOptions()
    ch_open.add_experimental_option('detach', True)
    driver = webdriver.Chrome(ch_open)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com")
        # Using string "id" as you used in your example
        driver.find_element("id", "user-name").send_keys(username)
        driver.find_element("id", "password").send_keys(password)
        driver.find_element("id", "login-button").click()

        time.sleep(2)

        try:
            wait.until(EC.url_contains("inventory"))
            print(f"\nSUCCESS: Logged in as {username}")
        except:
            print(f"\nFAILED: Login failed for {username}")

    except:
        print(f"\nERROR: Could not complete test for {username}")

    driver.close()
