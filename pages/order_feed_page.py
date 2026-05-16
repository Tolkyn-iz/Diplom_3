from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class OrderFeedPage(BasePage):
    ALL_TIME_COUNTER = (By.CSS_SELECTOR, ".OrderFeed_number__2MbrQ")
    
    def get_all_time_orders_count(self):
        counters = self.find_elements(self.ALL_TIME_COUNTER)
        if len(counters) >= 1:
            text = counters[0].text
        else:
            text = self.get_text(self.ALL_TIME_COUNTER)
        return int(text) if text.isdigit() else 0
    
    def get_today_orders_count(self):
        counters = self.find_elements(self.ALL_TIME_COUNTER)
        if len(counters) >= 2:
            text = counters[1].text
        else:
            text = self.get_text(self.ALL_TIME_COUNTER)
        return int(text) if text.isdigit() else 0