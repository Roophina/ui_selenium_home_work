from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage


class MainPage(BasePage):
    def find_element_by_class_name(self, locator):
        return WebDriverWait(self.app.driver, 20).until(
            ec.visibility_of_element_located(locator)
        )
