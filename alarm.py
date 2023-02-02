from selenium import webdriver
import time
def alarm_func():
    driver = webdriver.Chrome()
    driver.get('http://localhost:3500/alarms')
    driver.maximize_window()
    time.sleep(100)