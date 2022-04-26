import pytest
from .Pages.main_page import MainPage
from .Pages.login_page import LoginPage
from .Pages.basket_page import BasketPage


def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_formset()
    basket_page.should_be_empty_basket_message()
