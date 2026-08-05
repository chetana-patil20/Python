#JSON : Json stands for javascript object notation . It is used for configuration files and storing data 

# import json

# json_string = """
# {
#     "students": [
#         {
#             "name": "John",
#             "age": 30,
#             "city": "New York"
#         },
#         {
#             "name": "Alice",
#             "age": 25,
#             "city": "Los Angeles"
#         }
#     ]
# }
# """

# data = json.loads(json_string)
# print(data)

#Convert Python object to JSON string
# import json 
# data = {'name':'Chetana','age': 19}
# json_string = json.dumps(data)
# print(json_string)

#Convert JSON string to Python object
# import json
# json_string = '{"name": "Chetana", "age": 19}'
# data = json.loads(json_string)
# print(data)

#Reading a json file 
# import json 
# with open("data.json", "r") as f:
#     data = json.load(f)
#     print(data)

#Writing to a json file
# import json
# with open("data2.json", "w") as f:
#     json.dump(data,f)