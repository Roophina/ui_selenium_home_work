from selenium.webdriver.remote.webelement import WebElement

from locators.locators_login_page import LocatorsLoginPage
from pages.BasePage import BasePage


class LoginPage(BasePage):
    def find_login_field(self) -> WebElement:
        return self.find_element(LocatorsLoginPage.LOGIN)

    def find_password_field(self) -> WebElement:
        return self.find_element(LocatorsLoginPage.PASSWORD)

    def click_on_enter_button(self):
        self.click_on_button(LocatorsLoginPage.BUTTON_ENTER)

    def find_login_error_message(self) -> WebElement:
        return self.find_element(LocatorsLoginPage.LOGIN_ERROR_MESSAGE)
