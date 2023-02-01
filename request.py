import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup
import json

def requests_func():
    os.environ['PATH'] += r'C:/SeleniumDrivers'
    driver = webdriver.Chrome()
    driver.get('http://192.168.1.100/eventlog.htm')
    driver.implicitly_wait(10)
    url = driver.current_url
    driver.implicitly_wait(2)
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    liste = []

    item =soup.find_all('tr')
    for x in item:
        liste.append(str(x))

    def write_json(data, filename='data.json'):
        with open (filename,"w") as f:
            json.dump(data, f, indent =4)

    with open ("data.json") as json_file:
        data = json.load(json_file)
        temp = data["value"]
        y = {"log" : liste[-1]}
        temp.append(y)

    write_json(data)

