##################### 22/01/2026 ##################
import pytest

#            topic done in test_pytest.py file


# Rules : 1. create a package >> create a python file >> name in format test_filename.py
#         2. class name should start with test_ClassName
#         3. function name should start with filename_test or test_filename
#         4. in nested pytest functions, only the parent function gets executed.


# NOTE : 1. The naming convention is recommended to be followed as per the rules.
#        2. functions names following the rules (_test , test_) are automatically internally recognized by python/selenium
#           as pytest based function
#        3. even if one pytest based function has a mistake, instead of throwing error, it will execute the other functions.
#        4. but with normal functions, code will jot execute and will throw error.
