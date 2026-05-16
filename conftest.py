import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
import os
import time


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser: chrome or firefox")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    project_dir = os.path.dirname(os.path.abspath(__file__))
    
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-search-engine-choice-screen")
        
        chrome_driver_path = os.path.join(project_dir, "chromedriver.exe")
        if os.path.exists(chrome_driver_path):
            service = ChromeService(executable_path=chrome_driver_path)
            driver = webdriver.Chrome(service=service, options=options)
        else:
            driver = webdriver.Chrome(options=options)
            
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        # Указываем путь к Firefox
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        
        gecko_driver_path = os.path.join(project_dir, "geckodriver.exe")
        if os.path.exists(gecko_driver_path):
            service = FirefoxService(executable_path=gecko_driver_path)
            driver = webdriver.Firefox(service=service, options=options)
        else:
            driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    driver.get("https://stellarburgers.education-services.ru/")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def auth_driver(driver):
    import random
    
    email = f"test_{random.randint(10000, 99999)}@test.com"
    password = "Test123456"
    name = f"User_{random.randint(100, 999)}"
    
    driver.get("https://stellarburgers.education-services.ru/register")
    time.sleep(2)
    
    name_inputs = driver.find_elements(By.NAME, "name")
    if len(name_inputs) >= 1:
        name_inputs[0].send_keys(name)
    
    email_input = driver.find_element(By.XPATH, "(//input[@name='name'])[2]")
    email_input.send_keys(email)
    
    password_input = driver.find_element(By.NAME, "Пароль")
    password_input.send_keys(password)
    
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
    time.sleep(3)
    
    driver.get("https://stellarburgers.education-services.ru/login")
    time.sleep(2)
    
    driver.find_element(By.NAME, "name").send_keys(email)
    driver.find_element(By.NAME, "Пароль").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    
    time.sleep(3)
    yield driver