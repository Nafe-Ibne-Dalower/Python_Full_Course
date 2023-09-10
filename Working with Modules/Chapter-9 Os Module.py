print("Hello World😉😉😉")
# This module provides a portable way of using operating system dependent functionality.
import os
# ✨✨✨Getting current directory...
v = os.getcwd()
print(f"Current working directory is {v}")

# ✨✨✨Creating directory...
# os.mkdir("./Working with Os")
try:
    os.mkdir("./Working with Os")
except Exception as e:
    print("Path already created...")

# ✨✨✨Removing a directory...
try:
    os.rmdir("./Working with Os")
except Exception as e:
    print("Path already deleted...")

# Judging a file...
f = open("demofile.txt", "a")
import os
print(os.path.isfile("demofile.txt"))
print(os.path.isfile("file.txt"))

# Removing a file
import os
os.remove("demofile.txt")
# <<<---Explore more about os module--->>>