import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def trigger_func():

    os.environ['PATH'] +=r"C:/SeleniumDrivers"
    driver = webdriver.Chrome()
    driver.get('http://192.168.1.100/eventlog.htm')
    driver.implicitly_wait(8)

    retries = 1
    while retries <= 20:
        try:
            WebDriverWait(driver, 2).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, '/html/body/p/table'),('Input Missing (Signal Missing)')
            )
        )
            break
        except:
            driver.refresh()
            retries += 1
    
 


    
           
      


