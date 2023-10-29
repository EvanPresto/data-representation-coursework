import pip._vendor.requests as requests
import json
import urllib.parse



url = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en'


response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    #print(data)
else:
    print('Unable to retrieve data', response.status_code)

# using method dump within json to dump the retrieved data into a file called cso_data.json 
with open ('cso_data.json', 'wt') as pd:
    json.dump(data,pd)





label = data['dataset']['dimension']['STATISTIC']['label']
print(label)
