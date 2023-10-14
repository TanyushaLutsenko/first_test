from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Авторизация используя корректные данные (standard_user, secret_sauce)

def test_login_positiv():
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, "//input[@id = 'user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@id = 'login-button']").click()

    time.sleep(5)

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    driver.quit()

# Авторизация используя некорректные данные (user, user)
def test_login_negative():
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, "//input[@id = 'user-name']").send_keys("user")
    driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys("uesr")
    driver.find_element(By.XPATH, "//input[@id = 'login-button']").click()

    text_err = driver.find_element(By.XPATH, "//div[@class='error-message-container error']/h3[@data-test='error']").text

    assert text_err == "Epic sadface: Username and password do not match any user in this service"

    time.sleep(5)

    driver.quit()

# Добавление товара в корзину через каталог

def test_add_item_from_catalog():
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, "//input[@id = 'user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@id = 'login-button']").click()

    driver.find_element(By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-bolt-t-shirt']").click()

    time.sleep(5)

    button_text = driver.find_element(By.XPATH, "//button[@id = 'remove-sauce-labs-bolt-t-shirt']").text

    print(button_text)

    assert button_text == "Remove"

    time.sleep(5)

    driver.quit()

# Удаление товара из корзины через корзину

def test_delete_from_cart():
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    time.sleep(5)

    driver.find_element(By.XPATH, '//img[@alt="Sauce Labs Backpack"]').click()
    driver.find_element(By.XPATH, '//button[contains(text(), "Add to cart")]').click()

    driver.find_element(By.XPATH, '//a[contains(@class, "shopping_cart_link")]').click()

    time.sleep(5)

    driver.find_element(By.XPATH, "//button[contains(text(), 'Remove')]").click()

    time.sleep(5)
    find_list = driver.find_elements(By.XPATH, '//div[@class="cart_list"]/div[@class="cart_item"]')

    assert len(find_list) == 0

    driver.quit()


# Добавление товара в корзину из карточки товара AND Успешный переход к карточке товара после клика на картинку товара

def test_add_item_from_card():
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    time.sleep(5)

    driver.find_element(By.XPATH, '//img[@src = "/static/media/bolt-shirt-1200x1500.c2599ac5.jpg"]').click()
    driver.find_element(By.XPATH, '//button[@id = "add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    time.sleep(5)
    text_remove = driver.find_element(By.XPATH, '//button[@id = "remove-sauce-labs-bolt-t-shirt"]').text

    print(text_remove)

    assert text_remove == "Remove"

    driver.quit()

#Удаление товара из корзины через карточку товара

def test_delete_item_from_card():
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    time.sleep(5)

    driver.find_element(By.XPATH, '//img[@src = "/static/media/bolt-shirt-1200x1500.c2599ac5.jpg"]').click()
    driver.find_element(By.XPATH, '//button[@id = "add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    time.sleep(5)
    driver.find_element(By.XPATH, '//button[@id = "remove-sauce-labs-bolt-t-shirt"]').click()
    text_remove = driver.find_element(By.XPATH, '//button[@id = "add-to-cart-sauce-labs-bolt-t-shirt"]').text

    print(text_remove)

    assert text_remove == "Add to cart"

    driver.quit()

# Бургер меню. Выход из системы

def test_burger_exit():

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    time.sleep(5)

    driver.find_element(By.XPATH, '//button[@id = "react-burger-menu-btn"]').click()

    time.sleep(5)

    driver.find_element(By.XPATH, '//a[@id = "logout_sidebar_link"]').click()

    time.sleep(5)

    log_value = driver.find_element(By.XPATH, '//div[@class="login_logo"]').text

    # print('1111111', log_value)

    assert log_value == "Swag Labs"

    driver.quit()


# Бургер меню. Проверка работоспособности кнопки "About" в меню


    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    time.sleep(5)

    driver.find_element(By.XPATH, '//button[@id = "react-burger-menu-btn"]').click()

    time.sleep(5)

    driver.find_element(By.XPATH, '//a[@id = "about_sidebar_link"]').click()




    driver.quit()