import json


# write your code here
json_string = input()

py_obj = json.loads(json_string)

print(type(py_obj))

print(py_obj)
