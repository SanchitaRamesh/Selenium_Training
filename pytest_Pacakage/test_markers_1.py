##################### 27/01/2022 ###################
import pytest
import time

# #@pytest.mark.skip(reason="login was already tested successful")
# @pytest.mark.skip()
# def test_loginn():
#     print("login successfulll")
#
# def test_logout():
#     print("logout successful")


# @pytest.mark.skipif(4%2==0 ,reason="login was already tested successful")
# def test_login():
#     print("login successful")
#
# def test_logout():
#     print("logout successful")

# @pytest.mark.parametrize("a,b,c,d",[("my"," name"," is"," sanchita")])
# def test_login(a,b,c,d):
#     print(a+b+c+d)
#     #return a+b+c
#
# def test_logout():
#     print("logout successful")

@pytest.mark.xfail(reason="testcase failure expected")
def test_login():
    try:
        a=2
        if a%2==0:
            print("passed")
    except:
        raise Exception

def test_logout():
    print("logout successful")