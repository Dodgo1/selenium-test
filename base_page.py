"""Base page module"""
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


class BasePage:
    """ Base page class """

    def __init__(self, driver):
        """ function for driver """
        self._driver = driver

    def go_to(self, main_page_locator: tuple):
        """Go to start"""
        link = self._driver.find_element(*main_page_locator)
        link.click()

    def check_visbility(self, locator):
        """Checks if element is visible, if yes returns the element"""
        element = EC.visibility_of_element_located(locator)
        return element

    def title(self):
        """ Function for getting a title of current page"""
        return self._driver.title

    def page_content(self):
        """Function gets page source code"""
        html = self._driver.page_source
        data = BeautifulSoup(html, 'html.parser').get_text()
        data = data.split()
        data = ' '.join(data)
        return data
