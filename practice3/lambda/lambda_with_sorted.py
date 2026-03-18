# lambda_with_sorted.py
# Using lambda with sorted() for custom sorting

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
]

# Sort students by grade
sorted_students = sorted(students, key=lambda student: student[1])

print("Original:", students)
print("Sorted by grade:", sorted_students)