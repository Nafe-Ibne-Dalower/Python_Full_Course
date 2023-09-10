print("Hello World😉😉😉")
#  User-made Functions:
# Start...
def greet():
    print("Hello!")
greet()

def me(me = "Nafe"):
    print(me)
me()

# x's value identifier...
def y(x):
    if x < 0:
        return "x is less than zero."
    elif x == 0:
        return "x is equal to zero."
    else:
        return "x is greater than zero."
        
print(y(1))
print(y(0))
print(y(-1))

# Function as argument...
def exe(func):
    func("Nafe")

exe(print)

# Saying Hello to me
def g(me):
    print("Hello,",me)
g("Nafe")

# ____Doc-String____
def g(me):
    """This function says hello to me."""
    print("Hello,",me)
g("Nafe")
print(g.__doc__) # Without print it will return nothing...

# <<<---User Made Function--->>>