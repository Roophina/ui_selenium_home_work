from selenium.webdriver.remote.webelement import WebElement

from locators.locators_course_edit_page import LocatorsCourseEditPage
from pages.BasePage import BasePage


class CourseEditPage(BasePage):
    def find_full_name_field(self) -> WebElement:
        return self.find_element(LocatorsCourseEditPage.FULL_NAME)

    def find_short_name_field(self) -> WebElement:
        return self.find_element(LocatorsCourseEditPage.SHORT_NAME)

    def click_on_save_and_return(self):
        self.click_on_button(LocatorsCourseEditPage.SAVE_AND_RETURN)

    def find_error_message_about_short_name(self) -> WebElement:
        return self.find_element(LocatorsCourseEditPage.ERROR_SHORT_NAME)
