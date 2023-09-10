print("Hello World!😉")
# List of Patterns
"""
Square Pattern
Hollow Square Pattern
Left triangle star Pattern
Right triangle star Pattern
Hollow triangle star Pattern
Downward triangle star Pattern
Pyramid Pattern
Hollow Pyramid Pattern
Reverse pyramid Pattern
Diamond Pattern
Hollow Diamond Pattern
Hourglass Pattern
Right Pascal star Pattern
Left Pascal star Pattern
Heart Pattern
"""

# Square Pattern
for i in range(0,5): # Represents Lines.
    print("*" * 5) # Represents raw.

# Left triangle star Pattern
size = 11
for i in range(size):
    print("*" * i)

# Right triangle star Pattern
size = 11
for i in range(size):
    print("*" * (size-i))

# Pyramid
n = 5
for i in range(n): # Line Number
    print(" " * (n - 1 - i) + "*" * (i * 2 + 1))

# Inversed Pyramid
n = 5
for i in range(n): # Line Number
    print(" " * (i) + "*" * (n + (n-1) - 2*i))

# Dimond 
while 2==2:
    n = 5
    for i in range(n):
        print(" " * (n - 1 - i) + "*" * (i * 2 + 1))
    n = 5
    for i in range(n): # Line Number
        print(" " * (i) + "*" * (n + (n-1) - 2*i))
    break