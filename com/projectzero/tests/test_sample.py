from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time
import  allure
"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

SEARCH_INPUT = (By.NAME, 'q')


@allure.title("Google Search Test")
@allure.severity(allure.severity_level.NORMAL)
def test_search(get_browser):
        #https: // www.saucedemo.com /
        get_browser.get('https://www.google.com')
        g_search = get_browser.find_element(*SEARCH_INPUT)
        g_search.send_keys('github')
        g_search.send_keys(Keys.ENTER)
        title = get_browser.title
        assert "github" in title
        get_browser.close()




