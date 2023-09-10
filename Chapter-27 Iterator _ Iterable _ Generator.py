print("Hello World😉😉😉")

# Concept of Iterator & Iterable
# Iterable: An iterable is an object that can return an iterator. Any object with state that has an __iter__ method and returns an iterator is an iterable. It may also be an object without state that implements a __getitem__ method. 
for i in range(11):
    print(i) # 1-------------10
# The whole for loop in this section is an iterable.

# Iterator: An Iterator is an object that produces the next value in a sequence when you call next(*object*) on some object. Moreover, any object with a __next__ method is an iterator. 

s = [1,2,3,4,5,6,7]
iterable = iter(s)
next(iterable)
# <<<---......--->>>

# Extract values one by one
s = [1,2,3,4,5]
v = iter(s) # Making iterable
next(v)
next(v)
next(v)
next(v)
next(v)
next(v) # StopIteration(Error)

# Generator: It is slightly one type of iterator.
def gen(n):
    for i in range(n):
        yield i

g = gen(11)
print(next(g))
# <<<---Iterator & Iterable & Generator--->>>