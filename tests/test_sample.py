from webbrowser import Chrome

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium import webdriver as driver
import pytest
import time
"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""


class TestSample():
    SEARCH_INPUT = (By.NAME, 'q')

    def test_search(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_experimental_option("useAutomationExtension", False);
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("--disable-gpu")
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
        self.driver = Chrome(options=chrome_options) #executable_path='./TestProject/drivers/chromedriver.exe')
        # Wait implicitly for elements to be ready before attempting interactions
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get('https://www.google.com')
        g_search = self.driver.find_element(*self.SEARCH_INPUT)
        g_search.send_keys('github')
        g_search.send_keys(Keys.ENTER)
        time.sleep(5)
        title = self.driver.title
        assert "github" in title
        self.driver.close()




