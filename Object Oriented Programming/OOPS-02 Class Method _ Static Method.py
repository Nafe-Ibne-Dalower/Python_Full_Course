print("Hello World😉😉😉")

# Class methods: It is used to access or modify the state of the class. if we use only class variables, we should declare such methods as a class method.
class c():
    mul = int(2)
    @classmethod
    def f(cls, x):
        print(cls.mul * x)
c.f(2)


# Static methods: A static method is a general utility method that performs a task in isolation. Inside this method, we don’t use instance or class variable because this static method doesn’t take any parameters like self and cls.
class s():
    @staticmethod
    def g(x):
        x = x * 2
        print(x)
s.g(12)

# <<<---Class Method & Static Method--->>>