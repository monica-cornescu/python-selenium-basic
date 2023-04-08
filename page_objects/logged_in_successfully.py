from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LoggedInSuccessfully(BasePage):
    __url = "https://practicetestautomation.com/logged-in-successfully/"
    __expected_text = (By.TAG_NAME, "h1")
    __log_out_button = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def get_expected_url(self) -> str:
        return self.__url

    def verify_expected_text_is_displayed(self) -> str:
        return super()._return_text(self.__expected_text)

    @property
    def verify_logout_button_is_displayed(self) -> bool:
        return super().is_displayed(self.__log_out_button)
