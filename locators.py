from selenium.webdriver.common.by import By


class locators:
    locator_by_link_text = lambda text: (By.LINK_TEXT, text)
    locator_by_tag_name = lambda tag_name: (By.TAG_NAME, tag_name)
    locator_by_class_name = lambda class_name: (By.CLASS_NAME, class_name)
    locator_by_css_selector = lambda css_selector: (By.CSS_SELECTOR, css_selector)
