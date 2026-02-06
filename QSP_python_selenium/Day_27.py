######################### 29/01/2026 ###########
# also covered in test_fixture.py

def my_generator():
    print("Starting...")
    yield 1
    print("Resuming...")
    yield 2

# 1. Calling the function creates a 'generator object'
# but DOES NOT run the code yet.
gen = my_generator()

# 2. First call to next() runs the code until the first yield.
print(next(gen))  # Prints "Starting...", then 1

# 3. Second call to next() resumes right after the first yield.
print(next(gen))  # Prints "Resuming...", then 2
