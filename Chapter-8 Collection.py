print("Hello World!😉")
# ✨Collection in Python: There are four collection data types in the Python programming language:
'''
List: List is a collection which is ordered and changeable. Allows duplicate members.
Tuple: Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set: Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictinary: Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

# ✨List: The list is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets.[It is Changable...]
Planets_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(Planets_list)
print(type(Planets_list))
print(len(Planets_list))

# ✨Tuple: The list is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between first brackets.(It is not changable...)
Planets_tuple = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
print(Planets_tuple)
print(type(Planets_tuple))
print(len(Planets_tuple))

# ✨Set: {It is the collection of distinct objects between second bracket.}
Planets_set = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
print(Planets_set)
print(type(Planets_set))
print(len(Planets_set))

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
print(type(Planets_dict.items))
# print(Planets_dict.keys())
# print(Planets_dict.values())
# print(len(Planets_dict)) # It represents the number of elements.
