import allure

@allure.title("Проверка вопрос-ответа про стоимость")
def test_price_question(main_page):

    assert main_page.check_question_answer_pair(0, 'Сколько это стоит? И как оплатить?', 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')

@allure.title("Проверка вопрос-ответа про несколько самокатов")
def test_multiple_scooters_question(main_page):

    assert main_page.check_question_answer_pair(1, 'Хочу сразу несколько самокатов! Так можно?', 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')


@allure.title("Проверка вопрос-ответа про расчет времени аренды")
def test_rent_time_calculation_question(main_page):

    assert main_page.check_question_answer_pair(2, 'Как рассчитывается время аренды?', 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')


@allure.title("Проверка вопрос-ответа про доставку в тот же день")
def test_day_to_day_order_question(main_page):

    assert main_page.check_question_answer_pair(3, 'Можно ли заказать самокат прямо на сегодня?', 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.')


@allure.title("Проверка вопрос-ответа про изменение длительности аренды")
def test_changing_order_time_question(main_page):

    assert main_page.check_question_answer_pair(4, 'Можно ли продлить заказ или вернуть самокат раньше?', 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.')


@allure.title("Проверка вопрос-ответа про зарядку")
def test_charger_question(main_page):

    assert main_page.check_question_answer_pair(5, 'Вы привозите зарядку вместе с самокатом?', 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.')


@allure.title("Проверка вопрос-ответа про отмену заказа")
def test_cancel_order_question(main_page):

    assert main_page.check_question_answer_pair(6, 'Можно ли отменить заказ?', 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.')


@allure.title("Проверка вопрос-ответа про зону за МКАДом")
def test_beyond_mkad_question(main_page):

    assert main_page.check_question_answer_pair(7, 'Я жизу за МКАДом, привезёте?', 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')