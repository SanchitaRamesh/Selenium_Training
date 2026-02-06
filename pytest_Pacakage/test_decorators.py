################## 28/01/2026 #####################

import pytest
@pytest.fixture()
def greet():
    print('hello sanchita')
    yield
    print('bye sanchita')

def test_morning(greet):
    print('morning')

def test_evening(greet):
    print('evening')