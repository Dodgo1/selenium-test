import pytest
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from constants import PWSZ_MAIN_URL, LIBRARY_MAIN_URL


def pytest_addoption(parser):
    """ parser function """
    parser.addoption("--headless", action="store_true",
                     help="turn on headless option if headless arg is added")


@pytest.fixture()
def browser(request):
    # check if webdriver is already in local
    os.environ['WDM_LOCAL'] = '1'
    # don't show logs
    os.environ['WDM_LOG_LEVEL'] = '0'

    is_headless = request.config.getoption("--headless")
    chrome_options = Options()
    if is_headless:
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(PWSZ_MAIN_URL)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()


@pytest.fixture()
def library_browser(browser):
    browser.get(LIBRARY_MAIN_URL)
    yield browser
