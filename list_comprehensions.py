#List comprehensions : A concise way to create lists in Python. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.
#Basic syntax: [expression for item in iterable if condition == True]
#Compact and easy to read, list comprehensions are often more efficient than using traditional loops and list manipulation methods.

#Examples :
# doubles = [x*2 for x in range(1,11)]
# print(doubles)
# triples = [x*3 for x in range(1,11)]
# print(triples)
# squares = [ x*x for x in range(1,6)]
# print(squares)

#Example:
# fruits = ["apple", "banana", "cherry"]
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)

# fruits = ["apple", "banana", "cherry"]
# fruits_char = [ fruit[0] for fruit in fruits]
# print(fruits_char)

#with conditions: [expression for item in iterable if condition == True]
# even = [x for x in range(1,11) if x%2 ==0]
# print(even)
# odd = [ x for x in range(1,11) if x%2 !=0]
# print(odd)

#Nested list comprehensions: List comprehensions can be nested to create more complex lists. For example, you can use a nested list comprehension to flatten a list of lists or to create a matrix.
#Syntax : [expression for item in iterable1 for item2 in iterable2 if condition == True]
#Example :
# matrix = [ [i*j for j in range(1,4)] for i in range(1,4)]
# print(matrix)

#example for positive and negative numbers:
# numbers = [1, -2, 3, -4, 5]
# positive_numbers = [num for num in numbers if num > 0]
# negative_numbers = [num for num in numbers if num < 0]
# print("Positive numbers:", positive_numbers)
# print("Negative numbers:", negative_numbers)