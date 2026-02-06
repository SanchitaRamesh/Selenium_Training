####################### 30/01/2026 ########################
from selenium import webdriver
import pytest
import time

ch_open = webdriver.ChromeOptions()
ch_open.add_experimental_option("detach",True)


@pytest.fixture(scope="class")
def browser_setup():
    driver = webdriver.Chrome(ch_open)
    driver.get("https://demowebshop.tricentis.com/")
    yield driver
    driver.close()

class TestRegister:
    def test_reg(self,browser_setup):
        browser_setup.find_element("xpath","//a[text()='Register']").click()
        time.sleep(2)
    def test_gender(self,browser_setup):
        browser_setup.find_element("id","gender-female").click()
        time.sleep(2)
    def test_fname(self,browser_setup):
        browser_setup.find_element("id","FirstName").send_keys("Sanchita")
        time.sleep(2)
    def test_lname(self,browser_setup):
        browser_setup.find_element("id","LastName").send_keys("Ramesh")
        time.sleep(2)
    def test_email(self,browser_setup):
        browser_setup.find_element("id","Email").send_keys("sanchi123@gmail.com")
        time.sleep(2)
    def test_password(self,browser_setup):
        browser_setup.find_element("id","Password").send_keys("JeonSanchita")
        time.sleep(2)
    def test_confirmPassword(self,browser_setup):
        browser_setup.find_element("id","ConfirmPassword").send_keys("JeonSanchita")
        time.sleep(2)
    def test_clickRegister(self,browser_setup):
        browser_setup.find_element("id","register-button").click()
        time.sleep(2)


class TestLogin:
    def test_login(self,browser_setup):
        browser_setup.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(1)

    def test_login_email(self,browser_setup):
        browser_setup.find_element('id', 'Email').send_keys('sanchi123@gmail.com')
        time.sleep(1)

    def test_login_pwd(self,browser_setup):
        browser_setup.find_element('id', 'Password').send_keys('JeonSanchita')
        time.sleep(1)

#################################### trainers example ####################33

# import time
# import pytest
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# @pytest.fixture(scope='class')
# def setup():
#     driver = webdriver.Chrome(opts)
#     driver.get("https://demowebshop.tricentis.com/")
#     time.sleep(2)
#     yield driver
#     driver.close()
#
# ## setup --> webdriver.Chrome(opts)
#
# class TestRegister:
#
#     def test_reg(self, setup):
#         setup.find_element('xpath', '//a[text()="Register"]').click()
#         time.sleep(1)
#
#     def test_gender_btn(self, setup):
#         setup.find_element('id', 'gender-female').click()
#
#     def test_fname(self, setup):
#         setup.find_element('id', 'FirstName').send_keys('Pooja')
#
#     def test_lname(self, setup):
#         setup.find_element('id', 'LastName').send_keys('Mane')
#
#     def test_reg_email(self, setup):
#         setup.find_element('id', 'Email').send_keys('pooja@gmail.com')
#
#     def test_reg_pwd(self, setup):
#         setup.find_element('id', 'Password').send_keys('pooja@12345')
#
#     def test_confirm_pwd(self, setup):
#         setup.find_element('id', 'ConfirmPassword').send_keys('pooja@12345')
#         time.sleep(2)
#
#
# class TestLogin:
#
#     def test_login(self, setup):
#         setup.find_element('xpath', '//a[text()="Log in"]').click()
#         time.sleep(1)
#
#     def test_login_email(self, setup):
#         setup.find_element('id', 'Email').send_keys('pooja@gmail.com')
#
#     def test_login_pwd(self, setup):
#         setup.find_element('id', 'Password').send_keys('pooja@12345')