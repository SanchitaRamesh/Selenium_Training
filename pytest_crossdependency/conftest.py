##################### 03/02/2026 ##################################

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
#from pytest_Pacakage.test_markers import test_login


# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser",
#         action="store",
#         default="chrome",
#         help="Browser to run tests : chrome/firefox/edge"
#     )
#
# @pytest.fixture(scope='class')
# def browser_setup(request):
#     browser = request.config.getoption("--browser")
#
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#     elif browser=="firefox":
#         driver = webdriver.Firefox()
#     elif browser == "edge":
#         driver = webdriver.Edge()
#
#     driver.get("https://demowebshop.tricentis.com/")
#     time.sleep(2)
#     yield driver
#     driver.close()

#----------------------------------------------------------------------------------------------------

ch_open = webdriver.ChromeOptions()
ch_open.add_experimental_option("detach",True)

@pytest.fixture(scope="class")
def browser_setup():
    driver = webdriver.Chrome(ch_open)
    driver.get("https://www.saucedemo.com/")
    time.sleep(3)
    yield driver
    driver.close()