#Strings : A string is a sequence of characters. In Python, strings are enclosed in either single quotes (' ') or double quotes (" ").

#Example of a string
# name = "Tony"

#strings are immutable 
#Example :
# name = "Tony Shark"
# print(name.upper())
# print(name)

#string operations
#Concatenation : Joining two or more strings together using the + operator.
name = "Tony" +" " + "Shark"
print(name )

#Repetition : Repeating a string multiple times using the * operator.
name = "Tony" * 3
print(name)

#Indexing : Accessing individual characters in a string using their index positions. Indexing starts from 0 for the first character.
#positive indexing
text = "Python"
print(text[0])  # Output: P
print(text[1])  # Output: y

#negative indexing
print(text[-1])  # Output: n
print(text[-2])  # Output: o

#Slicing : Extracting a portion of a string using the slice notation [start:end]. The start index is inclusive, while the end index is exclusive.
text = "Python"
print(text[0:4])  # Output: Pyth
print(text[2:5])  # Output: tho
print(text[:3])   # Output: Pyt
print(text[3:])   # Output: hon

#Comparison : Comparing strings using comparison operators (==, !=, <, >, <=, >=) based on their lexicographical order.
print("Py" in "Python")  # Output: True
print("apple" < "banana")  # Output: True

#Built in string methods : Python provides a wide range of built-in string methods that allow you to manipulate and perform operations on strings. Some commonly used string methods include:
# upper() : Converts all characters in a string to uppercase.
text = "hello"
print(text.upper())#Output: HELLO

#lower() : Converts all characters in a string to lowercase.
text = "HELLO"
print(text.lower())#Output: hello

#isalpha() : Checks if all characters in a string are alphabetic.
text = "Hello"
print(text.isalpha())#Output: True

#isdigit() : Checks if all characters in a string are digits.
text = "12345"
print(text.isdigit())#Output: True

#isnumeric() : Checks if all characters in a string are numeric.
text = "12345"
print(text.isnumeric())#Output: True

#startswith() : Checks if a string starts with a specified prefix.
text = "Hello, World!"
print(text.startswith("Hello"))#Output: True

#title() : Converts the first character of each word in a string to uppercase and the rest to lowercase.
text = "hello world"
print(text.title())#Output: Hello World

#capitalize() : Converts the first character of a string to uppercase and the rest to lowercase.
text = "hello world"
print(text.capitalize())#Output: Hello world

#strip() : Removes leading and trailing whitespace characters from a string.
text = "   Hello, World!   "
print(text.strip())#Output: Hello, World!

#find() : Returns the index of the first occurrence of a specified substring in a string. If the substring is not found, it returns -1.
text = "Hello, World!"
print(text.find("World"))#Output: 7

#count() : Returns the number of occurrences of a specified substring in a string.
text = "banana"
print(text.count("a"))#Output: 3

#replace() : Replaces all occurrences of a specified substring with another substring in a string.
text = "Hello, World!"
print(text.replace("World", "Python"))#Output: Hello, Python!

#split() : Splits a string into a list of substrings based on a specified delimiter.
text = "Hello, World!"
print(text.split(","))#Output: ['Hello', ' World!']

#join() : Joins a list of strings into a single string using a specified delimiter.
text_list = ["Hello", "World"]
print(" ".join(text_list))#Output: Hello World

#format() : Formats a string by replacing placeholders with specified values.
name = "Tony"
age = 25
print("My name is {} and I am {} years old.".format(name, age))#Output: My name is Tony and I am 25 years old.

