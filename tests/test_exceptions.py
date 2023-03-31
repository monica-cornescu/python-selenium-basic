"""Test case 1: NoSuchElementException

    Open page
    Click Add button
    Verify Row 2 input field is displayed"""

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.exceptions
class TestExceptionsScenarios:
    def test_no_such_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()
        # Verify Row 2 input field is displayed
        row2_input_field_locator = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert row2_input_field_locator.is_displayed(), "Row2 input field is not displayed on the page"
