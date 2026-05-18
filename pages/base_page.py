from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def click_via_js(self, locator):
        """Клик через JavaScript (обходит перекрытия)"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def get_text(self, locator):
        return self.find_element(locator).text

    def get_current_url(self):
        return self.driver.current_url

    def is_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False

    def wait_for_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_invisibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def refresh_page(self):
        self.driver.refresh()

    def get_page_source(self):
        return self.driver.page_source

    def execute_script(self, script, *args):
        """Выполняет JavaScript (вынесено из main_page)"""
        return self.driver.execute_script(script, *args)

    def find_element_via_js(self, locator):
        """Поиск элемента через JavaScript (если нужно)"""
        element = self.find_element(locator)
        return element

    def force_close_overlay(self):
        """Принудительно закрывает оверлей через JavaScript"""
        try:
            self.execute_script("""
                var overlays = document.querySelectorAll('.Modal_modal_overlay__x2ZCr');
                var closeBtns = document.querySelectorAll('.Modal_modal__close__TnseK');
                for (var i = 0; i < overlays.length; i++) {
                    if (overlays[i].style.display !== 'none') {
                        overlays[i].style.display = 'none';
                    }
                }
                for (var i = 0; i < closeBtns.length; i++) {
                    closeBtns[i].click();
                }
            """)
        except:
            pass