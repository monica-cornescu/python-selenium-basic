from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoggedInSuccessfully:
    __url = "https://practicetestautomation.com/logged-in-successfully/"
    __expected_text = (By.TAG_NAME, "h1")
    __log_out_button = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def get_current_url(self) -> str:
        return self._driver.current_url

    @property
    def get_expected_url(self) -> str:
        return self.__url

    def verify_expected_text(self) -> str:
        return self._driver.find_element(self.__expected_text).text

    @property
    def verify_expected_text_is_displayed(self) -> bool:
        return self._driver.find_element(self.__log_out_button).is_displayed()



