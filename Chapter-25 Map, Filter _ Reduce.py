print("Hello World😉😉😉")
# ✨✨✨ Map, Filter & Reduce...
# The map function is the simplest one among Python built-ins used for functional programming. 
# map() applies a specified function to each element in an iterable
# Structure: map(func, iter)
num = ["3", "34", "64"]
# Example-1
# Without map...
for i in range(len(num)):
    num[i] = int(num[i])
num[2] = num[2] + 1
print(num[2])
# With map...
num = list(map(int, num))
num[2] = num[2] + 1
print(num[2])

# Example-2
# Square
def sq(a):
    return a*a
n = [1,2,3,4,5,6,7,8,9]
n = list(map(sq, n))
print(n)

def qb(a):
    return a*a*a

mainfunc = [sq , qb]
for i in range(7):
    print(list(map(lambda x:x(i),mainfunc)))
# Filter: It is used to filter discards elements of a sequence based on some criteria.
num = [1,2,3,4,5,6,7,8,9]
def greater_than_5(n): 
    return n > 5

grt = list(filter(greater_than_5, num))
print(grt)

# Reduce: Reduce takes a function and a collection of items. It returns a value that is created by combining the items.
num = [1,2,3,4,5,6,7,8,9]
x = 0
for i in num:
    x = x + i 
print(x)

# With Reduce
from functools import reduce
print(reduce(lambda x,y : x+y, num))
# <<<----Ending---->>>