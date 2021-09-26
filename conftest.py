import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from application.App import App
from common.constants import Constants


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://qacoursemoodle.innopolis.university/",
        help="Web site url",
    )


@pytest.fixture(scope="session")
def app_fixture(request):
    url = request.config.getoption("--url")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    app = App(
        webdriver.Chrome(
            ChromeDriverManager().install(), chrome_options=chrome_options
        ),
        url,
    )
    yield app
    app.quit()


@pytest.fixture
def authorization_fixture(app_fixture):
    app_fixture.open_main_page()
    app_fixture.main_page.click_on_enter_link()
    login_field = app_fixture.login_page.find_login_field()
    app_fixture.login_page.fill_element(login_field, Constants.VALID_LOGIN)
    password_field = app_fixture.login_page.find_password_field()
    app_fixture.login_page.fill_element(password_field, Constants.VALID_PASSWORD)
    app_fixture.login_page.click_on_enter_button()
    yield
    app_fixture.personal_account.exit_from_account()
