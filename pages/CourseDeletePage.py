from locators.locators_course_delete_page import LocatorsCourseDeletePage
from pages.BasePage import BasePage


class CourseDeletePage(BasePage):
    def confirm_delete(self):
        self.click_on_button(LocatorsCourseDeletePage.BUTTON_DELETE)
