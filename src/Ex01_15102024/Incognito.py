from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_chrome_options():
    chrome_option=Options()
    chrome_option.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_option)
    chrome_option.add_argument("--headless")
    driver.get("https://katalon-demo-cura.herokuapp.com/")
