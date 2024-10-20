from selenium import webdriver
import pytest
import allure

def test_lab02():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    print("url",driver.current_url)
    print("title",driver.title)
    page_source_data= driver.page_source
    assert "CURA Healthcare Service" in page_source_data
    print(page_source_data)
