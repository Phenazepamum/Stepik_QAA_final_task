from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        button = self.browser.find_element(*MainPageLocators.BASKET_BUTTON)
        button.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
