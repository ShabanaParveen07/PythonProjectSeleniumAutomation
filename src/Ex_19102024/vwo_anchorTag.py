from selenium import webdriver
from selenium.webdriver.common.by import By

def test_vwo_free_trial():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    #anchore_tag_element = driver.find_element(By.LINK_TEXT,"Start a free trial")
    #anchore_tag_element.click()

    #assert driver.current_url =="https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    buttons=driver.find_elements(By.TAG_NAME,"button")
    print(len(buttons))
    for i in buttons:
        print(i.text)
