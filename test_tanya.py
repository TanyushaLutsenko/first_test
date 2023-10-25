#from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from data import LOGIN, PASSWORD, MAIN_PAGE
from locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON, FAILD_DATA


# Authorization using correct data (standard_user, secret_sauce)
def test_login_positiv(driver):
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


# Authorization using incorrect data (user, user)
def test_login_negative(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(FAILD_DATA)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(FAILD_DATA)
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    time.sleep(5)

    text_err = driver.find_element(By.XPATH,
                                   "//div[@class='error-message-container error']/h3[@data-test='error']").text

    assert text_err == "Epic sadface: Username and password do not match any user in this service"


# Adding an item to the cart via the catalog
def test_add_item_from_catalog(driver):
    driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()

    time.sleep(5)

    button_text = driver.find_element(By.XPATH, "//button[@id = 'remove-sauce-labs-bolt-t-shirt']").text

    print(button_text)

    assert button_text == "Remove"


# Removing an item from the shopping cart via the shopping cart
def test_delete_from_cart(driver):
    driver.find_element(By.XPATH, '//img[@alt="Sauce Labs Backpack"]').click()
    driver.find_element(By.XPATH, '//button[contains(text(), "Add to cart")]').click()

    driver.find_element(By.XPATH, '//a[contains(@class, "shopping_cart_link")]').click()

    time.sleep(5)

    driver.find_element(By.XPATH, "//button[contains(text(), 'Remove')]").click()

    time.sleep(5)
    find_list = driver.find_elements(By.XPATH, '//div[@class="cart_list"]/div[@class="cart_item"]')

    assert len(find_list) == 0


# Adding an item to the cart from the product card
def test_add_item_from_card(driver):
    driver.find_element(By.XPATH, '//img[@src = "/static/media/bolt-shirt-1200x1500.c2599ac5.jpg"]').click()
    driver.find_element(By.XPATH, '//button[@id = "add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    time.sleep(5)
    text_remove = driver.find_element(By.XPATH, '//button[@id = "remove-sauce-labs-bolt-t-shirt"]').text

    print(text_remove)

    assert text_remove == "Remove"


# Removing an item from the shopping cart via the product card
def test_delete_item_from_card(driver):
    driver.find_element(By.XPATH, '//img[@src = "/static/media/bolt-shirt-1200x1500.c2599ac5.jpg"]').click()
    driver.find_element(By.XPATH, '//button[@id = "add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    time.sleep(5)
    driver.find_element(By.XPATH, '//button[@id = "remove-sauce-labs-bolt-t-shirt"]').click()
    text_remove = driver.find_element(By.XPATH, '//button[@id = "add-to-cart-sauce-labs-bolt-t-shirt"]').text

    print(text_remove)

    assert text_remove == "Add to cart"


# Burger menu. Log out of the system
def test_burger_exit(driver):
    driver.find_element(By.XPATH, '//button[@id = "react-burger-menu-btn"]').click()

    time.sleep(5)

    driver.find_element(By.XPATH, '//a[@id = "logout_sidebar_link"]').click()

    time.sleep(5)

    log_value = driver.find_element(By.XPATH, '//div[@class="login_logo"]').text

    assert log_value == "Swag Labs"

# Burger menu. Checking the operability of the "About" button in the menu
#
#     driver.get(MAIN_PAGE)
#
#     driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")
#     driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")
#     driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()
#
#     time.sleep(5)
#
#     driver.find_element(By.XPATH, '//button[@id = "react-burger-menu-btn"]').click()
#
#     time.sleep(5)
#
#     driver.find_element(By.XPATH, '//a[@id = "about_sidebar_link"]').click()

# setTimeout(function()
# {
#     debugger;
# }, 3000);
