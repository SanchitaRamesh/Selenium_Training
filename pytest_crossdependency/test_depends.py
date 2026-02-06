################################### 03/02/2026 ########################
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
import time

#from pytest_Pacakage.test_fixtureexample import browser_setup

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# @pytest.fixture(scope="module")
# def setup():
#     driver = webdriver.Chrome(opts)
#     driver.get("https://www.saucedemo.com/")
#     time.sleep(2)
#     yield driver
#     driver.close()

############################# PASS ###################################

# @pytest.mark.dependency()
# def test_login(setup):                           # PASS   - Independent test case
#     setup.find_element('id', 'user-name').send_keys('standard_user')
#     setup.find_element('id', 'password').send_keys('secret_sauce')
#     setup.find_element("id" , "login-button").click()
#     time.sleep(3)
#     try:
#         wait = WebDriverWait(setup, 10)
#         wait.until(EC.url_contains("inventory"))
#     except TimeoutException:
#         print("Timed out!!!!!!!!!!!!!!!!!!!!!!!!")
#
# @pytest.mark.dependency(depends=["test_login"])
# def test_logout(setup):                           # PASS dependent test case
#     setup.find_element('xpath', '//button[@id="react-burger-menu-btn"]').click()
#     time.sleep(2)
#     setup.find_element('id', 'logout_sidebar_link').click()

######################################## 1 FAILED 1 SKIP ###############################

# @pytest.mark.dependency()                           ## independent testcase      - FAILED
# def test_login(setup):
#     setup.find_element("id", "user-name").send_keys('standard_user')
#     time.sleep(1)
#     setup.find_element("id", "password").send_keys('secret_sauceeee')  # ERROR - FAILED
#     time.sleep(1)
#     setup.find_element("id", "login-button").click()
#     time.sleep(3)
#     wait = WebDriverWait(setup, 5)
#     wait.until(EC.url_contains("inventory"))
#
#
# @pytest.mark.dependency(depends=['test_login'])     ## dependent testcase         - SKIPPED
# def test_logout(setup):
#     setup.find_element('xpath', '//button[@id="react-burger-menu-btn"]').click()
#     time.sleep(2)
#     setup.find_element('id', 'logout_sidebar_link').click()

#####################################  3 PASS  ##############################

# @pytest.mark.dependency()                           ## independent testcase
# def test_login():
#     print("login executing")
#
# @pytest.mark.dependency()                           ## independent testcase
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.dependency(depends=['test_login', 'test_signup'])     ## dependent testcase
# def test_logout():
#     print("logout executing")

##################################### 1 PASS 1 FAilED 1 SKIPPED ######################

# @pytest.mark.dependency()                           ## independent testcase
# def test_login():
#     print("login executing")
#
# @pytest.mark.dependency()                           ## independent testcase
# def test_signup():
#     pnt("signup executing")                # ERROR - FAIL
#
# @pytest.mark.dependency(depends=['test_login', 'test_signup'])     ## dependent testcase
# def test_logout():
#     print("logout executing")
#
# # 1 independant test case failes , then the dependant test case gets skipped.
# # for the dependant test attrifute to pass , then "ALL THE" independant test cases should pass.

####################################### ###################################################

# class TestSample:
#
#     @pytest.mark.dependency()                           ## independent testcase
#     def test_login(self):
#         print("login executing")
#
#     @pytest.mark.dependency(depends=['test_login'])     ## dependent testcase
#     def test_logout(self):
#         print("logout executing")

# ## collected 2 items
# ## test_depends.py::TestSample::test_login     login executing     PASSED
# ## test_depends.py::TestSample::test_logout                        SKIPPED (test_logout depends on test_login)


'''
pytest will look for test_login in the global area(outside class).
There is no test_login in the global area, thats why test_logout is skipped'''

################# HENCE

# class TestSample:
#
#     @pytest.mark.dependency()                           ## independent testcase
#     def test_login(self):
#         print("login executing")
#
#     @pytest.mark.dependency(depends=['TestSample::test_login'])     ## dependent testcase
#     def test_logout(self):
#         print("logout executing")

############################################# 1 FAIL 1 SKIP #################################

# class TestSample:
#
#     @pytest.mark.dependency()                           ## independent testcase
#     def test_login(self):
#         prt("login executing")
#
#     @pytest.mark.dependency(depends=['TestSample::test_login'])     ## dependent testcase
#     def test_logout(self):
#         print("logout executing")

################################### CROSS func eg - conftest.py logic included #################

def test_login(browser_setup):                           # PASS   - Independent test case
    browser_setup.find_element('id', 'user-name').send_keys('standard_user')
    browser_setup.find_element('id', 'password').send_keys('secret_sauce')
    browser_setup.find_element("id" , "login-button").click()
    time.sleep(3)
    try:
        wait = WebDriverWait(browser_setup, 10)
        wait.until(EC.url_contains("inventory"))
    except TimeoutException:
        print("Timed out!!!!!!!!!!!!!!!!!!!!!!!!")

@pytest.mark.dependency(depends=["test_login"])
def test_logout(browser_setup):                           # PASS dependent test case
    browser_setup.find_element('xpath', '//button[@id="react-burger-menu-btn"]').click()
    time.sleep(2)
    browser_setup.find_element('id', 'logout_sidebar_link').click()