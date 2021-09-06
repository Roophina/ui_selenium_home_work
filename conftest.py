import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
