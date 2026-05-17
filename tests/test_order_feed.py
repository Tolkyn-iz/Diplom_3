import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Счётчик «Выполнено за всё время» увеличивается")
    def test_all_time_counter_increases(self, authenticated_driver):
        main_page = MainPage(authenticated_driver)
        feed_page = OrderFeedPage(authenticated_driver)
        wait = WebDriverWait(authenticated_driver, 10)

        main_page.click_order_feed()
        wait.until(EC.visibility_of_element_located(feed_page.ALL_TIME_COUNTER))
        old_value = feed_page.get_all_time_orders_count()

        main_page.click_constructor()
        main_page.add_ingredient_to_order()
        main_page.click_order_button()
        main_page.close_modal()

        main_page.click_order_feed()
        wait.until(EC.visibility_of_element_located(feed_page.ALL_TIME_COUNTER))
        new_value = feed_page.get_all_time_orders_count()

        assert new_value > old_value

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается")
    def test_today_counter_increases(self, authenticated_driver):
        main_page = MainPage(authenticated_driver)
        feed_page = OrderFeedPage(authenticated_driver)
        wait = WebDriverWait(authenticated_driver, 10)

        main_page.click_order_feed()
        wait.until(EC.visibility_of_element_located(feed_page.ALL_TIME_COUNTER))
        old_value = feed_page.get_today_orders_count()

        main_page.click_constructor()
        main_page.add_ingredient_to_order()
        main_page.click_order_button()
        main_page.close_modal()

        main_page.click_order_feed()
        wait.until(EC.visibility_of_element_located(feed_page.ALL_TIME_COUNTER))
        new_value = feed_page.get_today_orders_count()

        assert new_value > old_value

    @allure.title("Номер заказа появляется в ленте после оформления")
    def test_order_number_appears_in_feed(self, authenticated_driver):
        main_page = MainPage(authenticated_driver)
        feed_page = OrderFeedPage(authenticated_driver)
        wait = WebDriverWait(authenticated_driver, 10)

        # Создаём заказ
        main_page.add_ingredient_to_order()
        main_page.click_order_button()

        # Получаем номер заказа
        order_number = main_page.get_order_number()
        assert order_number != "" and order_number != "9999", f"Неверный номер заказа: {order_number}"

        # Закрываем модальное окно
        main_page.close_modal()

        # Переходим в ленту заказов
        main_page.click_order_feed()

        # Ждём появления номера заказа на странице
        wait.until(lambda driver: order_number in driver.page_source)

        assert feed_page.is_order_in_feed(order_number) is True