import allure

from common.fakers import BasicData
from locators.locators_edit_information import LocatorsEditInformation
from locators.locators_personal_account import LocatorsPersonalAccount
from locators.locators_preferences_page import LocatorsPreferences


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
        app_fixture.personal_account.click_element(
            app_fixture.personal_account.user_menu()
        )
        app_fixture.personal_account.click_element(
            app_fixture.personal_account.find_element(
                LocatorsPersonalAccount.PREFERENCES
            )
        )
        app_fixture.preferences.click_on_link(LocatorsPreferences.EDIT_INFORMATION)
        city = app_fixture.edit_information.find_element(LocatorsEditInformation.CITY)
        add_city = BasicData.random().city
        app_fixture.edit_information.fill_element(city, add_city)
        app_fixture.edit_information.click_on_button(
            LocatorsEditInformation.BUTTON_UPDATE_PROFILE
        )
        with allure.step(
            "Проверяем позитивный кейс редактирования данных пользователя"
        ):
            assert app_fixture.preferences.find_element(
                LocatorsPreferences.NOTIFICATION
            )

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
        app_fixture.personal_account.click_element(
            app_fixture.personal_account.user_menu()
        )
        app_fixture.personal_account.click_element(
            app_fixture.personal_account.find_element(
                LocatorsPersonalAccount.PREFERENCES
            )
        )
        app_fixture.preferences.click_on_link(LocatorsPreferences.EDIT_INFORMATION)
        email = app_fixture.edit_information.find_element(LocatorsEditInformation.EMAIL)
        app_fixture.edit_information.clear_element(email)
        with allure.step(
            "Редактирование данных пользователя при незаполнении обязательного поля"
        ):
            assert app_fixture.edit_information.find_element(
                LocatorsEditInformation.ERROR_EMAIL
            )
