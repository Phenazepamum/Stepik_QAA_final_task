from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-primary.btn-add-to-basket')
    ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    TOTAL_BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, '.alertinner > p:nth-child(1)')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_NAME_IN_ADDED_MESSAGE = (By.CSS_SELECTOR, '.alertinner strong:nth-child(1)')
