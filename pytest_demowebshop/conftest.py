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