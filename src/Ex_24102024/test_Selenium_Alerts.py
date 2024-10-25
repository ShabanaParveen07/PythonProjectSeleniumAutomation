import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_selenium_alerts():
    driver= webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()

    click_alert=driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
    click_alert.click()

    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())

    alert_box=driver.switch_to.alert
    alert_box.accept()

    result_text= driver.find_element(By.ID,"result").text
    assert result_text== "You successfully clicked an alert"
    time.sleep(5)
def test_selenium_confirm():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    element_confirm=driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']")
    element_confirm.click()

    WebDriverWait(driver=driver,timeout=5).until(EC.alert_is_present())
    alert_confirm=driver.switch_to.alert
    alert_confirm.accept()

    alert_confirm= driver.find_element(By.ID,"result").text
    assert alert_confirm =="You clicked: Ok"

    time.sleep(5)





