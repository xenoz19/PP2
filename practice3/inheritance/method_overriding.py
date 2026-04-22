# method_overriding.py
# Method overriding example

class Animal:
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self):  # Overriding parent method
        print("Meow")

cat = Cat()
cat.speak()

