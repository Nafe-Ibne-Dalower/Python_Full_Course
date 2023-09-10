print("Hello World😉😉😉")
# Recursion:
#  Start:
# def d(r1): 
#     d(r1)
#     print("This is" ,r1)
# d("Nafe")
# RecursionError: maximum recursion depth exceeded
# Use of recursion:
# Calculating Fibonacci Pattern:
# 0 1 1 2 3 5 8 13 .....
num = 12
def fib(n):
    if n==1:
        return 0
    elif n==2 or n==3:
        return 1
    else:
        return fib(n-1) + fib(n-2)
fib(num) 

# Calculating Factorial
def fac(n):
    if n==0:
        return 1
    else:
        return n * fac(n-1)
fac(12)

# <<<---Recursion--->>>