from locators.locators_admin_page import LocatorsAdminPage
from pages.BasePage import BasePage


class AdminPage(BasePage):
    def go_to_course_management(self):
        self.click_on_link(LocatorsAdminPage.COURSE_MANAGEMENT_LINK)
