import requests
from bs4 import BeautifulSoup
import json

def requests_func():
    url_two = "https://nodejs.medium.com/"
    response = requests.get(url_two).text
    soup = BeautifulSoup(response, 'lxml')
    liste = []

    item =soup.find(id='501a')
    for x in item:
        liste.append(str(x))
        print(liste)

    def write_json(data, filename='data.json'):
        with open (filename,"w") as f:
            json.dump(data, f, indent =4)

    with open ("data.json") as json_file:
        data = json.load(json_file)
        temp = data["value"]
        y = {"key" : liste}
        temp.append(y)

    write_json(data)

