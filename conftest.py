import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from data.urls import UrlsContainer
from locators.main_page_locators import MainPageLocators


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(UrlsContainer.MAIN_PAGE_URL)

    cookies_confirmation = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.COOKIE_LOCATOR))
    cookies_confirmation.click()

    yield driver
    driver.quit()
