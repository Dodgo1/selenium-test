"""tests for main page"""
import pytest

from functions import MainPageFunctions
from locators import MainPageLocators as MPL


# browser included in conftest.py

# how to get rid of MainPageLocators class when defining?
# TODO: - check if page contains text
#       - parametrize TestTabs
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

    @staticmethod
    def test_about_history(browser):
        """test for 'About'->'history of the university'"""
        home_page = MainPageFunctions(browser)
        start_title = home_page.title()
        home_page.go_to(MPL.about_tab)
        home_page.go_to(MPL.AboutMenu.history)
        new_title = home_page.title()
        # MPL.*[1] = name of the clicked link - move to constants?
        assert MPL.AboutMenu.history[1] == home_page.title()
        assert start_title != new_title

    @staticmethod
    def test_students_student_card(browser):
        """test for 'Student'->'student card'"""
        home_page = MainPageFunctions(browser)
        start_title = home_page.title()
        home_page.go_to(MPL.students_tab)
        home_page.go_to(MPL.StudentsMenu.student_card)
        new_title = home_page.title()
        # MPL.*[1] = name of the clicked link - move to constants?
        assert MPL.StudentsMenu.student_card[1] == home_page.title()
        assert start_title != new_title

    @staticmethod
    def test_candidates_offer(browser):
        """test for 'Candidates'->'offer'"""
        home_page = MainPageFunctions(browser)
        start_title = home_page.title()
        home_page.go_to(MPL.candidates_tab)
        home_page.go_to(MPL.CandidatesMenu.offer)
        new_title = home_page.title()
        # MPL.*[1] = name of the clicked link - move to constants?
        assert MPL.CandidatesMenu.offer[1] == home_page.title()
        assert start_title != new_title

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
        home_page = MainPageFunctions(browser)
        # roll down the menu
        home_page.go_to(tab)
        # check visibility
        menu = home_page.check_visbility(menu)
        assert menu
