import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

@allure.title("Verify the ebay items ")
@allure.description("Verify that 62 items are printed")
def test_find_links():
    driver= webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    search_box=driver.find_element(By.CSS_SELECTOR,"#gh-ac")
    search_box.send_keys("macmini")

    #search_button=driver.find_element(By.XPATH,"//input[@type='submit']")
    search_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    search_button.click()

    list_items= driver.find_elements(By.CSS_SELECTOR,".s-item__title")
    list_items_price=driver.find_elements(By.CSS_SELECTOR,".s-item__price")

    print(type(list_items_price))
    print(type(list_items))
    for title, price in zip(list_items, list_items_price):
        print(f"{title.text} - {price.text}")
    if list_items_price:
        max_price=max(list_items_price)
        print(f"max_price:${max_price}")

        min_price=min(list_items_price)
        print(f"Minimum price:${min_price}")