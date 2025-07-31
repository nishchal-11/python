import os

# Specify the path (use '.' for current directory)
path = '.'

# Check if path exists
if os.path.exists(path):
    print(f"Contents of directory '{path}':\n")
    for item in os.listdir(path):
        print(item)
else:
    print(f"The path '{path}' does not exist.")
