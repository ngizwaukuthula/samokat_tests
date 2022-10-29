from selenium import webdriver
from pages.main import MainPage
import pytest

@pytest.fixture
def driver():

    driver = webdriver.Firefox()

    yield driver

    driver.quit()

@pytest.fixture
def main_page():
    """Открывает браузер (FF) и переходит на главную страницу"""

    driver = webdriver.Firefox()

    main_page = MainPage(driver)
    main_page.get()

    yield main_page

    driver.quit()

