from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expcond

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.NAME, "password")
    __submit_button = (By.XPATH, "//button[@class='btn']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self, url: str = __url):
        super().open_url(self.__url)

    # def execute_login(self, username: str, password: str):   # upgrading this to use parent class BasePage
    #     # Type the username in its location after checking for visibility of element
    #     wait = WebDriverWait(self._driver, 6)
    #     wait.until(expcond.visibility_of_element_located(self.__username_field))
    #     self._driver.find_element(self.__username_field).send_keys(username)
    #
    #     # Type password in its location after checking for visibility of element
    #     wait.until(expcond.visibility_of_element_located(self.__password_field))
    #     self._driver.find_element(self.__password_field).send_keys(password)
    #
    #     # Press Submit button after checking for visibility of element
    #     wait.until(expcond.visibility_of_element_located(self.__submit_button))
    #     self._driver.find_element(self.__submit_button).click()

    def execute_login(self, username: str, password: str):
        super()._insert_text(self.__username_field, username)
        super()._insert_text(self.__password_field, password)
        super()._click(self.__submit_button)

