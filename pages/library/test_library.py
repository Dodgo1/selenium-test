import pytest
from functions import LibraryPageFunctions


# browser fixture in conftest.py

class TestVisibleElements:
    @staticmethod
    def test_title(library_browser):
        """test if the title has changed"""
        library_page = LibraryPageFunctions(library_browser)
        title_text = "Biblioteka PWSZ Leszno"
        assert title_text in library_page.title()

    @staticmethod
    def test_content(library_browser):
        """test if content of the page doesnt have an error"""
        library_page = LibraryPageFunctions(library_browser)
        assert "error" not in library_page.page_content()


class TestForm:
    """tests linked to library form"""

    @staticmethod
    @pytest.mark.parametrize("select_int", ["1", "2", "3", "4"])
    @pytest.mark.parametrize("searched_text", ["Przedwiośnie", "Chłopi", "Żeromski", "horror", "Wesele"])
    def test_from_choices(select_int, searched_text, library_browser):
        """tests for library from"""
        library_page = LibraryPageFunctions(library_browser)
        library_title = library_page.title()
        library_page.select_option(select_int)
        library_page.input_to_textfield(searched_text)

        library_page.submit_form()
        library_page.switch_tab()
        current_title = library_page.title()
        assert current_title != library_title
        assert library_page.get_number_of_results()
