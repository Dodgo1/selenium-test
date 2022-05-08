import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# os and else
os.environ['WDM_LOCAL'] = '1'
os.environ['WDM_LOG_LEVEL'] = '0'

@pytest.fixture
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_tab_1(browser):
    browser.get('https://pwsz.edu.pl/')
    browser.find_element(By.XPATH,'//*[@id="navbar"]/div[2]/div/ul/li[1]/a').click()


