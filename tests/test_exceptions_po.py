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
        #exceptions_page.click_on_add()

        # Verify Row 2 input field is displayed
        assert exceptions_page.verify_row2_shows_up(), "Row2 input field is not displayed on the page"
