""" Module for functions for library page"""
from locators import LibraryPageLocators as LPL
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class LibraryPageFunctions(BasePage):
    """Functions for library page"""

    def select_option(self, value: str):
        """Selects an option in library's from 1-4 available"""
        select = Select(self._driver.find_element(*LPL.form_select))
        select.select_by_value(value)

    def input_to_textfield(self, text: str):
        """inputs a string to a textfield in library form"""
        input = self._driver.find_element(*LPL.form_input)
        input.send_keys(text)

    def submit_form(self):
        """sumbits the form, remember to input text and select an option-deafult 1"""
        self._driver.find_element(*LPL.button_submit).click()

    def switch_tab(self):
        """when form is send, new tab is opening - webdriver has to switch"""
        self._driver.switch_to.window(self._driver.window_handles[1])

    def get_number_of_results(self):
        results = self._driver.find_elements(*LPL.articles)
        return len(results)
