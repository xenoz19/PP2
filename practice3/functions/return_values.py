# return_values.py
# Functions with return values

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

result = multiply(4, 5)
print("Result:", result)


# Returning multiple values
def get_user():
    name = "Alex"
    age = 20
    return name, age

user_name, user_age = get_user()
print(user_name, user_age)
