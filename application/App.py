from pages.AdminPage import AdminPage
from pages.CourseDeletePage import CourseDeletePage
from pages.CourseEditPage import CourseEditPage
from pages.CourseManagementPage import CourseManagementPage
from pages.EditInformationPage import EditInformationPage
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.PersonalAccountPage import PersonalAccountPage
from pages.PreferencesPage import PreferencesPage


class App:
    def __init__(self, driver, url):
        self.url = url
        self.driver = driver
        self.main_page = MainPage(self)
        self.login_page = LoginPage(self)
        self.personal_account = PersonalAccountPage(self)
        self.preferences = PreferencesPage(self)
        self.edit_information = EditInformationPage(self)
        self.admin_page = AdminPage(self)
        self.course_management = CourseManagementPage(self)
        self.course_edit = CourseEditPage(self)
        self.course_delete = CourseDeletePage(self)

    def open_main_page(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()
