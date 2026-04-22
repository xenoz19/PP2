# function_arguments.py
# Different types of function arguments

# Positional argument
def add(a, b):
    return a + b

print(add(3, 5))


# Default argument
def power(base, exponent=2):
    return base ** exponent

print(power(4))       # 4^2
print(power(2, 3))    # 2^3
