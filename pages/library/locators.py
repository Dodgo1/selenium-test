"""locators for library page"""
from selenium.webdriver.common.by import By


class LibraryPageLocators:
    """Locators for library page"""
    form_input = (By.CSS_SELECTOR, 'input[type="text"][name="q"]')
    form_select = (By.TAG_NAME, 'select')
    button_submit = (By.CSS_SELECTOR, 'button[type="submit"]')

    articles = (By.TAG_NAME, 'article')
