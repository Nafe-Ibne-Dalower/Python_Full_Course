print("Hello World😉😉😉")

# File Handling means controlling file by python code.
# File Handling
# The key function for working with files in Python is the open() function.


"""
There are different modes you can open a file with, specified by the mode parameter. These include:
'r' - reading mode. The default. It allows you only to read the file, not to modify it. When using this mode the
file must exist.
'w' - writing mode. It will create a new file if it does not exist, otherwise will erase the file and allow you to
write to it.
'a' - append mode. It will write data to the end of the file. It does not erase the file, and the file must exist for
this mode.
'rb' - reading mode in binary. This is similar to r except that the reading is forced in binary mode. This is
also a default choice.
'r+' - reading mode plus writing mode at the same time. This allows you to read and write into files at the
same time without having to use r and w.
'rb+' - reading and writing mode in binary. The same as r+ except the data is in binary
'wb' - writing mode in binary. The same as w except the data is in binary.
'w+' - writing and reading mode. The exact same as r+ but if the file does not exist, a new one is made.
Otherwise, the file is overwritten.
'wb+' - writing and reading mode in binary mode. The same as w+ but the data is in binary.
'ab' - appending in binary mode. Similar to a except that the data is in binary.
'a+' - appending and reading mode. Similar to w+ as it will create a new file if the file does not exist.
Otherwise, the file pointer is at the end of the file if it exists.
'ab+' - appending and reading mode in binary. The same as a+ except that the data is in binary.
"""

# By Append Method we will create a file.
f = open("Demofile1.txt", "a") # Append
# Reading the file.
f1 = open("Demofile1.txt", "r") # "r" is for read mode.
print(f1.read())

# Writing inside the file.
f2 = open("Demofile1.txt", "w")
f3 = f2.write("I have written the text by python code.")
f4 = open("Demofile1.txt", "r")
print(f4.read())

# Closing a file.
f5 = open("Demofile1.txt")
f5.close()

# Removing a file.
f6 = open("file1", "a")
import os
os.remove("file1")
#  Check whether a file or path exists

import os
os.path.isfile("file1.txt") # It returned "False" because it doesn't exist...
os.path.isfile("Demofile1.txt") # It returned "True" because it exists...

# Checking if a file is empty
import os
os.path.getsize("Demofile1.txt") == 0

# Checking the file length
import os
os.path.getsize("Demofile1.txt")

# seek and tell..
f = open("Demofile2.txt")