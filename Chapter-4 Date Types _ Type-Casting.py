print("Hello World!😉")
'''
✨✨✨Data Types..
Text Type:	str
Numeric Types :	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type  :	dict
Set Types     :	set, frozenset
Boolean Type  :	bool
Binary Types  :	bytes, bytearray, memoryview
'''
# Text Types...
a = "Nafe" #String
print(type(a))

# Numeric Types...
a = 12 #Integer
b = 12.0 #Float
c = 2j + 10 #Complex
print(type(a))
print(type(b))
print(type(c))

# Sequence Types...
Planets_tuple = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Urenus", "Neptune")
Planets_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Urenus", "Neptune"]
Planets_set = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Urenus", "Neptune"}
Planets_dic= {
    "P1":"Mercury",
    "P1":"Mercury",
    "P1":"Mercury",
    "P1":"Mercury",
    "P1":"Mercury",
    "P1":"Mercury",
    "P1":"Mercury",
    "P1":"Mercury"
}
print(type(Planets_tuple))
print(type(Planets_list))
print(type(Planets_set))
print(type(Planets_dic))


# ✨✨✨Type-Casting:Type Casting is a method by which we can change the data type.
# Type Casting in String.String Couldn't be changed to numeric number by type-casting.
a = "Nafe" #String
print(type(a))
b = list(a)
print(type(b))


# Type Casting in Numeric Number.
# Complex
a = 2j + 5
print(type(a)) # Complex ---Integer/FLoat isn't possible.
# Integer
b = 10
print(type(b))
x = float(b) # Integer--Float
print(x)
print(type(x))
y = str(b) # Integer--String
print(y)
print(type(y))
# Float
c = 12.5
print(c)
print(type(c))
x = str(c) # Float--String
print(x)
print(type(x))
y = int(c) # Float--String
print(y)
print(type(y))

# Type Casting in Collections...
Planets_tuple = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Urenus", "Neptune")
Planets_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Urenus", "Neptune"]
Planets_set = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Urenus", "Neptune"}
print(type(Planets_tuple))
print(type(Planets_list))
print(type(Planets_set))

# Tuple--List---Set
Planets_tuple = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Urenus", "Neptune")
print(type(Planets_tuple))
x = str(Planets_tuple)
print(type(x))
y = list(Planets_tuple)
print(y)
print(type(y))
z = set(Planets_tuple)
print(z)
print(type(z))
# <<<---Data Types & Type-Casting--->>>
