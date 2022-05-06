from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        registration_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_FIELD)
        registration_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        confirm_password_field.send_keys(password)
        registration_submit_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        registration_submit_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'There is no "login" in url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'register form is not presented'
