"""tests for main page"""
import pytest

from pages.main.functions import MainPageFunctions
from pages.main.locators import MainPageLocators as MPL


# browser fixture included in conftest.py

# how to get rid of MainPageLocators class when defining?
class TestTabs:
    """tests associated with tabs and their links to another pages located in menus"""

    @staticmethod
    def test_start_tab(browser):
        """test if start tab moves back to start"""
        home_page = MainPageFunctions(browser)
        university_name = "Państwowa Wyższa Szkoła Zawodowa"
        start_title = home_page.title()
        home_page.go_to(MPL.start_tab)
        new_title = home_page.title()

        assert university_name in start_title
        assert start_title == new_title
        assert "error" not in home_page.page_content()

    @staticmethod
    @pytest.mark.parametrize(
        "tab,menu_tab", [
            (MPL.about_tab, MPL.AboutMenu.history),
            (MPL.about_tab, MPL.AboutMenu.patron),
            (MPL.about_tab, MPL.AboutMenu.career),
            (MPL.about_tab, MPL.AboutMenu.fundation),  # fundation page has no title :(
            (MPL.about_tab, MPL.AboutMenu.news),
            (MPL.students_tab, MPL.StudentsMenu.student_card),
            (MPL.students_tab, MPL.StudentsMenu.update_info),
            (MPL.students_tab, MPL.StudentsMenu.ios),
            (MPL.candidates_tab, MPL.CandidatesMenu.offer),
        ])
    def test_tab_menu_redirect(tab, menu_tab, browser):
        """test for 'tab'->'menu_tab'"""
        home_page = MainPageFunctions(browser)
        start_title = home_page.title()
        home_page.go_to(tab)
        home_page.go_to(menu_tab)
        new_title = home_page.title()
        # MPL.*[1] = name of the clicked link - move to constants?
        assert menu_tab[1] == home_page.title()
        assert start_title != new_title
        assert "error" not in home_page.page_content()

    @staticmethod
    def test_institutes_polytechnic(browser):
        """test for 'Institutes'->'polytechnic'"""
        home_page = MainPageFunctions(browser)
        start_title = home_page.title()
        home_page.go_to(MPL.intitutes_tab)
        home_page.go_to(MPL.InstitutesMenu.polytechnic)
        new_title = home_page.title()
        assert "Instytut Politechniczny PWSZ Leszno" == home_page.title()
        assert start_title != new_title
        assert "error" not in home_page.page_content()

    @staticmethod
    def test_library_alert_and_redirect(browser):
        """test library tab alert for redirecting"""
        home_page = MainPageFunctions(browser)
        home_title = home_page.title()
        home_page.go_to(MPL.library_tab)
        assert home_page.accept_alert()
        new_title = home_page.title()
        assert home_title != new_title
        assert "Biblioteka" in new_title
        assert "error" not in home_page.page_content()
        # rest of library tests in pages/library


class TestDropdownMenus:
    """test associated with dropdown menus from tabs"""

    @staticmethod
    @pytest.mark.parametrize(
        "tab,menu",
        [
            (MPL.about_tab, MPL.AboutMenu.dropdown_menu),
            (MPL.students_tab, MPL.StudentsMenu.dropdown_menu),
            (MPL.candidates_tab, MPL.CandidatesMenu.dropdown_menu),
            (MPL.intitutes_tab, MPL.InstitutesMenu.dropdown_menu),
            (MPL.usos_tab, MPL.UsosMenu.dropdown_menu),
            (MPL.contact_tab, MPL.ContactMenu.dropdown_menu)
        ])
    def test_dropdown_menus_visibility(tab, menu, browser):
        """test for checking visibilities of the menus"""
        home_page = MainPageFunctions(browser)
        # roll down the menu
        home_page.go_to(tab)
        # check visibility
        menu = home_page.check_visbility(menu)
        assert menu


class TestLangChange:
    """test linked to change of the language"""

    @staticmethod
    def test_change_lang_to_english(browser):
        """change lang to english and test content"""
        home_page = MainPageFunctions(browser)
        title_pl = home_page.title()
        content_pl = home_page.page_content()
        main_eng_link = 'State School of Higher Vocational Education Leszno'
        home_page.switch_lang()
        content_eng = home_page.page_content()
        title_eng = home_page.title()

        assert title_eng != title_pl
        assert content_eng != content_pl
        assert main_eng_link in title_eng
