import allure

from common.constants import Constants


class TestAuthorization:
    @allure.story("Позитивный тест")
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
        app_fixture.open_main_page()
        app_fixture.main_page.click_on_enter_link()
        login_field = app_fixture.login_page.find_login_field()
        app_fixture.login_page.fill_element(login_field, Constants.VALID_LOGIN)
        password_field = app_fixture.login_page.find_password_field()
        app_fixture.login_page.fill_element(password_field, Constants.VALID_PASSWORD)
        app_fixture.login_page.click_on_enter_button()
        with allure.step("Проверяем авторизацию с валидными данными"):
            assert (
                app_fixture.personal_account.check_personal_account()
            ), "couldn't log in with valid data"
        app_fixture.personal_account.exit_from_account()

    @allure.story("Негативный тест")
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
        app_fixture.open_main_page()
        app_fixture.main_page.click_on_enter_link()
        password_field = app_fixture.login_page.find_password_field()
        app_fixture.login_page.fill_element(password_field, Constants.VALID_PASSWORD)
        app_fixture.login_page.click_on_enter_button()
        with allure.step("Проверяем авторизацию с пустым логином"):
            assert (
                app_fixture.login_page.find_login_error_message()
            ), "something went wrong"

    @allure.story("Негативный тест")
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
        app_fixture.open_main_page()
        app_fixture.main_page.click_on_enter_link()
        login_field = app_fixture.login_page.find_login_field()
        app_fixture.login_page.fill_element(login_field, Constants.VALID_LOGIN)
        app_fixture.login_page.click_on_enter_button()
        with allure.step("Проверяем авторизацию с пустым паролем"):
            assert (
                app_fixture.login_page.find_login_error_message()
            ), "something went wrong"

    @allure.story("Негативный тест")
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
        app_fixture.open_main_page()
        app_fixture.main_page.click_on_enter_link()
        login_field = app_fixture.login_page.find_login_field()
        app_fixture.login_page.fill_element(login_field, Constants.INVALID_LOGIN)
        password_field = app_fixture.login_page.find_password_field()
        app_fixture.login_page.fill_element(password_field, Constants.VALID_PASSWORD)
        app_fixture.login_page.click_on_enter_button()
        with allure.step("Проверяем авторизацию с невалидным логином"):
            assert (
                app_fixture.login_page.find_login_error_message()
            ), "something went wrong"
