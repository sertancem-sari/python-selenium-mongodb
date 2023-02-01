from selenium import webdriver
import time
def alarm_func():
    driver = webdriver.Chrome()
    driver.get('http://localhost:3500/alarms')
    time.sleep(100)