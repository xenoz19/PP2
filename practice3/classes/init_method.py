# init_method.py
# Using __init__ constructor method

class Person:
    """Person class with constructor."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating objects
person1 = Person("Nurkanat", 19)
person2 = Person("Ali", 20)

print(person1.name, person1.age)
print(person2.name, person2.age)
