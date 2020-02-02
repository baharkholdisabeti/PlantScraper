# Bahar Kholdi-Sabeti
# February 1, 2020
# Web scraper for plant names and urls to each plant's data
from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.guide-to-houseplants.com/house-plants-encyclopedia-a-z.html?fbclid=IwAR3lk_1IC9iYRFRWFLMYlzRV0IG2Ea00n7Ogq4p6zUV4Tu5PKsUKegQK_S0'
response = requests.get(url, timeout=5)
soup = BeautifulSoup(response.content, "html.parser")
plantArr = []

for plants in soup.findAll('a'):
    if plants.text == "Home":
        break
    elif plants.text != "Guide to Houseplants" and plants.text != "Return to top of House Plants Encyclopedia A-Z":
        plantObject = {
            "name": plants.text,
            "link": plants.get('href')
        }
        print(plantObject)
        plantArr.append(plantObject)

with open('nameData.json', 'w') as outfile:
    json.dump(plantArr, outfile)
