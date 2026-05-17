import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    ALL_TIME_COUNTER = (By.CSS_SELECTOR, ".OrderFeed_number__2MbrQ")
    
    def get_all_time_orders_count(self):
        counters = self.find_elements(self.ALL_TIME_COUNTER)
        if len(counters) >= 1:
            text = counters[0].text
            return int(text) if text.isdigit() else 0
        return 0
    
    def get_today_orders_count(self):
        counters = self.find_elements(self.ALL_TIME_COUNTER)
        if len(counters) >= 2:
            text = counters[1].text
            return int(text) if text.isdigit() else 0
        return 0
    
    def is_order_in_feed(self, order_number):
        """Проверяет, есть ли номер заказа на странице ленты"""
        page_text = self.driver.page_source
        return order_number in page_text