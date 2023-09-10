print("Hello World!😉")
# ✨Warm Up
Planets_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(Planets_list)
print(type(Planets_list)) # To Know type.
print(len(Planets_list)) # To Know length.
print(set(Planets_list)) # Type-Casting
print(tuple()(Planets_list)) # Type-Casting

# ✨List Methods:
'''
Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
'''
# Append:
Planets_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(Planets_list)
Planets_list.append("Pluto")
print(Planets_list)

# Insert: (More useful than others...)
Planets_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(Planets_list)
Planets_list.insert(9, "Pluto")
print(Planets_list)
Planets_list.insert(0, "Pluto") #Will Fill the place with inserted object.
print(Planets_list)

# Clear:
Planets_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(Planets_list)
Planets_list.clear()
print(Planets_list)

# Pop:
Planets_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(Planets_list)
Planets_list.pop(3)
print(Planets_list)

# Remove
Planets_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(Planets_list)
Planets_list.remove("Earth")
print(Planets_list)

# Del
Planets_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(Planets_list)
# del Planets_list
print(Planets_list)

# Count:
Planets_list = ["Mercury", "Venus", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(Planets_list)
Planets_list.count("Venus") # Counts how many time it exist in the list..

# Reverse Method:
Planets_list = ["Mercury", "Venus", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(Planets_list)
Planets_list.reverse()
print(Planets_list)
# The Other Methods should be practice by ownself. But all of the methods will not needed for coding...
# <<<---List Methods--->>>