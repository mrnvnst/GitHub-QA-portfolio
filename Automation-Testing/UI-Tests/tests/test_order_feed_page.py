import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from helpers.data import TestData, Credentials
from pages.login_page import LoginPage


@allure.feature("Лента заказов Stellar Burgers")
class TestOrderFeed:
    @allure.title("Счётчик 'Выполнено за всё время' увеличивается после заказа")
    def test_all_time_counter_increases(self, driver):
        main = MainPage(driver)
        order = OrderFeedPage(driver)
        login = LoginPage(driver)
        with allure.step("Переходим в 'Личный кабинет'"):
            main.go_to_personal_account()
        with allure.step("Авторизуемся"):
            login.login(Credentials.email, Credentials.password)
        with allure.step("Переходим на страницу 'Лента заказов' и получаем значение счётчика 'Выполнено за всё время'"):
            main.go_to_order_feed()
            initial_count = order.all_time_counter()
        with allure.step("Переходим на страницу 'Конструктор' и создаём заказ"):
            main.go_to_constructor()
            main.add_ingredient_to_basket(TestData.ingredient_name)
            main.place_order()
            order.close_order_modal()
        with allure.step("Открываем 'Ленту заказов' повторно и получаем новое значение счётчика"):
            main.go_to_order_feed()
            current_count = order.all_time_counter()
        with allure.step("Проверяем, что значение счётчика увеличилось"):
            assert current_count > initial_count

    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается после заказа")
    def test_today_counter_increases(self, driver):
        main = MainPage(driver)
        order = OrderFeedPage(driver)
        login = LoginPage(driver)
        with allure.step("Переходим в 'Личный кабинет'"):
            main.go_to_personal_account()
        with allure.step("Авторизуемся"):
            login.login(Credentials.email, Credentials.password)
        with allure.step("Переходим на страницу 'Лента заказов' и получаем значение счётчика 'Выполнено за сегодня'"):
            main.go_to_order_feed()
            initial_count = order.today_counter()
        with allure.step("Переходим на страницу 'Конструктор' и создаём заказ"):
            main.go_to_constructor()
            main.add_ingredient_to_basket(TestData.ingredient_name)
            main.place_order()
            order.close_order_modal()
        with allure.step("Открываем 'Ленту заказов' повторно и получаем новое значение счётчика"):
            main.go_to_order_feed()
            current_count = order.today_counter()
        with allure.step("Проверяем, что значение счётчика увеличилось"):
            assert current_count > initial_count

    @allure.title("Номер нового заказа появляется в разделе 'В работе'")
    def test_order_number_in_progress(self, driver):
        main = MainPage(driver)
        order = OrderFeedPage(driver)
        login = LoginPage(driver)
        with allure.step("Переходим в 'Личный кабинет'"):
            main.go_to_personal_account()
        with allure.step("Авторизуемся"):
            login.login(Credentials.email, Credentials.password)
        with allure.step(f"Создаём заказ с ингредиентом '{TestData.ingredient_name}'"):
            main.add_ingredient_to_basket(TestData.ingredient_name)
            main.place_order()
        with allure.step("Получаем номер заказа из всплывающего окна"):
            order_number = order.order_number_from_modal()
        with allure.step("Закрываем всплывающее окно"):
            order.close_order_modal()
        with allure.step("Переходим на страницу 'Лента заказов'"):
            main.go_to_order_feed()
        with allure.step(f"Проверяем, что заказ с номером {order_number} отображается в разделе 'В работе'"):
            assert order.is_order_in_progress(order_number)

