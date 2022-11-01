from selenium import webdriver
from pages.main import MainPage
import pytest

@pytest.fixture
def driver():

    driver = webdriver.Firefox()

    yield driver

    driver.quit()

