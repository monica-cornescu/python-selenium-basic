from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class ExceptionsPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button_locator = (By.ID, "add_btn")
    __row2_input_field_element = (By.XPATH, "//div[@id='row2']/input")
    __password_field = (By.NAME, "password")
    __submit_button = (By.XPATH, "//button[@class='btn']")
    __expected_error_text = (By.ID, "error")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self, url: str = __url):
        super()._open_url(self.__url)

    def click_on_add(self):
        super()._click(self.__add_button_locator)

    def verify_row2_shows_up(self) -> bool:
        super()._wait_until_element_is_visible(self.__row2_input_field_element)
        return super()._is_displayed(self.__row2_input_field_element)
