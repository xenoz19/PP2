names = ["Ivan", "Serega", "Aruzhan"]
scores = [85, 90, 95]


for i, name in enumerate(names):
    print(i, name)


for name, score in zip(names, scores):
    print(f"{name}: {score}")

numbers = [5, 2, 9, 1]
print("Sorted:", sorted(numbers))

x = "123"
print(int(x), type(int(x)))