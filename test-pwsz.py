import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoAlertPresentException
from webdriver_manager.chrome import ChromeDriverManager
from locators import *

# os and else
os.environ['WDM_LOCAL'] = '1'
os.environ['WDM_LOG_LEVEL'] = '0'


@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://pwsz.edu.pl/')
    yield driver
    driver.quit()


class TestInfo:
    @staticmethod
    def test_title(browser):
        assert "Szkoła" in browser.title


class TestTabs:
    def test_tab1_click(self, browser):
        card_name = 'O uczelni'
        subcard_name = "Aktualności"
        browser.find_element(*locators.locator_by_link_text(card_name)).click()
        browser.find_element(*locators.locator_by_link_text(subcard_name)).click()
        assert subcard_name == browser.title

    def test_tab2_click(self, browser):
        card_name = 'Dla studentów'
        subcard_name = "Różnice programowe"
        browser.find_element(*locators.locator_by_link_text(card_name)).click()
        browser.find_element(*locators.locator_by_link_text(subcard_name)).click()
        assert subcard_name == browser.title

    def test_tab3_click(self, browser):
        card_name = 'Dla kandydatów'
        subcard_name = "Kierunek: logistyka"
        browser.find_element(*locators.locator_by_link_text(card_name)).click()
        browser.find_element(*locators.locator_by_link_text(subcard_name)).click()
        assert subcard_name == browser.title

    def test_tab4_click(self, browser):
        card_name = 'Instytuty'
        subcard_href = "https://ipo.pwsz.edu.pl/"
        browser.find_element(*locators.locator_by_link_text(card_name)).click()
        browser.find_element(*locators.locator_by_css_selector(f'a[href="{subcard_href}"]')).click()


class TestBiblioteka:
    card_name = "Biblioteka"

    def test_title(self, browser):
        browser.find_element(*locators.locator_by_link_text(self.card_name)).click()
        try:
            alert = browser.switch_to.alert
        except NoAlertPresentException:
            alert = 0
            assert alert

        alert.accept()
        assert self.card_name in browser.title

    def test_form(self, browser):
        # pass alert
        browser.find_element(*locators.locator_by_link_text(self.card_name)).click()
        try:
            alert = browser.switch_to.alert
        except NoAlertPresentException:
            alert = None
            assert alert

        alert.accept()

        # send values
        select_tag = "select"
        input_field_css_selector = 'input[type="text"][name="q"]'
        searched_title = "Przedwiośnie"
        select_value = "2"
        key_enter = Keys.ENTER

        select = Select(browser.find_element(*locators.locator_by_tag_name(select_tag)))
        select.select_by_value(select_value)

        browser.find_element(*locators.locator_by_css_selector(input_field_css_selector)).send_keys(
            searched_title + key_enter)


class TestLangChange:
    def test_lang_change(self, browser):
        # zmiana języka
        langs_dropdown_class_name = "langs_toggler"
        langs_eng_href = "https://en.pwsz.edu.pl/"
        browser.find_element(*locators.locator_by_class_name(langs_dropdown_class_name)).click()
        browser.find_element(*locators.locator_by_css_selector(f'a[href="{langs_eng_href}"]')).click()
