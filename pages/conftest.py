import pytest
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


@pytest.fixture()
def browser():
    # check if webdriver is already in local
    os.environ['WDM_LOCAL'] = '1'
    # don't show logs
    os.environ['WDM_LOG_LEVEL'] = '0'

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://pwsz.edu.pl")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()
