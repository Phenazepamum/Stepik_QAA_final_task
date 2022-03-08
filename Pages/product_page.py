from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_message_about_adding(self):
        adding_message = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE)
        assert EC.visibility_of_element_located(adding_message), 'adding message is not visible or exists'

    def should_be_message_basket_price_equal_to_product_price(self):
        total_basket_price = self.browser.find_element(*ProductPageLocators.TOTAL_BASKET_PRICE_MESSAGE).text.split()[-1]
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert total_basket_price == product_price, 'basket price is not equal to product price'

    def should_be_message_total_basket_price(self):
        total_basket_price_message = self.browser.find_element(*ProductPageLocators.TOTAL_BASKET_PRICE_MESSAGE)
        assert EC.visibility_of_element_located(total_basket_price_message)

    def should_be_product_name_in_adding_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_adding_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ADDED_MESSAGE).text
        assert product_name == product_name_in_adding_message, \
            'product name is not in added to basket message'
