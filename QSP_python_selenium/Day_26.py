######################### 28/01/2026 ####################33
# also covered in test_decorators.py

## DECORATORS concept

def outer(func):
    def wrapper(*args, **kwargs):
        print('good morning')
        func(*args, **kwargs)
    return wrapper

@outer      # addition = outer(addition)  this is what happens internally that calls the decorator function
def addition(a, b):
    print(a + b)

addition(1, 2)

###############     working logic of decorator

# first class object : function taking another function as input and return a value. eg : decorators.
# addition = outer(addition) is a first class object

# addition() - function call
# addition - fucntion address
# @addition - decorator

# PYTHON is line by line execution ( interpreter language )
# Hence:
# func -> addition
# addition -> wrapper address
# args -> 1,2

# func - formal args    addition - actual args    formal args always points to actual args
# hence addition will contain the address of wrapper function.addition value is overriden by the wrapper address.
#
# hence when function call happens , wrapper is called with the values we pass.