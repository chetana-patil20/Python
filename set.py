#Set : A set is a collection of unique elements in Python. It is unordered and mutable. Sets are defined using curly braces {} or the set() constructor.
my_set = {1, 2, 3, 4, 5}
print(my_set, type(my_set))  # Output: {1, 2, 3, 4, 5} <class 'set'>

#Set Operations:
#1. Adding Elements: You can add elements to a set using the add() method.
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

#2. Removing Elements: You can remove elements from a set using the remove() method.
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}

#3. Length: You can find the number of elements in a set using the len() function.
print(len(my_set))  # Output: 5

#4. Iterating: You can iterate over the elements of a set using a for loop.
for item in my_set:
    print(item)

#5. Checking Membership: You can check if an element is in a set using the in keyword.
print(4 in my_set)  # Output: True

#6. Union: You can find the union of two sets using the | operator or the union() method.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1 | set2
print(set3)  # Output: {1, 2, 3, 4, 5}