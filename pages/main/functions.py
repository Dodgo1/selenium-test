""" Module for functions for main"""
from base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from pages.main.locators import MainPageLocators as MPL


class MainPageFunctions(BasePage):
    """
    Functions for the main page
    """

    def accept_alert(self):
        """Function tries to accept an alert, if no such - return 0"""
        try:
            alert = self._driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            alert = 0
        return alert

    def switch_lang(self):
        # roll down
        self._driver.find_element(*MPL.switch_lang).click()
        # click
        self._driver.find_element(*MPL.switch_lang_eng).click()
