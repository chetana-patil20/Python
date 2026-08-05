#Logical Operators : These are used to combine conditional statements and return a boolean result (True or False). The common logical operators in Python are: and , or , not

#or : returns True if at least one of the conditions is True
print(True or False)  # Output: True
print(False or False)  # Output: False

#and : returns True if both conditions are True
print(True and True)  # Output: True
print(True and False)  # Output: False

#not : returns the opposite of the boolean value
print(not True)  # Output: False
print(not False)  # Output: True

#Example on or :
age = int(input("Enter your age :"))
if age < 18 or age > 65:
    print("You are not eligible for the program.")
else:
    print("You are eligible for the program.")

#Example on and:
income = int(input("Enter your income :"))
if income > 50000 and income < 100000:
    print("You are eligible for the loan.")
else:
    print("You are not eligible for the loan.")

#Example on not:
is_student = input("Are you a student? (yes/no) :")
if not is_student.lower() == "yes":
    print("You are not eligible for the student discount.")
else:
    print("You are eligible for the student discount.")