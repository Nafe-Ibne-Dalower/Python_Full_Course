print("Hello World!😉")
# We should learn the concepts of "Placholeder" before starting Format Method.
# The Placeholders
# The placeholders can be identified using named indexes {}, numbered indexes {}, or even empty placeholders {}.
'''
Formatting Types
Inside the placeholders you can add a formatting type to format the result:

:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
:b		Binary format
:c		Converts the value into the corresponding unicode character
:d		Decimal format
:e		Scientific format, with a lower case e
:E		Scientific format, with an upper case E
:f		Fix point number format
:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%		Percentage format
'''
# Format Method.
# Type-01(Inline)
Me = "My name is {name} & age is {age}.".format(name = "Nafe", age = "15")
print(Me)
# Type-02(Multi-Line)
Me = "My name is {name} & age is {age}."
print(Me.format(name = "Nafe", age = "15"))

# Using Placeholders:
# Using :<
Me = "My name is {:>12} & age is {:>12}."
print(Me.format("Nafe", 15))
# Using :^
Me = "My name is {:^12} & age is {:^12}."
print(Me.format("Nafe", 15))
# Using :=
Me = "My age is {:=12}."
print(Me.format(+15))
print(Me.format(-15))
# Using :b
Binary = "The binary version of {0} is {0:b}"
print(Me.format(5))
print(Me.format(10))
print(Me.format(15))


# The Other Methods should be practice by ownself. But all of the methods will not needed for coding...
# <<<---Format Methods--->>>
