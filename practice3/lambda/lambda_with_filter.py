# lambda_with_filter.py
# Using lambda with filter() for selection

numbers = [1, 2, 3, 4, 5, 6]

# Keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Original:", numbers)
print("Even:", even_numbers)

