# Bahar Kholdi-Sabeti
# February 1, 2020
# Web scraper for plant info
# Parses data from
from bs4 import BeautifulSoup
import requests
import json

arrArr = [];
# open json file
light = 0
temp = 0
water = 0
soil = 0
humidity = 0
with open('imgData.json') as json_data:
    jsonData = json.load(json_data)
    # print
    #for i in jsonData:
    #    print (i['name'])

    infoArr=[]
    for i in jsonData:
        url = i['link'];
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, "html.parser")

        for info in soup.findAll('span', {'style':"background-color: transparent;"}):
            bval = info.find('b')
            if bval != None:
                if bval.text == "Light:":
                    light = info.text
                if bval.text == "Temperature:":
                    temp = info.text
                if bval.text == "Water:":
                    water = info.text
                if bval.text == "Humidity:":
                    humidity = info.text
                if bval.text == "Soil:":
                    soil = info.text

        infoObject = {
            "name": i['name'],
            "img": i['pic'],
            "light": light,
            "temp": temp,
            "water": water,
            "humidity": humidity,
            "soil": soil
        }

        arrArr.append(infoObject)
        #print(infoObject)
        infoObject = []

with open ('scraperData.json', 'w') as outfile:
    json.dump(arrArr, outfile)
