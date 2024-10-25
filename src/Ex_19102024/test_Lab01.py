import time

import pytest
import allure
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from faker import Faker

fake = Faker()
@pytest.mark.registration
@allure.title("Create Account/Register new User")
@allure.description("Verify if User is getting registered and Success response is notified")
def test_validate_registration():
    # optns = Options()
    driver = webdriver.Chrome()
    # optns.add_argument('--start-maximized')
    # optns.add_argument("--disable-extensions")
    driver.maximize_window()
    time.sleep(3)
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    first_name = driver.find_element(By.CSS_SELECTOR, "#input-firstname")
    first_name.send_keys(fake.first_name())

    last_name = driver.find_element(By.ID, "input-lastname")
    last_name.send_keys(fake.last_name())

    email_id = driver.find_element(By.XPATH, "//input[@placeholder='E-Mail']")
    email_id.send_keys(fake.email())

    telephone = driver.find_element(By.NAME, "telephone")
    telephone.send_keys(fake.random_int(000000, 999999, 5))

    pswd = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    pswd.send_keys("test123")

    cnfrm_pswd = driver.find_element(By.CSS_SELECTOR, "#input-confirm")
    cnfrm_pswd.send_keys("test123")

    subscribe_newsletter = driver.find_element(By.XPATH, "(.//input[@value='1'])[2]")
    subscribe_newsletter.click()

    privacy_checkbox = driver.find_element(By.NAME, "agree")
    privacy_checkbox.click()
    continue_button = driver.find_element(By.XPATH, "//*[@type='submit']")
    continue_button.click()
    success_message = driver.find_element(By.XPATH, "//div/h1").text
    print("Title of the Page is: ", driver.title)
    print("Text to be validated is: ", success_message)
    assert success_message.__eq__("Your Account Has Been Created!")


# import time
# from faker import Faker
# from faker.contrib.pytest.plugin import faker
# from selenium import webdriver
#
# from selenium.webdriver.common.by import By
# fake=Faker()
# def test_register_account():
#
#     driver =  webdriver.Chrome()
#     driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
#     driver.maximize_window()
#     first_name=driver.find_element(By.ID,"input-firstname")
#     first_name.send_keys(fake.first_name())
#
#     last_name=driver.find_element(By.ID,"input-lastname")
#     last_name.send_keys(fake.last_name())
#
#     email_id=driver.find_element(By.ID,"input-email")
#     email_id.send_keys(fake.email())
#
#     tel=driver.find_element(By.ID,"input-telephone")
#     tel.send_keys(fake.random_int(000000, 999999, 5)))
#
#     pwd= driver.find_element(By.NAME,"password")
#     pwd.send_keys("shiny@1")
#
#     cpwd=driver.find_element(By.NAME,"confirm")
#     cpwd.send_keys("shiny@12")
#     time.sleep(5)
#
#     subscribe_newsletter = driver.find_element(By.XPATH, "(.//input[@value='1'])[2]")
#     subscribe_newsletter.click()
#
#     privacy_checkbox = driver.find_element(By.NAME, "agree")
#     privacy_checkbox.click()
#
#     continue_button = driver.find_element(By.XPATH, "//*[@type='submit']")
#     continue_button.click()
#
#     success_message = driver.find_element(By.XPATH, "//div/h1").text
#     print("Title of the Page is: ", driver.title)
#     print("Text to be validated is: ", success_message)
#     assert success_message.__eq__("Your Account Has Been Created!")
#     # # driver.find_element(by=By.XPATH, value="//input[@name='newsletter'][@value='0']").click()
#     # check_privacy=driver.find_element(By.XPATH,"//input[@type='checkbox']")
#     # check_privacy.click()
#     # time.sleep(5)
#     #
#     # submit_btn=driver.find_element(By.XPATH,"//input[@value='Continue']")
#     # submit_btn.click()
#     # time.sleep(5)
#     #
#     # page_source_data = driver.page_source
#     #
#     # assert "Your Account Has Been Created!" in page_source_data
#     #
#     # time.sleep(10)


