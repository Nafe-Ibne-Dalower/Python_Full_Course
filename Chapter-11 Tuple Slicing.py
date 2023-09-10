print("Hello World!😉")
# ✨Warm Up
Planets_tuple = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
print(Planets_tuple)
print(type(Planets_tuple)) # To Know type.
print(len(Planets_tuple)) # To Know length.
print(set(Planets_tuple)) # Type-Casting
print(list(Planets_tuple)) # Type-Casting

# ✨Tuple Slicing:
# Tuple Slicing: # It is same to string slicing.
Planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
print(len(Planets))  # len function used to know the the number of items in a tuple.
print(Planets[0])
print(Planets[1])
print(Planets[0:7])
print(Planets[0:1000])  # No problem for the last range if it is infinity also but the 1st range matters.
print(Planets[-2])  # It will take reversed range
print(Planets[-1])  # It will take reversed range
print(Planets[::-1]) # To reverse any tuple
print(Planets[::2]) # Create Gaps
print(Planets[::3]) # Create Gaps

# <<<---Tuple Slicing--->>>