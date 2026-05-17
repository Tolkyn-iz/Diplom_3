from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ALL_COUNTERS = (By.CSS_SELECTOR, ".OrderFeed_number__2MbrQ")
    ORDER_ITEMS = (By.CSS_SELECTOR, ".OrderHistory_listItem__2x95r")
    ORDER_NUMBER_IN_ITEM = (By.CSS_SELECTOR, ".text_type_digits-default")