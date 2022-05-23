import pytest
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import sys, getopt


@pytest.fixture()
def browser():
    # check if webdriver is already in local
    os.environ['WDM_LOCAL'] = '1'
    # don't show logs
    os.environ['WDM_LOG_LEVEL'] = '0'
    # headless for whole project
    headless = True
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--window-size=1920,1080")
        # when page is smaller, mobile manu show up - additional click needed
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://pwsz.edu.pl")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()


@pytest.fixture()
def library_browser(browser):
    browser.get("https://biblioteka.pwsz.edu.pl")
    yield browser
