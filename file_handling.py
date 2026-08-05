#python writing files(.txt,.json,.csv )
#w - write mode
# a - append mode
#r - read mode
#x - create mode


 # EX : .txt file
# txt_data = "I like pizza"
# file_path = "output.txt"
# with open(file_path,"w") as file :
#     file.write(txt_data)
#     print(f"Text file {file_path } created successfully.")


#EX : .json file
# import json
# employee = {
#     "name": "John Doe",
#     "age": 30,
#     "department": "IT",
# }
# file_path = r"C:\Users\Hp\OneDrive\Desktop\employee.json"
# try :
#     with open(file_path,"w") as file:
#         json.dump(employee,file, indent = 4)
#         print(f"JSON file {file_path} created successfully.")
# except FileExistsError:
#     print(f"Error: The file path {file_path} already exist.")

#EX : .csv file
# import csv 
# employees = [["Name","Age","Job"],
#              ["John Doe",30,"IT"],
#              ["Jane Smith",28,"HR"],
#              ["Mike Johnson",35,"Finance"]]
# file_path = r"C:\Users\Hp\OneDrive\Desktop\employees.csv"
# try:
#     with open(file_path,"w",newline="") as file:
#         writer = csv.writer(file)
#         writer.writerows(employees)
#         print(f"CSV file {file_path} created successfully.")
# except FileExistsError:
#     print(f"Error: The file path {file_path} already exist.")

#Reading a file
with open('test.txt') as file:
    print(file.read())