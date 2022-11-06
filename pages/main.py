from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class MainPage:

    # Адрес страницы
    url = "https://qa-scooter.praktikum-services.ru/"

    # Ответы и вопросы в FAQ-блоке
    faq_block = {
        'price': {
            'question': [By.XPATH, ".//div[contains(@id, 'accordion__heading-') and text() = 'Сколько это стоит? И как оплатить?']"],
            'answer': [By.XPATH, ".//p[text() = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.']"]
        },
        'multiple_scooters': {
            'question': [By.XPATH, ".//div[contains(@id, 'accordion__heading-') and text() = 'Хочу сразу несколько самокатов! Так можно?']"],
            'answer': [By.XPATH, ".//p[text() = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']"]
        },
        'rent_time': {
            'question': [By.XPATH, ".//div[contains(@id, 'accordion__heading-') and text() = 'Как рассчитывается время аренды?']"],
            'answer': [By.XPATH, ".//p[text() = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']"]
        },
        'same_day': {
            'question': [By.XPATH, ".//div[contains(@id, 'accordion__heading-') and text() = 'Можно ли заказать самокат прямо на сегодня?']"],
            'answer': [By.XPATH, ".//p[text() = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.']"]
        },
        'changing_time': {
            'question': [By.XPATH, ".//div[contains(@id, 'accordion__heading-') and text() = 'Можно ли продлить заказ или вернуть самокат раньше?']"],
            'answer': [By.XPATH, ".//p[text() = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']"]
        },
        'charger': {
            'question': [By.XPATH, ".//div[contains(@id, 'accordion__heading-') and text() = 'Вы привозите зарядку вместе с самокатом?']"],
            'answer': [By.XPATH, ".//p[text() = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']"]
        },
        'cancel': {
            'question': [By.XPATH, ".//div[contains(@id, 'accordion__heading-') and text() = 'Можно ли отменить заказ?']"],
            'answer': [By.XPATH, ".//p[text() = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']"]
        },
        'mkad': {
            'question': [By.XPATH, ".//div[contains(@id, 'accordion__heading-') and text() = 'Я жизу за МКАДом, привезёте?']"],
            'answer': [By.XPATH, ".//p[text() = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']"]
        }
    }

    # Верхняя кнопка заказа
    top_order_button = [By.XPATH, ".//button[@class = 'Button_Button__ra12g' and text() = 'Заказать']"]

    # Нижняя кнопка заказа
    bottom_order_button = [By.XPATH, ".//div/div/div/div/div/div/button[text()='Заказать']"]

    def __init__(self, driver, time_out=5):

        self.driver = driver
        self.time_out = time_out


    def get(self):

        self.driver.get(self.url)
        WebDriverWait(self.driver, self.time_out).until(expected_conditions.url_to_be(self.url))