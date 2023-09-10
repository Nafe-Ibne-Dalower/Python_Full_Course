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