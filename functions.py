#FUNCTIONS- A block of reusable code that is used to perform a specific action.
    #place () after the function name to call it.
# def happy_birthday():
#     print("Happy Birthday to you!")
#     print("Happy Birthday to you!")
#     print("Happy Birthday dear friend!")
#     print("Happy Birthday to you!")
# happy_birthday()

#using arguments
# def happy_birthday(name):
#     print(f"Happy Birthday to you, {name}!")
#     print("Happy Birthday to you!")
# happy_birthday("Bro")

#using many names 
# def happy_birthday(name):
#     print(f"Happy Birthday to you! {name} ")

# happy_birthday("Chetana")
# happy_birthday("Nishu")

#using many arguments
# def happy_birthday(name,age):
#     print(f"Happy Birthday to you! {name} and you are {age} years old!")

# happy_birthday("Chetana",21)
# happy_birthday("Nishu",18)

# def display_invoice(username,amount,due_date):
#     print(f"Hello, {username}")
#     print(f"Your bill is ${amount:.2f} and is due: {due_date}")
# display_invoice("Joe",87.34,"01/01/2023")

#RETURN - The return statement is used to exit a function and return a value.
# def add(x,y):
#     z = x + y
#     return z
# print(add(1,2))

#complex function
# def create_name(first,last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last
# full_name = create_name("chetana","patil")
# print(full_name)