import requests

url = 'https://swapi.dev/api/people/1'
response = requests.get(url)
response_json = response.json()

name = response_json['name']
height = response_json['height']
gender = response_json['gender']

print(response_json)
print()
print(name)
print(height)
print(gender)
