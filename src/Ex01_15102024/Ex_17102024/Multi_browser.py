import time
from selenium import webdriver
import allure

@allure.title("Test case for Chrome")
def test_chrome():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    print(driver.title)
    time.sleep(10)

@allure.title("Test case for Firefox")
def test_firefox():
    driver = webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    print(driver.current_url)
    time.sleep(10)

@allure.title("Test case for Firefox")
def test_edge():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    print(driver.maximize_window)
    time.sleep(10)