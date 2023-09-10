print("Hello World!😉")
# ✨Warm Up
Planets_set = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
print(Planets_set)
print(type(Planets_set)) # To Know type.
print(len(Planets_set)) # To Know length.
print(set(Planets_set)) # Type-Casting
print(list(Planets_set)) # Type-Casting

# ✨Set Slicing:
# Set Slicing: # It is same to string slicing.
Planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
print(len(Planets))  # len function used to know the the number of items in a set.
print(Planets[0])
print(Planets[1])
print(Planets[0:7])
print(Planets[0:1000])  # No problem for the last range if it is infinity also but the 1st range matters.
print(Planets[-2])  # It will take reversed range
print(Planets[-1])  # It will take reversed range
print(Planets[::-1]) # To reverse any set
print(Planets[::2]) # Create Gaps
print(Planets[::3]) # Create Gaps

# <<<---Set Slicing--->>>