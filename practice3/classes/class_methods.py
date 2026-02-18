# class_methods.py
# Demonstrating instance methods and self parameter

class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand} is driving.")

    def stop(self):
        print(f"{self.brand} has stopped.")

car1 = Car("Toyota")

car1.drive()
car1.stop()
