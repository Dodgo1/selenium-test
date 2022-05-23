from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    Locators used for the main page of 'https://pwsz.edu.pl/'
    """
    # lang
    switch_lang = (By.CLASS_NAME, "langs_toggler")
    switch_lang_eng = (By.XPATH, '//*[@id="navbar"]/div[1]/div/div/div[3]/div/div/ul/li[2]/a')
    # tabs
    start_tab = (By.LINK_TEXT, "Start")
    about_tab = (By.LINK_TEXT, "O uczelni")
    students_tab = (By.LINK_TEXT, "Dla studentów")
    candidates_tab = (By.LINK_TEXT, "Dla kandydatów")
    intitutes_tab = (By.LINK_TEXT, "Instytuty")
    library_tab = (By.LINK_TEXT, "Biblioteka")  # library moves to another page
    elections_tab = (By.LINK_TEXT, "Wybory")  # election moves to another page
    usos_tab = (By.LINK_TEXT, "USOSWeb")
    contact_tab = (By.LINK_TEXT, "Kontakt")

    class AboutMenu:
        """additional class for dropdown menu, adds readability,easier to understand"""
        dropdown_menu = (By.XPATH, '//*[@id="navbar"]/div[2]/div/ul/li[3]/div')
        history = (By.LINK_TEXT, 'Historia powstania Uczelni')
        patron = (By.LINK_TEXT, 'Patron Uczelni')
        career = (By.LINK_TEXT, 'Twoja Kariera')
        fundation = (By.LINK_TEXT, 'Fundacja na Rzecz Rozwoju')
        news = (By.LINK_TEXT, 'Aktualności')
        # etc

    # for dropdown menus - locate by Xpath: no ID, same class everywhere
    class StudentsMenu:
        """additional class for dropdown menu, adds readability,easier to understand,scalability
        they show up after clicking ,
        dropdown_menu: Xpath of menu <div> used of checking visibility"""

        dropdown_menu = (By.XPATH, '//*[@id="navbar"]/div[2]/div/ul/li[3]/div')
        student_card = (By.LINK_TEXT, 'Legitymacja studencka')
        update_info = (By.LINK_TEXT, 'Aktualizacja danych osobowych')
        ios = (By.LINK_TEXT, 'Indywidualna Organizacja Studiów (IOS)')

    class CandidatesMenu:
        """additional class for dropdown menu, adds readability, easier to understand, scalability
        they show up after clicking,
        dropdown_menu: Xpath of menu <div> used of checking visibility"""

        dropdown_menu = (By.XPATH, '//*[@id="navbar"]/div[2]/div/ul/li[4]/div')
        offer = (By.LINK_TEXT, 'OFERTA STUDIÓW:')

    class InstitutesMenu:
        """additional class for dropdown menu, adds readability,easier to understand, scalability
        they show up after clicking,
        dropdown_menu: Xpath of menu <div> used of checking visibility"""

        dropdown_menu = (By.XPATH, '//*[@id="boxes"]')
        polytechnic = (By.CSS_SELECTOR, 'a[href="https://ipo.pwsz.edu.pl/"]')

    class UsosMenu:
        """additional class for dropdown menu, adds readability,easier to understand, scalability
        they show up after clicking,
        dropdown_menu: Xpath of menu <div> used of checking visibility"""

        dropdown_menu = (By.XPATH, '//*[@id="navbar"]/div[2]/div/ul/li[8]/div')
        usos_login = (By.LINK_TEXT, "USOS WEB - logowanie")

    class ContactMenu:
        """additional class for dropdown menu, adds readability,easier to understand, scalability
        they show up after clicking,
        dropdown_menu: Xpath of menu <div> used of checking visibility"""

        dropdown_menu = (By.XPATH, '//*[@id="navbar"]/div[2]/div/ul/li[9]/div')
        contact = (By.LINK_TEXT, "Kontakty")
