from selenium.webdriver.remote.webelement import WebElement

from locators.locators_personal_account import LocatorsPersonalAccount
from pages.BasePage import BasePage


class PersonalAccountPage(BasePage):
    def user_menu(self) -> WebElement:
        return self.find_element(LocatorsPersonalAccount.MENU)

    def exit(self) -> WebElement:
        return self.find_element(LocatorsPersonalAccount.EXIT)

    def exit_from_account(self):
        self.click_element(self.user_menu())
        self.click_element(self.exit())

    def side_panel(self) -> WebElement:
        return self.find_element(LocatorsPersonalAccount.SIDE_PANEL)

    def click_on_side_panel(self):
        self.click_element(self.side_panel())

    def administration(self) -> WebElement:
        return self.find_element(LocatorsPersonalAccount.ADMINISTRATION)

    def go_to_admin_page(self):
        self.click_element(self.administration())

    def check_personal_account(self):
        return self.find_element(LocatorsPersonalAccount.PERSONAL_ACCOUNT)
