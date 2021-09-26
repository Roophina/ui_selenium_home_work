import allure

from common.fakers import NewCourse


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
        app_fixture.personal_account.click_on_side_panel()
        app_fixture.personal_account.go_to_admin_page()
        app_fixture.admin_page.go_to_course_management()
        app_fixture.course_management.go_to_create_new_course()
        full_name_field = app_fixture.course_edit.find_full_name_field()
        full_name = NewCourse.random().full_name
        app_fixture.course_edit.fill_element(full_name_field, full_name)
        short_name_field = app_fixture.course_edit.find_short_name_field()
        short_name = NewCourse.random().short_name
        app_fixture.course_edit.fill_element(short_name_field, short_name)
        app_fixture.course_edit.click_on_save_and_return()
        with allure.step("Проверяем позитивный кейс создания нового курса"):
            search_field = app_fixture.course_management.find_search_field()
            app_fixture.course_management.fill_element(search_field, full_name)
            app_fixture.course_management.click_on_search_button()
            assert app_fixture.course_management.search_result()
        app_fixture.course_management.find_course_name(full_name)
        app_fixture.course_management.click_delete_icon()
        app_fixture.course_delete.confirm_delete()

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
        app_fixture.personal_account.click_on_side_panel()
        app_fixture.personal_account.go_to_admin_page()
        app_fixture.admin_page.go_to_course_management()
        app_fixture.course_management.go_to_create_new_course()
        full_name_field = app_fixture.course_edit.find_full_name_field()
        full_name = NewCourse.random().full_name
        app_fixture.course_edit.fill_element(full_name_field, full_name)
        app_fixture.course_edit.click_on_save_and_return()
        with allure.step("Проверяем негативный кейс создания нового курса"):
            assert app_fixture.course_edit.find_error_message_about_short_name()
