from selenium.webdriver.remote.webelement import WebElement

from locators.locators_preferences_page import LocatorsPreferences
from pages.BasePage import BasePage


class PreferencesPage(BasePage):
    def go_to_edit_information(self):
        self.click_on_link(LocatorsPreferences.EDIT_INFORMATION)

    def check_notifications(self) -> WebElement:
        return self.find_element(LocatorsPreferences.NOTIFICATION)
