import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expcond


@pytest.mark.exceptions
class TestExceptionsScenarios:
    def test_no_such_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # create an explicit wait to wait for the row2 web element to show up
        wait = WebDriverWait(driver, 6)
        row2_input_field_element = wait.until(
            expcond.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Verify Row 2 input field is displayed
        assert row2_input_field_element.is_displayed(), "Row2 input field is not displayed on the page"
