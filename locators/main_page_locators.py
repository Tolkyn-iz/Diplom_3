from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BTN = (By.XPATH, "//p[text()='Конструктор']/ancestor::a")
    ORDER_FEED_BTN = (By.XPATH, "//p[text()='Лента Заказов']/ancestor::a")
    FIRST_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]")
    COUNTER = (By.XPATH, "//p[contains(@class, 'counter_counter__num')]")
    CONSTRUCTOR_AREA = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    MODAL_CLOSE_BTN = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")