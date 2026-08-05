#tuple : A tuple is a collection of items that are ordered and immutable in Python.
# we use parentheses () to define a tuple and separate the items with commas.
#Even if we dont use parentheses, it will still be considered as a tuple. Tuples can contain items of different data types, including numbers, strings, and other tuples.
 

my_tuple = (1, 2, 3, 'A', 4, 5)
print(my_tuple, type(my_tuple))  # Output: (1, 2, 3, 'A', 4, 5) <class 'tuple'>

#Tuple Operations:
#1. Accessing Elements: You can access elements in a tuple using their index. Index starts from 0 for the first element, 1 for the second, and so on. You can also use negative indexing to access elements from the end of the tuple.
print(my_tuple[0])  # Output: 1
print(my_tuple[-1])  # Output: 5

#2. Slicing: You can extract a portion of a tuple using slicing. The syntax is tuple[start:end], where start is the index of the first element to include, and end is the index of the first element to exclude.
print(my_tuple[1:4])  # Output: (2, 3, 4)

#3. Length: You can find the number of elements in a tuple using the len() function.
print(len(my_tuple))  # Output: 6

#4. Iterating: You can iterate over the elements of a tuple using a for loop.
for item in my_tuple:
    print(item)

#5. Checking Membership: You can check if an element is in a tuple using the in keyword.
print(3 in my_tuple)  # Output: True

#6. Concatenation: You can concatenate two tuples using the + operator.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)  # Output: (1, 2, 3, 4, 5, 6)

#7. Repetition: You can repeat the elements of a tuple using the * operator.
repeated_tuple = tuple1 * 2
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3)
