#Generator expression : A generator expression is a concise way to create a generator object in Python. It is similar to a list comprehension, but instead of creating a list, it creates an iterator that generates values on-the-fly. This can be more memory-efficient for large datasets.
#Basic syntax: (expression for item in iterable if condition == True)

#Examples :
squares_gen = (x*x for x in range(1,6))
print(squares_gen)