from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from locators.locators_course_management_page import LocatorsCourseManagementPage
from pages.BasePage import BasePage


class CourseManagementPage(BasePage):
    def find_course_name(self, name) -> WebElement:
        locator = (By.LINK_TEXT, name)
        return self.find_element_by_link_text(locator)

    def delete(self) -> WebElement:
        return self.find_element(LocatorsCourseManagementPage.DELETE)

    def click_delete_icon(self):
        self.click_element(self.delete())

    def go_to_create_new_course(self):
        self.click_on_link(LocatorsCourseManagementPage.CREATE_NEW_COURSE)

    def find_search_field(self) -> WebElement:
        return self.find_element(LocatorsCourseManagementPage.SEARCH)

    def click_on_search_button(self):
        self.click_on_button(LocatorsCourseManagementPage.SEARCH_BUTTON)

    def search_result(self) -> WebElement:
        return self.find_element(LocatorsCourseManagementPage.SEARCH_RESULT)
