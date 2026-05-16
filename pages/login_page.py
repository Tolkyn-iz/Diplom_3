from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOGIN_BTN = (By.XPATH, "//button[text()='Войти']")
    
    def enter_email(self, email):
        self.find_element(self.EMAIL_INPUT).send_keys(email)
    
    def enter_password(self, password):
        self.find_element(self.PASSWORD_INPUT).send_keys(password)
    
    def enter_credentials(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
    
    def click_login_button(self):
        self.click(self.LOGIN_BTN)