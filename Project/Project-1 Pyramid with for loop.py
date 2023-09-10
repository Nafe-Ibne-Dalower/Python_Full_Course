print("Let's Start Building Pyramid😉😉😉")
v = input("Number of Storey: ")
x = int(v)
for i in range(x):
    print(" " * (x- 1 - i) + "*" * (i * 2 + 1))
