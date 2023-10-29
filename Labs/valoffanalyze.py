from valoffdao import getAll

PropertyData = getAll()
totalarea = 0
for entry in PropertyData:
    ValReports = entry["ValuationReport"]
    for Valreport in ValReports:
        if Valreport["FloorUse"] == "GYMNASIUM":
            totalarea += Valreport["Area"]

print(totalarea)




