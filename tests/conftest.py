"""
This file contains setup functions.
The driver function is initially created to take --browser argument passed at runtime.
Then we modify it to take the 2 browsers as parameters of the fixture
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    print(f"Creating {browser} driver")
    if browser == "chrome":
        used_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        used_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f'Expected "chrome" or "firefox", but got {browser}')
    # used_driver.implicitly_wait(5) # disable implicit wait because we will be using explicit waits from now on
    yield used_driver
    print(f"Closing {browser} driver")
    used_driver.quit()

# @pytest.fixture(params=["chrome", "firefox"])
# def driver(request):
#     browser = request.param
#     print(f"Creating {browser} driver")
#     if browser == "chrome":
#         used_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     elif browser == "firefox":
#         used_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#     else:
#         raise TypeError(f'Expected "chrome" or "firefox", but got {browser}')
#     yield used_driver
#     print(f"Closing {browser} driver")
#     used_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help='browsers to execute tests in (chrome, firefox)',
        choices=("chrome", "firefox", "opera"),
    )
