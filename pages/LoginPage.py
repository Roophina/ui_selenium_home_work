from selenium.webdriver.remote.webelement import WebElement

from locators.locators_login_page import LocatorsLoginPage
from pages.BasePage import BasePage


class LoginPage(BasePage):
    def login_input(self) -> WebElement:
        return self.find_element(LocatorsLoginPage.LOGIN)

    def password_input(self) -> WebElement:
        return self.find_element(LocatorsLoginPage.PASSWORD)
