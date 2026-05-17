import pytest
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import ENDPOINTS
from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser: chrome or firefox")


def force_close_overlay(driver):
    """Принудительно закрывает модальное окно"""
    try:
        driver.execute_script("""
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


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()


@pytest.fixture
def driver_main_page(driver):
    driver.get(ENDPOINTS["main"])
    return driver


@pytest.fixture
def driver_login_page(driver):
    driver.get(ENDPOINTS["login"])
    return driver


@pytest.fixture
def driver_register_page(driver):
    driver.get(ENDPOINTS["register"])
    return driver


@pytest.fixture
def authenticated_driver(driver):
    email = f"test_{random.randint(10000, 99999)}@test.com"
    password = "Test123456"
    name = f"User_{random.randint(100, 999)}"
    
    wait = WebDriverWait(driver, 15)

    # Регистрация
    driver.get(ENDPOINTS["register"])
    force_close_overlay(driver)
    wait.until(EC.presence_of_element_located((By.NAME, "name")))

    # Заполняем форму
    name_inputs = driver.find_elements(By.NAME, "name")
    name_inputs[0].send_keys(name)

    email_input = driver.find_element(By.XPATH, "(//input[@name='name'])[2]")
    email_input.send_keys(email)

    password_input = driver.find_element(By.NAME, "Пароль")
    password_input.send_keys(password)

    # Клик по кнопке регистрации
    register_btn = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    driver.execute_script("arguments[0].click();", register_btn)
    
    # Ждём появления кнопки "Войти" (успешная регистрация)
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Войти']")))

    # Вход
    driver.get(ENDPOINTS["login"])
    force_close_overlay(driver)
    wait.until(EC.presence_of_element_located((By.NAME, "name")))

    # Заполняем форму
    email_field = driver.find_element(By.NAME, "name")
    email_field.send_keys(email)

    password_field = driver.find_element(By.NAME, "Пароль")
    password_field.send_keys(password)

    # Клик по кнопке входа
    login_btn = driver.find_element(By.XPATH, "//button[text()='Войти']")
    driver.execute_script("arguments[0].click();", login_btn)

    # Ждём появления кнопки "Оформить заказ" (успешный вход)
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

    return driver