import requests

r = requests.get(url = "http://127.0.0.1:8000/stuinfo/1/" )

data = r.json()

print(data)