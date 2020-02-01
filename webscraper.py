# Bahar Kholdi-Sabeti
# February 1, 2020
# Web scraper for plant info
# Parses data from
from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.guide-to-houseplants.com/house-plants-encyclopedia-a-z.html?fbclid=IwAR3lk_1IC9iYRFRWFLMYlzRV0IG2Ea00n7Ogq4p6zUV4Tu5PKsUKegQK_S0'
response = requests.get(url, timeout=5)
soup = BeautifulSoup(response.content, "html.parser")
plantArr = []

# all illnesses have h2 tags and are in class "module__title"
# here we will fetch the illness titles
for plants in soup.findAll('a'):
    if plants.text == "Home":
        break
    plantObject = {
        "name": plants.text,
        "link": plants.get('href')
    }
    print(plantObject)
    plantArr.append(plantObject)

with open('scraperData.json', 'w') as outfile:
    json.dump(plantArr, outfile)
