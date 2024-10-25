import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def test_selenium_svg():
    driver=webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    search_element=driver.find_element(By.XPATH,"//input[@type='text']")
    search_element.send_keys("macmini")

    #WebDriverWait(driver=driver,timeout=5).until(EC.alert_is_present())

    list_svg=driver.find_elements(By.XPATH,"//*[name()='svg']")
    time.sleep(3)
    list_svg[0].click()
    time.sleep(5)



