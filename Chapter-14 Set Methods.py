print("Hello World!😉")
# ✨Warm Up
Planets_set = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
print(Planets_set)
print(type(Planets_set)) # To Know type.
print(len(Planets_set)) # To Know length.
print(set(Planets_set)) # Type-Casting
print(list(Planets_set)) # Type-Casting

# ✨✨✨Set Methods:
'''
Method	                        Description
add()	                        Adds an element to the set
clear()	                        Removes all the elements from the set
pop()	                        Removes an element from the set
remove()	                    Removes the specified element
copy()	                        Returns a copy of the set
difference()	                Returns a set containing the difference between two or more sets
difference_update()	            Removes the items in this set that are also included in another, specified set
discard()	                    Remove the specified item

isdisjoint()	                Returns whether two sets have a intersection or not
issubset()	                    Returns whether another set contains this set or not
issuperset()

intersection()	                Returns a set, that is the intersection of two or more sets
intersection_update()	        Removes the items in this set that are not present in other, specified set(s)

symmetric_difference()	        Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	                        Return a set containing the union of sets
update()	                    Update the set with another set, or any other iterable
'''

# Add Method...
S1 = {34, 56, 76, 89, 90}
S1.add(80)
print(S1)

# Pop Method: 
S1 = {34, 56, 56, 76, 89, 90}
S1.pop()
print(S1)

# Remove Method:
S1 = {34, 56, 76, 89, 90}
S1.remove(56) 
print(S1) 

# Discard Method:
S1 = {34, 56, 76, 89, 90}
S1.discard(56)
print(S1)

# Clear Method:
# S1 = {34, 56, 76, 89, 90}
# S1.clear()
# print(S1)

# Del Method:
# S1 = {34, 56, 76, 89, 90}
# del S1

# Difference Method:
S1 = {34, 56, 76, 89, 59}
S2 = {33, 56, 78, 88, 55}
x = S1.difference(S2)
type(x)
print(x)

# Diiference_update Method: More Useful...
S1 = {34, 56, 76, 89, 59}
S2 = {33, 56, 78, 88, 55}
S1.difference_update(S2)
# S2.difference_update(S1)
print(S1)


# Isubset Method:
S1 = {1, 2, 3 , 4, 5, 6, 7}
S2 = {5,6,7}
S3 = {10, 12, 13}
S1.issubset(S3)
S1.issubset(S2)
S2.issubset(S1)

# isdisjoint Method
S1 = {1, 2, 3 , 4, 5, 6, 7}
S3 = {10, 12, 13}
S1.isdisjoint(S3)
S3.isdisjoint(S1)

S1 = {1,2,3,4}
S2 = {1,2,3,4}
S1.isdisjoint(S2)

# Intersection & Union Method:
S1 = {1, 2, 3 , 4, 5, 6, 7}
S2 = {5,6,7}
S3 = {8, 9, 10}
print(S1.intersection(S2))
print(S2.intersection(S1))
print(S1.union(S3))

# The Other Methods should be practice by ownself. But all of the methods will not needed for coding...
# <<<---Set Methods--->>>