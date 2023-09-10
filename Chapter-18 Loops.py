print("Hello World!😉😉😉")

# ✨✨✨Loops
"""There are two types of loops:
for loop and while loop """

# While Loop
while 2 == 2:
    print("It is Okay..")
    break

while type(2) == int:
    print("It is Integer.")
    break

# Interaction with loops
a = int(input("Enter Value: "))
b = int(input("Enter Value: "))
print(f"a = {a}")
print(f"b = {b}")
while a > b:
    print("a is greater than b")
    break

while a < b:
    print("a is less than b")
    break

while a == b:
    print("a and b is equal.")
    break

# Nested Loops:

# Nested for loop...
for i in range(5):
    for j in range(2):
        print(i,j)

# Nested while lood...
while 2==2:
    while 5 > 0:
        print("5 is getter than 0")  
        break

# <<<---Loops--->>>