#Dictionary : A dictionary is a collection of key value pair 
#in Python. It is unordered, mutable, and indexed. Dictionaries are defined using curly braces {} with key-value pairs separated by colons (:). Each key in a dictionary must be unique and immutable (e.g., strings, numbers, tuples), while values can be of any data type.

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict, type(my_dict))  # Output: {'name': 'John', 'age': 30, 'city': 'New York'} <class 'dict'>

#Dictionary Operations:
#1. Accessing Values: You can access values in a dictionary using their keys.
print(my_dict['name'])  # Output: John
print(my_dict.get('age'))  # Output: 30

#2. Modifying Values: You can change the value of a key in a dictionary by assigning a new value to it.
my_dict['age'] = 31
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

#3. Adding Key-Value Pairs: You can add new key-value pairs to a dictionary by assigning a value to a new key.
my_dict['country'] = 'USA'
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA'}

#4. Removing Key-Value Pairs: You can remove key-value pairs from a dictionary using the del statement or the pop() method.
del my_dict['city']
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'country': 'USA'}
my_dict.pop('age')
print(my_dict)  # Output: {'name': 'John', 'country': 'USA'}

#5. Length: You can find the number of key-value pairs in a dictionary using the len() function.
print(len(my_dict))  # Output: 2

#6. Iterating: You can iterate over the keys, values, or key-value pairs of a dictionary using a for loop.
for key in my_dict:
    print(key, my_dict[key])  # Output: name John, country USA

for key, value in my_dict.items():
    print(key, value)  # Output: name John, country USA

#7. Checking Membership: You can check if a key is in a dictionary using the in keyword.
print('name' in my_dict)  # Output: True

#8. Copying: You can create a shallow copy of a dictionary using the copy() method.
copied_dict = my_dict.copy()
print(copied_dict)  # Output: {'name': 'John', 'country': 'USA'}

#9. Clearing: You can remove all key-value pairs from a dictionary using the clear() method.
my_dict.clear()
print(my_dict)  # Output: {}

