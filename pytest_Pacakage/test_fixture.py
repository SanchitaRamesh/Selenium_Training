import pytest

# @pytest.fixture()
# def greet():
#     print("Hello!! ")     # setup
#     yield
#     print("Goodbye")      # tear down
#
# def test_morning(greet):
#     print("Good morning Sanchita")
#
# def test_evening(greet):
#     print("Good evening Sanchita")

#####################################################

# @pytest.fixture(autouse=True)
# def greet():
#     print("Hello!! ")
#     yield
#     print("Goodbye!! ")
#
# def test_morning():
#     print("Good morning Sanchita")
#
# def test_evening():
#     print("Good evening Sanchita")

############################################################

# @pytest.fixture(autouse=True, scope='class')
# def greet():
#     print("Hello!! ")
#     yield
#     print("have a nice day")
#
# class TestClass:
#     def test_morning(self):
#         print("Good morning Sanchita")
#
#     def test_evening(self):
#         print("Good evening Sanchita")

##############################################################

# @pytest.fixture(autouse=True, scope='class')
# def greet():
#     print("Hello!! ")
#     yield
#     print("have a nice day")
#
# class TestClass:
#     def test_morning(self, greet):
#         print("Good morning Sanchita")
#
#     def test_evening(self,greet):
#         print("Good evening Sanchita")

#################################################################

# @pytest.fixture(autouse=True, scope='class')
# def greet():
#     print("Hello!! ")
#     yield
#     print("have a nice day")
#
# class TestClass:
#     def test_morning(self):
#         print("Good morning Sanchita")
#
#     def test_evening(self):
#         print("Good evening Sanchita")
# class TestClass2:
#     def test_morning(self):
#         print("Good morning Kavya")
#
#     def test_evening(self):
#         print("Good evening Kavya")

#######################################################################

# @pytest.fixture(scope="class")
# def greet():
#     print("Hello!! ")
#     yield
#     print("have a nice day")
#
# class TestClass:
#     def test_morning(self):
#         print("Good morning Sanchita")
#
#     def test_evening(self):
#         print("Good evening Sanchita")
#
# class TestClass2:
#     def test_morning(self, greet):
#         print("Good morning Kavya")
#
#     def test_evening(self, greet):
#         print("Good evening Kavya")

#######################################################################

# @pytest.fixture(autouse=True, scope='module')
# def greet():
#     print("Hello!! ")
#     yield
#     print("have a nice day")
#
# class TestClass:
#     def test_morning(self):
#         print("Good morning Sanchita")
#
#     def test_evening(self):
#         print("Good evening Sanchita")
# # class TestClass2:
# #     def test_morning(self):
# #         print("Good morning Kavya")
# #
# #     def test_evening(self):
# #         print("Good evening Kavya")

##############################################################

@pytest.fixture(autouse=True, scope='session')
def greet():
    print("Hello!! ")
    yield
    print("have a nice day")

class TestClass:
    def test_morning(self):
        print("Good morning Sanchita")

    def test_evening(self):
        print("Good evening Sanchita")
class TestClass2:
    def test_morning(self):
        print("Good morning Kavya")

    def test_evening(self):
        print("Good evening Kavya")
