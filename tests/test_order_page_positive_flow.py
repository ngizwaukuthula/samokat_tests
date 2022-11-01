from pages.order import OrderPage
from pages.common import CommonControls
from pages.main import MainPage
from utils import *

@allure.title("Проверка заказа по верхней кнопке")
@allure.description("Позитивный сценарий заказа с рандомными корректными данными и входом по верхней кнопке")
def test_top_button_positive_order_flow(driver):
    main_page = MainPage(driver)
    main_page.get()

    common_controls = CommonControls(driver)
    common_controls.accept_cookies()

    click_on_element(driver, main_page.top_order_button)
    order_page = OrderPage(driver)
    order_page.fill_in_order_form(random_client_info())

    assert is_element_displayed(driver, order_page.order_confirmation_title)


@allure.title("Проверка заказа по нижней кнопке")
@allure.description("Позитивный сценарий заказа с рандомными корректными данными и входом по нижней кнопке")
def test_bottom_button_positive_order_flow(driver):
    main_page = MainPage(driver)
    main_page.get()

    common_controls = CommonControls(driver)
    common_controls.accept_cookies()

    click_on_element(driver, main_page.bottom_order_button)

    order_page = OrderPage(driver)
    order_page.fill_in_order_form(random_client_info())

    assert is_element_displayed(driver, order_page.order_confirmation_title)


@allure.title("Проверка перехода через лого Яндекса")
@allure.description("Проверка перехода на страницу Самоката по клику на лого Яндекса.")
def test_yandex_main_page_transition(driver):
    order_page = OrderPage(driver)
    common_controls = CommonControls(driver)
    order_page.get()
    click_on_element(driver, common_controls.yandex_logo)

    switch_to_new_opened_window(driver)

    wait_until_url_is_changed(driver, "about:blank")

    assert "dzen.ru" in driver.current_url


@allure.title("Проверка перехода через лого Самоката")
@allure.description("Проверка перехода на страницу Самоката по клику на лого Самоката.")
def test_samokat_transition(driver):
    order_page = OrderPage(driver)
    common_controls = CommonControls(driver)
    order_page.get()
    click_on_element(driver, common_controls.samokat_logo)

    wait_until_url_is_changed(driver, OrderPage.url)

    assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'