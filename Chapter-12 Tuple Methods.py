print("Hello World!😉")
# ✨Warm Up
Planets_tuple = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
print(Planets_tuple)
print(type(Planets_tuple)) # To Know type.
print(len(Planets_tuple)) # To Know length.
print(set(Planets_tuple)) # Type-Casting
print(list(Planets_tuple)) # Type-Casting

# ✨Tuple Methods:
# Python has two built-in methods that you can use on tuples.
'''
Method	    Description
count()	    Returns the number of times a specified value occurs in a tuple
index()	    Searches the tuple for a specified value and returns the position of where it was found
'''

# Count Method
Planets_tuple = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
print(Planets_tuple)
print(Planets_tuple.count("Earth")) # Counts how many time it exist in the tuple..

# Index Method
Planets_tuple = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
print(Planets_tuple)
print(Planets_tuple.index("Earth"))
print(Planets_tuple.index("Mars"))
# <<<---Tuple Methods--->>>