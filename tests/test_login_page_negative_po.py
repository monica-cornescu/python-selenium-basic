import pytest

from page_objects.login_page import LoginPage


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_username(self, driver):
        login_page = LoginPage(driver)

        # Go to webpage
        login_page.open()

        # Type username incorrectUser into Username field
        # Type password Password123 into Password field
        # Press Submit button
        login_page.execute_login("incorrectUser", "Password123")

        # Verify error message text is Your username is invalid!
        assert login_page.verify_expected_error_is_displayed() == "Your username is invalid!", \
            'Did not expect this error message!'

    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_password(self, driver):
        login_page = LoginPage(driver)
        # Go to webpage
        login_page.open()

        # Type username student into Username field
        # Type password incorrectPassword into Password field
        # Press Submit button
        login_page.execute_login("student", "incorrectPassword")

        # Verify that error message text is "Your password is invalid!"
        assert login_page.verify_expected_error_is_displayed() == "Your password is invalid!", \
            'Did not expect this error message!'

