"""
This module contains shared fixtures for web UI tests.
"""
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.options import Options
import pytest
import json

CONFIG_PATH = 'com/projectzero/utilities/config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']


@pytest.fixture(scope='session')
def config():
    # Read the JSON config file and returns it as a parsed dict
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
        return data


@pytest.fixture(scope='session')
def config_browser(config):

    if 'browser' not in config:
        raise Exception('The config file doesnot contain "browser" tag')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'{config["browser"]} is not supported browser')
    else:
        return config['browser']


@pytest.fixture(scope='session')
def config_wait_time(config):
    return config['implicit_wait'] if 'implicit_wait' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope='session')
def get_browser(config_browser, config_wait_time):
    # Initialize WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--test-type")
    chrome_options.add_experimental_option("useAutomationExtension", False);
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
    if config_browser == 'chrome':
        driver = Chrome(options=chrome_options,executable_path='C:/Old D drive/SeleniumWorkSpace/TestProject/com/projectzero/drivers/chromedriver.exe')
        #driver = Chrome(options=chrome_options)

    elif config_browser == 'Firefox':
        raise Exception(f'{config_browser} is not supported for now')
    else:
        raise Exception(f'{config_browser} is not supported!!!')

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(config_wait_time)
    driver.maximize_window()

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()
