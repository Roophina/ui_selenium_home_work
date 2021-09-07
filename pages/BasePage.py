from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, app):
        self.app = app

    def find_element(self, locator, wait_time=20):
        return WebDriverWait(self.app.driver, wait_time).until(
            ec.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    @staticmethod
    def click_element(element):
        element.click()

    @staticmethod
    def fill_element(element, text):
        element.clear()
        if text:
            element.send_keys(text)
            return element

    def click_on_link(self, locator):
        return (
            WebDriverWait(self.app.driver, 20)
            .until(ec.element_to_be_clickable(locator))
            .click()
        )

    def click_on_button(self, locator):
        return (
            WebDriverWait(self.app.driver, 20)
            .until(ec.visibility_of_element_located(locator))
            .click()
        )

    def find_element_by_class_name(self, locator):
        return WebDriverWait(self.app.driver, 20).until(
            ec.visibility_of_element_located(locator)
        )
