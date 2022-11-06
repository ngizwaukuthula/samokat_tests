from pages.main import MainPage
from utils import *


@allure.title("Проверка вопрос-ответа про стоимость")
def test_price_question(driver):

    main_page = MainPage(driver)
    main_page.get()

    click_on_element(driver, main_page.faq_block['price']['question'])

    assert is_element_displayed(driver, main_page.faq_block['price']['answer'])


@allure.title("Проверка вопрос-ответа про несколько самокатов")
def test_multiple_scooters_question(driver):

    main_page = MainPage(driver)
    main_page.get()

    click_on_element(driver, main_page.faq_block['multiple_scooters']['question'])

    assert is_element_displayed(driver, main_page.faq_block['multiple_scooters']['answer'])


@allure.title("Проверка вопрос-ответа про расчет времени аренды")
def test_rent_time_calculation_question(driver):

    main_page = MainPage(driver)
    main_page.get()

    click_on_element(driver, main_page.faq_block['rent_time']['question'])

    assert is_element_displayed(driver, main_page.faq_block['rent_time']['answer'])


@allure.title("Проверка вопрос-ответа про доставку в тот же день")
def test_day_to_day_order_question(driver):

    main_page = MainPage(driver)
    main_page.get()

    click_on_element(driver, main_page.faq_block['same_day']['question'])

    assert is_element_displayed(driver, main_page.faq_block['same_day']['answer'])


@allure.title("Проверка вопрос-ответа про изменение длительности аренды")
def test_changing_order_time_question(driver):

    main_page = MainPage(driver)
    main_page.get()

    click_on_element(driver, main_page.faq_block['changing_time']['question'])

    assert is_element_displayed(driver, main_page.faq_block['changing_time']['answer'])


@allure.title("Проверка вопрос-ответа про зарядку")
def test_charger_question(driver):

    main_page = MainPage(driver)
    main_page.get()

    click_on_element(driver, main_page.faq_block['charger']['question'])

    assert is_element_displayed(driver, main_page.faq_block['charger']['answer'])


@allure.title("Проверка вопрос-ответа про отмену заказа")
def test_cancel_order_question(driver):

    main_page = MainPage(driver)
    main_page.get()

    click_on_element(driver, main_page.faq_block['cancel']['question'])

    assert is_element_displayed(driver, main_page.faq_block['cancel']['answer'])


@allure.title("Проверка вопрос-ответа про зону за МКАДом")
def test_beyond_mkad_question(driver):

    main_page = MainPage(driver)
    main_page.get()

    click_on_element(driver, main_page.faq_block['mkad']['question'])

    assert is_element_displayed(driver, main_page.faq_block['mkad']['answer'])