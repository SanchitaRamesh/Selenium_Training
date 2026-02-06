import time

import pytest
from selenium import webdriver
import pytest

ch_open = webdriver.ChromeOptions()
ch_open.add_experimental_option("detach",True)
#driver = webdriver.Chrome(ch_open)

# ed_open = webdriver.EdgeOptions()
# ed_open.add_experimental_option("detach",True)
# # driver_ed = webdriver.Edge(ed_open)


@pytest.fixture(scope="class",params=["chrome","edge","firefox"])
def browser_setup(request):
    parameters = request.param

    if parameters == "chrome":
        driver = webdriver.Chrome(ch_open)
    elif parameters == "edge":
        driver = webdriver.Edge()
    elif parameters == "firefox":
        driver = webdriver.Firefox()

    driver.get("https://demowebshop.tricentis.com/")
    time.sleep(4)
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