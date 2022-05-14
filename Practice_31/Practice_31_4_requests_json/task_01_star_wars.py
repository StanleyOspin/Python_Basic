import requests
import json

my_request = requests.get('https://swapi.dev/api/people/3/')
#print(my_request.text)

data = json.loads(my_request.text)
data['name'] = 'Vasya'
#print(data)

with open('test_file.json', 'w') as file:
  json.dump(data, file, indent=4)

with open('test_file.json', 'r') as file:
  data_1 = json.load(file)
print(data_1)
print()

my_request_2 = requests.get('https://swapi.dev/api/planets/8/')
data_2 = json.loads(my_request_2.text)

with open('test_file_2.json', 'w') as file:
  json.dump(data_2, file, indent=4)

with open('test_file_2.json', 'r') as file:
  data_2 = json.load(file)
print(data_2)