import os


os.makedirs("test_dir/sub_dir", exist_ok=True)


print("Files in current directory:")
print(os.listdir())

print("Current directory:", os.getcwd())