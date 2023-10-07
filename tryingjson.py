import json
import requests
url="https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
print(data)

with open ("bitcoindump.json", "w") as fp:
    json.dump(data, fp)


euroobject = data["bpi"]["EUR"]
print(euroobject["rate"])


