import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def trigger_func():
    os.environ['PATH'] +=r"C:/SeleniumDrivers"

    driver = webdriver.Chrome()
    driver.get('https://onlinesaat.web.tr/saat-kac/')
    driver.implicitly_wait(8)

    WebDriverWait(driver, 100).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, '//*[@id="lbl-time"]'),('00:13:30')
        )
    )

