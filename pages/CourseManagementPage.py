from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from locators.locators_course_management_page import LocatorsCourseManagementPage
from pages.BasePage import BasePage


class CourseManagementPage(BasePage):
    def course_name(self, name) -> WebElement:
        locator = (By.LINK_TEXT, name)
        return self.find_element_by_link_text(locator)

    def delete(self) -> WebElement:
        return self.find_element(LocatorsCourseManagementPage.DELETE)
