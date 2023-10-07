import requests

import csv 

from xml.dom.minidom import parseString

retrieveTags=['TrainStatus',
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction'
            ]

url= "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
#xml url
page = requests.get(url)
# setting page equla to get request get method to the specified train xml url 
# requests.get(url,params,args)params and arg optional 

doc = parseString(page.content)
# check to see if code works

print(doc.toprettyxml(),end ='')

with open ('train.xml','w') as xmlfp:
    doc.writexml(xmlfp)

#creating and writing train data to a file called train.xml  using doc.writexml(file)

#traincodenode= doc.getElementsByTagName("TrainCode").item(0)
#traincode = traincodenode.firstChild.nodeValue.strip()
#print(traincode)

with open ('wee02_trains.csv', mode = 'w', newline = '') as train_file:
    train_writer = csv.writer(train_file, delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        datalist = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            datalist.append(datanode.firstChild.nodeValue.strip())
            print(datalist)



