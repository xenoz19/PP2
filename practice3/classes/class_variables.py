# class_variables.py
# Class variable vs instance variable

class Student:
    school = "AITU"  # Class variable (shared by all objects)

    def __init__(self, name):
        self.name = name  # Instance variable (unique for each object)

student1 = Student("Nurkanat")
student2 = Student("Ali")

print(student1.name, student1.school)
print(student2.name, student2.school)

# Changing class variable
Student.school = "New University"

print(student1.school)
print(student2.school)
