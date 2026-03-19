with open("example.txt", "r") as f:
    content = f.read()
    print("Full content:\n", content)

with open("example.txt", "r") as f:
    print("Line by line:")
    for line in f:
        print(line.strip())