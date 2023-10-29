import pip._vendor.requests as requests
import json
import urllib.parse

url = "https://opendata.tailte.ie/api/Property/GetProperties?Fields=*&LocalAuthority=WICKLOW%20COUNTY%20COUNCIL&CategorySelected=OFFICE&Format=json&Download=false"


ParamatersDict = {
   "Download":"false",
   "Format":"json",
   "CategorySelected":"OFFICE",
   "LocalAuthority":"WICKLOW COUNTY COUNCIL",
   "Fields":"LocalAuthority , Category, Level, AreaPerFloor, NavTotal, CarPark, PropertyNumber"
}

#Fields=*&LocalAuthority=WICKLOW%20COUNTY%20COUNCIL&CategorySelected=OFFICE&Format=json&Download=false
def getAll():
    parameters = urllib.parse.urlencode(ParamatersDict)
    #print(parameters)
    fullurl = url + "?" + parameters
    response = requests.get(fullurl)
    return response.json()


if __name__ =="__main__":
    with open ("valoff.json", "wt") as fp:
        print (json.dumps(getAll()), file=fp)


