"""Base page module"""


class BasePage:
    """ Base page class """

    def __init__(self, driver):
        """ function for driver """
        self._driver = driver
