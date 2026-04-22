# inheritance_basics.py
# Basic parent and child class relationship

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    pass  # Inherits everything from Animal

dog = Dog()
dog.speak()
