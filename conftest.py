import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from application.App import App
from common.constants import Constants
from locators.locators_login_page import LocatorsLoginPage
from locators.locators_main_page import LocatorsMainPage
from locators.locators_personal_account import LocatorsPersonalAccount


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
    app_fixture.main_page.click_on_link(LocatorsMainPage.LINK_ENTER)
    login = app_fixture.login_page.find_element(LocatorsLoginPage.LOGIN)
    app_fixture.login_page.fill_element(login, Constants.VALID_LOGIN)
    password = app_fixture.login_page.find_element(LocatorsLoginPage.PASSWORD)
    app_fixture.login_page.fill_element(password, Constants.VALID_PASSWORD)
    app_fixture.login_page.click_on_button(LocatorsLoginPage.BUTTON_ENTER)
    assert app_fixture.personal_account.find_element(
        LocatorsPersonalAccount.PERSONAL_ACCOUNT
    ), "couldn't log in with valid data"
    yield
    app_fixture.personal_account.exit_from_account()
