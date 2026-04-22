import shutil
import os


shutil.copy("example.txt", "example_copy.txt")


shutil.copy("example.txt", "backup.txt")

print("Files copied")

if os.path.exists("example_copy.txt"):
    os.remove("example_copy.txt")
    print("example_copy.txt deleted")