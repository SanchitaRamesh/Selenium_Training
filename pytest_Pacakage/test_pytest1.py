####################### 23/01/2026 #####################
import pytest
import time
from selenium import webdriver

ch_open = webdriver.ChromeOptions()
ch_open.add_experimental_option('detach',True)
driver = webdriver.Chrome(ch_open)

driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)

class TestRegister:
    def test_reg(self):
        driver.find_element("xpath","//a[text()='Register']").click()
        time.sleep(2)
    def test_gender(self):
        driver.find_element("id","gender-female").click()
        time.sleep(2)
    def test_fname(self):
        driver.find_element("id","FirstName").send_keys("Sanchita")
        time.sleep(2)
    def test_lname(self):
        driver.find_element("id","LastName").send_keys("Ramesh")
        time.sleep(2)
    def test_email(self):
        driver.find_element("id","Email").send_keys("sanchi123@gmail.com")
        time.sleep(2)
    def test_password(self):
        driver.find_element("id","Password").send_keys("JeonSanchita")
        time.sleep(2)
    def test_confirmPassword(self):
        driver.find_element("id","ConfirmPassword").send_keys("JeonSanchita")
        time.sleep(2)
    def test_clickRegister(self):
        driver.find_element("id","register-button").click()
        time.sleep(2)

class TestLogin:

    def test_login(self):
        driver.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(1)
    def test_login_email(self):
        driver.find_element('id', 'Email').send_keys('sanchi123@gmail.com')
        time.sleep(1)
    def test_login_pwd(self):
        driver.find_element('id', 'Password').send_keys('JeonSanchita')
        time.sleep(1)
#driver.close()