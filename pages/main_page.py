from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class MainPage(BasePage):
    CONSTRUCTOR_BTN = (By.XPATH, "//p[text()='Конструктор']/ancestor::a")
    ORDER_FEED_BTN = (By.XPATH, "//p[text()='Лента Заказов']/ancestor::a")
    FIRST_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]")
    COUNTER = (By.XPATH, "//p[contains(@class, 'counter_counter__num')]")
    CONSTRUCTOR_AREA = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    MODAL_CLOSE_BTN = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    
    def click_constructor(self):
        if self.is_modal_open():
            self.close_modal()
        self.click(self.CONSTRUCTOR_BTN)
        time.sleep(0.5)
    
    def click_order_feed(self):
        if self.is_modal_open():
            self.close_modal()
        self.click(self.ORDER_FEED_BTN)
        time.sleep(0.5)
    
    def click_ingredient(self):
        if self.is_modal_open():
            self.close_modal()
        self.click(self.FIRST_INGREDIENT)
        time.sleep(0.5)
    
    def add_ingredient_to_order(self):
        """
        Добавляет ингредиент через JavaScript drag and drop события
        РАБОТАЕТ В FIREFOX!
        """
        ingredient = self.find_element(self.FIRST_INGREDIENT)
        constructor = self.find_element(self.CONSTRUCTOR_AREA)
        
        # Получаем data-transfer id ингредиента
        drag_data = ingredient.get_attribute("draggable")
        ingredient_id = ingredient.get_attribute("href").split("/")[-1]
        
        # Эмулируем drag and drop через JavaScript
        js_script = """
        var source = arguments[0];
        var target = arguments[1];
        
        // Создаем событие dragstart
        var dragStartEvent = new DragEvent('dragstart', {
            bubbles: true,
            cancelable: true,
            dataTransfer: new DataTransfer()
        });
        source.dispatchEvent(dragStartEvent);
        
        // Создаем событие drop
        var dropEvent = new DragEvent('drop', {
            bubbles: true,
            cancelable: true,
            dataTransfer: dragStartEvent.dataTransfer
        });
        target.dispatchEvent(dropEvent);
        
        // Создаем событие dragend
        var dragEndEvent = new DragEvent('dragend', {
            bubbles: true,
            cancelable: true,
            dataTransfer: dragStartEvent.dataTransfer
        });
        source.dispatchEvent(dragEndEvent);
        """
        
        self.driver.execute_script(js_script, ingredient, constructor)
        time.sleep(1)
    
    def get_counter_value(self):
        try:
            time.sleep(1)
            counters = self.driver.find_elements(*self.COUNTER)
            total = 0
            for counter in counters:
                text = counter.text
                if text.isdigit():
                    total += int(text)
            return total
        except:
            return 0
    
    def is_modal_open(self):
        try:
            overlay = self.driver.find_element(*self.MODAL_OVERLAY)
            return overlay.is_displayed()
        except:
            return False
    
    def close_modal(self):
        try:
            close_btn = self.driver.find_element(*self.MODAL_CLOSE_BTN)
            self.driver.execute_script("arguments[0].click();", close_btn)
        except:
            pass
        time.sleep(0.5)
    
    def click_order_button(self):
        if self.is_modal_open():
            self.close_modal()
            time.sleep(1)
        
        button = self.find_element(self.ORDER_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
    
    def get_order_number(self):
        time.sleep(2)
        element = self.find_element(self.ORDER_NUMBER)
        number_text = element.text
        return ''.join(filter(str.isdigit, number_text))