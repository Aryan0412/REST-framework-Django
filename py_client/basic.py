import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={'Name' : 'Aryan', 'age' : 21})
print('>>>>>>>>>>>>>>>',get_response.json())