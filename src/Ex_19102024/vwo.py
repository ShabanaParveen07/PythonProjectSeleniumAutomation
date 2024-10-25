# [Assignment] - Invalid error message Capture for the Login Page of VWO.com
# Fetch the locators - https://app.vwo.com/
# Create a Python Project
# Add the Allure Report (Allure Pytest)
# Automate the two Test cases of VWO.com
# Invalid Username and Valid Password.
# Capture the error and pass the test.
# Run them and share results.
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.title("Error message validation in VWO log in page")

def test_vwo_login():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    user_name=driver.find_element(By.ID,"login-username")
    user_name.send_keys("qwert@test.com")

    user_pwd=driver.find_element(By.NAME,"password")
    user_pwd.send_keys("test123")

    click_submit= driver.find_element(By.ID,"js-login-btn")
    click_submit.click()
    time.sleep(5)
    error_msg=driver.find_element(By.ID,"js-notification-box-msg")
    print(error_msg)
    assert error_msg.text=="Your email, password, IP address or location did not match"
