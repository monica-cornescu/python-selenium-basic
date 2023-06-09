import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_username(self, driver):
        # Go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorrectUser")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # Press Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed but it should be!"

        # Verify error message text is Your username is invalid!
        error_message = error_message_locator.text
        assert error_message == "Your username is invalid!", 'Did not expect this error message!'

    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_password(self, driver):
        # Go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type password incorrectPassword into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("incorrectPassword")

        # Press Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()

        # Verify that error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed but it should be!"

        # Verify that error message text is "Your password is invalid!"
        error_message = error_message_locator.text
        assert error_message == "Your password is invalid!", "Did not expect this error message!"
