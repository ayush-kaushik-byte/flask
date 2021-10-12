import requests
import json

URL = "http://127.0.0.1:5000/item"
URL2 = "http://127.0.0.1:5000/items"
headers = {"Content-Type": "application/json"}
AUTH = "http://127.0.0.1:5000/auth"

cred = {
	'username': 'Bob',
	'password': 'asdf'
}
resp1 = requests.post(AUTH, headers=headers, data=json.dumps(cred))
access_token = json.loads(resp1.text)['access_token']
headers['Authorization'] = f'JWT {access_token}'

item = {
	"price": "700"
}
resp1 = requests.post(f"{URL}/chair", headers=headers, data=json.dumps(item))
print(resp1.text)

item = {
	"price": "1200"
}
resp1 = requests.put(f"{URL}/chair", headers=headers, data=json.dumps(item))
print(resp1.text)

resp1 = requests.get(f"{URL}/chair", headers=headers)
print(resp1.text)

resp1 = requests.get(f"{URL}/laptop", headers=headers)
print(resp1.text)

resp1 = requests.delete(f"{URL}/chair", headers=headers)
print(resp1.text)

resp1 = requests.get(URL2, headers=headers)
print(resp1.text)
