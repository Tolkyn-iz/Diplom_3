from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOGIN_BTN = (By.XPATH, "//button[text()='Войти']")