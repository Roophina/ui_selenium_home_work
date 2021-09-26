from locators.locators_main_page import LocatorsMainPage
from pages.BasePage import BasePage


class MainPage(BasePage):
    def click_on_enter_link(self):
        self.click_on_link(LocatorsMainPage.LINK_ENTER)
