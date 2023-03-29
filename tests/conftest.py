import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    print("Creating Chrome driver (browser)")
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield chrome_driver
    print("Closing Chrome driver")
    chrome_driver.quit()