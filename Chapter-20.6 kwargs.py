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
    statement(s) # Effect

# Concept Clearing:
"""
In Python, we can pass a variable number of arguments to a function using special symbols. There are two special symbols:
1. *args (Non Keyword Arguments)
2. **kwargs (Keyword Arguments) 
"""
# **kwargs:
# **kwargs is just like *args but it is use for only dictionary...
"""
If we don't know how much data we have to pass through the function then we use **kwargs. Otherwise we will get an error. **kwargs starts with (**)double asterisk.
"""
# Let me give an example:
def dic(data):
    for key,value in data.items():
        print("{} is {}" .format(key, value))
dic(P1 = "Mercury", P2 = "Venus", P3 = "Earth")
# We got error: "TypeError: dic() got an unexpected keyword argument 'P1'"

# Now we will use kwargs...
def dic(**data): # kwargs
    for key,value in data.items():
        print("{} is {}" .format(key, value))
dic(P1 = "Mercury", P2 = "Venus", P3 = "Earth")

# Or we can do that...
Planetsdic = {
    "Planet1": "Mercury",
    "Planet2": "Venus",
    "Planet3": "Earth"
}
def dic(**data):
    for key,value in data.items():
        print("{} is {}" .format(key, value))
print(type(Planetsdic))
dic(**Planetsdic)
# <<<---**Kwargs--->>>