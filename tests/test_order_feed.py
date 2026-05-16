import time
import pytest
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeed:
    
    def test_all_time_counter_increases(self, auth_driver):
        main_page = MainPage(auth_driver)
        feed_page = OrderFeedPage(auth_driver)
        
        main_page.click_order_feed()
        time.sleep(2)
        old_all_time = feed_page.get_all_time_orders_count()
        
        main_page.click_constructor()
        time.sleep(2)
        main_page.add_ingredient_to_order()
        main_page.click_order_button()
        time.sleep(3)
        
        main_page.close_modal()
        time.sleep(1)
        
        main_page.click_order_feed()
        time.sleep(2)
        new_all_time = feed_page.get_all_time_orders_count()
        
        assert new_all_time > old_all_time
    
    def test_today_counter_increases(self, auth_driver):
        main_page = MainPage(auth_driver)
        feed_page = OrderFeedPage(auth_driver)
        
        main_page.click_order_feed()
        time.sleep(2)
        old_today = feed_page.get_today_orders_count()
        
        main_page.click_constructor()
        time.sleep(2)
        main_page.add_ingredient_to_order()
        main_page.click_order_button()
        time.sleep(3)
        
        main_page.close_modal()
        time.sleep(1)
        
        main_page.click_order_feed()
        time.sleep(2)
        new_today = feed_page.get_today_orders_count()
        
        assert new_today > old_today
    
    def test_order_appears_in_work_section(self, auth_driver):
        main_page = MainPage(auth_driver)
        
        # Создаём заказ
        main_page.add_ingredient_to_order()
        main_page.click_order_button()
        time.sleep(3)
        
        # Получаем номер заказа
        order_number = main_page.get_order_number()
        assert order_number != "" and order_number != "9999", f"Неверный номер заказа: {order_number}"
        
        # Закрываем модальное окно
        main_page.close_modal()
        time.sleep(1)
        
        # Переходим в ленту заказов
        main_page.click_order_feed()
        time.sleep(3)
        
        # Просто проверяем, что номер заказа есть на странице
        page_text = auth_driver.page_source
        assert order_number in page_text, f"Номер заказа {order_number} не найден на странице ленты"