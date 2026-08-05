#Given a list of numbers : [101,105,102,101,108,105,110] .Print all the unique numbers in the list using set() function.

numbers = [101, 105, 102, 101, 108, 105, 110]
unique_numbers = set(numbers)
print(unique_numbers)

#Given employee records in the form of a list of tuples contains: {Employee ID, Employee Name, Employee Salary}.Example=[(101, 'John', 50000), (102, 'Alice', 60000), (103, 'Bob', 55000)] Ask user to enter Employee ID and search it inside records and print the employee details if found otherwise print "Employee not found".

employee_records = [(101, 'John', 50000), (102, 'Alice', 60000), (103, 'Bob', 55000)]
employee_id = int(input("Enter Employee ID to search: "))
found = False
for record in employee_records:
    if record[0] == employee_id:
        print(f"Employee ID: {record[0]}, Name: {record[1]}, Salary: {record[2]}")
        found = True
        break
if not found:
    print("Employee not found")