from common.constants import Constants
from locators.locators_login_page import LocatorsLoginPage
from locators.locators_main_page import LocatorsMainPage
from locators.locators_personal_account import LocatorsPersonalAccount


class TestAuthorization:
    def test_authorization_with_valid_data(self, app_fixture):
        """
        Steps
        1. Open main page
        2. Click on the link "Вход"
        3. Find field "Логин"
        4. Fill field "Логин" with valid data
        5. Find field "Пароль"
        6. Fill field "Пароль" with valid data
        7. Click on the button "Вход"
        8. Check authorization.
        """
        app_fixture.open_page(Constants.MAIN_PAGE)
        app_fixture.main_page.click_on_link(LocatorsMainPage.LINK_ENTER)
        login = app_fixture.login_page.find_element(LocatorsLoginPage.LOGIN)
        app_fixture.login_page.fill_element(login, Constants.VALID_LOGIN)
        password = app_fixture.login_page.find_element(LocatorsLoginPage.PASSWORD)
        app_fixture.login_page.fill_element(password, Constants.VALID_PASSWORD)
        app_fixture.login_page.click_on_button(LocatorsLoginPage.BUTTON_ENTER)
        assert app_fixture.personal_account.find_element(
            LocatorsPersonalAccount.PERSONAL_ACCOUNT
        ), "couldn't log in with valid data"
        app_fixture.personal_account.exit_from_account()

    def test_authorization_with_empty_login(self, app_fixture):
        """
        Steps
        1. Open main page
        2. Click on the link "Вход"
        3. Find field "Пароль"
        4. Fill field "Пароль" with valid data
        5. Click on the button "Вход"
        6. Check authorization.
        """
        app_fixture.open_page(Constants.MAIN_PAGE)
        app_fixture.main_page.click_on_link(LocatorsMainPage.LINK_ENTER)
        password = app_fixture.login_page.find_element(LocatorsLoginPage.PASSWORD)
        app_fixture.login_page.fill_element(password, Constants.VALID_PASSWORD)
        app_fixture.login_page.click_on_button(LocatorsLoginPage.BUTTON_ENTER)
        assert app_fixture.login_page.find_element(
            LocatorsLoginPage.LOGIN_ERROR_MESSAGE
        ), "something went wrong"

    def test_authorization_with_empty_password(self, app_fixture):
        """
        Steps
        1. Open main page
        2. Click on the link "Вход"
        3. Find field "Логин"
        4. Fill field "Логин" with valid data
        5. Click on the button "Вход"
        6. Check authorization.
        """
        app_fixture.open_page(Constants.MAIN_PAGE)
        app_fixture.main_page.click_on_link(LocatorsMainPage.LINK_ENTER)
        login = app_fixture.login_page.find_element(LocatorsLoginPage.LOGIN)
        app_fixture.login_page.fill_element(login, Constants.VALID_LOGIN)
        app_fixture.login_page.click_on_button(LocatorsLoginPage.BUTTON_ENTER)
        assert app_fixture.login_page.find_element(
            LocatorsLoginPage.LOGIN_ERROR_MESSAGE
        ), "something went wrong"

    def test_authorization_with_invalid_login(self, app_fixture):
        """
        Steps
        1. Open main page
        2. Click on the link "Вход"
        3. Find field "Логин"
        4. Fill field "Логин" with invalid data
        5. Find field "Пароль"
        6. Fill field "Пароль" with valid data
        7. Click on the button "Вход"
        8. Check authorization.
        """
        app_fixture.open_page(Constants.MAIN_PAGE)
        app_fixture.main_page.click_on_link(LocatorsMainPage.LINK_ENTER)
        login = app_fixture.login_page.find_element(LocatorsLoginPage.LOGIN)
        app_fixture.login_page.fill_element(login, Constants.INVALID_LOGIN)
        password = app_fixture.login_page.find_element(LocatorsLoginPage.PASSWORD)
        app_fixture.login_page.fill_element(password, Constants.VALID_PASSWORD)
        app_fixture.login_page.click_on_button(LocatorsLoginPage.BUTTON_ENTER)
        assert app_fixture.login_page.find_element(
            LocatorsLoginPage.LOGIN_ERROR_MESSAGE
        ), "something went wrong"
