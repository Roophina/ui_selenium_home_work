from common.fakers import BasicData
from locators.locators_edit_information import LocatorsEditInformation
from locators.locators_personal_account import LocatorsPersonalAccount
from locators.locators_preferences_page import LocatorsPreferences


class TestEditInformation:
    def test_valid_edit_one_basic_data(self, authorization_fixture, app_fixture):
        """
        Steps
        1. Click on user menu
        2. Click on preferences
        3. Clink on the link "Редактировать информацию"
        4. Find field "Город"
        6. Fill field "Город" with valid data
        7. Click on the button "Обновить профиль"
        8. Check update.
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
        assert app_fixture.preferences.find_element(LocatorsPreferences.NOTIFICATION)

    def test_edit_basic_with_empty_email(self, authorization_fixture, app_fixture):
        """
        Steps
        1. Click on user menu
        2. Click on preferences
        3. Clink on the link "Редактировать информацию"
        4. Find field "Адрес электронной почты"
        6. Clear field "Адрес электронной почты"
        7. Click on the button "Обновить профиль"
        8. Check update.
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
        assert app_fixture.edit_information.find_element(
            LocatorsEditInformation.ERROR_EMAIL
        )
