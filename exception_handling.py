#Exception handling in Python allows you to handle errors gracefully and prevent your program from crashing. You can use try-except blocks to catch and handle exceptions.

#Example:
try:
 number = int(input("Enter a number: "))
 print(1/number)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except TypeError:
    print("Error: Invalid type. Please enter a valid number.")
except Exception:
    print("An unexpected error occurred.")
finally:
    print("Execution completed.")