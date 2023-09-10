print("Hello World!😉")
# ✨String Slicers.....
'''
The String Slicers are:
+, *, [], [:], in, not in, \Escape Sequences etc.
'''
# Type-01(+)
a = "Nafe" + " Ibne Dalower"
print(a)
b = "Comput" + "er"
print(b)

# Type-02(*)
a = "Ha"*8
print(a)
b = "😉"*100
print(b)

# Type-03([])
greet = "Hello!"
print(greet)
print(greet[0])
print(greet[5])

# Type-04([:])--Range
greet = "Hello!"
print(greet)
print(greet[0:5])
print(greet[0:3])
print(greet[0:100]) # Last Range can be taken as much as we want.

# ✨String Slicing:
Computer = "Computer is a thing which can compute."
print(Computer)
print(len(Computer)) # To know the length.
print(Computer[23])
print(Computer[4:100]) # Last Range can be taken as much as we want.
print(Computer[-38:-19]) # Negative range will take the range from the last number.
print(Computer[-38:-1]) # Negative range will take the range from the last number.
print(Computer[::-1]) # To reverse any string.
Computer1 = "C1o1m1p1u1t1e1r  1i1s  1a  1t1h1i1n1g1  w1h1i1c1h1  c1a1n  1c1o1m1p1u1t1e1."
print(Computer1[0:100:2]) # For Gaping in string.
# <<<---String Operators & String Slicing--->>>
