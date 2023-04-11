from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class ExceptionsPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button_locator = (By.ID, "add_btn")
    __row1_input_field_element = (By.XPATH, "//div[@id='row1']/input")
    __row2_input_field_element = (By.XPATH, "//div[@id='row2']/input")
    __save_button_row1_locator = (By.XPATH, "//div[@id='row1']/button[@name='Save']")
    __save_button_row2_locator = (By.XPATH, "//div[@id='row2']/button[@name='Save']")
    __confirmation_locator = (By.ID, "confirmation")
    __edit_button_locator = (By.XPATH, "//div[@id='row1']/button[@name='Edit']")
    __instructions_text_locator = (By.XPATH, "//p[@id='instructions']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self, url: str = __url):
        super()._open_url(self.__url)

    def add_row2(self):
        super()._click(self.__add_button_locator)
        super()._wait_until_element_is_visible(self.__row2_input_field_element)

    def verify_row2_shows_up(self) -> bool:
        return super()._is_displayed(self.__row2_input_field_element)

    def save_text_in_row2(self, text: str):
        super()._insert_text(self.__row2_input_field_element, text, time=6)
        super()._click(self.__save_button_row2_locator)
        super()._wait_until_element_is_visible(self.__confirmation_locator)

    def get_confirmation_message(self) -> str:
        return super()._return_text(self.__confirmation_locator)

    def change_text_in_row1(self, newtext: str):
        super()._click(self.__edit_button_locator)
        super()._wait_until_element_is_clickable(self.__row1_input_field_element)
        super()._clear_content(self.__row1_input_field_element)
        super()._insert_text(self.__row1_input_field_element, newtext)
        super()._click(self.__save_button_row1_locator)
        # super()._wait_until_element_is_visible(self.__confirmation_locator)

    def verify_text_in_row1(self) -> str:
        return super()._find(self.__row1_input_field_element).get_attribute(name="value")

    def verify_instructions_shows_up(self) -> bool:
        return super()._is_displayed(self.__instructions_text_locator)

    def verify_instructions_disappear(self) -> bool:
        #super()._click(self.__add_button_locator)
        return super()._wait_until_element_is_invisible(self.__instructions_text_locator)

