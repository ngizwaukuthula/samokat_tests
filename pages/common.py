import allure
from selenium.webdriver.common.by import By
from utils import click_on_element
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class CommonControls:

    # Логотип "Яндекс" вверху сайта
    yandex_logo = [By.XPATH, ".//img[@alt = 'Yandex']"]

    # Логотип "Самоката" вверху сайта
    samokat_logo = [By.XPATH, ".//img[@alt = 'Scooter']"]

    # Кнопка согласия использования кук
    accept_cookies_button = [By.XPATH, ".//button[@class = 'App_CookieButton__3cvqF']"]

    def __init__(self, driver, time_out=5):

        self.driver = driver
        self.time_out = time_out

    @allure.step('Соглашаемся на использование куки')
    def accept_cookies(self):
        click_on_element(self.driver, self.accept_cookies_button)
        WebDriverWait(self.driver, self.time_out).until(expected_conditions.invisibility_of_element_located(self.accept_cookies_button))

