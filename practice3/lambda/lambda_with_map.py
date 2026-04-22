# lambda_with_map.py
# Using lambda with map() for transformation

numbers = [1, 2, 3, 4, 5]

# Square each number
squared_numbers = list(map(lambda x: x ** 2, numbers))

print("Original:", numbers)
print("Squared:", squared_numbers)
