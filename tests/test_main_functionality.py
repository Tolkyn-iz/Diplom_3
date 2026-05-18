import allure
from pages.main_page import MainPage


@allure.feature("Основная функциональность")
class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_constructor_navigation(self, driver_main_page):
        page = MainPage(driver_main_page)
        page.click_order_feed()
        page.click_constructor()
        assert "/feed" not in page.get_current_url()

    @allure.title("Переход по клику на «Лента заказов»")
    def test_order_feed_navigation(self, driver_main_page):
        page = MainPage(driver_main_page)
        page.click_order_feed()
        assert "feed" in page.get_current_url()

    @allure.title("При клике на ингредиент появляется всплывающее окно")
    def test_ingredient_modal_appears(self, driver_main_page):
        page = MainPage(driver_main_page)
        page.click_ingredient()
        assert page.is_modal_open() is True
        page.close_modal()  # cleanup

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_modal_closes_by_cross(self, driver_main_page):
        page = MainPage(driver_main_page)
        page.click_ingredient()
        assert page.is_modal_open() is True
        page.close_modal()
        assert page.is_modal_open() is False

    @allure.title("При добавлении ингредиента счётчик увеличивается")
    def test_counter_increases(self, driver_main_page):
        page = MainPage(driver_main_page)
        old_counter = page.get_counter_value()
        page.add_ingredient_to_order()
        new_counter = page.get_counter_value()
        assert new_counter > old_counter