# Open browser
# selenium 4
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        time.sleep(2)
        # Go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # Press Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        url_after_login = driver.current_url
        assert url_after_login == "https://practicetestautomation.com/logged-in-successfully/"

        # Verify new page contains expected text ('Logged In Successfully' or'Congratulations' or 'successfully logged in')
        expected_text_locator = driver.find_element(By.TAG_NAME, "h1")
        # expected_text_locator = driver.find_element(By.LINK_TEXT, "Congratulations student. You successfully logged in!")
        actual_text = expected_text_locator.text
        assert actual_text == "Logged In Successfully"

        # Verify button Log out is displayed on the new page
        log_out_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
        # log_out_button_locator = driver.find_element(By.XPATH, "//div[@id='loop-container']/div/article//a[@href='https://practicetestautomation.com/practice-test-login/']")
        assert log_out_button_locator.is_displayed()