with open("example.txt", "w") as f:
    f.write("Hello, this is the first line\n")
    f.write("This is the second line\n")

# append new data
with open("example.txt", "a") as f:
    f.write("This line was appended\n")

print("File written and appended successfully")