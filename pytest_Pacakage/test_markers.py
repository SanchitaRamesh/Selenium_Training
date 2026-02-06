############### 23/02/2026 ##############3

import pytest
from selenium import webdriver

@pytest.mark.logout
@pytest.mark.login
def test_login():
    print("Login Test")

#@pytest.mark.logout
@pytest.mark.register
def test_reg():
    print("Register Test")

@pytest.mark.register
@pytest.mark.logout
def test_logout():
    print("Logout Test")

'''

pytest test_markers.py -vs -m="register and logout"   : 1 passed 
pytest test_markers.py -vs -m="register or logout"    : 3 passed
'''