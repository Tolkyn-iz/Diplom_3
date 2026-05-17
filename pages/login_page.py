import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    @allure.step("Ввод email: {email}")
    def enter_email(self, email):
        self.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(email)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    @allure.step("Клик на кнопку 'Войти'")
    def click_login_button(self):
        self.click(LoginPageLocators.LOGIN_BTN)

    @allure.step("Выполнение входа")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()