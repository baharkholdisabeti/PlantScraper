#Bahar Kholdi-Sabeti
#Jan. 11, 2020
# data parser for illness list
import json

# open json file
with open('nameData.json') as json_data:
    jsonData = json.load(json_data)
    # print illness titles
    for i in jsonData:
        print (i['name'])
