import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from application.App import App


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
    app = App(webdriver.Chrome(ChromeDriverManager().install()), url)
    yield app
    app.quit()
