import pytest

from page_objects.logged_in_successfully import LoggedInSuccessfully
from page_objects.login_page import LoginPage


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)

        # Go to webpage
        login_page.open()

        # Type username student into Username field
        # Type password Password123 into Password field
        # Press Submit button
        login_page.execute_login("student", "Password123")

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        logged_in_page = LoggedInSuccessfully(driver)
        assert logged_in_page.get_expected_url == logged_in_page.get_current_url, "Actual URL is not the expected one"

        # Verify new page contains expected text ('Logged In Successfully' or'Congratulations' or 'successfully logged in')
        assert logged_in_page.verify_expected_text_is_displayed() == "Logged In Successfully", "Unexpected header text"

        # Verify button Log out is displayed on the new page
        assert logged_in_page.verify_logout_button_is_displayed(), "Logout button is not present"
