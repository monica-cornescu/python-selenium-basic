import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expcond


class TestExceptionsScenarios:
    @pytest.mark.exceptions
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

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # create an explicit wait to wait for the row2 web element to show up
        wait = WebDriverWait(driver, 6)
        row2_input_field_element = wait.until(
            expcond.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Type text into the second input field
        row2_input_field_element.send_keys("chocolate cake")

        # Push Save button using locator By.name("Save"); combine element locator with click method in one command
        # driver.find_element(By.NAME, "Save").click()   # with this we will get the ElementNotInteractableException
        # because there are 2 Save buttons and the first is not interactable
        driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']").click()

        # Verify text saved
        confirmation_locator = wait.until(expcond.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_locator.text
        assert confirmation_message == "Row 2 was saved", "Unexpected confirmation message received"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Clear input field (remove pizza from the first row. You'll get InvalidElementStateException if not
        # clicking first on Edit button and then remove text
        driver.find_element(By.XPATH, "//div[@id='row1']/button[@name='Edit']").click()
        row1_input_field_element = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        wait = WebDriverWait(driver, 10)
        wait.until(expcond.element_to_be_clickable(row1_input_field_element))
        row1_input_field_element.clear()

        # Type different text into the input field (and press Save button)
        row1_input_field_element.send_keys("chicken soup")
        driver.find_element(By.XPATH, "//div[@id='row1']/button[@name='Save']").click()

        # Verify that the text changed
        row1_text = row1_input_field_element.get_attribute(name="value")
        print(f"Expected chicken soup but got {row1_text}")
        assert row1_text == "chicken soup", f"Expected chicken soup but got {row1_text}"

        # # Or verify confirmation message
        # save_confirmation_locator = wait.until(expcond.visibility_of_element_located((By.ID, "confirmation")))
        # save_confirmation_message = save_confirmation_locator.text
        # assert save_confirmation_message == "Row 1 was saved", "Did not receive save confirmation message"
