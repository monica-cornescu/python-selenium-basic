import pytest

from page_objects.exceptions_page import ExceptionsPage


class TestExceptionsScenarios:
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        # Open page
        exceptions_page.open()

        # Don't click on Add button to get NoSuchElementException(return False from _isdisplayed)
        # Click Add button to fix the test
        exceptions_page.add_row2()

        # Verify Row 2 input field is displayed
        assert exceptions_page.verify_row2_shows_up(), "Row2 input field is not displayed on the page"


    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_row2()
        exceptions_page.save_text_in_row2("chicken soup")
        assert exceptions_page.get_confirmation_message() == "Row 2 was saved", "Unexpected confirmation message received"


    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.change_text_in_row1("hamburger")
        assert exceptions_page.verify_text_in_row1() == "hamburger", "Unexpected text was saved"
        # Verify with confirmation message as another variant
        #assert exceptions_page.get_confirmation_message() == "Row 1 was saved", "Unexpected confirmation message received"


    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_stale_element_reference_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        assert exceptions_page.verify_instructions_shows_up(), "The instructions text element is not displayed and it should"
        exceptions_page.add_row2()
        assert exceptions_page.verify_instructions_disappear(), "Something is still there!"

        ## Or verify with filed not displayed anymore
        #exceptions_page.add_row2()
        #assert not exceptions_page.verify_instructions_shows_up(), "The instructions text element is still displayed"




