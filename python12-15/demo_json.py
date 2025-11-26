import json

with open("sample1.json") as f:
    data = json.load(f)
print(data['name'])
print(data['city'])
print(data['hobbies'])