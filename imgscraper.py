# Bahar Kholdi-Sabeti
# February 1, 2020
# Web scraper for plant images
from bs4 import BeautifulSoup
import requests
import json
from PIL import Image

imgArr = []
# open json file
with open('nameData.json') as json_data:
    jsonData = json.load(json_data)

    for i in jsonData:
        divChild = 0
        url = i['link'];
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, "html.parser")

        div = soup.find('div', {'class': "ImageBlock ImageBlockCenter"})
        if div == None:
            div = soup.find('div', {'class': "ImageBlock ImageBlockRight"})
            if div == None:
                div = soup.find('div', {'class': "ImageBlock ImageBlockLeft"})
        if div != None:
            #divChild = (div.img).find('img')
            divChild = (div.img).get('data-pin-media')
            #print(divChild)
        else:
            divChild = "noimgplant.jpg"
        imgObject = {
            "name": i['name'],
            "link": i['link'],
            "pic": divChild
        }
        imgArr.append(imgObject)

    with open ('imgData.json', 'w') as outfile:
        json.dump(imgArr, outfile)
