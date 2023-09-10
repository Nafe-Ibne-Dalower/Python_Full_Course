print("Hello World😉😉😉")

# Scope: A variable is only available from inside the region it is created. This is called scope.
"""
# There are two types of scope:
1. Global Scope
2. Local Scope
"""
# Global & Local Scope:
x = 10 # Global
def sc(d):
    y = 20 # Local
    print(y)

# Global Keyword...
v = 10
def gb(f):
    v = v + 10 # UnboundLocalError: local variable 'v' referenced before assignment
    print(v)
gb("y")


v = 10
def gb(f):
    global v # I have given permission by global variable
    v = v + 10
    print(v)
gb("y")


# <<<---Scope--->>>