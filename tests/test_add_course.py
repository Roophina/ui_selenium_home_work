import allure

from common.fakers import NewCourse
from locators.locators_admin_page import LocatorsAdminPage
from locators.locators_course_delete_page import LocatorsCourseDeletePage
from locators.locators_course_edit_page import LocatorsCourseEditPage
from locators.locators_course_management_page import LocatorsCourseManagementPage


class TestAddCourse:
    @allure.story("Позитивный тест")
    def test_add_course(self, authorization_fixture, app_fixture):
        """
        Steps
        1. Click on side panel
        2. Click on "Администрирование"
        3. Click on the link "Управление курсами и категориями"
        4. Click on the link "Создать новый курс"
        5. Fill field "Полное название курса" with faker data
        6. Fill field "Краткое название курса" with faker data
        7. Click on the button "Сохранить и вернуться"
        8. Check creation.
        """
        app_fixture.personal_account.click_element(
            app_fixture.personal_account.side_panel()
        )
        app_fixture.personal_account.click_element(
            app_fixture.personal_account.administration()
        )
        app_fixture.admin_page.click_on_link(LocatorsAdminPage.COURSE_MANAGEMENT_LINK)
        app_fixture.course_management.click_on_link(
            LocatorsCourseManagementPage.CREATE_NEW_COURSE
        )
        full_name = app_fixture.course_edit.find_element(
            LocatorsCourseEditPage.FULL_NAME
        )
        add_full_name = NewCourse.random().full_name
        app_fixture.course_edit.fill_element(full_name, add_full_name)
        short_name = app_fixture.course_edit.find_element(
            LocatorsCourseEditPage.SHORT_NAME
        )
        add_short_name = NewCourse.random().short_name
        app_fixture.course_edit.fill_element(short_name, add_short_name)
        app_fixture.course_edit.click_on_button(LocatorsCourseEditPage.SAVE_AND_RETURN)
        with allure.step("Проверяем позитивный кейс создания нового курса"):
            search = app_fixture.course_management.find_element(
                LocatorsCourseManagementPage.SEARCH
            )
            app_fixture.course_management.fill_element(search, add_full_name)
            app_fixture.course_management.click_on_button(
                LocatorsCourseManagementPage.SEARCH_BUTTON
            )
            assert app_fixture.course_management.find_element(
                LocatorsCourseManagementPage.SEARCH_RESULT
            )
        app_fixture.course_management.course_name(add_full_name)
        app_fixture.course_management.click_element(
            app_fixture.course_management.delete()
        )
        app_fixture.course_delete.click_on_button(
            LocatorsCourseDeletePage.BUTTON_DELETE
        )

    @allure.story("Негативный тест")
    def test_add_course_with_empty_required_field(
        self, authorization_fixture, app_fixture
    ):
        """
        Steps
        1. Click on side panel
        2. Click on "Администрирование"
        3. Click on the link "Управление курсами и категориями"
        4. Click on the link "Создать новый курс"
        5. Fill field "Полное название курса" with faker data
        6. Click on the button "Сохранить и вернуться"
        7. Check creation.
        """
        app_fixture.personal_account.click_element(
            app_fixture.personal_account.side_panel()
        )
        app_fixture.personal_account.click_element(
            app_fixture.personal_account.administration()
        )
        app_fixture.admin_page.click_on_link(LocatorsAdminPage.COURSE_MANAGEMENT_LINK)
        app_fixture.course_management.click_on_link(
            LocatorsCourseManagementPage.CREATE_NEW_COURSE
        )
        full_name = app_fixture.course_edit.find_element(
            LocatorsCourseEditPage.FULL_NAME
        )
        add_full_name = NewCourse.random().full_name
        app_fixture.course_edit.fill_element(full_name, add_full_name)
        app_fixture.course_edit.click_on_button(LocatorsCourseEditPage.SAVE_AND_RETURN)
        with allure.step("Проверяем негативный кейс создания нового курса"):
            assert app_fixture.course_edit.find_element(
                LocatorsCourseEditPage.ERROR_SHORT_NAME
            )
