print("Hello World😉😉😉")
# Random Module
"""
random.randint()       Returns a random integer between x and y (inclusive)
random.randrange()     random.randrange has the same syntax as range and unlike random.randint,the last value is not inclusive
random.random()        Returns a random floating point number between 0 and 1 
random.uniform()       Returns a random floating point number between x and y (inclusive)
"""
import random
a = random.randint(1, 10)
b = random.randrange(1, 10)
c = random.randrange(1, 2)
d = random.random()
e = random.uniform(1,2)
print(a)
print(b)
print(c)
print(d)
print(e)

# shuffe, choice and sample...
"""
shuffle() - Shuffles the items of the sequence
choice()  - Takes a random element from an arbitrary sequence
sample()  - Like choice it takes random elements from an arbitrary sequence but you can specify how many
"""

Numlst = [1,2,3,4,5]
random.shuffle(Numlst)
print(Numlst)
print(random.choice(Numlst))
print(random.sample(Numlst, 2))