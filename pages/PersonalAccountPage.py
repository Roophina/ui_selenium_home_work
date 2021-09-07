from selenium.webdriver.remote.webelement import WebElement

from locators.locators_personal_account import LocatorsPersonalAccount
from pages.BasePage import BasePage


class PersonalAccountPage(BasePage):
    def user_menu(self) -> WebElement:
        return self.find_element(LocatorsPersonalAccount.PERSONAL_ACCOUNT_MENU)

    def exit(self) -> WebElement:
        return self.find_element(LocatorsPersonalAccount.PERSONAL_ACCOUNT_EXIT)

    def exit_from_account(self):
        self.click_element(self.user_menu())
        self.click_element(self.exit())
