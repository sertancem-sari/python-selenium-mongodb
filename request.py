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
    item=[]
    log_alert =[]
    """ log_port =[]
    log_desc = []
    log_date =[] """

    value =soup.find_all('tr')
    
    for tr in value:
        item = tr.find_all('td')
       
    print(item)
    for i in range(5):
        if i == 3:
            continue
        log_alert.append(item[i].text)
    
    """ log_alert.append(item[0].text)
    log_port.append(item[1].text)
    log_desc.append(item[2].text)
    log_date.append(item[4].text) """

    def write_json(data, filename='data.json'):
        with open (filename,"w") as f:
            json.dump(data, f, indent =4)

    with open ("data.json") as json_file:
        data = json.load(json_file)
        data.append({"logs": log_alert})
        """ data.append({"log_desc": log_desc[0]})
        data.append({"log_port": log_port[0]})
        data.append({"log_date": log_date[0]}) """

    write_json(data)

