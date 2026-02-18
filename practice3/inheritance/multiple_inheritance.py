# multiple_inheritance.py
# Multiple inheritance example

class Father:
    def skill1(self):
        print("Gardening")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

child = Child()

child.skill1()
child.skill2()
