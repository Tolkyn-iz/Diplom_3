from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Поиск элемента {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Поиск всех элементов {locator}")
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Клик по элементу {locator}")
    def click(self, locator):
        self._close_overlay_if_exists()
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Клик по элементу через JavaScript {locator}")
    def click_via_js(self, locator):
        self._close_overlay_if_exists()
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получение текста элемента {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Проверка видимости элемента {locator}")
    def is_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False

    @allure.step("Ожидание видимости элемента {locator}")
    def wait_for_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидание исчезновения элемента {locator}")
    def wait_for_invisibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Обновление страницы")
    def refresh_page(self):
        self.driver.refresh()

    @allure.step("Получение исходного кода страницы")
    def get_page_source(self):
        return self.driver.page_source

    @allure.step("Проверка URL на содержание {text}")
    def url_contains(self, text):
        return self.wait.until(EC.url_contains(text))

    def _close_overlay_if_exists(self):
        """Закрывает модальное окно, если оно есть на странице"""
        try:
            overlay = self.driver.find_element(By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
            if overlay.is_displayed():
                close_btn = self.driver.find_element(By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
                self.driver.execute_script("arguments[0].click();", close_btn)
                self.wait.until(EC.invisibility_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
                ))
        except:
            pass