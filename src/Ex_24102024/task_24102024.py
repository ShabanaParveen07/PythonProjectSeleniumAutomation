import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_radio_checkbox():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    first_name=driver.find_element(By.XPATH,"//input[@name='firstname']")
    first_name.send_keys("shabana")
    last_name=driver.find_element(By.XPATH,"//input[@name='lastname']")
    last_name.send_keys("parveen")

    driver.find_element(By.XPATH,"// input[ @ value = 'Female']").click()
    driver.find_element(By.XPATH,"//input[@id='exp-2']").click()
    driver.find_element(By.XPATH,"//input[@value='Automation Tester']").click()
    driver.find_element(By.XPATH,"//input[@value='Selenium Webdriver']").click()
    time.sleep(5)


