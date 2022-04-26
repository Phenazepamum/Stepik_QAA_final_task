from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-group a.btn.btn-default')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-primary.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    TOTAL_BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, '.alertinner > p:nth-child(1)')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_NAME_IN_ADDED_MESSAGE = (By.CSS_SELECTOR, '.alertinner strong:nth-child(1)')


class BasketPageLocators:
    BASKET_FORMSET = (By.ID, 'basket_formset')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
