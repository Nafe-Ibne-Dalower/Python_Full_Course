print("Hello World😉😉😉")
# Return
def funcret(ret):
    return "I am returned the function..."
print(funcret(0))

# Pass: Does Nothing
def funcpass(pas):
    pass # None
print(funcpass("don't")) 

# Nested Function: A function in a function...
def greet(me):
    print("Hello!",me)
    def hlw():
        print("How are you?")
    hlw()
greet("Nafe")

# <<<---Return,Pass & Nested Function--->>>

