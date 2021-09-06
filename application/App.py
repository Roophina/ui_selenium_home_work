from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.PersonalAccountPage import PersonalAccountPage


class App:
    def __init__(self, driver, url):
        self.driver = driver
        self.main_page = MainPage(self)
        self.login_page = LoginPage(self)
        self.personal_account = PersonalAccountPage(self)

    def open_page(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()
