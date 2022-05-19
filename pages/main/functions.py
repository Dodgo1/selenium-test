""" Module for functions"""
from base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException


class MainPageFunctions(BasePage):
    """
    Functions for the main page
    """

    def title(self):
        """ Function for getting a title of current page"""
        return self._driver.title

    def go_to(self, main_page_locator: tuple):
        """Go to start"""
        link = self._driver.find_element(*main_page_locator)
        link.click()

    def check_visbility(self, locator):
        """Checks if element is visible, if yes returns the element"""
        element = EC.visibility_of_element_located(locator)
        return element

    def accept_alert(self):
        """Function tries to accept an alert, if no such - return 0"""
        try:
            alert = self._driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            alert = 0
        return alert
