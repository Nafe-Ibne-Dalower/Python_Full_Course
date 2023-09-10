print("Hello World😉😉😉")
# ✨✨✨Function

"""
Parameter          Details
arg1, ..., argN    Regular arguments
*args              Unnamed positional arguments
kw1, ..., kwN      Keyword-only arguments
**kwargs           The rest of keyword arguments
"""
# Simple form of a function
def func_name(Parameter):
    # statement(s) # Effect
    return

"""
Concept Clearing:
In Python, we can pass a variable number of arguments to a function using special symbols. There are two special symbols:
1. *args (Non Keyword Arguments)
2. **kwargs (Keyword Arguments)
*args
"""
"""
If we don't know how much data we have to pass through the function then we use *args. Otherwise we will get an error. *args starts with (*)one asterisk.
"""
# Let me give an example:
def adder(num):
    for n in num:
        sum = sum + n 
        print("Sum:",sum)
# adder(1,2,3,4,5) 
# We got this "TypeError: adder() takes 1 positional argument but 5 were given"...

# But if I use *args then:
def adder(*num): # *
    for n in num:
        sum = sum + n
    print("Sum:",sum)
adder(1,2,3,4,5)

# Practice
Planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
def func_arg(*args):
    for itm in args:
        print(itm)
func_arg(*Planets)

# <<<---*args--->>>