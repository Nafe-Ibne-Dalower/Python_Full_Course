from optparse import Values


print("Hello World😉😉😉")

# ✨Dictionary: Dictionaries are collections of items that have a “key” and a “value”.
Planets_dict = {
    "P1" : "Mercury",
    "P2" : "Venus",
    "P3" : "Earth",
    "P4" : "Mars",
    "P5" : "Jupiter",
    "P6" : "Saturn",
    "P7" : "Uranus",
    "P8" : "Neptune",
}
# print(Planets_dict)
print(Planets_dict.items())
print(Planets_dict.keys())
print(Planets_dict.values())
print(len(Planets_dict)) # It represents the number of elements.

# Nested Dictionary...
Student = {1:{"name":"Nafe","age":16},
          2:{"name":"Jimam","age":8}
}
print(Student[1].keys())
print(Student[1].values())