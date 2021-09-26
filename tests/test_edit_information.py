import allure

from common.fakers import BasicData


class TestEditInformation:
    @allure.story("Позитивный тест")
    def test_valid_edit_one_basic_data(self, authorization_fixture, app_fixture):
        """
        Steps
        1. Click on user menu
        2. Click on preferences
        3. Click on the link "Редактировать информацию"
        4. Find field "Город"
        5. Fill field "Город" with valid data
        6. Click on the button "Обновить профиль"
        7. Check update.
        """
        app_fixture.personal_account.click_on_user_menu()
        app_fixture.personal_account.go_to_preferences()
        app_fixture.preferences.go_to_edit_information()
        city_field = app_fixture.edit_information.find_city_field()
        city = BasicData.random().city
        app_fixture.edit_information.fill_element(city_field, city)
        app_fixture.edit_information.click_on_update_profile_button()
        with allure.step(
            "Проверяем позитивный кейс редактирования данных пользователя"
        ):
            assert app_fixture.preferences.check_notifications()

    @allure.story("Негативный тест")
    def test_edit_basic_with_empty_email(self, authorization_fixture, app_fixture):
        """
        Steps
        1. Click on user menu
        2. Click on preferences
        3. Click on the link "Редактировать информацию"
        4. Find field "Адрес электронной почты"
        5. Clear field "Адрес электронной почты"
        6. Click on the button "Обновить профиль"
        7. Check update.
        """
        app_fixture.personal_account.click_on_user_menu()
        app_fixture.personal_account.go_to_preferences()
        app_fixture.preferences.go_to_edit_information()
        email_field = app_fixture.edit_information.find_email_field()
        app_fixture.edit_information.clear_element(email_field)
        app_fixture.edit_information.click_on_update_profile_button()
        with allure.step(
            "Редактирование данных пользователя при незаполнении обязательного поля"
        ):
            assert app_fixture.edit_information.find_email_error_message()
