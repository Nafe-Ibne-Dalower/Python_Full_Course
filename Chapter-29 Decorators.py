print("Hello World😉😉😉")

# ✨✨✨Decorators: Decorator functions are software design patterns. They dynamically alter the functionality of a function, method, or class without having to directly use subclasses or change the source code of the decorated function.
# Use: It is used to modify function.
# Decorators starts with "@"

# Start:
def func(func1):
    def hel(): # Nested Function...
        v = input("Your name: ")
        print(f"Hello! {v}")
        func1()
    return hel

def nf():
    print("How are you?")
nf = func(nf) # Same as decorator...
nf()


# Using Decorator...
def dec1(func1):
    def hel():
        v = input("Your name: ")
        print(f"Hello! {v} ")
        func1()
    return hel

@dec1
def nf():
    print("How are you?")
nf()

# <<<---Decorators--->>>
