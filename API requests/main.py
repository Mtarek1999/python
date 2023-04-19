import requests

response = requests.get("https://api.github.com/users/Mtarek1999/projects")
my_projects = response.json()
print(response.text)
print(response.json())
print(type(response.text))
print(type(response.json()))