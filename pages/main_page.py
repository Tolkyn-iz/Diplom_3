import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Клик на кнопку 'Конструктор'")
    def click_constructor(self):
        self.force_close_overlay()
        self.click(MainPageLocators.CONSTRUCTOR_BTN)

    @allure.step("Клик на кнопку 'Лента заказов'")
    def click_order_feed(self):
        self.force_close_overlay()
        self.click(MainPageLocators.ORDER_FEED_BTN)

    @allure.step("Клик на первый ингредиент")
    def click_ingredient(self):
        self.force_close_overlay()
        self.click_via_js(MainPageLocators.FIRST_INGREDIENT)

    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient_to_order(self):
        source = self.find_element(MainPageLocators.FIRST_INGREDIENT)
        target = self.find_element(MainPageLocators.CONSTRUCTOR_AREA)

        js_script = """
        var source = arguments[0];
        var target = arguments[1];
        var dragStartEvent = new DragEvent('dragstart', {
            bubbles: true,
            cancelable: true,
            dataTransfer: new DataTransfer()
        });
        source.dispatchEvent(dragStartEvent);
        var dropEvent = new DragEvent('drop', {
            bubbles: true,
            cancelable: true,
            dataTransfer: dragStartEvent.dataTransfer
        });
        target.dispatchEvent(dropEvent);
        var dragEndEvent = new DragEvent('dragend', {
            bubbles: true,
            cancelable: true,
            dataTransfer: dragStartEvent.dataTransfer
        });
        source.dispatchEvent(dragEndEvent);
        """

        self.execute_script(js_script, source, target)

    @allure.step("Получение значения счётчика ингредиента")
    def get_counter_value(self):
        counters = self.find_elements(MainPageLocators.COUNTER)
        total = 0
        for counter in counters:
            text = counter.text
            if text.isdigit():
                total += int(text)
        return total

    @allure.step("Проверка, открыто ли модальное окно")
    def is_modal_open(self):
        return self.is_visible(MainPageLocators.MODAL_OVERLAY)

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        self.force_close_overlay()
        self.click_via_js(MainPageLocators.MODAL_CLOSE_BTN)

    @allure.step("Клик на кнопку 'Оформить заказ'")
    def click_order_button(self):
        self.force_close_overlay()
        self.click_via_js(MainPageLocators.ORDER_BUTTON)
        self.wait_for_visibility(MainPageLocators.ORDER_NUMBER)

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        element = self.find_element(MainPageLocators.ORDER_NUMBER)
        number_text = element.text
        return ''.join(filter(str.isdigit, number_text))