from selenium.webdriver.remote.webelement import WebElement

from locators.locators_edit_information import LocatorsEditInformation
from pages.BasePage import BasePage


class EditInformationPage(BasePage):
    def find_city_field(self) -> WebElement:
        return self.find_element(LocatorsEditInformation.CITY)

    def click_on_update_profile_button(self):
        self.click_on_button(LocatorsEditInformation.BUTTON_UPDATE_PROFILE)

    def find_email_field(self) -> WebElement:
        return self.find_element(LocatorsEditInformation.EMAIL)

    def find_email_error_message(self) -> WebElement:
        return self.find_element(LocatorsEditInformation.ERROR_EMAIL)
