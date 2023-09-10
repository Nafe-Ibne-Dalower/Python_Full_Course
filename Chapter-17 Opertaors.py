print("Hello World!😉")
# There are many types of opeartors in pyhton...
"""
Arithmetic operators
Assignment operators
Comparison operators
Logical operators // and or not
Identity operators // is isn't
Membership operators // in not in
Bitwise operators
"""
# Arithmatic Operator...
(a,b) = (5,10)
print(a+b) # Addition
print(a-b) # Substraction
print(a*b)  # Multiply
print(a**b) # Exponent
print(a/b)  # Divide
print(a//b) # Integer
print(a%b)  # Remainder
# <<<---Arithmatic--->>>

# Comparison Operator...
"""
Operator	   Name	                          Example	
==	           Equal	                      x == y	
!=	           Not equal	                  x != y	
>	           Greater than	                  x > y	
<	           Less than	                  x < y	
>=	           Greater than or equal to	      x >= y	
<=	           Less than or equal to	      x <= y
"""

# ==
print(5 == 5)
print(4 == 3)
v1 = 10 
v2 = 13
print(v1 == v2)

# !=
print(4 != 3)
print(5 != 5)
v1 = 5
v2 = 6
print(v1 != v2)

# > and <
print(4 > 3) # Greater than
print(5 < 2) # Less than

# >= Greater than or equal
print(5 >= 2)
print(5 >= 5)

# <= Less than or equal
print(5 <= 2)
print(5 <= 5)
# <<<---Comparison--->>>

# Logical Operator...
name = "Nafe"
age = 16
name_matched = name == "Nafe"
age_matched = age > 15
print(name_matched)
print(age_matched)
# <<<---Logical--->>>


# Bitwise Operator....
# ----- After HSC ---


# Assainment Operator...
# It heps us to assain a value to a variable...

n = 5
# n= n + 5
n += 5
print(n)
n -= 5
print(n)
n *= 5
print(n)
n **= 5
print(n)
n /= 5
print(n)

# Identity & Membership Operator
# is and is not
a = 5
b = 5
print(a is b)
print(a is not b)

a = 5
b = 10
print(a is b)
print(a is not b)

# in and not in
v = "Nafe"
print ("n" in v)
print ("n" not in v)