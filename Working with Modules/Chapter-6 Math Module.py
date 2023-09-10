print("Hello World😉😉😉")

import math
# Constants:
"""
Math        Constants
Constant	Description
math.e	    Returns Euler's number (2.7182...)
math.inf	Returns a floating-point positive infinity
math.nan	Returns a floating-point NaN (Not a Number) value
math.pi	    Returns Pi (3.1415...)
math.tau	Returns tau (6.2831...)"
"""

# Use of math module:
# Round,floor,ceil,trunc:
# Round: Round to the nearest integer
x = 1.2 # It considers from half...
print(round(x))
y = 1.5 # It considers from half...
print(round(y))
x = -1.2 # It considers from half...
print(round(x))
y = -1.5 # It considers from half...
print(round(y))

# floor: It gets the largest integer less than x...
import math
x = 1.5 # We must input float...
print(math.floor(x))

# ceil: It gets the smallest integer greater than x...
import math
x = 1.5 # We must input float...
print(math.ceil(x))

# trunc: It drops fractional part of x
import math
x = 1.55
print(math.trunc(x)) # 1, equivalent to math.floor for positive numbers
y = -1.55
print(math.trunc(y)) # -1, equivalent to math.ceil for negative numbers


# Infinity:
import math
v = math.inf
print(math.isinf(v))
# Nan: Not a number
import math
v = math.nan
print(math.isnan(v))

# <<<---Trigonmetry--->>>
# hypot: It is used to get the hypotenuse...
import math
base = 3
parendicular = 4
print(math.hypot(base, parendicular))
# Just practice
import math
base = int(input("Base(m): "))
parendicular = int(input("Parendicular(m): "))
v = int(math.hypot(base, parendicular)) 
print(f"Hypotenuse is {v}m")

# Radian & degree:
import math
x = 45
print(math.radians(x)) # Convert degree to radian...
import math
x = 0.8939966636005579
print(math.degrees(x)) # Convert radian to degree...

# Sin, Cos, tan:
import math
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))

# <<<---Logarithm--->>>
"""
Logarithm are of two types:
1. Natural Logarithm 
2. Common Logarithm
"""
# Python gives more priority on Natural Logarithm...
# Start:
import math
math.log(1)
math.log(100) # Base e = 2.71......
math.log10(100) # Base 10
math.log(100,10) # Base 10
math.log(100,10) # Structure: math.log('Param','Base')
math.log(100,5) # Structure: math.log('Param','Base')
math.log(100,2) # Structure: math.log('Param','Base')
math.log(100,0) # Base couldn't be 0 & 1...
math.log(100,1) # Base couldn't be 0 & 1...

# Explore Math & CMath Module...
# <<<---Math Module--->>>