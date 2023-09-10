print("Let's Start Building Pyramid😉😉😉")
v = input("Size of Diamond(2 < Data should < 70): ")
x = int(v)
# z = int(x / 2)
while 2==2:
    for i in range(x):
        print(" " * (x - 1 - i) + "*" * (i * 2 + 1))
    for i in range(x):
        print(" " * i + "*" * (x + (x - 1) - 2 * i))
    break