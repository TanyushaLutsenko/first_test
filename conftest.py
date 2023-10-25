import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from data import LOGIN, PASSWORD, MAIN_PAGE
from locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON, FAILD_DATA



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def login1(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    time.sleep(5)