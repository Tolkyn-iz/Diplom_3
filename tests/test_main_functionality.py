import time
from pages.main_page import MainPage


class TestMainFunctionality:
    
    def test_constructor_navigation(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        time.sleep(1)
        main_page.click_constructor()
        time.sleep(1)
        assert "/feed" not in driver.current_url
    
    def test_order_feed_navigation(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        time.sleep(1)
        assert "feed" in driver.current_url
    
    def test_ingredient_modal_appears(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        time.sleep(1)
        assert main_page.is_modal_open() is True
    
    def test_modal_closes_with_cross(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        assert main_page.is_modal_open() is True
        time.sleep(0.5)
        main_page.close_modal()
        time.sleep(0.5)
        assert main_page.is_modal_open() is False
    
    def test_counter_increases(self, driver):
        main_page = MainPage(driver)
        old_counter = main_page.get_counter_value()
        main_page.add_ingredient_to_order()
        time.sleep(2)
        new_counter = main_page.get_counter_value()
        assert new_counter > old_counter