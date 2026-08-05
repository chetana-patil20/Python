#list : A list is a collection of items that are ordered and mutable in Python.
# we use square brackets [] to define a list and separate the items with commas.
# lists can contain items of different data types, including numbers, strings, and other lists.

my_list = [1, 2, 3, 'A', 4, 5]
print(my_list, type(my_list))  # Output: [1, 2, 3, 'A', 4, 5] <class 'list'>

#List Operations:
#1. Accessing Elements: You can access elements in a list using their index. Index starts from 0 for the first element, 1 for the second, and so on. You can also use negative indexing to access elements from the end of the list.
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: 5

#2. Modifying Elements: You can change the value of an element in a list by assigning a new value to its index.
my_list[3] = 'B'
print(my_list)  # Output: [1, 2, 3, 'B', 4, 5]

#3. Adding Elements: You can add elements to a list using the append() method to add an element at the end, or the insert() method to add an element at a specific index.
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 'B', 4, 5, 6]

#4. Removing Elements: You can remove elements from a list using the remove() method to remove a specific value, or the pop() method to remove an element at a specific index.
my_list.remove('B')
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

#5. Slicing: You can extract a portion of a list using slicing. The syntax is list[start:end], where start is the index of the first element to include, and end is the index of the first element to exclude.
print(my_list[1:4])  # Output: [2, 3, 4]

#6. Length: You can find the number of elements in a list using the len() function.
print(len(my_list))  # Output: 6

#7. Iterating: You can iterate over the elements of a list using a for loop.
for item in my_list:
    print(item)

#8. List Comprehension: You can create a new list by applying an expression to each element of an existing list using list comprehension.
squared_list = [x**2 for x in my_list]
print(squared_list)  # Output: [1, 4, 9, 16, 25, 36]

#9. Checking Membership: You can check if an element is in a list using the in keyword.
print(3 in my_list)  # Output: True

#10. Sorting: You can sort a list in ascending order using the sort() method or the sorted() function.
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

#11. Reversing: You can reverse the order of elements in a list using the reverse() method.
my_list.reverse()
print(my_list)  # Output: [6, 5, 4, 3, 2, 1]

#12. Copying: You can create a shallow copy of a list using the copy() method or the list() constructor.
copied_list = my_list.copy()
print(copied_list)  # Output: [6, 5, 4, 3, 2, 1]

#13. Clearing: You can remove all elements from a list using the clear() method.
my_list.clear()
print(my_list)  # Output: []

#14. Concatenation: You can concatenate two lists using the + operator.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list = list1 + list2
print(list)  # Output: [1, 2, 3, 4, 5, 6]

#15. Repetition: You can repeat the elements of a list using the * operator.
repeated_list = list1 * 2
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3]

