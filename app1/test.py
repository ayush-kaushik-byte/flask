import requests
import json

URL = "http://127.0.0.1:5000/store"
headers = {"Content-Type": "application/json"}

resp1 = requests.get(URL)
print(resp1.text)

resp2 = requests.get(f"{URL}/My Wonderful Store/item")
print(resp2.text)

resp3 = requests.get(f"{URL}/My Wonderful Store")
print(resp3.text)

data = {"name":"new store"}
resp4 = requests.post(URL, headers=headers, data=json.dumps(data))
print(resp4.text)

item = {
	"name": "almond butter",
	"price": "700"
}
resp5 = requests.post(url=f"{URL}/My Wonderful Store/item",
					headers=headers,
					data=json.dumps(item))
print(resp5.text)