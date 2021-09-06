from common.constants import MAIN_PAGE, VALID_LOGIN, VALID_PASSWORD
from locators.locators_login_page import LOGIN, PASSWORD, BUTTON_ENTER
from locators.locators_main_page import LINK_ENTER
from locators.locators_personal_account import PERSONAL_ACCOUNT


class TestAuthorization:
    def test_authorization_with_valid_data(self, app_fixture):
        """
        Steps
        1. Open main page
        2. Click on the link "Вход"
        3. Find field "Логин"
        4. Fill field "Логин"
        5. Find field "Пароль"
        6. Fill field "Пароль"
        7. Click on the button "Вход"
        8. Check authorization.
        """
        app_fixture.open_page(MAIN_PAGE)
        app_fixture.main_page.click_on_link(LINK_ENTER)
        login = app_fixture.login_page.find_element(LOGIN)
        app_fixture.login_page.fill_element(login, VALID_LOGIN)
        password = app_fixture.login_page.find_element(PASSWORD)
        app_fixture.login_page.fill_element(password, VALID_PASSWORD)
        app_fixture.login_page.click_on_button(BUTTON_ENTER)
        assert app_fixture.personal_account.find_element(
            PERSONAL_ACCOUNT
        ), "couldn't log in"

    def test_authorization_with_empty_data(self):
        pass

    def test_authorization_with_invalid_login(self):
        pass
